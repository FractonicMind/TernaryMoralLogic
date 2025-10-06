/**
 * Always Memory Header - Immutable logging and audit trail system
 * 
 * Path: /sdk/cpp/always_memory.h
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This defines the Always Memory logging system that creates immutable,
 * cryptographically secured audit trails for all TML operations including
 * Sacred Zero triggers, environmental impacts, and stakeholder decisions.
 */

#ifndef TML_ALWAYS_MEMORY_H
#define TML_ALWAYS_MEMORY_H

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <chrono>
#include <functional>
#include <optional>
#include <variant>
#include <queue>
#include <array>

namespace TML {

// Forward declarations
class Config;
class GuardianConnection;

/**
 * Log levels for Always Memory
 */
enum class LogLevel {
    DEBUG = 0,
    INFO = 1,
    WARNING = 2,
    ERROR = 3,
    CRITICAL = 4,
    FATAL = 5     // Sacred Zero violations
};

/**
 * Log categories for classification
 */
enum class LogCategory {
    GENERAL,
    SACRED_ZERO,
    ENVIRONMENTAL,
    COMPLIANCE,
    INDIGENOUS,
    STAKEHOLDER,
    SECURITY,
    PERFORMANCE,
    AUDIT,
    SYSTEM
};

/**
 * Metadata type for flexible log data
 */
using LogMetadata = std::map<std::string, std::variant<std::string, double, int, bool>>;

/**
 * Base log entry structure
 */
struct LogEntry {
    std::string id;
    LogLevel level;
    LogCategory category;
    std::string message;
    LogMetadata metadata;
    std::chrono::system_clock::time_point timestamp;
    std::string trace_id;
    std::optional<std::string> parent_id;
    std::string source;
    std::array<uint8_t, 32> hash;  // SHA-256 hash
};

/**
 * Environmental log entry
 */
struct EnvironmentalLogEntry : public LogEntry {
    double carbon_kg;
    double water_liters;
    double energy_kwh;
    double e_waste_kg;
    std::string data_center;
    std::chrono::milliseconds duration;
    std::vector<std::string> mitigation_applied;
};

/**
 * Compliance log entry
 */
struct ComplianceLogEntry : public LogEntry {
    std::string framework;
    std::string requirement;
    std::string status;  // COMPLIANT, NON_COMPLIANT, PARTIAL
    std::map<std::string, std::string> evidence;
    std::optional<std::string> violation_id;
    std::vector<std::string> remediation_steps;
};

/**
 * Indigenous data log entry
 */
struct IndigenousDataLogEntry : public LogEntry {
    std::string data_type;
    std::string community;
    std::string consent_type;  // FPIC, Standard, Emergency
    std::chrono::system_clock::time_point consent_date;
    std::string purpose;
    std::vector<std::string> restrictions;
    std::optional<std::chrono::system_clock::time_point> expiry;
};

/**
 * Stakeholder decision log entry
 */
struct StakeholderLogEntry : public LogEntry {
    std::string stakeholder_type;
    std::string stakeholder_name;
    std::string decision_type;
    double impact_score;
    bool consent_given;
    std::map<std::string, std::string> conditions;
    std::vector<std::string> affected_parties;
};

/**
 * Log storage options
 */
struct StorageOptions {
    bool local_enabled;
    std::string local_path;
    size_t max_local_size_bytes;
    bool compress_logs;
    bool encrypt_at_rest;
    std::chrono::seconds retention_period;
    bool blockchain_anchor;
    std::string blockchain_network;
};

/**
 * Log batch for efficient transmission
 */
struct LogBatch {
    std::string batch_id;
    std::vector<std::shared_ptr<LogEntry>> entries;
    std::chrono::system_clock::time_point created_at;
    size_t total_size_bytes;
    std::array<uint8_t, 32> merkle_root;
};

/**
 * Guardian receipt for log submission
 */
struct GuardianReceipt {
    std::string receipt_id;
    std::string batch_id;
    std::chrono::system_clock::time_point received_at;
    std::string guardian_node;
    std::array<uint8_t, 64> signature;  // Ed25519 signature
    std::optional<std::string> blockchain_tx_id;
    bool verified;
};

/**
 * Log query filters
 */
struct LogQuery {
    std::optional<std::chrono::system_clock::time_point> start_time;
    std::optional<std::chrono::system_clock::time_point> end_time;
    std::optional<LogLevel> min_level;
    std::optional<LogCategory> category;
    std::optional<std::string> trace_id;
    std::optional<std::string> search_text;
    std::map<std::string, std::string> metadata_filters;
    size_t limit{1000};
    size_t offset{0};
};

/**
 * Log statistics
 */
struct LogStatistics {
    uint64_t total_logs;
    uint64_t logs_by_level[6];  // DEBUG through FATAL
    uint64_t logs_by_category[10];
    uint64_t sacred_zero_violations;
    uint64_t environmental_logs;
    uint64_t compliance_logs;
    uint64_t indigenous_data_logs;
    size_t total_size_bytes;
    size_t compressed_size_bytes;
    double average_latency_ms;
    double success_rate;
};

/**
 * Always Memory Logger class
 * 
 * This class implements the immutable logging system that records all
 * TML operations, ensuring complete audit trails for compliance,
 * debugging, and accountability. All logs are cryptographically
 * secured and anchored to prevent tampering.
 */
class AlwaysMemoryLogger {
public:
    /**
     * Constructor with configuration
     * @param config Configuration settings
     */
    explicit AlwaysMemoryLogger(std::shared_ptr<Config> config);
    
