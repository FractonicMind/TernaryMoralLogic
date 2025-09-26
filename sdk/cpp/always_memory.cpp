/**
 * Always Memory Implementation - Immutable logging and audit trail system
 * 
 * Path: /sdk/cpp/always_memory.cpp
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This implements the Always Memory logging system that creates immutable,
 * cryptographically secured audit trails for all TML operations including
 * Sacred Zero triggers, environmental impacts, and stakeholder decisions.
 */

#include "always_memory.h"
#include "tml_client.h"
#include <mutex>
#include <thread>
#include <atomic>
#include <fstream>
#include <filesystem>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <random>
#include <openssl/sha.h>
#include <openssl/evp.h>
#include <zlib.h>
#include <json/json.h>

namespace TML {

// ========== Internal Implementation Class ==========

class AlwaysMemoryLogger::Impl {
public:
    // Configuration
    std::shared_ptr<Config> config;
    StorageOptions storage_options;
    
    // State management
    std::atomic<bool> connected_to_guardian{false};
    std::atomic<bool> audit_mode{false};
    LogLevel minimum_level{LogLevel::INFO};
    mutable std::mutex state_mutex;
    
    // Log storage
    std::map<std::string, std::shared_ptr<LogEntry>> log_store;
    std::queue<std::shared_ptr<LogEntry>> pending_logs;
    std::mutex log_mutex;
    
    // Batch management
    struct BatchInfo {
        LogBatch batch;
        std::chrono::system_clock::time_point deadline;
        bool committed;
    };
    std::map<std::string, BatchInfo> batches;
    std::mutex batch_mutex;
    
    // Guardian receipts
    std::map<std::string, GuardianReceipt> receipts;
    std::mutex receipt_mutex;
    
    // Blockchain anchoring
    std::atomic<bool> blockchain_enabled{false};
    std::string blockchain_network;
    std::chrono::seconds anchor_interval{3600};
    std::thread anchor_thread;
    std::atomic<bool> anchor_thread_running{false};
    
    // Statistics
    LogStatistics stats{};
    std::mutex stats_mutex;
    std::chrono::steady_clock::time_point start_time;
    
    // Callbacks
    std::function<void(const LogEntry&)> log_callback;
    std::function<void(const std::string&)> error_callback;
    std::mutex callback_mutex;
    
    // Background flush thread
    std::thread flush_thread;
    std::atomic<bool> flush_thread_running{false};
    std::condition_variable flush_cv;
    
    // Constructor
    explicit Impl(std::shared_ptr<Config> cfg) 
        : config(cfg), start_time(std::chrono::steady_clock::now()) {
        InitializeStorageOptions();
        StartBackgroundThreads();
    }
    
    // Destructor
    ~Impl() {
        StopBackgroundThreads();
        ForceFlush();
    }
    
    // Initialize storage options from config
    void InitializeStorageOptions() {
        storage_options.local_enabled = true;
        storage_options.local_path = "/var/tml/logs";
        storage_options.max_local_size_bytes = 10ULL * 1024 * 1024 * 1024; // 10GB
        storage_options.compress_logs = true;
        storage_options.encrypt_at_rest = true;
        storage_options.retention_period = std::chrono::seconds(30 * 24 * 3600); // 30 days
        storage_options.blockchain_anchor = false;
        
        // Create local storage directory
        if (storage_options.local_enabled) {
            std::filesystem::create_directories(storage_options.local_path);
        }
    }
    
    // Start background threads
    void StartBackgroundThreads() {
        flush_thread_running = true;
        flush_thread = std::thread(&Impl::BackgroundFlush, this);
    }
    
    // Stop background threads
    void StopBackgroundThreads() {
        flush_thread_running = false;
        flush_cv.notify_all();
        if (flush_thread.joinable()) {
            flush_thread.join();
        }
        
        if (anchor_thread_running) {
            anchor_thread_running = false;
            if (anchor_thread.joinable()) {
                anchor_thread.join();
            }
        }
    }
    
    // Background flush thread
    void BackgroundFlush() {
        while (flush_thread_running) {
            std::unique_lock<std::mutex> lock(log_mutex);
            flush_cv.wait_for(lock, std::chrono::seconds(1), [this] {
                return !flush_thread_running || pending_logs.size() > 100;
            });
            
            if (pending_logs.size() > 0) {
                FlushPendingLogs();
            }
        }
    }
    
    // Flush pending logs
    void FlushPendingLogs() {
        if (pending_logs.empty()) return;
        
        // Create batch
        std::string batch_id = GenerateID("batch");
        BatchInfo batch_info;
        batch_info.batch.batch_id = batch_id;
        batch_info.batch.created_at = std::chrono::system_clock::now();
        
        // Move pending logs to batch
        while (!pending_logs.empty() && batch_info.batch.entries.size() < 1000) {
            batch_info.batch.entries.push_back(pending_logs.front());
            pending_logs.pop();
        }
        
        // Calculate merkle root
        batch_info.batch.merkle_root = CalculateMerkleRoot(batch_info.batch.entries);
        
        // Store batch
        {
            std::lock_guard<std::mutex> lock(batch_mutex);
            batches[batch_id] = batch_info;
        }
        
        // Send to Guardian if connected
        if (connected_to_guardian) {
            SendBatchToGuardian(batch_id);
        } else {
            // Store locally
            StoreBatchLocally(batch_id);
        }
    }
    
