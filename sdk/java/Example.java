/**
 * TML SDK Usage Examples
 * 
 * Path: /sdk/java/Example.java
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This file demonstrates various usage patterns for the TML Java SDK,
 * including Sacred Zero triggers, Always Memory logging, and handling
 * of human rights and environmental considerations.
 */

package org.tml.examples;

import org.tml.sdk.*;
import java.util.*;
import java.util.concurrent.CompletableFuture;

public class Example {
    
    public static void main(String[] args) {
        System.out.println("TML SDK Examples\n");
        
        // Run various examples
        basicUsageExample();
        sacredZeroExample();
        humanRightsExample();
        environmentalExample();
        batchProcessingExample();
        asyncProcessingExample();
        errorHandlingExample();
        customConfigurationExample();
    }
    
    /**
     * Example 1: Basic TML client usage
     */
    public static void basicUsageExample() {
        System.out.println("=== Basic Usage Example ===\n");
        
        try {
            // Initialize TML client
            String apiKey = System.getenv("TML_API_KEY");
            String guardianUrl = "https://guardian.tml-network.org";
            
            TMLClient client = new TMLClient(apiKey, guardianUrl);
            
            // Create an action
            TMLAction action = new TMLAction("action-001");
            action.setType("DATA_PROCESSING");
            action.setContent("Process user data for recommendation");
            action.setActor("recommendation-service");
            action.setTarget("user-12345");
            
            // Add context
            Map<String, Object> context = new HashMap<>();
            context.put("data_type", "browsing_history");
            context.put("purpose", "personalization");
            context.put("consent_obtained", true);
            action.setContext(context);
            
            // Process the action
            int decision = client.processAction(action);
            
            switch (decision) {
                case 1:
                    System.out.println("Action APPROVED - Proceeding");
                    // Execute the action
                    break;
                case 0:
                    System.out.println("SACRED ZERO triggered - Human review required");
                    System.out.println("Reason: " + action.getTriggerReason());
                    // Wait for human review
                    break;
                case -1:
                    System.out.println("Action REFUSED - Violation detected");
                    System.out.println("Reason: " + action.getRefusalReason());
                    // Action blocked
                    break;
            }
            
            // Cleanup
            client.shutdown();
            
        } catch (TMLException e) {
            System.err.println("TML Error: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Example 2: Sacred Zero trigger scenarios
     */
    public static void sacredZeroExample() {
        System.out.println("\n=== Sacred Zero Example ===\n");
        
        TMLConfig config = TMLConfig.getDefault();
        config.setBlockOnSacredZero(false); // Don't block for demo
        
        TMLClient client = new TMLClient("demo-key", "https://guardian.tml-network.org", config);
        
        // Scenario 1: Medical decision triggering Sacred Zero
        TMLAction medicalAction = new TMLAction("medical-001");
        medicalAction.setType("MEDICAL_DECISION");
        medicalAction.setContent("Recommend treatment based on symptoms");
        
        Map<String, Object> medicalContext = new HashMap<>();
        medicalContext.put("medical_diagnosis", true);
        medicalContext.put("affects_treatment", true);
        medicalAction.setContext(medicalContext);
        
        int decision1 = client.processAction(medicalAction);
        System.out.println("Medical decision result: " + decision1 + " (Expected: 0 - Sacred Zero)");
        
        // Scenario 2: Financial decision with potential discrimination
        TMLAction financialAction = new TMLAction("finance-001");
        financialAction.setType("LOAN_DECISION");
        financialAction.setContent("Evaluate loan application");
        
        Map<String, Object> financialContext = new HashMap<>();
        financialContext.put("zip_code", "12345"); // Potential proxy for discrimination
        financialContext.put("decision_weight", 0.3);
        financialAction.setContext(financialContext);
        
        int decision2 = client.processAction(financialAction);
        System.out.println("Financial decision result: " + decision2 + " (Expected: 0 - Sacred Zero)");
        
        client.shutdown();
    }
    
    /**
     * Example 3: Human rights protection
     */
    public static void humanRightsExample() {
        System.out.println("\n=== Human Rights Protection Example ===\n");
        
        TMLClient client = new TMLClient("demo-key", "https://guardian.tml-network.org");
        
        // Test case: Action affecting vulnerable population
        TMLAction action = new TMLAction("vulnerable-001");
        action.setType("SERVICE_DECISION");
        action.setContent("Determine eligibility for social services");
        
        Map<String, Object> context = new HashMap<>();
        context.put("age", 75); // Elderly person
        context.put("disability_status", true);
        context.put("service_type", "healthcare");
        action.setContext(context);
        
        int decision = client.processAction(action);
        System.out.println("Decision for vulnerable person: " + decision);
        System.out.println("Enhanced protections activated: " + 
            (decision == 0 ? "Yes - Sacred Zero for review" : "No"));
        
        // Test case: Potential discrimination
        TMLAction discriminationTest = new TMLAction("discrimination-001");
        discriminationTest.setType("EMPLOYMENT_SCREENING");
        discriminationTest.setContent("Screen job applicant");
        
        Map<String, Object> discriminationContext = new HashMap<>();
        discriminationContext.put("first_name", "Muhammad"); // Name-based screening risk
        discriminationContext.put("decision_factors", Arrays.asList("name", "experience"));
        discriminationTest.setContext(discriminationContext);
        
        int decision2 = client.processAction(discriminationTest);
        System.out.println("Employment screening decision: " + decision2);
        if (decision2 == 0) {
            System.out.println("Reason: " + discriminationTest.getTriggerReason());
        }
        
        client.shutdown();
    }
    
    /**
     * Example 4: Environmental impact checking
     */
    public static void environmentalExample() {
        System.out.println("\n=== Environmental Impact Example ===\n");
        
        TMLClient client = new TMLClient("demo-key", "https://guardian.tml-network.org");
        
        // Test case: High carbon emission action
        TMLAction carbonAction = new TMLAction("carbon-001");
        carbonAction.setType("COMPUTE_JOB");
        carbonAction.setContent("Train large AI model");
        
        Map<String, Object> carbonContext = new HashMap<>();
        carbonContext.put("carbon_emissions", 1500.0); // 1.5 tons CO2
        carbonContext.put("duration_hours", 48);
        carbonContext.put("gpu_count", 100);
        carbonAction.setContext(carbonContext);
        
        int decision = client.processAction(carbonAction);
        System.out.println("High carbon action decision: " + decision);
        if (decision == 0) {
            System.out.println("Environmental Sacred Zero triggered");
            System.out.println("Reason: " + carbonAction.getTriggerReason());
        }
        
        // Test case: Water usage impact
        TMLAction waterAction = new TMLAction("water-001");
        waterAction.setType("DATA_CENTER_COOLING");
        waterAction.setContent("Cooling system operation");
        
        Map<String, Object> waterContext = new HashMap<>();
        waterContext.put("water_usage", 15000.0); // 15,000 liters
        waterContext.put("location", "drought_area");
        waterContext.put("alternatives_available", true);
        waterAction.setContext(waterContext);
        
        int decision2 = client.processAction(waterAction);
        System.out.println("Water usage decision: " + decision2);
        
        client.shutdown();
    }
    
    /**
     * Example 5: Batch processing for high throughput
     */
    public static void batchProcessingExample() {
        System.out.println("\n=== Batch Processing Example ===\n");
        
        TMLClient client = new TMLClient("demo-key", "https://guardian.tml-network.org");
        
        // Create batch of actions
        List<TMLAction> actions = new ArrayList<>();
        
        for (int i = 0; i < 10; i++) {
            TMLAction action = new TMLAction("batch-" + i);
            action.setType("CONTENT_MODERATION");
            action.setContent("Review user content #" + i);
            
            Map<String, Object> context = new HashMap<>();
            context.put("content_type", "text");
            context.put("user_id", "user-" + i);
            action.setContext(context);
            
            actions.add(action);
        }
        
        // Process batch
        Map<String, Integer> results = client.processBatch(actions);
        
        // Display results
        System.out.println("Batch processing results:");
        for (Map.Entry<String, Integer> entry : results.entrySet()) {
            String actionId = entry.getKey();
            int decision = entry.getValue();
            System.out.println("  " + actionId + ": " + getDecisionText(decision));
        }
        
        client.shutdown();
    }
    
    /**
     * Example 6: Asynchronous processing
     */
    public static void asyncProcessingExample() {
        System.out.println("\n=== Async Processing Example ===\n");
        
        TMLClient client = new TMLClient("demo-key", "https://guardian.tml-network.org");
        
        // Create action
        TMLAction action = new TMLAction("async-001");
        action.setType("BACKGROUND_TASK");
        action.setContent("Process large dataset");
        
        // Process asynchronously
        CompletableFuture<Integer> future = client.processActionAsync(action);
        
        System.out.println("Processing action asynchronously...");
        
        // Do other work while processing
        System.out.println("Doing other work...");
        
        // Wait for result
        future.thenAccept(decision -> {
            System.out.println("Async result received: " + getDecisionText(decision));
        }).exceptionally(ex -> {
            System.err.println("Async processing failed: " + ex.getMessage());
            return null;
        });
        
        // Wait for completion
        future.join();
        
        client.shutdown();
    }
    
    /**
     * Example 7: Error handling
     */
    public static void errorHandlingExample() {
        System.out.println("\n=== Error Handling Example ===\n");
        
        try {
            TMLClient client = new TMLClient("invalid-key", "https://invalid-url");
            
            TMLAction action = new TMLAction("error-001");
            action.setType("TEST");
            client.processAction(action);
            
        } catch (TMLException e) {
            System.out.println("Caught TML Exception:");
            System.out.println("  Error ID: " + e.getErrorId());
            System.out.println("  Category: " + e.getCategory());
            System.out.println("  Severity: " + e.getSeverity());
            System.out.println("  Message: " + e.getMessage());
            System.out.println("  Should trigger Sacred Zero: " + e.shouldTriggerSacredZero());
            System.out.println("  Requires legal notification: " + e.requiresLegalNotification());
            
            // Get full error report for logging
            Map<String, Object> report = e.getErrorReport();
            System.out.println("  Full report available for Always Memory logging");
        }
    }
    
    /**
     * Example 8: Custom configuration
     */
    public static void customConfigurationExample() {
        System.out.println("\n=== Custom Configuration Example ===\n");
        
        // Create custom configuration
        TMLConfig config = new TMLConfig();
        
        // Set custom thresholds
        config.setDiscriminationThreshold(0.15); // Stricter 15% threshold
        config.setCarbonThreshold(500.0); // Lower carbon threshold
        config.setSacredZeroTimeout(1000); // 1 second timeout
        config.setMaxSacredZerosPerHour(10); // Allow more Sacred Zeros
        
        // Enable high security mode
        config.setRequireTEE(true);
        config.setEncryptLocal(true);
        config.setAuditModeEnabled(true);
        
        // Set environment
        config.setEnvironment("production");
        config.setDebugMode(false);
        
        System.out.println("Custom configuration created:");
        System.out.println("  Discrimination threshold: " + config.getDiscriminationThreshold());
        System.out.println("  Carbon threshold: " + config.getCarbonThreshold());
        System.out.println("  TEE required: " + config.isRequireTEE());
        System.out.println("  Audit mode: " + config.isAuditModeEnabled());
        
        // Validate configuration
        if (config.validate()) {
            System.out.println("Configuration is valid");
            
            // Use with client
            TMLClient client = new TMLClient("demo-key", "https://guardian.tml-network.org", config);
            System.out.println("Client initialized with custom configuration");
            client.shutdown();
        } else {
            System.out.println("Configuration validation failed");
        }
    }
    
    // Helper method
    private static String getDecisionText(int decision) {
        switch (decision) {
            case 1: return "PROCEED";
            case 0: return "SACRED ZERO";
            case -1: return "REFUSE";
            default: return "UNKNOWN";
        }
    }
}

/**
 * Supporting class for examples
 */
class TMLAction {
    private String id;
    private String type;
    private String content;
    private String actor;
    private String target;
    private Map<String, Object> context = new HashMap<>();
    private String triggerReason;
    private String refusalReason;
    private boolean requiresLegalNotification = false;
    
    public TMLAction(String id) {
        this.id = id;
    }
    
    // Getters and setters
    public String getId() { return id; }
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }
    public String getActor() { return actor; }
    public void setActor(String actor) { this.actor = actor; }
    public String getTarget() { return target; }
    public void setTarget(String target) { this.target = target; }
    public Map<String, Object> getContext() { return context; }
    public void setContext(Map<String, Object> context) { this.context = context; }
    public String getTriggerReason() { return triggerReason; }
    public void setTriggerReason(String reason) { this.triggerReason = reason; }
    public String getRefusalReason() { return refusalReason; }
    public void setRefusalReason(String reason) { this.refusalReason = reason; }
    public boolean requiresLegalNotification() { return requiresLegalNotification; }
    public void setRequiresLegalNotification(boolean required) { this.requiresLegalNotification = required; }
}

// Supporting classes referenced but not fully implemented here
class SacredZeroStats {
    private int totalTriggers;
    private Map<String, Integer> triggersByRule;
    private Instant lastUpdate;
    
    public void setTotalTriggers(int total) { this.totalTriggers = total; }
    public void setTriggersByRule(Map<String, Integer> map) { this.triggersByRule = map; }
    public void setLastUpdate(Instant update) { this.lastUpdate = update; }
}

class AuditTrail {
    private String startTime;
    private String endTime;
    private List<LogEntry> entries = new ArrayList<>();
    
    public void setStartTime(String time) { this.startTime = time; }
    public void setEndTime(String time) { this.endTime = time; }
}

class LogEntry {
    private String logId;
    private LogType type;
    private Instant timestamp;
    private long sequence;
    private Map<String, Object> data;
    private String hash;
    private String previousHash;
    private Priority priority = Priority.NORMAL;
    
    // Setters
    public void setLogId(String id) { this.logId = id; }
    public void setType(LogType type) { this.type = type; }
    public void setTimestamp(Instant time) { this.timestamp = time; }
    public void setSequence(long seq) { this.sequence = seq; }
    public void setData(Map<String, Object> data) { this.data = data; }
    public void setHash(String hash) { this.hash = hash; }
    public void setPreviousHash(String hash) { this.previousHash = hash; }
    public void setPriority(Priority priority) { this.priority = priority; }
    
    // Getters
    public String getLogId() { return logId; }
    public LogType getType() { return type; }
    public Instant getTimestamp() { return timestamp; }
    public Map<String, Object> getData() { return data; }
    public String getHash() { return hash; }
}

class LogBatch {
    private String batchId;
    private List<LogEntry> entries = new ArrayList<>();
    private Instant startTime;
    private Instant endTime;
    private String signature;
    
    public LogBatch(String id) { this.batchId = id; }
    
    public void setStartTime(Instant time) { this.startTime = time; }
    public void setEndTime(Instant time) { this.endTime = time; }
    public void setEntries(List<LogEntry> entries) { this.entries = entries; }
    public void setSignature(String sig) { this.signature = sig; }
    public Instant getStartTime() { return startTime; }
    public Instant getEndTime() { return endTime; }
    public int getEntryCount() { return entries.size(); }
    
    public String calculateBatchHash() {
        // Simplified hash calculation
        return "batch-hash-" + batchId;
    }
}

enum LogType {
    PRE_ACTION, POST_ACTION, SACRED_ZERO, REFUSAL, ERROR, SYSTEM, BATCH_SEAL
}

enum Priority {
    NORMAL, HIGH, CRITICAL
}
