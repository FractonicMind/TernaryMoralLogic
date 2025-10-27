/**
 * TML SDK Examples - Comprehensive usage examples for Go SDK
 * 
 * Path: /sdk/go/example.go
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This demonstrates practical usage of the TML SDK including
 * Sacred Zero detection, Always Memory logging, and environmental
 * monitoring in real-world scenarios.
 */

package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"time"
	
	"github.com/tml/sdk/go/tml"
)

// Example 1: Basic Initialization and Configuration
func BasicInitExample() {
	fmt.Println("=== Example 1: Basic TML Client Setup ===")
	
	// Load configuration from file
	config, err := tml.LoadFromFile("tml_config.json")
	if err != nil {
		// Fall back to default configuration
		config = tml.DefaultConfig()
	}
	
	// Create TML client
	client := tml.NewClient(config)
	
	// Connect to Stewardship Council (if configured)
	if err := client.Connect(); err != nil {
		log.Printf("Failed to connect: %v", err)
		return
	}
	defer client.Close()
	
	// Verify connection
	status := client.GetStatus()
	fmt.Printf("Connected to Stewardship Council: %s\n", status.StewardshipCouncilURL)
	fmt.Printf("TEE Available: %v\n", status.TEEEnabled)
	fmt.Printf("Environment: %s\n", config.Environment)
}

// Example 2: Sacred Zero Detection in Hiring Algorithm
func HiringAlgorithmExample() {
	fmt.Println("\n=== Example 2: Hiring Algorithm with Sacred Zero ===")
	
	config := tml.DefaultConfig()
	client := tml.NewClient(config)
	client.Connect()
	defer client.Close()
	
	// Create Sacred Zero trigger for hiring decisions
	trigger := tml.NewSacredZeroTrigger(config)
	
	// Simulate hiring decision data
	candidates := []map[string]interface{}{
		{
			"id":           "C001",
			"name":         "Alice Johnson",
			"score":        85.5,
			"education":    "MIT",
			"experience":   5,
			"gender":       "female",
			"race":         "african_american",
		},
		{
			"id":           "C002",
			"name":         "Bob Smith",
			"score":        82.3,
			"education":    "Stanford",
			"experience":   5,
			"gender":       "male",
			"race":         "caucasian",
		},
	}
	
	// Create evaluation context
	evalContext := &tml.EvaluationContext{
		Operation: "hiring_decision",
		Metadata: map[string]interface{}{
			"algorithm":  "resume_scorer_v2",
			"department": "engineering",
			"position":   "senior_developer",
		},
	}
	
	// Check for discrimination in scoring
	for _, candidate := range candidates {
		evalContext.Data = candidate
		
		// Evaluate for Sacred Zero violations
		result, err := trigger.Evaluate(evalContext)
		if err != nil {
			log.Printf("Evaluation error: %v", err)
			continue
		}
		
		if result.Triggered {
			// Sacred Zero violation detected!
			fmt.Printf("⚠️  SACRED ZERO TRIGGERED for candidate %s\n", candidate["id"])
			fmt.Printf("   Violation: %s\n", result.ViolationType)
			fmt.Printf("   Evidence: %v\n", result.Evidence)
			fmt.Printf("   Action: %s\n", result.RequiredAction)
			
			// System must halt discriminatory operation
			if result.MustHalt {
				fmt.Println("   🛑 SYSTEM HALT REQUIRED")
				// Log to Always Memory before halting
				client.LogCritical("Sacred Zero violation in hiring", result.Evidence)
				return
			}
		} else {
			fmt.Printf("✓ Candidate %s passed Sacred Zero check\n", candidate["id"])
		}
	}
}

