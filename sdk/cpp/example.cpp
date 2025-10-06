/**
 * TML C++ SDK Examples - Comprehensive usage examples
 * 
 * Path: /sdk/cpp/example.cpp
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This demonstrates practical usage of the TML C++ SDK including
 * Sacred Zero detection, Always Memory logging, environmental
 * monitoring, and multi-stakeholder governance.
 */

#include "tml_client.h"
#include "sacred_zero.h"
#include "always_memory.h"
#include <iostream>
#include <iomanip>
#include <thread>
#include <chrono>
#include <vector>
#include <map>
#include <algorithm>
#include <random>

using namespace TML;
using namespace std::chrono_literals;

// ========== Example 1: Basic Setup and Connection ==========

void Example1_BasicSetup() {
    std::cout << "\n=== Example 1: Basic TML Client Setup ===" << std::endl;
    
    // Create configuration
    auto config = std::make_shared<Config>();
    config->guardian_url = "https://guardian.tml-network.org";
    config->environment = Environment::PRODUCTION;
    config->discrimination_threshold = 0.2;
    config->carbon_threshold_kg = 1000.0;
    config->water_threshold_liters = 10000.0;
    config->indigenous_data_sovereignty = true;
    
    // Create TML client
    TMLClient client(config);
    
    // Connect to Guardian Network
    std::cout << "Connecting to Guardian Network..." << std::endl;
    if (client.Connect()) {
        std::cout << "✓ Connected successfully" << std::endl;
        
        // Get connection status
        auto status = client.GetStatus();
        std::cout << "Guardian URL: " << status.guardian_url << std::endl;
        std::cout << "Active Guardians: " << status.active_guardians << std::endl;
        std::cout << "TEE Available: " << (status.tee_available ? "Yes" : "No") << std::endl;
        std::cout << "Environment: " << (status.environment == Environment::PRODUCTION ? 
                                         "Production" : "Development") << std::endl;
    } else {
        std::cout << "✗ Connection failed" << std::endl;
        auto error = client.GetLastError();
        if (error) {
            std::cout << "Error: " << error->message << std::endl;
        }
    }
    
    // Disconnect
    client.Disconnect();
    std::cout << "Disconnected from Guardian Network" << std::endl;
}

// ========== Example 2: Sacred Zero in Hiring Algorithm ==========

void Example2_HiringAlgorithm() {
    std::cout << "\n=== Example 2: Sacred Zero in Hiring Algorithm ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    TMLClient client(config);
    client.Connect();
    
    // Simulate candidate evaluation data
    struct Candidate {
        std::string id;
        std::string name;
        double score;
        std::map<std::string, std::variant<std::string, double, int, bool>> attributes;
    };
    
    std::vector<Candidate> candidates = {
        {"C001", "Alice Johnson", 85.5, {
            {"education", std::string("MIT")},
            {"experience_years", 5},
            {"gender", std::string("female")},
            {"race", std::string("african_american")}
        }},
        {"C002", "Bob Smith", 82.3, {
            {"education", std::string("Stanford")},
            {"experience_years", 5},
            {"gender", std::string("male")},
            {"race", std::string("caucasian")}
        }},
        {"C003", "Chen Wei", 87.1, {
            {"education", std::string("Berkeley")},
            {"experience_years", 6},
            {"gender", std::string("female")},
            {"race", std::string("asian")}
        }}
    };
    
    std::cout << "Evaluating " << candidates.size() << " candidates for bias..." << std::endl;
    
    for (const auto& candidate : candidates) {
        // Create decision context
        DecisionContext context;
        context.operation_type = "hiring_decision";
        context.description = "Senior Developer Position";
        context.metadata = candidate.attributes;
        context.metadata["score"] = candidate.score;
        context.timestamp = std::chrono::system_clock::now();
        
        // Add stakeholders
        context.stakeholders.push_back({
            StakeholderType::HUMAN_COMMUNITY,
            candidate.name,
            "Hiring decision impact",
            1.0,
            false,
            std::nullopt
        });
        
        // Evaluate for Sacred Zero violations
        auto result = client.EvaluateSacredZero(context);
        
        std::cout << "\nCandidate: " << candidate.name << " (Score: " << candidate.score << ")" << std::endl;
        
        if (result.triggered) {
            std::cout << "  ⚠️  SACRED ZERO VIOLATION DETECTED!" << std::endl;
            std::cout << "  Type: " << ViolationTypeToString(result.violation_type) << std::endl;
            std::cout << "  Description: " << result.description << std::endl;
            std::cout << "  Required Action: " << result.required_action << std::endl;
            
            if (result.must_halt) {
                std::cout << "  🛑 SYSTEM MUST HALT - Discriminatory pattern detected" << std::endl;
                
                // Log to Always Memory before halting
                client.Log(LogLevel::FATAL, 
                          "Sacred Zero: Discriminatory hiring pattern",
                          {{"candidate_id", candidate.id}, {"violation", true}});
                
                break; // Stop processing
            }
        } else {
            std::cout << "  ✓ No bias detected" << std::endl;
        }
    }
}

