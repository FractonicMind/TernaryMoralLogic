/**
 * TML C++ Client Header - Main client interface for TML SDK
 * 
 * Path: /sdk/cpp/tml_client.h
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This provides the main C++ interface for TML operations including
 * Sacred Zero enforcement, Always Memory logging, environmental
 * monitoring, and multi-stakeholder governance.
 */

#ifndef TML_CLIENT_H
#define TML_CLIENT_H

#include <string>
#include <vector>
#include <map>
#include <memory>
#include <chrono>
#include <functional>
#include <atomic>
#include <optional>
#include <variant>

namespace TML {

// Forward declarations
class SacredZeroTrigger;
class AlwaysMemoryLogger;
class GuardianConnection;
class Config;
class TMLError;

// Type aliases for clarity
using Timestamp = std::chrono::system_clock::time_point;
using Duration = std::chrono::milliseconds;
using Metadata = std::map<std::string, std::variant<std::string, double, int, bool>>;

/**
 * Environment enumeration for deployment contexts
 */
enum class Environment {
    PRODUCTION,
    STAGING,
    DEVELOPMENT
};

/**
 * Log levels for Always Memory
 */
enum class LogLevel {
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL,
    FATAL
};

/**
 * Stakeholder types for multi-stakeholder governance
 */
enum class StakeholderType {
    HUMAN_COMMUNITY,
    INDIGENOUS_COMMUNITY,
    NON_HUMAN_ENTITIES,
    FUTURE_GENERATIONS,
    ECOSYSTEM
};

/**
 * Compliance framework identifiers
 */
enum class ComplianceFramework {
    GDPR,
    CCPA,
    EU_AI_ACT,
    UN_HUMAN_RIGHTS,
    PARIS_AGREEMENT,
    CBD,  // Convention on Biological Diversity
    UNDRIP,  // UN Declaration on Rights of Indigenous Peoples
    CUSTOM
};

/**
 * Resource usage tracking for environmental impact
 */
struct ResourceUsage {
    int cpu_cores;
    int gpu_count;
    double memory_gb;
    double storage_gb;
    double network_gbps;
    Duration duration;
    std::string data_center;
    double carbon_intensity;  // kg CO2 per kWh
};

/**
 * Environmental impact metrics
 */
struct EnvironmentalImpact {
    double carbon_kg;
    double water_liters;
    double energy_kwh;
    double e_waste_kg;
    double renewable_percentage;
    bool exceeds_threshold;
    std::vector<std::string> mitigations;
};

/**
 * Stakeholder representation for decisions
 */
struct Stakeholder {
    StakeholderType type;
    std::string name;
    std::string impact_description;
    double weight;
    bool consent_given;
    std::optional<std::string> consent_conditions;
};

/**
 * Decision context for multi-stakeholder evaluation
 */
struct DecisionContext {
    std::string operation_type;
    std::string description;
    std::vector<Stakeholder> stakeholders;
    Metadata metadata;
    std::optional<std::string> location;
    Timestamp timestamp;
};

/**
 * Sacred Zero evaluation result
 */
struct SacredZeroResult {
    bool triggered;
    std::string violation_type;
    std::string description;
    Metadata evidence;
    std::string required_action;
    bool must_halt;
    Timestamp timestamp;
    std::string trace_id;
};

/**
 * Connection status information
 */
struct ConnectionStatus {
    bool connected;
    std::string guardian_url;
    int active_guardians;
    bool tee_available;
    Environment environment;
    std::chrono::milliseconds latency;
    double uptime_percentage;
};

/**
 * Compliance report structure
 */
struct ComplianceReport {
    std::string period;
    std::map<ComplianceFramework, std::string> framework_status;
    int total_evaluations;
    int violations_detected;
    int violations_prevented;
    EnvironmentalImpact cumulative_impact;
    std::vector<SacredZeroResult> sacred_zero_events;
    Metadata additional_metrics;
};

/**
 * Main TML Client class
 * 
 * This is the primary interface for all TML operations. It manages
 * connections to the Guardian Network, enforces Sacred Zero rules,
 * maintains Always Memory logs, and coordinates multi-stakeholder
 * governance.
 */
class TMLClient {
public:
    /**
     * Constructor with configuration
     * @param config Configuration object (if nullptr, uses default)
     */
    explicit TMLClient(std::shared_ptr<Config> config = nullptr);
    
