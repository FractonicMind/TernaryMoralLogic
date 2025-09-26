/**
 * TML Configuration - Configuration management for TML SDK
 * 
 * Path: /sdk/java/TMLConfig.java
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This class manages configuration settings for TML client,
 * including Guardian endpoints, security settings, and 
 * operational parameters.
 */

package org.tml.sdk;

import java.util.Map;
import java.util.HashMap;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;

public class TMLConfig {
    
    // Network Configuration
    private String guardianUrl = "https://guardian.tml-network.org";
    private String[] backupGuardians = {
        "https://guardian2.tml-network.org",
        "https://guardian3.tml-network.org"
    };
    private int connectionTimeout = 5000; // ms
    private int readTimeout = 10000; // ms
    private int maxRetries = 3;
    
    // Security Configuration
    private boolean requireTEE = false; // TEE requirement
    private boolean encryptLocal = true; // Encrypt local storage
    private String hmacKey = ""; // HMAC key for signing
    private boolean validateCertificates = true;
    private String[] trustedCAs = {};
    
    // Sacred Zero Configuration
    private boolean blockOnSacredZero = true; // Block until review
    private long sacredZeroTimeout = 500; // ms
    private int maxSacredZerosPerHour = 5; // Rate limit
    private boolean autoEscalate = true; // Auto-escalate repeated triggers
    
    // Always Memory Configuration
    private boolean localStorageEnabled = true;
    private String localStoragePath = "/var/tml/logs";
    private long maxLocalStorageSize = 10L * 1024 * 1024 * 1024; // 10GB
    private int batchSize = 1000;
    private long batchTimeout = 100; // ms
    private boolean compressLogs = true;
    
    // Operational Configuration
    private String environment = "production"; // production, staging, development
    private boolean debugMode = false;
    private String logLevel = "INFO"; // DEBUG, INFO, WARN, ERROR
    private boolean metricsEnabled = true;
    private int metricsReportInterval = 60000; // ms
    
    // Human Rights Configuration
    private double discriminationThreshold = 0.2; // 20% disparate impact
    private boolean vulnerablePopulationEnhanced = true;
    private String[] protectedCharacteristics = {
        "race", "color", "religion", "sex", "national_origin",
        "disability", "age", "gender_identity", "sexual_orientation"
    };
    
    // Environmental Configuration
    private double carbonThreshold = 1000.0; // kg CO2
    private double waterThreshold = 10000.0; // liters
    private boolean indigenousDataSovereignty = true;
    
    // Compliance Configuration
    private String jurisdiction = "US"; // Primary jurisdiction
    private String[] complianceFrameworks = {
        "GDPR", "CCPA", "EU_AI_ACT", "UN_HUMAN_RIGHTS"
    };
    private boolean auditModeEnabled = false;
    
    /**
     * Default constructor with standard settings
     */
    public TMLConfig() {
        // Use defaults as initialized above
    }
    
    /**
     * Create config from properties file
     */
    public TMLConfig(String propertiesPath) {
        loadFromProperties(propertiesPath);
    }
    
    /**
     * Create config from map
     */
    public TMLConfig(Map<String, Object> settings) {
        applySettings(settings);
    }
    
    /**
     * Get default configuration
     */
    public static TMLConfig getDefault() {
        return new TMLConfig();
    }
    
    /**
     * Get development configuration
     */
    public static TMLConfig getDevelopment() {
        TMLConfig config = new TMLConfig();
        config.environment = "development";
        config.debugMode = true;
        config.logLevel = "DEBUG";
        config.requireTEE = false;
        config.validateCertificates = false;
        config.guardianUrl = "http://localhost:8080";
        return config;
    }
    
    /**
     * Get high-security configuration
     */
    public static TMLConfig getHighSecurity() {
        TMLConfig config = new TMLConfig();
        config.requireTEE = true;
        config.encryptLocal = true;
        config.validateCertificates = true;
        config.blockOnSacredZero = true;
        config.auditModeEnabled = true;
        config.maxSacredZerosPerHour = 3;
        return config;
    }
    