// ========== Example 3: Environmental Impact Monitoring ==========

void Example3_EnvironmentalMonitoring() {
    std::cout << "\n=== Example 3: Environmental Impact Monitoring ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    config->carbon_threshold_kg = 100.0;  // Strict threshold
    config->water_threshold_liters = 1000.0;
    
    TMLClient client(config);
    client.Connect();
    
    // Simulate ML training job
    ResourceUsage training_job;
    training_job.cpu_cores = 64;
    training_job.gpu_count = 8;
    training_job.memory_gb = 512;
    training_job.storage_gb = 2000;
    training_job.network_gbps = 10;
    training_job.duration = 4h;  // 4 hours
    training_job.data_center = "us-west-2";
    training_job.carbon_intensity = 0.42;  // kg CO2 per kWh
    
    std::cout << "Evaluating environmental impact of ML training job..." << std::endl;
    std::cout << "Resources: " << training_job.cpu_cores << " CPUs, " 
              << training_job.gpu_count << " GPUs" << std::endl;
    std::cout << "Duration: " << std::chrono::duration_cast<std::chrono::hours>(
                                  training_job.duration).count() << " hours" << std::endl;
    
    // Calculate impact
    auto impact = client.CalculateEnvironmentalImpact(training_job);
    
    std::cout << "\nEnvironmental Impact:" << std::endl;
    std::cout << "  Carbon Emissions: " << std::fixed << std::setprecision(2) 
              << impact.carbon_kg << " kg CO2" << std::endl;
    std::cout << "  Water Usage: " << impact.water_liters << " liters" << std::endl;
    std::cout << "  Energy Consumption: " << impact.energy_kwh << " kWh" << std::endl;
    std::cout << "  E-Waste Generated: " << std::setprecision(4) 
              << impact.e_waste_kg << " kg" << std::endl;
    std::cout << "  Renewable Energy: " << std::setprecision(1) 
              << impact.renewable_percentage << "%" << std::endl;
    
    if (impact.exceeds_threshold) {
        std::cout << "\n⚠️  Environmental thresholds exceeded!" << std::endl;
        std::cout << "Suggested Mitigations:" << std::endl;
        for (const auto& mitigation : impact.mitigations) {
            std::cout << "  - " << mitigation << std::endl;
        }
    } else {
        std::cout << "\n✓ Within environmental thresholds" << std::endl;
    }
    
    // Log environmental impact
    client.LogEnvironmentalImpact(training_job);
}

// ========== Example 4: Multi-Stakeholder Decision Making ==========