    /**
     * Destructor - ensures clean shutdown
     */
    virtual ~TMLClient();
    
    // Prevent copying to ensure single instance per context
    TMLClient(const TMLClient&) = delete;
    TMLClient& operator=(const TMLClient&) = delete;
    
    // Allow moving
    TMLClient(TMLClient&&) noexcept;
    TMLClient& operator=(TMLClient&&) noexcept;
    
    // ========== Connection Management ==========
    
    /**
     * Connect to Guardian Network
     * @return true if connection successful
     */
    bool Connect();
    
    /**
     * Connect with timeout
     * @param timeout Maximum time to wait for connection
     * @return true if connection successful
     */
    bool ConnectWithTimeout(Duration timeout);
    
    /**
     * Disconnect from Guardian Network
     */
    void Disconnect();
    
    /**
     * Check if connected to Guardian Network
     * @return true if connected
     */
    bool IsConnected() const;
    
    /**
     * Get current connection status
     * @return Connection status information
     */
    ConnectionStatus GetStatus() const;
    
    // ========== Sacred Zero Operations ==========
    
    /**
     * Evaluate an operation for Sacred Zero violations
     * @param context Decision context to evaluate
     * @return Sacred Zero evaluation result
     */
    SacredZeroResult EvaluateSacredZero(const DecisionContext& context);
    
    /**
     * Register a Sacred Zero trigger callback
     * @param callback Function to call when Sacred Zero triggered
     */
    void OnSacredZeroTrigger(std::function<void(const SacredZeroResult&)> callback);
    
    /**
     * Get Sacred Zero statistics
     * @return Map of statistic name to value
     */
    std::map<std::string, double> GetSacredZeroStatistics() const;
    
    // ========== Always Memory Logging ==========
    
    /**
     * Log a message to Always Memory
     * @param level Log level
     * @param message Log message
     * @param metadata Additional metadata
     */
    void Log(LogLevel level, const std::string& message, const Metadata& metadata = {});
    
    /**
     * Log environmental impact
     * @param resources Resource usage information
     * @return Calculated environmental impact
     */
    EnvironmentalImpact LogEnvironmentalImpact(const ResourceUsage& resources);
    
    /**
     * Log compliance event
     * @param framework Compliance framework
     * @param status Compliance status
     * @param details Additional details
     */
    void LogCompliance(ComplianceFramework framework, 
                       const std::string& status,
                       const Metadata& details = {});
    
    /**
     * Log indigenous data governance event
     * @param data_type Type of indigenous data
     * @param community Community name
     * @param consent_type Type of consent obtained
     * @param restrictions Usage restrictions
     */
    void LogIndigenousData(const std::string& data_type,
                           const std::string& community,
                           const std::string& consent_type,
                           const std::vector<std::string>& restrictions);
    
    /**
     * Flush all pending logs to Guardian Network
     * @return true if flush successful
     */
    bool FlushLogs();
    
    // ========== Environmental Monitoring ==========
    
    /**
     * Calculate environmental impact for an operation
     * @param resources Resource usage information
     * @return Environmental impact metrics
     */
    EnvironmentalImpact CalculateEnvironmentalImpact(const ResourceUsage& resources);
    
    /**
     * Check if environmental thresholds exceeded
     * @param impact Environmental impact to check
     * @return true if any threshold exceeded
     */
    bool CheckEnvironmentalThresholds(const EnvironmentalImpact& impact);
    
