/**
 * Sacred Zero Header - Detection and prevention of discrimination
 * 
 * Path: /sdk/cpp/sacred_zero.h
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This defines the Sacred Zero trigger system that detects and prevents
 * discrimination against protected characteristics, vulnerable populations,
 * and ecosystem stakeholders. It enforces immediate halt on violations.
 */

#ifndef TML_SACRED_ZERO_H
#define TML_SACRED_ZERO_H

#include <string>
#include <vector>
#include <map>
#include <set>
#include <memory>
#include <chrono>
#include <functional>
#include <optional>
#include <variant>

namespace TML {

// Forward declarations
class Config;
class DecisionContext;

/**
 * Protected characteristics under Sacred Zero
 */
enum class ProtectedCharacteristic {
    RACE,
    COLOR,
    RELIGION,
    SEX,
    NATIONAL_ORIGIN,
    DISABILITY,
    AGE,
    GENDER_IDENTITY,
    SEXUAL_ORIENTATION,
    GENETIC_INFORMATION,
    PREGNANCY,
    VETERAN_STATUS,
    POLITICAL_BELIEF,
    SOCIOECONOMIC_STATUS,
    EDUCATION_LEVEL,
    LANGUAGE,
    CITIZENSHIP_STATUS,
    CRIMINAL_HISTORY,
    MEDICAL_CONDITION,
    FAMILY_STATUS,
    // Ecosystem extensions
    SPECIES,
    HABITAT,
    ECOLOGICAL_ROLE,
    CONSERVATION_STATUS
};

/**
 * Types of Sacred Zero violations
 */
enum class ViolationType {
    DIRECT_DISCRIMINATION,      // Explicit discrimination
    INDIRECT_DISCRIMINATION,     // Disparate impact
    SYSTEMIC_BIAS,              // Pattern of bias
    INTERSECTIONAL_DISCRIMINATION, // Multiple characteristics
    ALGORITHMIC_BIAS,           // Model-based discrimination
    DATA_BIAS,                  // Training data issues
    REPRESENTATION_BIAS,        // Underrepresentation
    ENVIRONMENTAL_INJUSTICE,    // Disproportionate environmental harm
    INDIGENOUS_RIGHTS_VIOLATION, // Violation of indigenous sovereignty
    INTERGENERATIONAL_HARM,     // Harm to future generations
    ECOSYSTEM_DISCRIMINATION,    // Harm to non-human entities
    DIGNITY_VIOLATION,          // Human dignity compromise
    CONSENT_VIOLATION,          // Lack of informed consent
    ACCESSIBILITY_VIOLATION,    // Accessibility barriers
    PRIVACY_VIOLATION          // Privacy rights violation
};

/**
 * Severity levels for violations
 */
enum class ViolationSeverity {
    LOW,        // Minor impact, correctable
    MEDIUM,     // Moderate impact, requires review
    HIGH,       // Significant impact, immediate action
    CRITICAL,   // Severe impact, system intervention
    FATAL       // Catastrophic, immediate halt required
};

/**
 * Evidence types for violation detection
 */
struct Evidence {
    std::string type;
    std::variant<std::string, double, int, bool> value;
    double confidence;
    std::string source;
    std::chrono::system_clock::time_point timestamp;
};

/**
 * Statistical disparity metrics
 */
struct DisparityMetrics {
    double disparity_ratio;      // Ratio between groups
    double p_value;              // Statistical significance
    double effect_size;          // Magnitude of effect
    double confidence_interval_lower;
    double confidence_interval_upper;
    size_t sample_size;
    std::string statistical_test;
};

/**
 * Bias detection result
 */
struct BiasDetectionResult {
    bool bias_detected;
    ViolationType violation_type;
    std::vector<ProtectedCharacteristic> affected_characteristics;
    DisparityMetrics metrics;
    std::vector<Evidence> evidence;
    double confidence_score;
    std::string explanation;
};

/**
 * Evaluation context for Sacred Zero
 */
struct SacredZeroContext {
    std::string operation_id;
    std::string operation_type;
    std::map<std::string, std::variant<std::string, double, int, bool>> input_data;
    std::map<std::string, std::variant<std::string, double, int, bool>> output_data;
    std::vector<std::string> affected_groups;
    std::optional<std::string> model_id;
    std::optional<std::string> algorithm_type;
    std::chrono::system_clock::time_point timestamp;
};

/**
 * Sacred Zero evaluation result
 */
struct SacredZeroResult {
    bool triggered;
    ViolationType violation_type;
    ViolationSeverity severity;
    std::string description;
    std::map<std::string, std::variant<std::string, double, int, bool>> evidence;
    std::string required_action;
    bool must_halt;
    std::chrono::system_clock::time_point timestamp;
    std::string trace_id;
    std::vector<std::string> remediation_steps;
    std::optional<std::string> legal_reference;
};

/**
 * Fairness metrics for evaluation
 */
struct FairnessMetrics {
    double demographic_parity;
    double equal_opportunity;
    double equalized_odds;
    double disparate_impact;
    double statistical_parity;
    double conditional_demographic_disparity;
    double fairness_through_awareness;
    double counterfactual_fairness;
};

/**
 * Sacred Zero Trigger class
 * 
 * This class implements the core Sacred Zero detection logic,
 * evaluating decisions and operations for discriminatory patterns
 * and triggering immediate halt when violations are detected.
 */
class SacredZeroTrigger {
public:
    /**
     * Constructor with configuration
     * @param config Configuration settings
     */
    explicit SacredZeroTrigger(std::shared_ptr<Config> config);
    