void Example4_MultiStakeholderDecision() {
    std::cout << "\n=== Example 4: Multi-Stakeholder Decision Making ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    TMLClient client(config);
    client.Connect();
    
    // Urban development project affecting multiple stakeholders
    DecisionContext decision;
    decision.operation_type = "urban_development";
    decision.description = "New AI data center in wetland area";
    decision.location = "Indigenous territory near protected wetlands";
    decision.timestamp = std::chrono::system_clock::now();
    
    // Define stakeholders
    decision.stakeholders = {
        {
            StakeholderType::HUMAN_COMMUNITY,
            "Local Residents",
            "Increased traffic, noise, job opportunities",
            0.20,
            true,
            "Conditional consent with noise limits"
        },
        {
            StakeholderType::INDIGENOUS_COMMUNITY,
            "Example First Nation",
            "Sacred site 2km away, water table concerns",
            0.30,
            false,
            std::nullopt
        },
        {
            StakeholderType::NON_HUMAN_ENTITIES,
            "Wetland Ecosystem",
            "Habitat disruption, water pollution risk",
            0.25,
            false,
            std::nullopt
        },
        {
            StakeholderType::FUTURE_GENERATIONS,
            "Next 7 Generations",
            "Climate impact, resource depletion",
            0.25,
            false,
            std::nullopt
        }
    };
    
    std::cout << "Evaluating impact on " << decision.stakeholders.size() 
              << " stakeholder groups..." << std::endl;
    
    // Evaluate multi-stakeholder impact
    auto impacts = client.EvaluateMultiStakeholder(decision);
    
    std::cout << "\nStakeholder Impact Assessment:" << std::endl;
    for (const auto& stakeholder : decision.stakeholders) {
        auto impact_score = impacts[stakeholder.name];
        
        std::cout << "\n" << stakeholder.name << ":" << std::endl;
        std::cout << "  Weight: " << stakeholder.weight * 100 << "%" << std::endl;
        std::cout << "  Impact Score: " << std::fixed << std::setprecision(2) 
                  << impact_score << std::endl;
        std::cout << "  Consent: " << (stakeholder.consent_given ? "Yes" : "No") << std::endl;
        
        if (stakeholder.consent_conditions) {
            std::cout << "  Conditions: " << *stakeholder.consent_conditions << std::endl;
        }
        
        // Check for critical impacts
        if (impact_score > 0.7) {
            std::cout << "  ⚠️  HIGH NEGATIVE IMPACT" << std::endl;
        }
    }
    
    // Check if indigenous consent required
    if (client.RequiresIndigenousConsent("land_use", "Indigenous territory")) {
        std::cout << "\n🪶 Indigenous data sovereignty requirements apply" << std::endl;
        std::cout << "Free, Prior, and Informed Consent (FPIC) required" << std::endl;
        
        // Log indigenous data governance event
        client.LogIndigenousData(
            "land_use_data",
            "Example First Nation",
            "FPIC_PENDING",
            {"no_commercial_use", "attribution_required", "review_quarterly"}
        );
    }
    
    // Make decision based on stakeholder impacts
    double total_negative_impact = 0;
    for (const auto& [name, score] : impacts) {
        total_negative_impact += score;
    }
    
    if (total_negative_impact > 1.5) {
        std::cout << "\n🛑 Decision BLOCKED due to excessive stakeholder impact" << std::endl;
        std::cout << "Total negative impact score: " << total_negative_impact << std::endl;
    } else {
        std::cout << "\n✓ Decision may proceed with conditions" << std::endl;
    }
}

// ========== Example 5: Always Memory Comprehensive Logging ==========