    /**
     * Get suggested mitigations for environmental impact
     * @param impact Environmental impact to mitigate
     * @return List of mitigation suggestions
     */
    std::vector<std::string> SuggestMitigations(const EnvironmentalImpact& impact);
    
    // ========== Multi-stakeholder Governance ==========
    
    /**
     * Evaluate decision across all stakeholders
     * @param context Decision context with stakeholders
     * @return Map of stakeholder name to impact assessment
     */
    std::map<std::string, double> EvaluateMultiStakeholder(const DecisionContext& context);
    
    /**
     * Check if indigenous consent required
     * @param data_type Type of data being processed
     * @param location Geographic location
     * @return true if indigenous consent required
     */
    bool RequiresIndigenousConsent(const std::string& data_type,
                                   const std::string& location);
    
    /**
     * Register stakeholder feedback
     * @param stakeholder_type Type of stakeholder
     * @param feedback Feedback content
     * @param impact_score Numeric impact score
     */
    void RegisterStakeholderFeedback(StakeholderType stakeholder_type,
                                     const std::string& feedback,
                                     double impact_score);
    
    // ========== Compliance and Reporting ==========
    
    /**
     * Generate compliance report
     * @param start_time Report start time
     * @param end_time Report end time
     * @return Compliance report
     */
    ComplianceReport GenerateComplianceReport(Timestamp start_time,
                                             Timestamp end_time);
    
    /**
     * Submit compliance report to regulators
     * @param report Report to submit
     * @param framework Target regulatory framework
     * @return Submission ID
     */
    std::string SubmitComplianceReport(const ComplianceReport& report,
                                       ComplianceFramework framework);
    
    /**
     * Perform compliance audit
     * @param framework Framework to audit against
     * @return Audit results
     */
    std::map<std::string, bool> PerformAudit(ComplianceFramework framework);
    
    // ========== Error Handling ==========
    
    /**
     * Get last error
     * @return Last error or nullptr if no error
     */
    std::shared_ptr<TMLError> GetLastError() const;
    
    /**
     * Clear error state
     */
    void ClearError();
    
    /**
     * Set error callback
     * @param callback Function to call on error
     */
    void OnError(std::function<void(const TMLError&)> callback);
    
    // ========== Configuration ==========
    
    /**
     * Get current configuration
     * @return Current configuration
     */
    std::shared_ptr<Config> GetConfig() const;
    
    /**
     * Update configuration (requires reconnection)
     * @param config New configuration
     * @return true if update successful
     */
    bool UpdateConfig(std::shared_ptr<Config> config);
    
    /**
     * Enable audit mode
     * @param enable true to enable, false to disable
     */
    void SetAuditMode(bool enable);
    
    // ========== Monitoring and Metrics ==========
    
    /**
     * Get performance metrics
     * @return Map of metric name to value
     */
    std::map<std::string, double> GetMetrics() const;
    
    /**
     * Subscribe to real-time events
     * @param event_types Types of events to subscribe to
     * @param callback Function to call for each event
     * @return Subscription ID
     */
    std::string SubscribeToEvents(const std::vector<std::string>& event_types,
                                  std::function<void(const Metadata&)> callback);
    
    /**
     * Unsubscribe from events
     * @param subscription_id Subscription to cancel
     */
    void UnsubscribeFromEvents(const std::string& subscription_id);
    
    // ========== Utility Functions ==========
    
    /**
     * Get SDK version
     * @return Version string
     */
    static std::string GetVersion();
    
    /**
     * Check if running in Trusted Execution Environment
     * @return true if TEE available
     */
    static bool IsTEEAvailable();
    
    /**
     * Generate unique trace ID for operations
     * @return Unique trace ID
     */
    static std::string GenerateTraceID();
    
private:
    class Impl;
    std::unique_ptr<Impl> pImpl;  // PIMPL idiom for ABI stability
};

} // namespace TML

#endif // TML_CLIENT_H