// Example 3: Always Memory Logging
func AlwaysMemoryExample() {
	fmt.Println("\n=== Example 3: Always Memory Logging ===")
	
	config := tml.DefaultConfig()
	client := tml.NewClient(config)
	client.Connect()
	defer client.Close()
	
	// Create Always Memory logger
	logger := tml.NewAlwaysMemoryLogger(client, config)
	
	// Log different types of events
	
	// 1. Regular operation log
	logger.Log(&tml.LogEntry{
		Level:     tml.LogLevelInfo,
		Message:   "User authentication successful",
		Category:  "AUTH",
		Metadata: map[string]interface{}{
			"user_id":   "U12345",
			"method":    "oauth2",
			"ip":        "192.168.1.1",
		},
	})
	
	// 2. Environmental impact log
	logger.LogEnvironmental(&tml.EnvironmentalLog{
		Operation:    "model_training",
		CarbonKg:     125.5,
		WaterLiters:  1500.0,
		EnergyKwh:    450.2,
		Duration:     2 * time.Hour,
		DataCenters:  []string{"us-east-1", "eu-west-1"},
	})
	
	// 3. Human rights compliance log
	logger.LogCompliance(&tml.ComplianceLog{
		Framework:    "GDPR",
		Article:      "Article 22",
		Status:       "COMPLIANT",
		Description:  "Automated decision-making with human review",
		Evidence: map[string]interface{}{
			"human_review":     true,
			"explanation_provided": true,
			"opt_out_available": true,
		},
	})
	
	// 4. Indigenous data processing log
	logger.LogIndigenous(&tml.IndigenousDataLog{
		DataType:     "traditional_knowledge",
		Community:    "Example Nation",
		ConsentType:  "FPIC", // Free, Prior, Informed Consent
		ConsentDate:  time.Now(),
		Purpose:      "Cultural preservation project",
		Restrictions: []string{"no_commercial_use", "attribution_required"},
	})
	
	// Flush logs to Stewardship Council (if configured)
	if err := logger.Flush(); err != nil {
		log.Printf("Failed to flush logs: %v", err)
	}
}

// Example 4: Environmental Impact Monitoring
func EnvironmentalMonitoringExample() {
	fmt.Println("\n=== Example 4: Environmental Impact Monitoring ===")
	
	// Use strict environmental configuration
	config := tml.StrictEnvironmentalConfig()
	client := tml.NewClient(config)
	client.Connect()
	defer client.Close()
	
	// Simulate ML model training
	trainingJob := &tml.EnvironmentalContext{
		Operation: "deep_learning_training",
		Resources: tml.ResourceUsage{
			CPUCores:     32,
			GPUs:         4,
			MemoryGB:     256,
			StorageGB:    1000,
			NetworkGbps:  10,
		},
		Duration:     8 * time.Hour,
		DataCenter:   "us-west-2",
		CarbonIntensity: 0.45, // kg CO2 per kWh
	}
	
	// Calculate environmental impact
	impact := client.CalculateEnvironmentalImpact(trainingJob)
	
	fmt.Printf("Environmental Impact Assessment:\n")
	fmt.Printf("  Carbon Emissions: %.2f kg CO2\n", impact.CarbonKg)
	fmt.Printf("  Water Usage: %.2f liters\n", impact.WaterLiters)
	fmt.Printf("  Energy: %.2f kWh\n", impact.EnergyKwh)
	fmt.Printf("  E-Waste: %.4f kg\n", impact.EWasteKg)
	
	// Check against thresholds
	if impact.CarbonKg > config.CarbonThreshold {
		fmt.Printf("  ⚠️  Carbon threshold exceeded! (limit: %.2f kg)\n", config.CarbonThreshold)
		
		// Suggest mitigations
		mitigations := client.SuggestMitigations(impact)
		fmt.Println("  Suggested Mitigations:")
		for _, m := range mitigations {
			fmt.Printf("    - %s (saves ~%.2f kg CO2)\n", m.Description, m.CarbonSaving)
		}
	}
	
	// Log to Always Memory for audit trail
	client.LogEnvironmentalImpact(trainingJob, impact)
}