    /**
     * Destructor - ensures all logs are flushed
     */
    virtual ~AlwaysMemoryLogger();
    
    // Prevent copying
    AlwaysMemoryLogger(const AlwaysMemoryLogger&) = delete;
    AlwaysMemoryLogger& operator=(const AlwaysMemoryLogger&) = delete;
    
    // ========== Core Logging ==========
    
    /**
     * Log a standard entry
     * @param entry Log entry to record
     * @return Log ID
     */
    std::string Log(const LogEntry& entry);
    
    /**
     * Log with level and message
     * @param level Log level
     * @param message Log message
     * @param metadata Optional metadata
     * @return Log ID
     */
    std::string Log(LogLevel level, const std::string& message, 
                    const LogMetadata& metadata = {});
    
    /**
     * Log environmental impact
     * @param entry Environmental log entry
     * @return Log ID
     */
    std::string LogEnvironmental(const EnvironmentalLogEntry& entry);
    
    /**
     * Log compliance event
     * @param entry Compliance log entry
     * @return Log ID
     */
    std::string LogCompliance(const ComplianceLogEntry& entry);
    
    /**
     * Log indigenous data governance
     * @param entry Indigenous data log entry
     * @return Log ID
     */
    std::string LogIndigenous(const IndigenousDataLogEntry& entry);
    
    /**
     * Log stakeholder decision
     * @param entry Stakeholder log entry
     * @return Log ID
     */
    std::string LogStakeholder(const StakeholderLogEntry& entry);
    
    // ========== Batch Operations ==========
    
    /**
     * Create a new batch
     * @return Batch ID
     */
    std::string CreateBatch();
    
    /**
     * Add log to batch
     * @param batch_id Batch to add to
     * @param entry Log entry
     * @return True if added successfully
     */
    bool AddToBatch(const std::string& batch_id, const LogEntry& entry);
    
    /**
     * Commit batch to Guardian Network
     * @param batch_id Batch to commit
     * @return Guardian receipt
     */
    std::optional<GuardianReceipt> CommitBatch(const std::string& batch_id);
    
    /**
     * Get pending batch size
     * @param batch_id Batch ID
     * @return Number of entries in batch
     */
    size_t GetBatchSize(const std::string& batch_id) const;
    
    // ========== Storage Management ==========
    
