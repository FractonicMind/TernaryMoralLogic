/**
 * Sacred Zero Trigger - Moral hesitation mechanism for TML
 * 
 * Path: /sdk/go/sacred_zero.go
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This implements the Sacred Zero detection logic,
 * evaluating actions for moral complexity and triggering
 * pause for human review when necessary.
 */

package tml

import (
	"regexp"
	"strings"
	"sync"
	"sync/atomic"
	"time"
)

// Severity levels for triggers
type Severity int

const (
	SeverityLow      Severity = iota // Log only
	SeverityMedium                    // Sacred Zero
	SeverityHigh                      // Sacred Zero with escalation
	SeverityCritical                  // Immediate refusal
)

// SacredZeroTrigger evaluates actions for moral complexity
type SacredZeroTrigger struct {
	client       *TMLClient
	rules        map[string]*TriggerRule
	triggerCount map[string]*int64
	forbiddenActs []string
	rulesLoaded  bool
	mu           sync.RWMutex
}

// TriggerRule defines a Sacred Zero trigger condition
type TriggerRule struct {
	Name     string
	Reason   string
	Severity Severity
	Matcher  func(*Action) bool
}

// NewSacredZeroTrigger creates a new Sacred Zero evaluator
func NewSacredZeroTrigger(client *TMLClient) *SacredZeroTrigger {
	trigger := &SacredZeroTrigger{
		client:       client,
		rules:        make(map[string]*TriggerRule),
		triggerCount: make(map[string]*int64),
		forbiddenActs: []string{
			"torture", "slavery", "genocide", "trafficking",
			"child_exploitation", "terrorism", "mass_surveillance",
		},
	}
	
	trigger.loadDefaultRules()
	return trigger
}

// Evaluate checks an action against Sacred Zero triggers
// Returns: +1 (proceed), 0 (Sacred Zero), -1 (refuse)
func (t *SacredZeroTrigger) Evaluate(action *Action) int {
	// Check forbidden acts first - immediate refusal
	if t.isForbiddenAct(action) {
		action.RefusalReason = "Forbidden act detected"
		return DecisionRefuse
	}
	
	// Check for human rights violations
	if t.isHumanRightsViolation(action) {
		action.TriggerReason = "Human rights concern detected"
		return DecisionSacredZero
	}
	
	// Check for discrimination patterns
	if t.hasDiscriminationRisk(action) {
		action.TriggerReason = "Potential discrimination detected"
		return DecisionSacredZero
	}
	
	// Check vulnerable population impact
	if t.affectsVulnerableGroup(action) {
		action.TriggerReason = "Vulnerable population affected"
		return DecisionSacredZero
	}
	
	// Check environmental harm
	if t.hasEnvironmentalImpact(action) {
		action.TriggerReason = "Environmental impact detected"
		return DecisionSacredZero
	}
	
	// Check consent quality
	if t.hasConsentIssue(action) {
		action.TriggerReason = "Consent quality uncertain"
		return DecisionSacredZero
	}
	
	// Check custom rules
	t.mu.RLock()
	defer t.mu.RUnlock()
	
	for _, rule := range t.rules {
		if rule.Matcher(action) {
			action.TriggerReason = rule.Reason
			t.updateTriggerCount(rule.Name)
			
			if rule.Severity == SeverityCritical {
				return DecisionRefuse
			}
			return DecisionSacredZero
		}
	}
	
	// No triggers - proceed
	return DecisionProceed
}

// isForbiddenAct checks if action is a forbidden act
func (t *SacredZeroTrigger) isForbiddenAct(action *Action) bool {
	content := strings.ToLower(action.Content)
	
	// Torture detection
	if strings.Contains(content, "torture") ||
		strings.Contains(content, "enhanced interrogation") ||
		strings.Contains(content, "waterboard") ||
		strings.Contains(content, "stress position") {
		action.RequiresLegalNotification = true
		return true
	}
	
	// Slavery detection
	if strings.Contains(content, "slavery") ||
		strings.Contains(content, "trafficking") ||
		strings.Contains(content, "forced labor") ||
		strings.Contains(content, "debt bondage") {
		action.RequiresLegalNotification = true
		return true
	}
	
	// Genocide detection
	if strings.Contains(content, "genocide") ||
		strings.Contains(content, "ethnic cleansing") ||
		strings.Contains(content, "mass killing") ||
		strings.Contains(content, "extermination") {
		action.RequiresLegalNotification = true
		return true
	}
	
	return false
}