    /**
     * Load configuration from properties file
     */
    private void loadFromProperties(String path) {
        Properties props = new Properties();
        try (FileInputStream fis = new FileInputStream(path)) {
            props.load(fis);
            
            // Network settings
            guardianUrl = props.getProperty("tml.guardian.url", guardianUrl);
            connectionTimeout = Integer.parseInt(
                props.getProperty("tml.connection.timeout", String.valueOf(connectionTimeout)));
            readTimeout = Integer.parseInt(
                props.getProperty("tml.read.timeout", String.valueOf(readTimeout)));
            
            // Security settings
            requireTEE = Boolean.parseBoolean(
                props.getProperty("tml.security.tee", String.valueOf(requireTEE)));
            encryptLocal = Boolean.parseBoolean(
                props.getProperty("tml.security.encrypt", String.valueOf(encryptLocal)));
            hmacKey = props.getProperty("tml.security.hmac", "");
            
            // Sacred Zero settings
            blockOnSacredZero = Boolean.parseBoolean(
                props.getProperty("tml.sacred.block", String.valueOf(blockOnSacredZero)));
            sacredZeroTimeout = Long.parseLong(
                props.getProperty("tml.sacred.timeout", String.valueOf(sacredZeroTimeout)));
            
            // Always Memory settings
            localStorageEnabled = Boolean.parseBoolean(
                props.getProperty("tml.memory.local", String.valueOf(localStorageEnabled)));
            localStoragePath = props.getProperty("tml.memory.path", localStoragePath);
            batchSize = Integer.parseInt(
                props.getProperty("tml.memory.batch", String.valueOf(batchSize)));
            
            // Operational settings
            environment = props.getProperty("tml.environment", environment);
            debugMode = Boolean.parseBoolean(
                props.getProperty("tml.debug", String.valueOf(debugMode)));
            logLevel = props.getProperty("tml.log.level", logLevel);
            
            // Human Rights settings
            discriminationThreshold = Double.parseDouble(
                props.getProperty("tml.rights.threshold", String.valueOf(discriminationThreshold)));
            
            // Environmental settings
            carbonThreshold = Double.parseDouble(
                props.getProperty("tml.env.carbon", String.valueOf(carbonThreshold)));
            waterThreshold = Double.parseDouble(
                props.getProperty("tml.env.water", String.valueOf(waterThreshold)));
            
            // Compliance settings
            jurisdiction = props.getProperty("tml.compliance.jurisdiction", jurisdiction);
            auditModeEnabled = Boolean.parseBoolean(
                props.getProperty("tml.compliance.audit", String.valueOf(auditModeEnabled)));
            
        } catch (IOException e) {
            throw new TMLException("Failed to load configuration from: " + path, e);
        }
    }
    
    /**
     * Apply settings from map
     */
    private void applySettings(Map<String, Object> settings) {
        settings.forEach((key, value) -> {
            switch (key) {
                case "guardianUrl":
                    this.guardianUrl = (String) value;
                    break;
                case "requireTEE":
                    this.requireTEE = (Boolean) value;
                    break;
                case "blockOnSacredZero":
                    this.blockOnSacredZero = (Boolean) value;
                    break;
                case "environment":
                    this.environment = (String) value;
                    break;
                case "debugMode":
                    this.debugMode = (Boolean) value;
                    break;
                case "discriminationThreshold":
                    this.discriminationThreshold = (Double) value;
                    break;
                case "carbonThreshold":
                    this.carbonThreshold = (Double) value;
                    break;
                // Add more cases as needed
            }
        });
    }
    
    /**
     * Validate configuration
     */
    public boolean validate() {
        // Check required fields
        if (guardianUrl == null || guardianUrl.isEmpty()) {
            return false;
        }
        
        // Check thresholds
        if (discriminationThreshold < 0 || discriminationThreshold > 1) {
            return false;
        }
        
        // Check timeouts
        if (connectionTimeout <= 0 || readTimeout <= 0) {
            return false;
        }
        
        // Check batch settings
        if (batchSize <= 0 || batchTimeout <= 0) {
            return false;
        }
        
        // Validate environment
        if (!environment.matches("production|staging|development")) {
            return false;
        }
        
        // Validate log level
        if (!logLevel.matches("DEBUG|INFO|WARN|ERROR")) {
            return false;
        }
        
        return true;
    }
    