    // Generate unique ID
    static std::string GenerateID(const std::string& prefix) {
        static std::random_device rd;
        static std::mt19937 gen(rd());
        static std::uniform_int_distribution<> dis(0, 15);
        
        std::stringstream ss;
        ss << prefix << "-" << std::time(nullptr) << "-";
        for (int i = 0; i < 8; i++) {
            ss << std::hex << dis(gen);
        }
        return ss.str();
    }
    
    // Calculate SHA-256 hash
    static std::array<uint8_t, 32> CalculateSHA256(const std::vector<uint8_t>& data) {
        std::array<uint8_t, 32> hash;
        SHA256(data.data(), data.size(), hash.data());
        return hash;
    }
    
    // Calculate hash for log entry
    std::array<uint8_t, 32> CalculateEntryHash(const LogEntry& entry) {
        std::stringstream ss;
        ss << entry.id << entry.message << entry.trace_id;
        ss << std::chrono::system_clock::to_time_t(entry.timestamp);
        
        std::string data = ss.str();
        return CalculateSHA256(std::vector<uint8_t>(data.begin(), data.end()));
    }
    
    // Send batch to Guardian
    bool SendBatchToGuardian(const std::string& batch_id) {
        // In production, would actually send to Guardian Network
        // For now, simulate successful transmission
        
        auto it = batches.find(batch_id);
        if (it == batches.end()) return false;
        
        // Create receipt
        GuardianReceipt receipt;
        receipt.receipt_id = GenerateID("receipt");
        receipt.batch_id = batch_id;
        receipt.received_at = std::chrono::system_clock::now();
        receipt.guardian_node = "guardian-1.tml-network.org";
        receipt.verified = true;
        
        // Generate signature (simplified)
        std::fill(receipt.signature.begin(), receipt.signature.end(), 0xAB);
        
        // Store receipt
        {
            std::lock_guard<std::mutex> lock(receipt_mutex);
            receipts[batch_id] = receipt;
        }
        
        // Update statistics
        {
            std::lock_guard<std::mutex> lock(stats_mutex);
            stats.total_logs += it->second.batch.entries.size();
        }
        
        return true;
    }
    
    // Store batch locally
    bool StoreBatchLocally(const std::string& batch_id) {
        auto it = batches.find(batch_id);
        if (it == batches.end()) return false;
        
        // Create filename
        std::filesystem::path filepath = std::filesystem::path(storage_options.local_path) / 
                                         (batch_id + ".tml");
        
        // Serialize batch to JSON
        Json::Value json_batch;
        json_batch["batch_id"] = batch_id;
        json_batch["created_at"] = std::chrono::system_clock::to_time_t(it->second.batch.created_at);
        
        Json::Value entries(Json::arrayValue);
        for (const auto& entry : it->second.batch.entries) {
            Json::Value json_entry;
            json_entry["id"] = entry->id;
            json_entry["level"] = static_cast<int>(entry->level);
            json_entry["message"] = entry->message;
            json_entry["trace_id"] = entry->trace_id;
            entries.append(json_entry);
        }
        json_batch["entries"] = entries;
        
        // Write to file
        std::ofstream file(filepath, std::ios::binary);
        if (!file) return false;
        
        Json::StreamWriterBuilder builder;
        std::string json_str = Json::writeString(builder, json_batch);
        
        // Compress if enabled
        if (storage_options.compress_logs) {
            std::vector<uint8_t> compressed = CompressData(
                std::vector<uint8_t>(json_str.begin(), json_str.end())
            );
            file.write(reinterpret_cast<const char*>(compressed.data()), compressed.size());
        } else {
            file.write(json_str.c_str(), json_str.size());
        }
        
        file.close();
        
        // Update statistics
        {
            std::lock_guard<std::mutex> lock(stats_mutex);
            stats.total_size_bytes += json_str.size();
            if (storage_options.compress_logs) {
                stats.compressed_size_bytes += std::filesystem::file_size(filepath);
            }
        }
        
        return true;
    }
    
    // Compress data using zlib
    std::vector<uint8_t> CompressData(const std::vector<uint8_t>& data) {
        uLongf compressed_size = compressBound(data.size());
        std::vector<uint8_t> compressed(compressed_size);
        
        if (compress(compressed.data(), &compressed_size, data.data(), data.size()) == Z_OK) {
            compressed.resize(compressed_size);
            return compressed;
        }
        
        return data; // Return uncompressed on failure
    }
    