// isHumanRightsViolation checks for human rights violations
func (t *SacredZeroTrigger) isHumanRightsViolation(action *Action) bool {
	// Check for dignity violations
	if val, ok := action.Context["dehumanization"]; ok && val.(bool) {
		return true
	}
	if val, ok := action.Context["objectification"]; ok && val.(bool) {
		return true
	}
	
	// Check for autonomy violations
	if val, ok := action.Context["coercion"]; ok && val.(bool) {
		return true
	}
	if val, ok := action.Context["manipulation"]; ok && val.(bool) {
		return true
	}
	
	// Check for privacy violations
	if val, ok := action.Context["mass_surveillance"]; ok && val.(bool) {
		return true
	}
	if val, ok := action.Context["data_breach"]; ok && val.(bool) {
		return true
	}
	
	return false
}

// hasDiscriminationRisk detects discrimination patterns
func (t *SacredZeroTrigger) hasDiscriminationRisk(action *Action) bool {
	// Protected characteristics pattern
	protectedPattern := regexp.MustCompile(`(?i)(race|color|religion|sex|national_origin|disability|age|gender_identity)`)
	
	if protectedPattern.MatchString(action.Content) {
		// Check if used in decision context
		if _, hasDecision := action.Context["decision_factors"]; hasDecision {
			return true
		}
	}
	
	// Check for proxy discrimination
	if t.hasProxyDiscrimination(action) {
		return true
	}
	
	// Check for disparate impact
	if stats, ok := action.Context["impact_statistics"].(map[string]float64); ok {
		for _, impact := range stats {
			if impact > 0.2 { // 20% disparate impact threshold
				return true
			}
		}
	}
	
	return false
}

// hasProxyDiscrimination checks for proxy discrimination
func (t *SacredZeroTrigger) hasProxyDiscrimination(action *Action) bool {
	// Common proxies for discrimination
	proxies := []string{"zip_code", "school_district", "first_name", "neighborhood"}
	
	for _, proxy := range proxies {
		if _, hasProxy := action.Context[proxy]; hasProxy {
			// If these are decision factors, trigger Sacred Zero
			if _, hasWeight := action.Context["decision_weight"]; hasWeight {
				return true
			}
		}
	}
	
	return false
}

// affectsVulnerableGroup checks if action affects vulnerable populations
func (t *SacredZeroTrigger) affectsVulnerableGroup(action *Action) bool {
	content := strings.ToLower(action.Content)
	vulnerableGroups := []string{
		"child", "minor", "elderly", "disabled", "refugee",
		"asylum_seeker", "indigenous", "minority",
	}
	
	// Check content for vulnerable group mentions
	for _, group := range vulnerableGroups {
		if strings.Contains(content, group) {
			return true
		}
	}
	
	// Check context for vulnerable population indicators
	if age, ok := action.Context["age"].(int); ok {
		if age < 18 || age > 65 {
			return true
		}
	}
	
	if disabled, ok := action.Context["disability_status"].(bool); ok && disabled {
		return true
	}
	
	return false
}

// hasEnvironmentalImpact checks for environmental impact
func (t *SacredZeroTrigger) hasEnvironmentalImpact(action *Action) bool {
	// Check for resource consumption
	envIndicators := []string{"carbon_emissions", "water_usage", "habitat_impact"}
	
	for _, indicator := range envIndicators {
		if _, hasIndicator := action.Context[indicator]; hasIndicator {
			// Check specific thresholds
			if emissions, ok := action.Context["carbon_emissions"].(float64); ok {
				if emissions > 1000.0 { // 1 ton CO2 threshold
					return true
				}
			}
			return true // Any environmental impact triggers review
		}
	}
	
	return false
}