    /**
     * Destructor
     */
    virtual ~SacredZeroTrigger();
    
    // Prevent copying
    SacredZeroTrigger(const SacredZeroTrigger&) = delete;
    SacredZeroTrigger& operator=(const SacredZeroTrigger&) = delete;
    
    // ========== Core Evaluation ==========
    
    /**
     * Evaluate a decision for Sacred Zero violations
     * @param context Decision context to evaluate
     * @return Evaluation result
     */
    SacredZeroResult Evaluate(const DecisionContext& context);
    
    /**
     * Evaluate with Sacred Zero context
     * @param context Sacred Zero specific context
     * @return Evaluation result
     */
    SacredZeroResult Evaluate(const SacredZeroContext& context);
    
    /**
     * Batch evaluation for multiple decisions
     * @param contexts Vector of contexts to evaluate
     * @return Vector of results
     */
    std::vector<SacredZeroResult> BatchEvaluate(const std::vector<SacredZeroContext>& contexts);
    
    // ========== Bias Detection ==========
    
    /**
     * Detect bias in data
     * @param data Input data to analyze
     * @param protected_attributes Attributes to check for bias
     * @return Bias detection result
     */
    BiasDetectionResult DetectBias(
        const std::map<std::string, std::vector<double>>& data,
        const std::vector<std::string>& protected_attributes);
    
    /**
     * Detect algorithmic bias
     * @param predictions Model predictions
     * @param ground_truth Actual outcomes
     * @param protected_attributes Protected attributes
     * @return Bias detection result
     */
    BiasDetectionResult DetectAlgorithmicBias(
        const std::vector<double>& predictions,
        const std::vector<double>& ground_truth,
        const std::vector<std::string>& protected_attributes);
    
    /**
     * Detect intersectional bias
     * @param data Input data
     * @param characteristic_combinations Combinations to check
     * @return Bias detection result
     */
    BiasDetectionResult DetectIntersectionalBias(
        const std::map<std::string, std::vector<double>>& data,
        const std::vector<std::vector<ProtectedCharacteristic>>& characteristic_combinations);
    
    // ========== Fairness Metrics ==========
    
    /**
     * Calculate fairness metrics
     * @param predictions Predictions or decisions
     * @param protected_attribute Protected attribute values
     * @param ground_truth Optional ground truth
     * @return Fairness metrics
     */
    FairnessMetrics CalculateFairnessMetrics(
        const std::vector<double>& predictions,
        const std::vector<int>& protected_attribute,
        const std::optional<std::vector<double>>& ground_truth = std::nullopt);
    
    /**
     * Check if fairness thresholds are violated
     * @param metrics Fairness metrics to check
     * @return True if any threshold violated
     */
    bool CheckFairnessThresholds(const FairnessMetrics& metrics);
    
    // ========== Vulnerable Population Protection ==========
    
    /**
     * Check if decision affects vulnerable population
     * @param context Decision context
     * @return True if vulnerable population affected
     */
    bool AffectsVulnerablePopulation(const SacredZeroContext& context);
    
    /**
     * Get enhanced protection requirements for vulnerable groups
     * @param group_identifier Group identifier
     * @return Enhanced protection requirements
     */
    std::map<std::string, std::string> GetEnhancedProtectionRequirements(
        const std::string& group_identifier);
    
    // ========== Ecosystem Protection ==========
    
    /**
     * Evaluate ecosystem impact
     * @param context Decision context
     * @return True if ecosystem harm detected
     */
    bool EvaluateEcosystemImpact(const SacredZeroContext& context);
    