    /**
     * Store logs locally
     * @param entry Log entry to store
     * @param metadata Additional metadata
     * @return True if stored successfully
     */
    bool StoreLocal(LogLevel level, const std::string& message, 
                    const LogMetadata& metadata = {});
    
    /**
     * Flush all pending logs to Guardian Network
     * @return True if all logs flushed successfully
     */
    bool Flush();
    
    /**
     * Force immediate flush (bypasses batching)
     * @return True if flush successful
     */
    bool ForceFlush();
    
    /**
     * Get storage options
     * @return Current storage options
     */
    StorageOptions GetStorageOptions() const;
    
    /**
     * Update storage options
     * @param options New storage options
     */
    void SetStorageOptions(const StorageOptions& options);
    
    // ========== Query and Retrieval ==========
    
    /**
     * Query logs
     * @param query Query parameters
     * @return Vector of matching log entries
     */
    std::vector<std::shared_ptr<LogEntry>> Query(const LogQuery& query);
    
    /**
     * Get log by ID
     * @param log_id Log ID
     * @return Log entry or nullptr if not found
     */
    std::shared_ptr<LogEntry> GetLog(const std::string& log_id);
    
    /**
     * Get logs by trace ID
     * @param trace_id Trace ID
     * @return Vector of related log entries
     */
    std::vector<std::shared_ptr<LogEntry>> GetLogsByTrace(const std::string& trace_id);
    
    /**
     * Export logs to file
     * @param filename Export file path
     * @param query Query to filter logs
     * @return True if export successful
     */
    bool ExportLogs(const std::string& filename, const LogQuery& query);
    
    // ========== Verification and Integrity ==========
    
    /**
     * Verify log integrity
     * @param log_id Log ID to verify
     * @return True if log intact
     */
    bool VerifyLogIntegrity(const std::string& log_id);
    
    /**
     * Verify batch integrity
     * @param batch_id Batch ID to verify
     * @return True if batch intact
     */
    bool VerifyBatchIntegrity(const std::string& batch_id);
    
    /**
     * Get log hash
     * @param log_id Log ID
     * @return SHA-256 hash
     */
    std::array<uint8_t, 32> GetLogHash(const std::string& log_id);
    
    /**
     * Get merkle proof for log
     * @param log_id Log ID
     * @return Merkle proof path
     */
    std::vector<std::array<uint8_t, 32>> GetMerkleProof(const std::string& log_id);
    
    // ========== Guardian Network ==========
    
    /**
     * Connect to Guardian Network
     * @return True if connection successful
     */
    bool ConnectToGuardian();
    
    /**
     * Check Guardian connection
     * @return True if connected
     */
    bool IsConnectedToGuardian() const;
    
    /**
     * Get Guardian receipt for log
     * @param log_id Log ID
     * @return Guardian receipt or nullopt
     */
    std::optional<GuardianReceipt> GetGuardianReceipt(const std::string& log_id);
    
    /**
     * Verify Guardian signature
     * @param receipt Receipt to verify
     * @return True if signature valid
     */
    bool VerifyGuardianSignature(const GuardianReceipt& receipt);
    
    // ========== Blockchain Anchoring ==========
    
    /**
     * Enable Blockchain anchoring
     * @param network Blockchain network to use
     * @param interval Anchoring interval
     */
    void EnableBlockchainAnchoring(const std::string& network,
                                   std::chrono::seconds interval);
    
    /**
     * Get Blockchain transaction for log
     * @param log_id Log ID
     * @return Transaction ID or nullopt
     */
    std::optional<std::string> GetBlockchainTransaction(const std::string& log_id);
    
    /**
     * Verify Blockchain anchor
     * @param log_id Log ID
     * @return True if anchor valid
     */
    bool VerifyBlockchainAnchor(const std::string& log_id);
    
    // ========== Statistics and Monitoring ==========
    
    /**
     * Get logging statistics
     * @return Current statistics
     */
    LogStatistics GetStatistics() const;
    
    /**
     * Reset statistics
     */
    void ResetStatistics();
    