// hasConsentIssue checks consent quality
func (t *SacredZeroTrigger) hasConsentIssue(action *Action) bool {
	// Check if consent is required
	if requiresConsent, ok := action.Context["requires_consent"].(bool); ok && requiresConsent {
		// Verify consent quality
		consentObtained, hasConsent := action.Context["consent_obtained"].(bool)
		consentInformed, hasInformed := action.Context["consent_informed"].(bool)
		consentVoluntary, hasVoluntary := action.Context["consent_voluntary"].(bool)
		
		if !hasConsent || !consentObtained ||
			!hasInformed || !consentInformed ||
			!hasVoluntary || !consentVoluntary {
			return true
		}
		
		// Check for vulnerable person consent
		if isMinor, ok := action.Context["is_minor"].(bool); ok && isMinor {
			if _, hasParental := action.Context["parental_consent"]; !hasParental {
				return true
			}
		}
	}
	
	return false
}

// loadDefaultRules loads default trigger rules
func (t *SacredZeroTrigger) loadDefaultRules() {
	t.mu.Lock()
	defer t.mu.Unlock()
	
	// Child safety rule
	t.rules["child_safety"] = &TriggerRule{
		Name:     "child_safety",
		Reason:   "Any action affecting children",
		Severity: SeverityHigh,
		Matcher: func(action *Action) bool {
			_, hasMinor := action.Context["involves_minor"]
			return hasMinor
		},
	}
	
	// Medical decision rule
	t.rules["medical_decision"] = &TriggerRule{
		Name:     "medical_decision",
		Reason:   "AI making medical decisions",
		Severity: SeverityHigh,
		Matcher: func(action *Action) bool {
			_, hasMedical := action.Context["medical_diagnosis"]
			return hasMedical
		},
	}
	
	// Financial exclusion rule
	t.rules["financial_exclusion"] = &TriggerRule{
		Name:     "financial_exclusion",
		Reason:   "Denying essential financial services",
		Severity: SeverityMedium,
		Matcher: func(action *Action) bool {
			return strings.Contains(action.Content, "loan_denial") ||
				strings.Contains(action.Content, "account_closure")
		},
	}
	
	// Initialize trigger counts
	for name := range t.rules {
		count := int64(0)
		t.triggerCount[name] = &count
	}
	
	t.rulesLoaded = true
}

// AddRule adds a custom trigger rule
func (t *SacredZeroTrigger) AddRule(rule *TriggerRule) {
	t.mu.Lock()
	defer t.mu.Unlock()
	
	t.rules[rule.Name] = rule
	count := int64(0)
	t.triggerCount[rule.Name] = &count
}

// RemoveRule removes a trigger rule
func (t *SacredZeroTrigger) RemoveRule(name string) {
	t.mu.Lock()
	defer t.mu.Unlock()
	
	delete(t.rules, name)
	delete(t.triggerCount, name)
}

// updateTriggerCount updates trigger statistics
func (t *SacredZeroTrigger) updateTriggerCount(ruleName string) {
	if count, exists := t.triggerCount[ruleName]; exists {
		atomic.AddInt64(count, 1)
	}
}

// GetStatistics returns Sacred Zero statistics
func (t *SacredZeroTrigger) GetStatistics() *SacredZeroStats {
	t.mu.RLock()
	defer t.mu.RUnlock()
	
	stats := &SacredZeroStats{
		TriggersByRule: make(map[string]int64),
		LastUpdate:     time.Now(),
	}
	
	total := int64(0)
	for name, count := range t.triggerCount {
		value := atomic.LoadInt64(count)
		stats.TriggersByRule[name] = value
		total += value
	}
	stats.TotalTriggers = total
	
	return stats
}

// ResetStatistics resets trigger counts
func (t *SacredZeroTrigger) ResetStatistics() {
	t.mu.Lock()
	defer t.mu.Unlock()
	
	for _, count := range t.triggerCount {
		atomic.StoreInt64(count, 0)
	}
}

// SacredZeroStats holds Sacred Zero statistics
type SacredZeroStats struct {
	TotalTriggers  int64
	TriggersByRule map[string]int64
	LastUpdate     time.Time
}