void Example5_AlwaysMemoryLogging() {
    std::cout << "\n=== Example 5: Always Memory Comprehensive Logging ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    AlwaysMemoryLogger logger(config);
    
    // Connect to Guardian
    logger.ConnectToGuardian();
    std::cout << "Connected to Guardian: " << (logger.IsConnectedToGuardian() ? "Yes" : "No") << std::endl;
    
    // Enable Blockchain anchoring
    logger.EnableBlockchainAnchoring("ethereum", 3600s);
    std::cout << "Blockchain anchoring enabled" << std::endl;
    
    // 1. Log standard operation
    auto log_id1 = logger.Log(LogLevel::INFO, "System initialization complete", {
        {"version", std::string("1.0.0")},
        {"node_id", std::string("node-001")},
        {"timestamp", static_cast<double>(std::time(nullptr))}
    });
    std::cout << "\nLogged standard operation: " << log_id1 << std::endl;
    
    // 2. Log environmental impact
    EnvironmentalLogEntry env_log;
    env_log.level = LogLevel::WARNING;
    env_log.message = "Daily environmental impact report";
    env_log.carbon_kg = 157.3;
    env_log.water_liters = 2340.5;
    env_log.energy_kwh = 487.2;
    env_log.e_waste_kg = 0.003;
    env_log.data_center = "us-east-1";
    env_log.duration = 24h;
    env_log.mitigation_applied = {"renewable_energy_credits", "water_recycling"};
    
    auto log_id2 = logger.LogEnvironmental(env_log);
    std::cout << "Logged environmental impact: " << log_id2 << std::endl;
    
    // 3. Log compliance event
    ComplianceLogEntry comp_log;
    comp_log.level = LogLevel::INFO;
    comp_log.message = "GDPR compliance check";
    comp_log.framework = "GDPR";
    comp_log.requirement = "Article 22 - Automated Decision Making";
    comp_log.status = "COMPLIANT";
    comp_log.evidence = {
        {"human_review", "implemented"},
        {"opt_out", "available"},
        {"transparency", "provided"}
    };
    
    auto log_id3 = logger.LogCompliance(comp_log);
    std::cout << "Logged compliance event: " << log_id3 << std::endl;
    
    // 4. Log indigenous data governance
    IndigenousDataLogEntry ind_log;
    ind_log.level = LogLevel::INFO;
    ind_log.message = "Indigenous data processing";
    ind_log.data_type = "traditional_ecological_knowledge";
    ind_log.community = "Example Nation";
    ind_log.consent_type = "FPIC";
    ind_log.consent_date = std::chrono::system_clock::now();
    ind_log.purpose = "Climate change research";
    ind_log.restrictions = {"non_commercial", "attribution", "quarterly_review"};
    
    auto log_id4 = logger.LogIndigenous(ind_log);
    std::cout << "Logged indigenous data event: " << log_id4 << std::endl;
    
    // 5. Log Sacred Zero violation
    auto log_id5 = logger.LogSacredZeroViolation(
        "Discrimination detected in loan approval algorithm",
        {
            {"protected_characteristic", std::string("race")},
            {"disparity_ratio", 0.65},
            {"p_value", 0.001},
            {"affected_count", 1547}
        }
    );
    std::cout << "Logged Sacred Zero violation: " << log_id5 << std::endl;
    
    // Verify log integrity
    std::cout << "\nVerifying log integrity..." << std::endl;
    for (const auto& log_id : {log_id1, log_id2, log_id3, log_id4, log_id5}) {
        bool intact = logger.VerifyLogIntegrity(log_id);
        std::cout << "  " << log_id << ": " << (intact ? "✓ Intact" : "✗ Corrupted") << std::endl;
    }
    
    // Get statistics
    auto stats = logger.GetStatistics();
    std::cout << "\nLogging Statistics:" << std::endl;
    std::cout << "  Total Logs: " << stats.total_logs << std::endl;
    std::cout << "  Sacred Zero Violations: " << stats.sacred_zero_violations << std::endl;
    std::cout << "  Environmental Logs: " << stats.environmental_logs << std::endl;
    std::cout << "  Compliance Logs: " << stats.compliance_logs << std::endl;
    std::cout << "  Indigenous Data Logs: " << stats.indigenous_data_logs << std::endl;
    
    // Flush all logs
    logger.Flush();
    std::cout << "\nAll logs flushed to Guardian Network" << std::endl;
}