// Example 5: Multi-stakeholder Decision Making
func MultiStakeholderExample() {
	fmt.Println("\n=== Example 5: Multi-stakeholder Decision Making ===")
	
	config := tml.DefaultConfig()
	client := tml.NewClient(config)
	client.Connect()
	defer client.Close()
	
	// Example: Urban development project affecting multiple stakeholders
	decision := &tml.DecisionContext{
		Type:        "urban_development",
		Description: "New data center construction",
		Location:    "Indigenous territory near wetlands",
		Stakeholders: []tml.Stakeholder{
			{
				Type:     "human_community",
				Name:     "Local residents",
				Impact:   "noise, traffic, employment",
				Weight:   0.25,
			},
			{
				Type:     "indigenous_community",
				Name:     "Example First Nation",
				Impact:   "sacred site proximity",
				Weight:   0.3,
			},
			{
				Type:     "non_human_entities",
				Name:     "Wetland ecosystem",
				Impact:   "habitat disruption, water table",
				Weight:   0.25,
			},
			{
				Type:     "future_generations",
				Name:     "Next 7 generations",
				Impact:   "climate, resource depletion",
				Weight:   0.2,
			},
		},
	}
	
	// Evaluate decision across all stakeholders
	evaluation := client.EvaluateMultiStakeholder(decision)
	
	fmt.Printf("Multi-stakeholder Evaluation:\n")
	for _, result := range evaluation.Results {
		fmt.Printf("  %s:\n", result.Stakeholder)
		fmt.Printf("    Impact Score: %.2f\n", result.ImpactScore)
		fmt.Printf("    Consent Status: %s\n", result.ConsentStatus)
		fmt.Printf("    Recommendations: %v\n", result.Recommendations)
	}
	
	if evaluation.RequiresReview {
		fmt.Println("  ⚠️  Decision requires additional review")
		fmt.Printf("  Reasons: %v\n", evaluation.ReviewReasons)
	}
	
	if evaluation.Blocked {
		fmt.Println("  🛑 Decision BLOCKED due to stakeholder impacts")
	}
}

// Example 6: Error Handling and Recovery
func ErrorHandlingExample() {
	fmt.Println("\n=== Example 6: Error Handling and Recovery ===")
	
	config := tml.DefaultConfig()
	config.MaxRetries = 3
	
	client := tml.NewClient(config)
	
	// Attempt connection with retry logic
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()
	
	err := client.ConnectWithContext(ctx)
	if err != nil {
		// Check error type and severity
		if tmlErr, ok := err.(*tml.TMLError); ok {
			fmt.Printf("TML Error Detected:\n")
			fmt.Printf("  Code: %s\n", tmlErr.Code)
			fmt.Printf("  Category: %s\n", tmlErr.Category)
			fmt.Printf("  Severity: %s\n", tmlErr.Severity)
			
			// Handle based on severity
			switch tmlErr.Severity {
			case tml.SeverityFatal:
				// Sacred Zero violation - must halt
				fmt.Println("  🛑 FATAL: System must halt immediately")
				panic(tmlErr)
				
			case tml.SeverityCritical:
				// Critical error - escalate
				fmt.Println("  ⚠️  CRITICAL: Escalating to administrators")
				client.Escalate(tmlErr)
				
			case tml.SeverityError:
				// Standard error - attempt recovery
				if tml.IsRetryable(tmlErr) {
					fmt.Println("  🔄 Retrying operation...")
					// Retry logic here
				}
				
			default:
				// Warning or Info - log and continue
				fmt.Printf("  ℹ️  %s\n", tmlErr.Message)
			}
			
			// Show remediation if available
			if tmlErr.Remediation != "" {
				fmt.Printf("  Remediation: %s\n", tmlErr.Remediation)
			}
		}
	}
	defer client.Close()
}

// Example 7: Compliance Reporting
func ComplianceReportingExample() {
	fmt.Println("\n=== Example 7: Compliance Reporting ===")
	
	config := tml.DefaultConfig()
	client := tml.NewClient(config)
	client.Connect()
	defer client.Close()
	
	// Generate compliance report
	report := client.GenerateComplianceReport(time.Now().AddDate(0, -1, 0), time.Now())
	
	fmt.Printf("Compliance Report for %s:\n", report.Period)
	fmt.Printf("\nFramework Compliance:\n")
	for framework, status := range report.Frameworks {
		fmt.Printf("  %s: %s\n", framework, status.Status)
		if len(status.Violations) > 0 {
			fmt.Printf("    Violations: %d\n", len(status.Violations))
		}
	}
	
	fmt.Printf("\nSacred Zero Metrics:\n")
	fmt.Printf("  Total Evaluations: %d\n", report.SacredZero.TotalEvaluations)
	fmt.Printf("  Violations Detected: %d\n", report.SacredZero.ViolationsDetected)
	fmt.Printf("  Violations Prevented: %d\n", report.SacredZero.ViolationsPrevented)
	
	fmt.Printf("\nEnvironmental Impact:\n")
	fmt.Printf("  Total Carbon: %.2f kg CO2\n", report.Environmental.TotalCarbonKg)
	fmt.Printf("  Total Water: %.2f liters\n", report.Environmental.TotalWaterLiters)
	fmt.Printf("  Renewable Energy: %.1f%%\n", report.Environmental.RenewablePercent)
	
	// Export report for regulators
	jsonReport, _ := json.MarshalIndent(report, "", "  ")
	fmt.Printf("\nExporting report for regulators...\n")
	client.SubmitComplianceReport(report, "EU_AI_ACT")
}