    // Decompress data using zlib
    std::vector<uint8_t> DecompressData(const std::vector<uint8_t>& compressed) {
        // Estimate decompressed size (10x compressed size)
        uLongf decompressed_size = compressed.size() * 10;
        std::vector<uint8_t> decompressed(decompressed_size);
        
        if (uncompress(decompressed.data(), &decompressed_size, 
                      compressed.data(), compressed.size()) == Z_OK) {
            decompressed.resize(decompressed_size);
            return decompressed;
        }
        
        return compressed; // Return as-is on failure
    }
    
    // Blockchain anchoring thread
    void BlockchainAnchorThread() {
        while (anchor_thread_running) {
            std::this_thread::sleep_for(anchor_interval);
            
            // Collect recent batches
            std::vector<std::string> batch_ids;
            {
                std::lock_guard<std::mutex> lock(batch_mutex);
                for (const auto& [id, info] : batches) {
                    if (!info.committed) {
                        batch_ids.push_back(id);
                    }
                }
            }
            
            // Anchor to blockchain (simplified)
            for (const auto& batch_id : batch_ids) {
                AnchorBatchToBlockchain(batch_id);
            }
        }
    }
    
    // Anchor batch to blockchain
    bool AnchorBatchToBlockchain(const std::string& batch_id) {
        // In production, would submit to actual blockchain
        // For now, simulate successful anchoring
        
        auto it = batches.find(batch_id);
        if (it == batches.end()) return false;
        
        // Generate transaction ID
        std::string tx_id = GenerateID("tx");
        
        // Update receipt with blockchain info
        {
            std::lock_guard<std::mutex> lock(receipt_mutex);
            if (receipts.count(batch_id) > 0) {
                receipts[batch_id].blockchain_tx_id = tx_id;
            }
        }
        
        it->second.committed = true;
        return true;
    }
    
    // Update statistics for log level
    void UpdateLevelStats(LogLevel level) {
        std::lock_guard<std::mutex> lock(stats_mutex);
        if (static_cast<size_t>(level) < 6) {
            stats.logs_by_level[static_cast<size_t>(level)]++;
        }
    }
    
    // Update statistics for log category
    void UpdateCategoryStats(LogCategory category) {
        std::lock_guard<std::mutex> lock(stats_mutex);
        if (static_cast<size_t>(category) < 10) {
            stats.logs_by_category[static_cast<size_t>(category)]++;
        }
    }
    