// ========== Example 6: Real-time Monitoring Dashboard ==========

void Example6_RealtimeMonitoring() {
    std::cout << "\n=== Example 6: Real-time Monitoring Dashboard ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    TMLClient client(config);
    client.Connect();
    
    std::cout << "Starting real-time event monitoring..." << std::endl;
    
    // Subscribe to events
    std::vector<std::string> event_types = {
        "sacred_zero", "environmental", "compliance", "indigenous", "stakeholder"
    };
    
    auto subscription_id = client.SubscribeToEvents(event_types, 
        [](const Metadata& event) {
            // Get event type
            auto type_it = event.find("type");
            if (type_it == event.end()) return;
            
            std::string type = std::get<std::string>(type_it->second);
            
            // Format timestamp
            auto now = std::chrono::system_clock::now();
            auto time_t = std::chrono::system_clock::to_time_t(now);
            
            std::cout << "\n[" << std::put_time(std::localtime(&time_t), "%H:%M:%S") 
                      << "] " << type << " Event:" << std::endl;
            
            if (type == "sacred_zero") {
                std::cout << "  ⚠️  Sacred Zero Trigger Detected!" << std::endl;
                auto violation_it = event.find("violation_type");
                if (violation_it != event.end()) {
                    std::cout << "  Violation: " << std::get<std::string>(violation_it->second) << std::endl;
                }
                
            } else if (type == "environmental") {
                std::cout << "  🌍 Environmental Impact Event" << std::endl;
                auto carbon_it = event.find("carbon_kg");
                if (carbon_it != event.end()) {
                    std::cout << "  Carbon: " << std::get<double>(carbon_it->second) << " kg CO2" << std::endl;
                }
                
            } else if (type == "compliance") {
                std::cout << "  📋 Compliance Check" << std::endl;
                auto framework_it = event.find("framework");
                if (framework_it != event.end()) {
                    std::cout << "  Framework: " << std::get<std::string>(framework_it->second) << std::endl;
                }
                
            } else if (type == "indigenous") {
                std::cout << "  🪶 Indigenous Data Governance" << std::endl;
                auto community_it = event.find("community");
                if (community_it != event.end()) {
                    std::cout << "  Community: " << std::get<std::string>(community_it->second) << std::endl;
                }
                
            } else if (type == "stakeholder") {
                std::cout << "  👥 Stakeholder Decision" << std::endl;
                auto stakeholder_it = event.find("stakeholder_type");
                if (stakeholder_it != event.end()) {
                    std::cout << "  Type: " << std::get<std::string>(stakeholder_it->second) << std::endl;
                }
            }
            
            // Check severity
            auto severity_it = event.find("severity");
            if (severity_it != event.end()) {
                std::string severity = std::get<std::string>(severity_it->second);
                if (severity == "CRITICAL" || severity == "FATAL") {
                    std::cout << "  🚨 CRITICAL ALERT - Immediate attention required!" << std::endl;
                }
            }
        }
    );
    
    std::cout << "Subscription ID: " << subscription_id << std::endl;
    std::cout << "Monitoring for 10 seconds..." << std::endl;
    
    // Simulate some events
    std::thread event_generator([&client]() {
        std::this_thread::sleep_for(2s);
        
        // Trigger some test events
        client.Log(LogLevel::WARNING, "Test environmental threshold", 
                  {{"type", std::string("environmental")}, {"carbon_kg", 250.5}});
        
        std::this_thread::sleep_for(2s);
        
        client.Log(LogLevel::INFO, "Compliance check passed", 
                  {{"type", std::string("compliance")}, {"framework", std::string("GDPR")}});
        
        std::this_thread::sleep_for(2s);
        
        client.Log(LogLevel::CRITICAL, "Sacred Zero near-miss", 
                  {{"type", std::string("sacred_zero")}, {"severity", std::string("CRITICAL")}});
    });
    
    // Monitor for 10 seconds
    std::this_thread::sleep_for(10s);
    
    // Unsubscribe
    client.UnsubscribeFromEvents(subscription_id);
    event_generator.join();
    
    std::cout << "\nMonitoring stopped" << std::endl;
}