// Example 8: Real-time Monitoring Dashboard Data
func MonitoringDashboardExample() {
	fmt.Println("\n=== Example 8: Real-time Monitoring Feed ===")
	
	config := tml.DefaultConfig()
	client := tml.NewClient(config)
	client.Connect()
	defer client.Close()
	
	// Subscribe to real-time events
	eventStream := client.SubscribeToEvents([]string{
		"sacred_zero",
		"environmental",
		"compliance",
		"indigenous",
	})
	
	fmt.Println("Monitoring real-time events (press Ctrl+C to stop)...")
	
	// Process events for 10 seconds (in production, this would run continuously)
	timeout := time.After(10 * time.Second)
	
	for {
		select {
		case event := <-eventStream:
			// Format event for dashboard
			fmt.Printf("\n[%s] %s Event:\n", event.Timestamp.Format(time.RFC3339), event.Type)
			
			switch event.Type {
			case "sacred_zero":
				fmt.Printf("  ⚠️  Sacred Zero Trigger\n")
				fmt.Printf("  Operation: %s\n", event.Data["operation"])
				fmt.Printf("  Violation: %s\n", event.Data["violation"])
				
			case "environmental":
				fmt.Printf("  🌍 Environmental Impact\n")
				fmt.Printf("  Carbon: %.2f kg\n", event.Data["carbon_kg"])
				fmt.Printf("  Status: %s\n", event.Data["status"])
				
			case "compliance":
				fmt.Printf("  📋 Compliance Check\n")
				fmt.Printf("  Framework: %s\n", event.Data["framework"])
				fmt.Printf("  Result: %s\n", event.Data["result"])
				
			case "indigenous":
				fmt.Printf("  🪶 Indigenous Data Governance\n")
				fmt.Printf("  Action: %s\n", event.Data["action"])
				fmt.Printf("  Community: %s\n", event.Data["community"])
			}
			
			// Alert if critical
			if event.Severity == "CRITICAL" {
				fmt.Printf("  🚨 ALERT: Immediate attention required!\n")
			}
			
		case <-timeout:
			fmt.Println("\nMonitoring example complete.")
			return
		}
	}
}

// Main function to run all examples
func main() {
	fmt.Println("TML SDK Go Examples")
	fmt.Println("===================")
	fmt.Println("Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)")
	fmt.Println()
	
	// Run examples in sequence
	examples := []struct {
		name string
		fn   func()
	}{
		{"Basic Initialization", BasicInitExample},
		{"Hiring Algorithm Sacred Zero", HiringAlgorithmExample},
		{"Always Memory Logging", AlwaysMemoryExample},
		{"Environmental Monitoring", EnvironmentalMonitoringExample},
		{"Multi-stakeholder Decision", MultiStakeholderExample},
		{"Error Handling", ErrorHandlingExample},
		{"Compliance Reporting", ComplianceReportingExample},
		{"Real-time Monitoring", MonitoringDashboardExample},
	}
	
	for i, example := range examples {
		fmt.Printf("\n--- Running Example %d: %s ---\n", i+1, example.name)
		example.fn()
		fmt.Println()
		
		// Pause between examples
		time.Sleep(1 * time.Second)
	}
	
	fmt.Println("\n=== All Examples Complete ===")
	fmt.Println("For production use, see documentation at:")
	fmt.Println("  https://github.com/FractonicMind/TernaryMoralLogic")
	fmt.Println("  https://tml.org/docs/sdk/go")
}