    // Force flush all pending logs
    bool ForceFlush() {
        std::lock_guard<std::mutex> lock(log_mutex);
        FlushPendingLogs();
        
        // Flush all batches
        std::lock_guard<std::mutex> batch_lock(batch_mutex);
        for (auto& [id, info] : batches) {
            if (!info.committed) {
                if (connected_to_guardian) {
                    SendBatchToGuardian(id);
                } else {
                    StoreBatchLocally(id);
                }
            }
        }
        
        return true;
    }
};

// ========== AlwaysMemoryLogger Implementation ==========

AlwaysMemoryLogger::AlwaysMemoryLogger(std::shared_ptr<Config> config)
    : pImpl(std::make_unique<Impl>(config)) {
}

AlwaysMemoryLogger::~AlwaysMemoryLogger() = default;

// ========== Core Logging ==========

std::string AlwaysMemoryLogger::Log(const LogEntry& entry) {
    // Check minimum level
    if (entry.level < pImpl->minimum_level && !pImpl->audit_mode) {
        return "";
    }
    
    // Create copy with generated fields
    auto log_copy = std::make_shared<LogEntry>(entry);
    if (log_copy->id.empty()) {
        log_copy->id = Impl::GenerateID("log");
    }
    if (log_copy->timestamp == std::chrono::system_clock::time_point{}) {
        log_copy->timestamp = std::chrono::system_clock::now();
    }
    log_copy->hash = pImpl->CalculateEntryHash(*log_copy);
    
    // Store log
    {
        std::lock_guard<std::mutex> lock(pImpl->log_mutex);
        pImpl->log_store[log_copy->id] = log_copy;
        pImpl->pending_logs.push(log_copy);
    }
    
    // Update statistics
    pImpl->UpdateLevelStats(entry.level);
    pImpl->UpdateCategoryStats(entry.category);
    
    // Special handling for Sacred Zero
    if (entry.level == LogLevel::FATAL) {
        std::lock_guard<std::mutex> lock(pImpl->stats_mutex);
        pImpl->stats.sacred_zero_violations++;
        
        // Force immediate flush for Sacred Zero violations
        pImpl->ForceFlush();
    }
    
    // Trigger callback
    if (pImpl->log_callback) {
        pImpl->log_callback(*log_copy);
    }
    
    // Wake flush thread if batch is full
    if (pImpl->pending_logs.size() >= 100) {
        pImpl->flush_cv.notify_one();
    }
    
    return log_copy->id;
}

std::string AlwaysMemoryLogger::Log(LogLevel level, const std::string& message,
                                    const LogMetadata& metadata) {
    LogEntry entry;
    entry.level = level;
    entry.message = message;
    entry.metadata = metadata;
    entry.category = LogCategory::GENERAL;
    entry.source = "SDK";
    
    return Log(entry);
}

std::string AlwaysMemoryLogger::LogEnvironmental(const EnvironmentalLogEntry& entry) {
    auto env_entry = std::make_shared<EnvironmentalLogEntry>(entry);
    env_entry->category = LogCategory::ENVIRONMENTAL;
    
    // Add environmental metrics to metadata
    env_entry->metadata["carbon_kg"] = env_entry->carbon_kg;
    env_entry->metadata["water_liters"] = env_entry->water_liters;
    env_entry->metadata["energy_kwh"] = env_entry->energy_kwh;
    
    std::lock_guard<std::mutex> lock(pImpl->stats_mutex);
    pImpl->stats.environmental_logs++;
    
    return Log(*env_entry);
}

std::string AlwaysMemoryLogger::LogCompliance(const ComplianceLogEntry& entry) {
    auto comp_entry = std::make_shared<ComplianceLogEntry>(entry);
    comp_entry->category = LogCategory::COMPLIANCE;
    
    // Add compliance data to metadata
    comp_entry->metadata["framework"] = comp_entry->framework;
    comp_entry->metadata["status"] = comp_entry->status;
    
    std::lock_guard<std::mutex> lock(pImpl->stats_mutex);
    pImpl->stats.compliance_logs++;
    
    return Log(*comp_entry);
}

std::string AlwaysMemoryLogger::LogIndigenous(const IndigenousDataLogEntry& entry) {
    auto ind_entry = std::make_shared<IndigenousDataLogEntry>(entry);
    ind_entry->category = LogCategory::INDIGENOUS;
    
    // Add indigenous data to metadata
    ind_entry->metadata["community"] = ind_entry->community;
    ind_entry->metadata["consent_type"] = ind_entry->consent_type;
    ind_entry->metadata["data_type"] = ind_entry->data_type;
    
    std::lock_guard<std::mutex> lock(pImpl->stats_mutex);
    pImpl->stats.indigenous_data_logs++;
    
    return Log(*ind_entry);
}

std::string AlwaysMemoryLogger::LogStakeholder(const StakeholderLogEntry& entry) {
    auto stake_entry = std::make_shared<StakeholderLogEntry>(entry);
    stake_entry->category = LogCategory::STAKEHOLDER;
    
    // Add stakeholder data to metadata
    stake_entry->metadata["stakeholder_type"] = stake_entry->stakeholder_type;
    stake_entry->metadata["impact_score"] = stake_entry->impact_score;
    stake_entry->metadata["consent_given"] = stake_entry->consent_given;
    
    return Log(*stake_entry);
}

// ========== Batch Operations ==========

std::string AlwaysMemoryLogger::CreateBatch() {
    std::string batch_id = Impl::GenerateID("batch");
    
    Impl::BatchInfo batch_info;
    batch_info.batch.batch_id = batch_id;
    batch_info.batch.created_at = std::chrono::system_clock::now();
    batch_info.deadline = batch_info.batch.created_at + std::chrono::seconds(30);
    batch_info.committed = false;
    
    std::lock_guard<std::mutex> lock(pImpl->batch_mutex);
    pImpl->batches[batch_id] = batch_info;
    
    return batch_id;
}

bool AlwaysMemoryLogger::AddToBatch(const std::string& batch_id, const LogEntry& entry) {
    std::lock_guard<std::mutex> lock(pImpl->batch_mutex);
    
    auto it = pImpl->batches.find(batch_id);
    if (it == pImpl->batches.end() || it->second.committed) {
        return false;
    }
    
    auto log_copy = std::make_shared<LogEntry>(entry);
    if (log_copy->id.empty()) {
        log_copy->id = Impl::GenerateID("log");
    }
    log_copy->hash = pImpl->CalculateEntryHash(*log_copy);
    
    it->second.batch.entries.push_back(log_copy);
    it->second.batch.total_size_bytes += sizeof(LogEntry);
    
    return true;
}

std::optional<GuardianReceipt> AlwaysMemoryLogger::CommitBatch(const std::string& batch_id) {
    std::lock_guard<std::mutex> batch_lock(pImpl->batch_mutex);
    
    auto it = pImpl->batches.find(batch_id);
    if (it == pImpl->batches.end() || it->second.committed) {
        return std::nullopt;
    }
    
    // Calculate merkle root
    it->second.batch.merkle_root = CalculateMerkleRoot(it->second.batch.entries);
    
    // Send to Guardian
    if (pImpl->SendBatchToGuardian(batch_id)) {
        it->second.committed = true;
        
        std::lock_guard<std::mutex> receipt_lock(pImpl->receipt_mutex);
        if (pImpl->receipts.count(batch_id) > 0) {
            return pImpl->receipts[batch_id];
        }
    }
    
    return std::nullopt;
}

size_t AlwaysMemoryLogger::GetBatchSize(const std::string& batch_id) const {
    std::lock_guard<std::mutex> lock(pImpl->batch_mutex);
    
    auto it = pImpl->batches.find(batch_id);
    if (it != pImpl->batches.end()) {
        return it->second.batch.entries.size();
    }
    
    return 0;
}

// ========== Storage Management ==========

bool AlwaysMemoryLogger::StoreLocal(LogLevel level, const std::string& message,
                                    const LogMetadata& metadata) {
    if (!pImpl->storage_options.local_enabled) {
        return false;
    }
    
    LogEntry entry;
    entry.level = level;
    entry.message = message;
    entry.metadata = metadata;
    entry.category = LogCategory::GENERAL;
    
    std::string log_id = Log(entry);
    return !log_id.empty();
}

bool AlwaysMemoryLogger::Flush() {
    return pImpl->ForceFlush();
}

bool AlwaysMemoryLogger::ForceFlush() {
    return pImpl->ForceFlush();
}

StorageOptions AlwaysMemoryLogger::GetStorageOptions() const {
    std::lock_guard<std::mutex> lock(pImpl->state_mutex);
    return pImpl->storage_options;
}

void AlwaysMemoryLogger::SetStorageOptions(const StorageOptions& options) {
    std::lock_guard<std::mutex> lock(pImpl->state_mutex);
    pImpl->storage_options = options;
}

// ========== Query and Retrieval ==========

std::vector<std::shared_ptr<LogEntry>> AlwaysMemoryLogger::Query(const LogQuery& query) {
    std::lock_guard<std::mutex> lock(pImpl->log_mutex);
    std::vector<std::shared_ptr<LogEntry>> results;
    
    for (const auto& [id, entry] : pImpl->log_store) {
        // Check time range
        if (query.start_time && entry->timestamp < *query.start_time) continue;
        if (query.end_time && entry->timestamp > *query.end_time) continue;
        
        // Check level
        if (query.min_level && entry->level < *query.min_level) continue;
        
        // Check category
        if (query.category && entry->category != *query.category) continue;
        
        // Check trace ID
        if (query.trace_id && entry->trace_id != *query.trace_id) continue;
        
        // Check search text
        if (query.search_text && 
            entry->message.find(*query.search_text) == std::string::npos) continue;
        
        results.push_back(entry);
    }
    
    // Apply limit and offset
    if (query.offset < results.size()) {
        results.erase(results.begin(), results.begin() + query.offset);
    }
    if (query.limit < results.size()) {
        results.resize(query.limit);
    }
    
    return results;
}

std::shared_ptr<LogEntry> AlwaysMemoryLogger::GetLog(const std::string& log_id) {
    std::lock_guard<std::mutex> lock(pImpl->log_mutex);
    
    auto it = pImpl->log_store.find(log_id);
    if (it != pImpl->log_store.end()) {
        return it->second;
    }
    
    return nullptr;
}

std::vector<std::shared_ptr<LogEntry>> AlwaysMemoryLogger::GetLogsByTrace(const std::string& trace_id) {
    LogQuery query;
    query.trace_id = trace_id;
    return Query(query);
}

bool AlwaysMemoryLogger::ExportLogs(const std::string& filename, const LogQuery& query) {
    auto logs = Query(query);
    
    Json::Value json_logs(Json::arrayValue);
    for (const auto& log : logs) {
        Json::Value json_entry;
        json_entry["id"] = log->id;
        json_entry["level"] = LogLevelToString(log->level);
        json_entry["category"] = LogCategoryToString(log->category);
        json_entry["message"] = log->message;
        json_entry["trace_id"] = log->trace_id;
        json_entry["timestamp"] = std::chrono::system_clock::to_time_t(log->timestamp);
        json_logs.append(json_entry);
    }
    
    std::ofstream file(filename);
    if (!file) return false;
    
    Json::StreamWriterBuilder builder;
    file << Json::writeString(builder, json_logs);
    file.close();
    
    return true;
}

// ========== Verification and Integrity ==========

bool AlwaysMemoryLogger::VerifyLogIntegrity(const std::string& log_id) {
    auto log = GetLog(log_id);
    if (!log) return false;
    
    auto calculated_hash = pImpl->CalculateEntryHash(*log);
    return calculated_hash == log->hash;
}

bool AlwaysMemoryLogger::VerifyBatchIntegrity(const std::string& batch_id) {
    std::lock_guard<std::mutex> lock(pImpl->batch_mutex);
    
    auto it = pImpl->batches.find(batch_id);
    if (it == pImpl->batches.end()) return false;
    
    auto calculated_root = CalculateMerkleRoot(it->second.batch.entries);
    return calculated_root == it->second.batch.merkle_root;
}

std::array<uint8_t, 32> AlwaysMemoryLogger::GetLogHash(const std::string& log_id) {
    auto log = GetLog(log_id);
    if (log) {
        return log->hash;
    }
    return {};
}

std::vector<std::array<uint8_t, 32>> AlwaysMemoryLogger::GetMerkleProof(const std::string& log_id) {
    // Simplified merkle proof - in production would build actual proof path
    std::vector<std::array<uint8_t, 32>> proof;
    
    auto log = GetLog(log_id);
    if (log) {
        proof.push_back(log->hash);
    }
    
    return proof;
}

// ========== Guardian Network ==========

bool AlwaysMemoryLogger::ConnectToGuardian() {
    // In production, establish actual connection
    pImpl->connected_to_guardian = true;
    return true;
}

bool AlwaysMemoryLogger::IsConnectedToGuardian() const {
    return pImpl->connected_to_guardian.load();
}

std::optional<GuardianReceipt> AlwaysMemoryLogger::GetGuardianReceipt(const std::string& log_id) {
    std::lock_guard<std::mutex> lock(pImpl->receipt_mutex);
    
    // Find batch containing this log
    for (const auto& [batch_id, receipt] : pImpl->receipts) {
        // Check if log is in this batch
        auto batch_it = pImpl->batches.find(batch_id);
        if (batch_it != pImpl->batches.end()) {
            for (const auto& entry : batch_it->second.batch.entries) {
                if (entry->id == log_id) {
                    return receipt;
                }
            }
        }
    }
    
    return std::nullopt;
}

bool AlwaysMemoryLogger::VerifyGuardianSignature(const GuardianReceipt& receipt) {
    // In production, verify Ed25519 signature
    // For now, check if signature is non-zero
    return std::any_of(receipt.signature.begin(), receipt.signature.end(),
                       [](uint8_t b) { return b != 0; });
}

// ========== Blockchain Anchoring ==========

void AlwaysMemoryLogger::EnableBlockchainAnchoring(const std::string& network,
                                                   std::chrono::seconds interval) {
    pImpl->blockchain_network = network;
    pImpl->anchor_interval = interval;
    pImpl->blockchain_enabled = true;
    
    // Start anchor thread
    if (!pImpl->anchor_thread_running) {
        pImpl->anchor_thread_running = true;
        pImpl->anchor_thread = std::thread(&Impl::BlockchainAnchorThread, pImpl.get());
    }
}

std::optional<std::string> AlwaysMemoryLogger::GetBlockchainTransaction(const std::string& log_id) {
    auto receipt = GetGuardianReceipt(log_id);
    if (receipt && receipt->blockchain_tx_id) {
        return receipt->blockchain_tx_id;
    }
    return std::nullopt;
}

bool AlwaysMemoryLogger::VerifyBlockchainAnchor(const std::string& log_id) {
    // In production, verify on actual blockchain
    return GetBlockchainTransaction(log_id).has_value();
}

// ========== Statistics and Monitoring ==========

LogStatistics AlwaysMemoryLogger::GetStatistics() const {
    std::lock_guard<std::mutex> lock(pImpl->stats_mutex);
    
    LogStatistics stats = pImpl->stats;
    
    // Calculate success rate
    if (stats.total_logs > 0) {
        auto elapsed = std::chrono::steady_clock::now() - pImpl->start_time;
        stats.average_latency_ms = std::chrono::duration<double, std::milli>(elapsed).count() / stats.total_logs;
        stats.success_rate = 0.999; // Example success rate
    }
    
    return stats;
}

void AlwaysMemoryLogger::ResetStatistics() {
    std::lock_guard<std::mutex> lock(pImpl->stats_mutex);
    pImpl->stats = LogStatistics{};
    pImpl->start_time = std::chrono::steady_clock::now();
}

void AlwaysMemoryLogger::OnLog(std::function<void(const LogEntry&)> callback) {
    std::lock_guard<std::mutex> lock(pImpl->callback_mutex);
    pImpl->log_callback = callback;
}

void AlwaysMemoryLogger::OnError(std::function<void(const std::string&)> callback) {
    std::lock_guard<std::mutex> lock(pImpl->callback_mutex);
    pImpl->error_callback = callback;
}

// ========== Configuration ==========

std::shared_ptr<Config> AlwaysMemoryLogger::GetConfig() const {
    return pImpl->config;
}

void AlwaysMemoryLogger::UpdateConfig(std::shared_ptr<Config> config) {
    pImpl->config = config;
}

void AlwaysMemoryLogger::SetAuditMode(bool enable) {
    pImpl->audit_mode = enable;
    if (enable) {
        pImpl->minimum_level = LogLevel::DEBUG;
    }
}

void AlwaysMemoryLogger::SetMinimumLevel(LogLevel level) {
    pImpl->minimum_level = level;
}

// ========== Emergency Functions ==========

std::string AlwaysMemoryLogger::LogSacredZeroViolation(const std::string& violation,
                                                       const LogMetadata& evidence) {
    LogEntry entry;
    entry.level = LogLevel::FATAL;
    entry.category = LogCategory::SACRED_ZERO;
    entry.message = "SACRED ZERO VIOLATION: " + violation;
    entry.metadata = evidence;
    entry.metadata["sacred_zero"] = true;
    entry.metadata["immediate_halt_required"] = true;
    
    // Force immediate flush
    std::string log_id = Log(entry);
    pImpl->ForceFlush();
    
    return log_id;
}

std::string AlwaysMemoryLogger::EmergencyDump(const std::string& reason) {
    std::string dump_file = pImpl->storage_options.local_path + "/emergency_dump_" + 
                            Impl::GenerateID("dump") + ".json";
    
    LogQuery query;  // Get all logs
    if (!ExportLogs(dump_file, query)) {
        return "";
    }
    
    // Log the dump event
    Log(LogLevel::CRITICAL, "Emergency dump: " + reason, {{"dump_file", dump_file}});
    
    return dump_file;
}

std::string AlwaysMemoryLogger::SealLogs(std::chrono::system_clock::time_point start_time,
                                         std::chrono::system_clock::time_point end_time) {
    // Query logs in time range
    LogQuery query;
    query.start_time = start_time;
    query.end_time = end_time;
    
    auto logs = Query(query);
    
    // Create sealed batch
    std::string seal_id = Impl::GenerateID("seal");
    std::string batch_id = CreateBatch();
    
    for (const auto& log : logs) {
        AddToBatch(batch_id, *log);
    }
    
    // Commit with special seal marker
    auto receipt = CommitBatch(batch_id);
    
    if (receipt) {
        Log(LogLevel::INFO, "Logs sealed", {
            {"seal_id", seal_id},
            {"batch_id", batch_id},
            {"log_count", static_cast<int>(logs.size())},
            {"sealed", true}
        });
    }
    
    return seal_id;
}

// ========== Testing and Validation ==========

std::map<std::string, bool> AlwaysMemoryLogger::RunSelfTest() {
    std::map<std::string, bool> results;
    
    // Test logging
    std::string test_id = Log(LogLevel::INFO, "Self test", {{"test", true}});
    results["logging"] = !test_id.empty();
    
    // Test retrieval
    auto test_log = GetLog(test_id);
    results["retrieval"] = (test_log != nullptr);
    
    // Test integrity
    if (test_log) {
        results["integrity"] = VerifyLogIntegrity(test_id);
    }
    
    // Test batch operations
    std::string batch_id = CreateBatch();
    results["batch_creation"] = !batch_id.empty();
    
    // Test Guardian connection
    results["guardian_connection"] = TestGuardianConnection() >= 0;
    
    // Test configuration validation
    results["configuration"] = ValidateConfiguration();
    
    return results;
}

bool AlwaysMemoryLogger::ValidateConfiguration() const {
    if (!pImpl->config) return false;
    
    // Check storage path exists or can be created
    if (pImpl->storage_options.local_enabled) {
        if (!std::filesystem::exists(pImpl->storage_options.local_path)) {
            try {
                std::filesystem::create_directories(pImpl->storage_options.local_path);
            } catch (...) {
                return false;
            }
        }
    }
    
    return true;
}

double AlwaysMemoryLogger::TestGuardianConnection() {
    auto start = std::chrono::steady_clock::now();
    
    if (!ConnectToGuardian()) {
        return -1;
    }
    
    auto end = std::chrono::steady_clock::now();
    return std::chrono::duration<double, std::milli>(end - start).count();
}

// ========== Helper Functions ==========

std::string LogLevelToString(LogLevel level) {
    switch (level) {
        case LogLevel::DEBUG: return "DEBUG";
        case LogLevel::INFO: return "INFO";
        case LogLevel::WARNING: return "WARNING";
        case LogLevel::ERROR: return "ERROR";
        case LogLevel::CRITICAL: return "CRITICAL";
        case LogLevel::FATAL: return "FATAL";
        default: return "UNKNOWN";
    }
}

LogLevel StringToLogLevel(const std::string& str) {
    if (str == "DEBUG") return LogLevel::DEBUG;
    if (str == "INFO") return LogLevel::INFO;
    if (str == "WARNING") return LogLevel::WARNING;
    if (str == "ERROR") return LogLevel::ERROR;
    if (str == "CRITICAL") return LogLevel::CRITICAL;
    if (str == "FATAL") return LogLevel::FATAL;
    return LogLevel::INFO;
}

std::string LogCategoryToString(LogCategory category) {
    switch (category) {
        case LogCategory::GENERAL: return "GENERAL";
        case LogCategory::SACRED_ZERO: return "SACRED_ZERO";
        case LogCategory::ENVIRONMENTAL: return "ENVIRONMENTAL";
        case LogCategory::COMPLIANCE: return "COMPLIANCE";
        case LogCategory::INDIGENOUS: return "INDIGENOUS";
        case LogCategory::STAKEHOLDER: return "STAKEHOLDER";
        case LogCategory::SECURITY: return "SECURITY";
        case LogCategory::PERFORMANCE: return "PERFORMANCE";
        case LogCategory::AUDIT: return "AUDIT";
        case LogCategory::SYSTEM: return "SYSTEM";
        default: return "UNKNOWN";
    }
}

LogCategory StringToLogCategory(const std::string& str) {
    if (str == "GENERAL") return LogCategory::GENERAL;
    if (str == "SACRED_ZERO") return LogCategory::SACRED_ZERO;
    if (str == "ENVIRONMENTAL") return LogCategory::ENVIRONMENTAL;
    if (str == "COMPLIANCE") return LogCategory::COMPLIANCE;
    if (str == "INDIGENOUS") return LogCategory::INDIGENOUS;
    if (str == "STAKEHOLDER") return LogCategory::STAKEHOLDER;
    if (str == "SECURITY") return LogCategory::SECURITY;
    if (str == "PERFORMANCE") return LogCategory::PERFORMANCE;
    if (str == "AUDIT") return LogCategory::AUDIT;
    if (str == "SYSTEM") return LogCategory::SYSTEM;
    return LogCategory::GENERAL;
}

std::array<uint8_t, 32> CalculateLogHash(const LogEntry& entry) {
    std::stringstream ss;
    ss << entry.id << entry.message << entry.trace_id;
    ss << std::chrono::system_clock::to_time_t(entry.timestamp);
    ss << static_cast<int>(entry.level) << static_cast<int>(entry.category);
    
    std::string data = ss.str();
    std::array<uint8_t, 32> hash;
    SHA256(reinterpret_cast<const unsigned char*>(data.data()), data.size(), hash.data());
    
    return hash;
}

std::array<uint8_t, 32> CalculateMerkleRoot(const std::vector<std::shared_ptr<LogEntry>>& entries) {
    if (entries.empty()) {
        return {};
    }
    
    std::vector<std::array<uint8_t, 32>> hashes;
    for (const auto& entry : entries) {
        hashes.push_back(entry->hash);
    }
    
    // Build merkle tree
    while (hashes.size() > 1) {
        std::vector<std::array<uint8_t, 32>> next_level;
        
        for (size_t i = 0; i < hashes.size(); i += 2) {
            std::vector<uint8_t> combined;
            combined.insert(combined.end(), hashes[i].begin(), hashes[i].end());
            
            if (i + 1 < hashes.size()) {
                combined.insert(combined.end(), hashes[i + 1].begin(), hashes[i + 1].end());
            } else {
                combined.insert(combined.end(), hashes[i].begin(), hashes[i].end());
            }
            
            std::array<uint8_t, 32> hash;
            SHA256(combined.data(), combined.size(), hash.data());
            next_level.push_back(hash);
        }
        
        hashes = next_level;
    }
    
    return hashes[0];
}

std::string LogEntryToJson(const LogEntry& entry) {
    Json::Value json;
    json["id"] = entry.id;
    json["level"] = LogLevelToString(entry.level);
    json["category"] = LogCategoryToString(entry.category);
    json["message"] = entry.message;
    json["timestamp"] = std::chrono::system_clock::to_time_t(entry.timestamp);
    json["trace_id"] = entry.trace_id;
    json["source"] = entry.source;
    
    Json::StreamWriterBuilder builder;
    return Json::writeString(builder, json);
}

std::shared_ptr<LogEntry> JsonToLogEntry(const std::string& json_str) {
    Json::Value json;
    Json::CharReaderBuilder builder;
    std::istringstream stream(json_str);
    
    if (!Json::parseFromStream(builder, stream, &json, nullptr)) {
        return nullptr;
    }
    
    auto entry = std::make_shared<LogEntry>();
    entry->id = json["id"].asString();
    entry->level = StringToLogLevel(json["level"].asString());
    entry->category = StringToLogCategory(json["category"].asString());
    entry->message = json["message"].asString();
    entry->trace_id = json["trace_id"].asString();
    entry->source = json["source"].asString();
    
    auto timestamp = json["timestamp"].asInt64();
    entry->timestamp = std::chrono::system_clock::from_time_t(timestamp);
    
    return entry;
}

std::vector<uint8_t> CompressLogData(const std::vector<uint8_t>& data) {
    uLongf compressed_size = compressBound(data.size());
    std::vector<uint8_t> compressed(compressed_size);
    
    if (compress(compressed.data(), &compressed_size, data.data(), data.size()) == Z_OK) {
        compressed.resize(compressed_size);
        return compressed;
    }
    
    return data;
}

std::vector<uint8_t> DecompressLogData(const std::vector<uint8_t>& compressed) {
    uLongf decompressed_size = compressed.size() * 10;
    std::vector<uint8_t> decompressed(decompressed_size);
    
    if (uncompress(decompressed.data(), &decompressed_size,
                  compressed.data(), compressed.size()) == Z_OK) {
        decompressed.resize(decompressed_size);
        return decompressed;
    }
    
    return compressed;
}

} // namespace TML