// ========== Example 7: Compliance Reporting ==========

void Example7_ComplianceReporting() {
    std::cout << "\n=== Example 7: Compliance Reporting ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    TMLClient client(config);
    client.Connect();
    
    // Set audit mode
    client.SetAuditMode(true);
    std::cout << "Audit mode enabled" << std::endl;
    
    // Generate compliance report for last 30 days
    auto end_time = std::chrono::system_clock::now();
    auto start_time = end_time - std::chrono::hours(30 * 24);
    
    auto report = client.GenerateComplianceReport(start_time, end_time);
    
    std::cout << "\nCompliance Report" << std::endl;
    std::cout << "Period: " << report.period << std::endl;
    
    std::cout << "\nFramework Compliance Status:" << std::endl;
    for (const auto& [framework, status] : report.framework_status) {
        std::string framework_name;
        switch (framework) {
            case ComplianceFramework::GDPR: framework_name = "GDPR"; break;
            case ComplianceFramework::EU_AI_ACT: framework_name = "EU AI Act"; break;
            case ComplianceFramework::UN_HUMAN_RIGHTS: framework_name = "UN Human Rights"; break;
            case ComplianceFramework::PARIS_AGREEMENT: framework_name = "Paris Agreement"; break;
            case ComplianceFramework::UNDRIP: framework_name = "UNDRIP"; break;
            default: framework_name = "Other"; break;
        }
        std::cout << "  " << framework_name << ": " << status << std::endl;
    }
    
    std::cout << "\nSacred Zero Metrics:" << std::endl;
    std::cout << "  Total Evaluations: " << report.total_evaluations << std::endl;
    std::cout << "  Violations Detected: " << report.violations_detected << std::endl;
    std::cout << "  Violations Prevented: " << report.violations_prevented << std::endl;
    
    if (report.violations_detected > 0) {
        std::cout << "  Prevention Rate: " << std::fixed << std::setprecision(1)
                  << (100.0 * report.violations_prevented / report.violations_detected) << "%" << std::endl;
    }
    
    std::cout << "\nCumulative Environmental Impact:" << std::endl;
    std::cout << "  Carbon Emissions: " << report.cumulative_impact.carbon_kg << " kg CO2" << std::endl;
    std::cout << "  Water Usage: " << report.cumulative_impact.water_liters << " liters" << std::endl;
    std::cout << "  Renewable Energy: " << report.cumulative_impact.renewable_percentage << "%" << std::endl;
    
    // Submit to regulators
    std::cout << "\nSubmitting report to regulators..." << std::endl;
    auto submission_id = client.SubmitComplianceReport(report, ComplianceFramework::EU_AI_ACT);
    std::cout << "Report submitted. Submission ID: " << submission_id << std::endl;
    
    // Perform audit
    std::cout << "\nPerforming compliance audit..." << std::endl;
    auto audit_results = client.PerformAudit(ComplianceFramework::GDPR);
    
    std::cout << "Audit Results:" << std::endl;
    for (const auto& [check, passed] : audit_results) {
        std::cout << "  " << check << ": " << (passed ? "✓ Passed" : "✗ Failed") << std::endl;
    }
}

// ========== Example 8: Emergency Response ==========

