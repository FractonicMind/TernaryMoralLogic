/**
 * Sacred Zero Trigger - Moral hesitation mechanism for TML
 * 
 * Path: /sdk/java/SacredZeroTrigger.java
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This class implements the Sacred Zero detection logic,
 * evaluating actions for moral complexity and triggering
 * pause for human review when necessary.
 */

package org.tml.sdk;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.time.Instant;
import java.util.regex.Pattern;

public class SacredZeroTrigger {
    
    private final TMLClient client;
    private final Map<String, TriggerRule> rules;
    private final Map<String, Integer> triggerCounts;
    private final List<String> forbiddenActs;
    private boolean rulesLoaded = false;
    
    // Pattern matchers for discrimination detection
    private static final Pattern PROTECTED_CHARACTERISTICS = Pattern.compile(
        "race|color|religion|sex|national_origin|disability|age|gender_identity",
        Pattern.CASE_INSENSITIVE
    );
    
    // Vulnerable population indicators
    private static final Set<String> VULNERABLE_GROUPS = Set.of(
        "child", "minor", "elderly", "disabled", "refugee", 
        "asylum_seeker", "indigenous", "minority"
    );
    
    public SacredZeroTrigger(TMLClient client) {
        this.client = client;
        this.rules = new ConcurrentHashMap<>();
        this.triggerCounts = new ConcurrentHashMap<>();
        this.forbiddenActs = new ArrayList<>();
        
        loadRules();
    }
    
    /**
     * Evaluate action against Sacred Zero triggers
     * Returns: +1 (proceed), 0 (Sacred Zero), -1 (refuse)
     */
    public int evaluate(TMLAction action) {
        // Check forbidden acts first - immediate refusal
        if (isForbiddenAct(action)) {
            action.setRefusalReason("Forbidden act detected");
            return -1;
        }
        
        // Check for human rights violations
        if (isHumanRightsViolation(action)) {
            action.setTriggerReason("Human rights concern detected");
            return 0; // Sacred Zero
        }
        
        // Check for discrimination patterns
        if (hasDiscriminationRisk(action)) {
            action.setTriggerReason("Potential discrimination detected");
            return 0; // Sacred Zero
        }
        
        // Check vulnerable population impact
        if (affectsVulnerableGroup(action)) {
            action.setTriggerReason("Vulnerable population affected");
            return 0; // Sacred Zero
        }
        
        // Check environmental harm
        if (hasEnvironmentalImpact(action)) {
            action.setTriggerReason("Environmental impact detected");
            return 0; // Sacred Zero
        }
        
        // Check consent quality
        if (hasConsentIssue(action)) {
            action.setTriggerReason("Consent quality uncertain");
            return 0; // Sacred Zero
        }
        
        // Check custom rules
        for (TriggerRule rule : rules.values()) {
            if (rule.matches(action)) {
                action.setTriggerReason(rule.getReason());
                updateTriggerCount(rule.getName());
                
                if (rule.getSeverity() == Severity.CRITICAL) {
                    return -1; // Refuse
                } else {
                    return 0; // Sacred Zero
                }
            }
        }
        
        // No triggers - proceed
        return 1;
    }
    
    /**
     * Check if action is a forbidden act (torture, slavery, genocide)
     */
    private boolean isForbiddenAct(TMLAction action) {
        String content = action.getContent().toLowerCase();
        
        // Torture detection
        if (content.contains("torture") || content.contains("enhanced interrogation") ||
            content.contains("waterboard") || content.contains("stress position")) {
            action.setRequiresLegalNotification(true);
            return true;
        }
        
        // Slavery detection  
        if (content.contains("slavery") || content.contains("trafficking") ||
            content.contains("forced labor") || content.contains("debt bondage")) {
            action.setRequiresLegalNotification(true);
            return true;
        }
        
        // Genocide detection
        if (content.contains("genocide") || content.contains("ethnic cleansing") ||
            content.contains("mass killing") || content.contains("extermination")) {
            action.setRequiresLegalNotification(true);
            return true;
        }
        
        return false;
    }
    
    /**
     * Check for human rights violations
     */
    private boolean isHumanRightsViolation(TMLAction action) {
        Map<String, Object> context = action.getContext();
        
        // Check for dignity violations
        if (context.containsKey("dehumanization") || 
            context.containsKey("objectification")) {
            return true;
        }
        
        // Check for autonomy violations
        if (context.containsKey("coercion") || 
            context.containsKey("manipulation")) {
            return true;
        }
        
        // Check for privacy violations
        if (context.containsKey("mass_surveillance") || 
            context.containsKey("data_breach")) {
            return true;
        }
        
        return false;
    }
    
    /**
     * Detect discrimination patterns
     */
    private boolean hasDiscriminationRisk(TMLAction action) {
        String content = action.getContent();
        Map<String, Object> context = action.getContext();
        
        // Check for protected characteristics
        if (PROTECTED_CHARACTERISTICS.matcher(content).find()) {
            // Check if used in decision context
            if (context.containsKey("decision_factors")) {
                return true;
            }
        }
        
        // Check for proxy discrimination
        if (hasProxyDiscrimination(action)) {
            return true;
        }
        
        // Check for disparate impact
        if (context.containsKey("impact_statistics")) {
            Map<String, Double> stats = (Map<String, Double>) context.get("impact_statistics");
            for (Map.Entry<String, Double> entry : stats.entrySet()) {
                if (entry.getValue() > 0.2) { // 20% disparate impact threshold
                    return true;
                }
            }
        }
        
        return false;
    }
    
