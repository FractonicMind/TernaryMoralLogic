/**
 * TML Exception - Custom exception handling for TML SDK
 * 
 * Path: /sdk/java/TMLException.java
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This class provides structured exception handling for TML operations,
 * ensuring that all errors are properly logged in Always Memory and
 * that Sacred Zero triggers on unexpected failures.
 */

package org.tml.sdk;

import java.time.Instant;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class TMLException extends RuntimeException {
    
    private final String errorId;
    private final ErrorCategory category;
    private final ErrorSeverity severity;
    private final Map<String, Object> context;
    private final Instant timestamp;
    private boolean logged = false;
    
    /**
     * Error categories for classification
     */
    public enum ErrorCategory {
        CONFIGURATION("Configuration error"),
        CONNECTION("Network/connection error"),
        AUTHENTICATION("Authentication/authorization error"),
        VALIDATION("Input validation error"),
        SACRED_ZERO("Sacred Zero trigger error"),
        ALWAYS_MEMORY("Always Memory logging error"),
        COUNCIL("Stewardship Council error"),
        TEE("Trusted Execution Environment error"),
        COMPLIANCE("Compliance violation error"),
        HUMAN_RIGHTS("Human rights protection error"),
        ENVIRONMENTAL("Environmental protection error"),
        SYSTEM("System/internal error");
        
        private final String description;
        
        ErrorCategory(String description) {
            this.description = description;
        }
        
        public String getDescription() {
            return description;
        }
    }
    
    /**
     * Error severity levels
     */
    public enum ErrorSeverity {
        LOW("Minor issue, can continue"),
        MEDIUM("Degraded operation"),
        HIGH("Significant impact, Sacred Zero triggered"),
        CRITICAL("System failure, immediate shutdown required");
        
        private final String description;
        
        ErrorSeverity(String description) {
            this.description = description;
        }
        
        public String getDescription() {
            return description;
        }
    }
    
    /**
     * Basic constructor with message
     */
    public TMLException(String message) {
        this(message, ErrorCategory.SYSTEM, ErrorSeverity.MEDIUM);
    }
    
    /**
     * Constructor with message and cause
     */
    public TMLException(String message, Throwable cause) {
        this(message, cause, ErrorCategory.SYSTEM, ErrorSeverity.MEDIUM);
    }
    
    /**
     * Constructor with category and severity
     */
    public TMLException(String message, ErrorCategory category, ErrorSeverity severity) {
        super(message);
        this.errorId = generateErrorId();
        this.category = category;
        this.severity = severity;
        this.context = new HashMap<>();
        this.timestamp = Instant.now();
    }
    
    /**
     * Full constructor with cause
     */
    public TMLException(String message, Throwable cause, ErrorCategory category, ErrorSeverity severity) {
        super(message, cause);
        this.errorId = generateErrorId();
        this.category = category;
        this.severity = severity;
        this.context = new HashMap<>();
        this.timestamp = Instant.now();
        
        // Add cause information to context
        if (cause != null) {
            context.put("cause_type", cause.getClass().getName());
            context.put("cause_message", cause.getMessage());
        }
    }
    
    /**
     * Add context information
     */
    public TMLException withContext(String key, Object value) {
        this.context.put(key, value);
        return this;
    }
    
    /**
     * Add multiple context entries
     */
    public TMLException withContext(Map<String, Object> contextData) {
        this.context.putAll(contextData);
        return this;
    }
    
    /**
     * Check if this error should trigger Sacred Zero
     */
    public boolean shouldTriggerSacredZero() {
        // High and Critical errors always trigger Sacred Zero
        if (severity == ErrorSeverity.HIGH || severity == ErrorSeverity.CRITICAL) {
            return true;
        }
        
        // Certain categories always trigger Sacred Zero
        if (category == ErrorCategory.HUMAN_RIGHTS || 
            category == ErrorCategory.ENVIRONMENTAL ||
            category == ErrorCategory.COMPLIANCE) {
            return true;
        }
        
        // Check context for specific triggers
        if (context.containsKey("affects_vulnerable_population") &&
            (Boolean) context.get("affects_vulnerable_population")) {
            return true;
        }
        
        if (context.containsKey("discrimination_detected") &&
            (Boolean) context.get("discrimination_detected")) {
            return true;
        }
        
        return false;
    }
    
    /**
     * Check if this error requires legal notification
     */
    public boolean requiresLegalNotification() {
        // Critical compliance violations
        if (category == ErrorCategory.COMPLIANCE && severity == ErrorSeverity.CRITICAL) {
            return true;
        }
        
        // Human rights violations
        if (category == ErrorCategory.HUMAN_RIGHTS &&
            (severity == ErrorSeverity.HIGH || severity == ErrorSeverity.CRITICAL)) {
            return true;
        }
        
        // Check context for specific requirements
        if (context.containsKey("legal_notification_required") &&
            (Boolean) context.get("legal_notification_required")) {
            return true;
        }
        
        return false;
    }
    
    /**
     * Get structured error report for logging
     */
    public Map<String, Object> getErrorReport() {
        Map<String, Object> report = new HashMap<>();
        
        report.put("error_id", errorId);
        report.put("timestamp", timestamp.toString());
        report.put("category", category.name());
        report.put("category_desc", category.getDescription());
        report.put("severity", severity.name());
        report.put("severity_desc", severity.getDescription());
        report.put("message", getMessage());
        report.put("context", context);
        
        if (getCause() != null) {
            Map<String, Object> causeInfo = new HashMap<>();
            causeInfo.put("type", getCause().getClass().getName());
            causeInfo.put("message", getCause().getMessage());
            causeInfo.put("stack_trace", getStackTraceString(getCause()));
            report.put("cause", causeInfo);
        }
        
        report.put("stack_trace", getStackTraceString(this));
        report.put("sacred_zero_required", shouldTriggerSacredZero());
        report.put("legal_notification_required", requiresLegalNotification());
        
        return report;
    }
    
    /**
     * Mark this exception as logged to Always Memory
     */
    public void markLogged() {
        this.logged = true;
    }
    
    /**
     * Check if this exception has been logged
     */
    public boolean isLogged() {
        return logged;
    }
    
    /**
     * Create an exception for configuration errors
     */
    public static TMLException configurationError(String message) {
        return new TMLException(message, ErrorCategory.CONFIGURATION, ErrorSeverity.HIGH);
    }
    
    /**
     * Create an exception for connection errors
     */
    public static TMLException connectionError(String message, Throwable cause) {
        return new TMLException(message, cause, ErrorCategory.CONNECTION, ErrorSeverity.MEDIUM);
    }
    
    /**
     * Create an exception for Sacred Zero violations
     */
    public static TMLException sacredZeroViolation(String message) {
        return new TMLException(message, ErrorCategory.SACRED_ZERO, ErrorSeverity.HIGH);
    }
    
    /**
     * Create an exception for Always Memory failures
     */
    public static TMLException alwaysMemoryFailure(String message, Throwable cause) {
        return new TMLException(message, cause, ErrorCategory.ALWAYS_MEMORY, ErrorSeverity.CRITICAL);
    }
    
    /**
     * Create an exception for human rights violations
     */
    public static TMLException humanRightsViolation(String message) {
        TMLException ex = new TMLException(message, ErrorCategory.HUMAN_RIGHTS, ErrorSeverity.CRITICAL);
        ex.withContext("legal_notification_required", true);
        return ex;
    }
    
    /**
     * Create an exception for environmental violations
     */
    public static TMLException environmentalViolation(String message, Map<String, Object> impact) {
        TMLException ex = new TMLException(message, ErrorCategory.ENVIRONMENTAL, ErrorSeverity.HIGH);
        ex.withContext("environmental_impact", impact);
        return ex;
    }
    
    /**
     * Generate unique error ID
     */
    private String generateErrorId() {
        return String.format("TML-ERR-%d-%s",
            System.currentTimeMillis(),
            UUID.randomUUID().toString().substring(0, 8));
    }
    
    /**
     * Convert stack trace to string
     */
    private String getStackTraceString(Throwable throwable) {
        StringBuilder sb = new StringBuilder();
        for (StackTraceElement element : throwable.getStackTrace()) {
            sb.append("    at ").append(element.toString()).append("\n");
        }
        return sb.toString();
    }
    
    // Getters
    
    public String getErrorId() {
        return errorId;
    }
    
    public ErrorCategory getCategory() {
        return category;
    }
    
    public ErrorSeverity getSeverity() {
        return severity;
    }
    
    public Map<String, Object> getContext() {
        return new HashMap<>(context);
    }
    
    public Instant getTimestamp() {
        return timestamp;
    }
    
    @Override
    public String toString() {
        return String.format("TMLException[%s]: %s (Category: %s, Severity: %s) - %s",
            errorId,
            getMessage(),
            category.name(),
            severity.name(),
            context.isEmpty() ? "No additional context" : context.toString());
    }
}

================================================================================
NOTE: TMLConfig.java in the repository contains Go code, not Java code.
================================================================================