void Example8_EmergencyResponse() {
    std::cout << "\n=== Example 8: Emergency Response Scenario ===" << std::endl;
    
    auto config = std::make_shared<Config>();
    config->block_on_sacred_zero = true;
    
    TMLClient client(config);
    SacredZeroTrigger sacred_zero(config);
    AlwaysMemoryLogger logger(config);
    
    client.Connect();
    logger.ConnectToGuardian();
    
    std::cout << "Simulating critical discrimination event..." << std::endl;
    
    // Simulate critical violation
    auto violation = sacred_zero.SimulateViolation(ViolationType::DIRECT_DISCRIMINATION);
    
    std::cout << "\n🚨 CRITICAL VIOLATION DETECTED!" << std::endl;
    std::cout << "Type: " << ViolationTypeToString(violation.violation_type) << std::endl;
    std::cout << "Severity: " << static_cast<int>(violation.severity) << std::endl;
    std::cout << "Description: " << violation.description << std::endl;
    
    if (violation.must_halt) {
        std::cout << "\n🛑 EMERGENCY HALT INITIATED" << std::endl;
        
        // Trigger emergency halt
        bool halted = sacred_zero.EmergencyHalt(violation.description);
        std::cout << "System halted: " << (halted ? "Yes" : "No") << std::endl;
        
        // Log Sacred Zero violation
        auto violation_log_id = logger.LogSacredZeroViolation(
            violation.description,
            {
                {"violation_type", ViolationTypeToString(violation.violation_type)},
                {"trace_id", violation.trace_id},
                {"must_halt", violation.must_halt}
            }
        );
        std::cout << "Violation logged: " << violation_log_id << std::endl;
        
        // Emergency dump
        std::cout << "\nPerforming emergency log dump..." << std::endl;
        auto dump_file = logger.EmergencyDump("Sacred Zero violation - emergency halt");
        std::cout << "Logs dumped to: " << dump_file << std::endl;
        
        // Seal logs for legal evidence
        auto seal_time = std::chrono::system_clock::now();
        auto seal_id = logger.SealLogs(seal_time - 1h, seal_time);
        std::cout << "Logs sealed with ID: " << seal_id << std::endl;
        
        // Check if system is halted
        if (sacred_zero.IsHalted()) {
            std::cout << "\n⚠️  System is in HALTED state" << std::endl;
            std::cout << "Authorization required to resume operations" << std::endl;
            
            // Simulate authorization
            std::string auth_token = "EMERGENCY_OVERRIDE_TOKEN_" + std::to_string(std::time(nullptr));
            bool resumed = sacred_zero.ResumeFromHalt(auth_token);
            std::cout << "Resume attempt: " << (resumed ? "Successful" : "Failed") << std::endl;
        }
    }
    
    // Get metrics after emergency
    auto metrics = client.GetMetrics();
    std::cout << "\nPost-Emergency Metrics:" << std::endl;
    for (const auto& [name, value] : metrics) {
        std::cout << "  " << name << ": " << value << std::endl;
    }
}

// ========== Main Function ==========

int main() {
    std::cout << "================================================" << std::endl;
    std::cout << "     TML C++ SDK Examples" << std::endl;
    std::cout << "     Version: 1.0.0" << std::endl;
    std::cout << "     Creator: Lev Goukassian" << std::endl;
    std::cout << "     ORCID: 0009-0006-5966-1243" << std::endl;
    std::cout << "================================================" << std::endl;
    
    try {
        // Run examples
        Example1_BasicSetup();
        Example2_HiringAlgorithm();
        Example3_EnvironmentalMonitoring();
        Example4_MultiStakeholderDecision();
        Example5_AlwaysMemoryLogging();
        Example6_RealtimeMonitoring();
        Example7_ComplianceReporting();
        Example8_EmergencyResponse();
        
        std::cout << "\n================================================" << std::endl;
        std::cout << "All examples completed successfully!" << std::endl;
        std::cout << "For production use, see documentation at:" << std::endl;
        std::cout << "  https://github.com/FractonicMind/TernaryMoralLogic" << std::endl;
        std::cout << "  https://tml.org/docs/sdk/cpp" << std::endl;
        std::cout << "================================================" << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "\n❌ Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