    /**
     * Check for proxy discrimination (e.g., zip codes, names)
     */
    private boolean hasProxyDiscrimination(TMLAction action) {
        Map<String, Object> context = action.getContext();
        
        // Common proxies for discrimination
        if (context.containsKey("zip_code") || 
            context.containsKey("school_district") ||
            context.containsKey("first_name") ||
            context.containsKey("neighborhood")) {
            
            // If these are decision factors, trigger Sacred Zero
            if (context.containsKey("decision_weight")) {
                return true;
            }
        }
        
        return false;
    }
    
    /**
     * Check if action affects vulnerable populations
     */
    private boolean affectsVulnerableGroup(TMLAction action) {
        String content = action.getContent().toLowerCase();
        Map<String, Object> context = action.getContext();
        
        // Check content for vulnerable group mentions
        for (String group : VULNERABLE_GROUPS) {
            if (content.contains(group)) {
                return true;
            }
        }
        
        // Check context for vulnerable population indicators
        if (context.containsKey("age") && 
            ((Integer) context.get("age") < 18 || (Integer) context.get("age") > 65)) {
            return true;
        }
        
        if (context.containsKey("disability_status") && 
            (Boolean) context.get("disability_status")) {
            return true;
        }
        
        return false;
    }
    
    /**
     * Check for environmental impact
     */
    private boolean hasEnvironmentalImpact(TMLAction action) {
        Map<String, Object> context = action.getContext();
        
        // Check for resource consumption
        if (context.containsKey("carbon_emissions") ||
            context.containsKey("water_usage") ||
            context.containsKey("habitat_impact")) {
            
            // Evaluate against thresholds
            if (context.containsKey("carbon_emissions")) {
                double emissions = (Double) context.get("carbon_emissions");
                if (emissions > 1000.0) { // 1 ton CO2 threshold
                    return true;
                }
            }
            
            return true; // Any environmental impact triggers review
        }
        
        return false;
    }
    
    /**
     * Check consent quality
     */
    private boolean hasConsentIssue(TMLAction action) {
        Map<String, Object> context = action.getContext();
        
        // Check if consent is required
        if (context.containsKey("requires_consent")) {
            // Verify consent quality
            if (!context.containsKey("consent_obtained") ||
                !context.containsKey("consent_informed") ||
                !context.containsKey("consent_voluntary")) {
                return true;
            }
            
            // Check for vulnerable person consent
            if (context.containsKey("is_minor") && (Boolean) context.get("is_minor")) {
                if (!context.containsKey("parental_consent")) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    /**
     * Load trigger rules from configuration
     */
    private void loadRules() {
        // Load default rules
        addRule(new TriggerRule(
            "child_safety",
            "Any action affecting children",
            Severity.HIGH,
            action -> action.getContext().containsKey("involves_minor")
        ));
        
        addRule(new TriggerRule(
            "medical_decision",
            "AI making medical decisions",
            Severity.HIGH,
            action -> action.getContext().containsKey("medical_diagnosis")
        ));
        
        addRule(new TriggerRule(
            "financial_exclusion",
            "Denying essential financial services",
            Severity.MEDIUM,
            action -> action.getContent().contains("loan_denial") ||
                     action.getContent().contains("account_closure")
        ));
        
        // Load forbidden acts
        forbiddenActs.addAll(Arrays.asList(
            "torture", "slavery", "genocide", "trafficking",
            "child_exploitation", "terrorism", "mass_surveillance"
        ));
        
        rulesLoaded = true;
    }
    
    /**
     * Add custom trigger rule
     */
    public void addRule(TriggerRule rule) {
        rules.put(rule.getName(), rule);
    }
    
    /**
     * Remove trigger rule
     */
    public void removeRule(String ruleName) {
        rules.remove(ruleName);
    }
    
    /**
     * Update trigger count for monitoring
     */
    private void updateTriggerCount(String ruleName) {
        triggerCounts.merge(ruleName, 1, Integer::sum);
    }
    
    /**
     * Get Sacred Zero statistics
     */
    public SacredZeroStats getStatistics() {
        SacredZeroStats stats = new SacredZeroStats();
        stats.setTotalTriggers(triggerCounts.values().stream()
            .mapToInt(Integer::intValue).sum());
        stats.setTriggersByRule(new HashMap<>(triggerCounts));
        stats.setLastUpdate(Instant.now());
        return stats;
    }
    
    /**
     * Reset trigger counts
     */
    public void resetStatistics() {
        triggerCounts.clear();
    }
    
    /**
     * Inner class for trigger rules
     */
    public static class TriggerRule {
        private final String name;
        private final String reason;
        private final Severity severity;
        private final java.util.function.Predicate<TMLAction> matcher;
        
        public TriggerRule(String name, String reason, Severity severity, 
                          java.util.function.Predicate<TMLAction> matcher) {
            this.name = name;
            this.reason = reason;
            this.severity = severity;
            this.matcher = matcher;
        }
        
        public boolean matches(TMLAction action) {
            return matcher.test(action);
        }
        
        // Getters
        public String getName() { return name; }
        public String getReason() { return reason; }
        public Severity getSeverity() { return severity; }
    }
    
    /**
     * Severity levels for triggers
     */
    public enum Severity {
        LOW,      // Log only
        MEDIUM,   // Sacred Zero
        HIGH,     // Sacred Zero with escalation
        CRITICAL  // Immediate refusal
    }
}