    /**
     * Set log callback
     * @param callback Function to call for each log
     */
    void OnLog(std::function<void(const LogEntry&)> callback);
    
    /**
     * Set error callback
     * @param callback Function to call on error
     */
    void OnError(std::function<void(const std::string&)> callback);
    
    // ========== Configuration ==========
    
    /**
     * Get current configuration
     * @return Configuration
     */
    std::shared_ptr<Config> GetConfig() const;
    
    /**
     * Update configuration
     * @param config New configuration
     */
    void UpdateConfig(std::shared_ptr<Config> config);
    
    /**
     * Enable audit mode (maximum verbosity)
     * @param enable True to enable
     */
    void SetAuditMode(bool enable);
    
    /**
     * Set minimum log level
     * @param level Minimum level to log
     */
    void SetMinimumLevel(LogLevel level);
    
    // ========== Emergency Functions ==========
    
    /**
     * Log Sacred Zero violation (highest priority)
     * @param violation Description of violation
     * @param evidence Evidence data
     * @return Log ID
     */
    std::string LogSacredZeroViolation(const std::string& violation,
                                       const LogMetadata& evidence);
    
    /**
     * Emergency dump all logs
     * @param reason Reason for dump
     * @return Path to dump file
     */
    std::string EmergencyDump(const std::string& reason);
    
    /**
     * Seal logs (make immutable)
     * @param start_time Start of period to seal
     * @param end_time End of period to seal
     * @return Seal ID
     */
    std::string SealLogs(std::chrono::system_clock::time_point start_time,
                         std::chrono::system_clock::time_point end_time);
    
    // ========== Testing and Validation ==========
    
    /**
     * Run self-test
     * @return Map of test name to pass/fail
     */
    std::map<std::string, bool> RunSelfTest();
    
    /**
     * Validate configuration
     * @return True if configuration valid
     */
    bool ValidateConfiguration() const;
    
    /**
     * Test Guardian connection
     * @return Latency in milliseconds or -1 if failed
     */
    double TestGuardianConnection();
    
private:
    class Impl;
    std::unique_ptr<Impl> pImpl;
};

// ========== Helper Functions ==========

/**
 * Convert log level to string
 * @param level Log level
 * @return String representation
 */
std::string LogLevelToString(LogLevel level);

/**
 * Convert string to log level
 * @param str String representation
 * @return Log level
 */
LogLevel StringToLogLevel(const std::string& str);

/**
 * Convert log category to string
 * @param category Log category
 * @return String representation
 */
std::string LogCategoryToString(LogCategory category);

/**
 * Convert string to log category
 * @param str String representation
 * @return Log category
 */
LogCategory StringToLogCategory(const std::string& str);

/**
 * Calculate SHA-256 hash of log entry
 * @param entry Log entry
 * @return SHA-256 hash
 */
std::array<uint8_t, 32> CalculateLogHash(const LogEntry& entry);

/**
 * Calculate merkle root of log batch
 * @param entries Vector of log entries
 * @return Merkle root hash
 */
std::array<uint8_t, 32> CalculateMerkleRoot(const std::vector<std::shared_ptr<LogEntry>>& entries);

/**
 * Format log entry as JSON
 * @param entry Log entry
 * @return JSON string
 */
std::string LogEntryToJson(const LogEntry& entry);

/**
 * Parse log entry from JSON
 * @param json JSON string
 * @return Log entry or nullptr if parse failed
 */
std::shared_ptr<LogEntry> JsonToLogEntry(const std::string& json);

/**
 * Compress log data
 * @param data Data to compress
 * @return Compressed data
 */
std::vector<uint8_t> CompressLogData(const std::vector<uint8_t>& data);

/**
 * Decompress log data
 * @param compressed Compressed data
 * @return Decompressed data
 */
std::vector<uint8_t> DecompressLogData(const std::vector<uint8_t>& compressed);

} // namespace TML

#endif // TML_ALWAYS_MEMORY_H