    /**
     * Check future generation impact
     * @param context Decision context
     * @param years_ahead Number of years to project
     * @return Impact score (0-1, higher is worse)
     */
    double AssessFutureGenerationImpact(const SacredZeroContext& context, int years_ahead = 100);
    
    // ========== Configuration and Thresholds ==========
    
    /**
     * Set discrimination threshold
     * @param threshold Threshold value (0-1)
     */
    void SetDiscriminationThreshold(double threshold);
    
    /**
     * Get current discrimination threshold
     * @return Current threshold
     */
    double GetDiscriminationThreshold() const;
    
    /**
     * Add protected characteristic
     * @param characteristic Characteristic to add
     */
    void AddProtectedCharacteristic(ProtectedCharacteristic characteristic);
    
    /**
     * Remove protected characteristic
     * @param characteristic Characteristic to remove
     */
    void RemoveProtectedCharacteristic(ProtectedCharacteristic characteristic);
    
    /**
     * Get all protected characteristics
     * @return Set of protected characteristics
     */
    std::set<ProtectedCharacteristic> GetProtectedCharacteristics() const;
    
    // ========== Callbacks and Monitoring ==========
    
    /**
     * Register callback for violations
     * @param callback Function to call on violation
     */
    void OnViolation(std::function<void(const SacredZeroResult&)> callback);
    
    /**
     * Register callback for near-violations (warnings)
     * @param callback Function to call on warning
     */
    void OnWarning(std::function<void(const SacredZeroResult&)> callback);
    
    /**
     * Get violation statistics
     * @return Map of statistic name to value
     */
    std::map<std::string, double> GetStatistics() const;
    
    /**
     * Reset statistics
     */
    void ResetStatistics();
    
    // ========== Emergency Response ==========
    
    /**
     * Trigger emergency halt
     * @param reason Reason for emergency halt
     * @return True if halt successful
     */
    bool EmergencyHalt(const std::string& reason);
    
    /**
     * Check if system is in halted state
     * @return True if halted
     */
    bool IsHalted() const;
    
    /**
     * Resume from halt (requires authorization)
     * @param authorization_token Authorization token
     * @return True if resume successful
     */
    bool ResumeFromHalt(const std::string& authorization_token);
    
    // ========== Audit and Compliance ==========
    
    /**
     * Generate audit report
     * @param start_time Start of audit period
     * @param end_time End of audit period
     * @return Audit report as JSON string
     */
    std::string GenerateAuditReport(
        std::chrono::system_clock::time_point start_time,
        std::chrono::system_clock::time_point end_time);
    
    /**
     * Export violation history
     * @param limit Maximum number of violations to export
     * @return Vector of historical violations
     */
    std::vector<SacredZeroResult> ExportViolationHistory(size_t limit = 1000);
    
    /**
     * Verify Sacred Zero integrity
     * @return True if integrity check passes
     */
    bool VerifyIntegrity() const;
    
    // ========== Testing and Validation ==========
    
    /**
     * Run self-test
     * @return Map of test name to pass/fail
     */
    std::map<std::string, bool> RunSelfTest();
    
    /**
     * Simulate violation for testing
     * @param violation_type Type of violation to simulate
     * @return Simulated result
     */
    SacredZeroResult SimulateViolation(ViolationType violation_type);
    
    /**
     * Validate configuration
     * @return True if configuration valid
     */
    bool ValidateConfiguration() const;
    
private:
    class Impl;
    std::unique_ptr<Impl> pImpl;
};

// ========== Helper Functions ==========

/**
 * Convert violation type to string
 * @param type Violation type
 * @return String representation
 */
std::string ViolationTypeToString(ViolationType type);

/**
 * Convert string to violation type
 * @param str String representation
 * @return Violation type
 */
ViolationType StringToViolationType(const std::string& str);

/**
 * Get severity of violation type
 * @param type Violation type
 * @return Severity level
 */
ViolationSeverity GetViolationSeverity(ViolationType type);

/**
 * Check if characteristic is protected
 * @param characteristic Characteristic to check
 * @return True if protected
 */
bool IsProtectedCharacteristic(const std::string& characteristic);

/**
 * Calculate disparate impact ratio
 * @param group1_positive Group 1 positive rate
 * @param group2_positive Group 2 positive rate
 * @return Disparate impact ratio
 */
double CalculateDisparateImpact(double group1_positive, double group2_positive);

/**
 * Perform statistical parity test
 * @param group1_outcomes Outcomes for group 1
 * @param group2_outcomes Outcomes for group 2
 * @return P-value from statistical test
 */
double StatisticalParityTest(const std::vector<double>& group1_outcomes,
                             const std::vector<double>& group2_outcomes);

} // namespace TML

#endif // TML_SACRED_ZERO_H