    /**
     * Create a copy of this configuration
     */
    public TMLConfig copy() {
        TMLConfig copy = new TMLConfig();
        
        // Copy all fields
        copy.guardianUrl = this.guardianUrl;
        copy.backupGuardians = this.backupGuardians.clone();
        copy.connectionTimeout = this.connectionTimeout;
        copy.readTimeout = this.readTimeout;
        copy.maxRetries = this.maxRetries;
        
        copy.requireTEE = this.requireTEE;
        copy.encryptLocal = this.encryptLocal;
        copy.hmacKey = this.hmacKey;
        copy.validateCertificates = this.validateCertificates;
        
        copy.blockOnSacredZero = this.blockOnSacredZero;
        copy.sacredZeroTimeout = this.sacredZeroTimeout;
        copy.maxSacredZerosPerHour = this.maxSacredZerosPerHour;
        copy.autoEscalate = this.autoEscalate;
        
        copy.localStorageEnabled = this.localStorageEnabled;
        copy.localStoragePath = this.localStoragePath;
        copy.maxLocalStorageSize = this.maxLocalStorageSize;
        copy.batchSize = this.batchSize;
        copy.batchTimeout = this.batchTimeout;
        copy.compressLogs = this.compressLogs;
        
        copy.environment = this.environment;
        copy.debugMode = this.debugMode;
        copy.logLevel = this.logLevel;
        copy.metricsEnabled = this.metricsEnabled;
        copy.metricsReportInterval = this.metricsReportInterval;
        
        copy.discriminationThreshold = this.discriminationThreshold;
        copy.vulnerablePopulationEnhanced = this.vulnerablePopulationEnhanced;
        copy.protectedCharacteristics = this.protectedCharacteristics.clone();
        
        copy.carbonThreshold = this.carbonThreshold;
        copy.waterThreshold = this.waterThreshold;
        copy.indigenousDataSovereignty = this.indigenousDataSovereignty;
        
        copy.jurisdiction = this.jurisdiction;
        copy.complianceFrameworks = this.complianceFrameworks.clone();
        copy.auditModeEnabled = this.auditModeEnabled;
        
        return copy;
    }
    
    /**
     * Export configuration as map
     */
    public Map<String, Object> toMap() {
        Map<String, Object> map = new HashMap<>();
        
        map.put("guardianUrl", guardianUrl);
        map.put("connectionTimeout", connectionTimeout);
        map.put("requireTEE", requireTEE);
        map.put("blockOnSacredZero", blockOnSacredZero);
        map.put("environment", environment);
        map.put("discriminationThreshold", discriminationThreshold);
        map.put("carbonThreshold", carbonThreshold);
        // Add all other fields as needed
        
        return map;
    }
    
    // Getters and setters for all fields
    
    public String getGuardianUrl() { return guardianUrl; }
    public void setGuardianUrl(String url) { this.guardianUrl = url; }
    
    public String[] getBackupGuardians() { return backupGuardians; }
    public void setBackupGuardians(String[] urls) { this.backupGuardians = urls; }
    
    public int getConnectionTimeout() { return connectionTimeout; }
    public void setConnectionTimeout(int timeout) { this.connectionTimeout = timeout; }
    
    public int getReadTimeout() { return readTimeout; }
    public void setReadTimeout(int timeout) { this.readTimeout = timeout; }
    
    public boolean isRequireTEE() { return requireTEE; }
    public void setRequireTEE(boolean require) { this.requireTEE = require; }
    
    public boolean isEncryptLocal() { return encryptLocal; }
    public void setEncryptLocal(boolean encrypt) { this.encryptLocal = encrypt; }
    
    public String getHMACKey() { return hmacKey; }
    public void setHMACKey(String key) { this.hmacKey = key; }
    
    public boolean isBlockOnSacredZero() { return blockOnSacredZero; }
    public void setBlockOnSacredZero(boolean block) { this.blockOnSacredZero = block; }
    
    public long getSacredZeroTimeout() { return sacredZeroTimeout; }
    public void setSacredZeroTimeout(long timeout) { this.sacredZeroTimeout = timeout; }
    
    public boolean isLocalStorageEnabled() { return localStorageEnabled; }
    public void setLocalStorageEnabled(boolean enabled) { this.localStorageEnabled = enabled; }
    
    public String getLocalStoragePath() { return localStoragePath; }
    public void setLocalStoragePath(String path) { this.localStoragePath = path; }
    
    public int getBatchSize() { return batchSize; }
    public void setBatchSize(int size) { this.batchSize = size; }
    
    public String getEnvironment() { return environment; }
    public void setEnvironment(String env) { this.environment = env; }
    
    public boolean isDebugMode() { return debugMode; }
    public void setDebugMode(boolean debug) { this.debugMode = debug; }
    
    public String getLogLevel() { return logLevel; }
    public void setLogLevel(String level) { this.logLevel = level; }
    
    public double getDiscriminationThreshold() { return discriminationThreshold; }
    public void setDiscriminationThreshold(double threshold) { this.discriminationThreshold = threshold; }
    
    public double getCarbonThreshold() { return carbonThreshold; }
    public void setCarbonThreshold(double threshold) { this.carbonThreshold = threshold; }
    
    public String getJurisdiction() { return jurisdiction; }
    public void setJurisdiction(String jurisdiction) { this.jurisdiction = jurisdiction; }
    
    public boolean isAuditModeEnabled() { return auditModeEnabled; }
    public void setAuditModeEnabled(boolean enabled) { this.auditModeEnabled = enabled; }
}
