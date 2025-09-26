/**
 * TML Error Handling - Comprehensive error management for TML SDK
 * 
 * Path: /sdk/go/errors.go
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This provides structured error handling with severity levels,
 * categorization, and automatic escalation for Sacred Zero
 * violations and critical failures.
 */

package tml

import (
	"encoding/json"
	"fmt"
	"runtime"
	"strings"
	"time"
)

// ErrorSeverity defines the severity level of TML errors
type ErrorSeverity int

const (
	// SeverityInfo indicates informational error
	SeverityInfo ErrorSeverity = iota
	// SeverityWarning indicates warning level
	SeverityWarning
	// SeverityError indicates standard error
	SeverityError
	// SeverityCritical indicates critical failure requiring attention
	SeverityCritical
	// SeverityFatal indicates Sacred Zero violation - immediate halt required
	SeverityFatal
)

// ErrorCategory defines the category of TML errors
type ErrorCategory string

const (
	// Core TML Categories
	CategorySacredZero    ErrorCategory = "SACRED_ZERO"
	CategoryAlwaysMemory  ErrorCategory = "ALWAYS_MEMORY"
	CategoryConfiguration ErrorCategory = "CONFIGURATION"
	CategoryNetwork       ErrorCategory = "NETWORK"
	CategorySecurity      ErrorCategory = "SECURITY"
	
	// Human Rights Categories
	CategoryDiscrimination   ErrorCategory = "DISCRIMINATION"
	CategoryPrivacy          ErrorCategory = "PRIVACY"
	CategoryConsent          ErrorCategory = "CONSENT"
	CategoryAccessibility    ErrorCategory = "ACCESSIBILITY"
	CategoryDignity          ErrorCategory = "DIGNITY"
	
	// Environmental Categories
	CategoryCarbon           ErrorCategory = "CARBON_IMPACT"
	CategoryWater            ErrorCategory = "WATER_IMPACT"
	CategoryBiodiversity     ErrorCategory = "BIODIVERSITY"
	CategoryIndigenous       ErrorCategory = "INDIGENOUS_RIGHTS"
	CategoryCircularEconomy  ErrorCategory = "CIRCULAR_ECONOMY"
	
	// Operational Categories
	CategoryValidation       ErrorCategory = "VALIDATION"
	CategoryGuardian         ErrorCategory = "GUARDIAN"
	CategoryStorage          ErrorCategory = "STORAGE"
	CategoryCompliance       ErrorCategory = "COMPLIANCE"
)

// TMLError represents a comprehensive error in the TML system
type TMLError struct {
	// Core fields
	Code        string        `json:"code"`
	Message     string        `json:"message"`
	Category    ErrorCategory `json:"category"`
	Severity    ErrorSeverity `json:"severity"`
	Timestamp   time.Time     `json:"timestamp"`
	
	// Context fields
	Context     map[string]interface{} `json:"context,omitempty"`
	StackTrace  []string               `json:"stack_trace,omitempty"`
	OriginalErr error                  `json:"-"`
	
	// Tracking fields
	TraceID     string `json:"trace_id"`
	SpanID      string `json:"span_id"`
	
	// Response fields
	Remediation string   `json:"remediation,omitempty"`
	References  []string `json:"references,omitempty"`
	
	// Escalation fields
	RequiresEscalation bool   `json:"requires_escalation"`
	EscalatedTo        string `json:"escalated_to,omitempty"`
	EscalationTime     *time.Time `json:"escalation_time,omitempty"`
}

// Error implements the error interface
func (e *TMLError) Error() string {
	return fmt.Sprintf("[%s] %s: %s", e.Severity.String(), e.Code, e.Message)
}

// String provides severity level string representation
func (s ErrorSeverity) String() string {
	switch s {
	case SeverityInfo:
		return "INFO"
	case SeverityWarning:
		return "WARNING"
	case SeverityError:
		return "ERROR"
	case SeverityCritical:
		return "CRITICAL"
	case SeverityFatal:
		return "FATAL"
	default:
		return "UNKNOWN"
	}
}

// NewTMLError creates a new TML error
func NewTMLError(code, message string, category ErrorCategory, severity ErrorSeverity) *TMLError {
	return &TMLError{
		Code:      code,
		Message:   message,
		Category:  category,
		Severity:  severity,
		Timestamp: time.Now().UTC(),
		Context:   make(map[string]interface{}),
		TraceID:   generateTraceID(),
		SpanID:    generateSpanID(),
	}
}

// WithContext adds context to the error
func (e *TMLError) WithContext(key string, value interface{}) *TMLError {
	e.Context[key] = value
	return e
}

// WithStackTrace captures the current stack trace
func (e *TMLError) WithStackTrace() *TMLError {
	e.StackTrace = captureStackTrace()
	return e
}

// WithOriginal wraps an original error
func (e *TMLError) WithOriginal(err error) *TMLError {
	e.OriginalErr = err
	if err != nil {
		e.Context["original_error"] = err.Error()
	}
	return e
}

// WithRemediation adds remediation instructions
func (e *TMLError) WithRemediation(remediation string) *TMLError {
	e.Remediation = remediation
	return e
}

// WithReference adds documentation references
func (e *TMLError) WithReference(refs ...string) *TMLError {
	e.References = append(e.References, refs...)
	return e
}

// NeedsEscalation marks the error for escalation
func (e *TMLError) NeedsEscalation() *TMLError {
	e.RequiresEscalation = true
	return e
}

// Escalate performs escalation
func (e *TMLError) Escalate(to string) *TMLError {
	e.EscalatedTo = to
	now := time.Now().UTC()
	e.EscalationTime = &now
	return e
}

// ToJSON converts error to JSON
func (e *TMLError) ToJSON() ([]byte, error) {
	return json.MarshalIndent(e, "", "  ")
}

// Common Errors - Pre-defined error constructors

// Sacred Zero Violations
func SacredZeroViolation(description string, context map[string]interface{}) *TMLError {
	err := NewTMLError(
		"TML_SZ_001",
		fmt.Sprintf("Sacred Zero Violation: %s", description),
		CategorySacredZero,
		SeverityFatal,
	).WithStackTrace().NeedsEscalation()
	
	for k, v := range context {
		err.WithContext(k, v)
	}
	
	err.WithRemediation("Immediate action required. System must halt discriminatory operation.")
	err.WithReference("https://tml.org/sacred-zero", "https://tml.org/emergency-response")
	
	return err
}

// Discrimination Detection
func DiscriminationDetected(characteristic string, threshold float64, detected float64) *TMLError {
	return NewTMLError(
		"TML_HR_001",
		fmt.Sprintf("Discrimination detected on protected characteristic: %s", characteristic),
		CategoryDiscrimination,
		SeverityCritical,
	).WithContext("protected_characteristic", characteristic).
		WithContext("threshold", threshold).
		WithContext("detected_value", detected).
		WithStackTrace().
		NeedsEscalation()
}

// Environmental Threshold Exceeded
func CarbonThresholdExceeded(limit, actual float64) *TMLError {
	return NewTMLError(
		"TML_ENV_001",
		fmt.Sprintf("Carbon threshold exceeded: %.2f kg CO2 (limit: %.2f)", actual, limit),
		CategoryCarbon,
		SeverityError,
	).WithContext("limit_kg", limit).
		WithContext("actual_kg", actual).
		WithContext("exceeded_by", actual-limit).
		WithRemediation("Consider optimizing algorithm efficiency or offsetting carbon impact.")
}

// Water Impact Exceeded
func WaterThresholdExceeded(limit, actual float64) *TMLError {
	return NewTMLError(
		"TML_ENV_002",
		fmt.Sprintf("Water usage threshold exceeded: %.2f liters (limit: %.2f)", actual, limit),
		CategoryWater,
		SeverityError,
	).WithContext("limit_liters", limit).
		WithContext("actual_liters", actual).
		WithContext("exceeded_by", actual-limit)
}

// Guardian Connection Failed
func GuardianConnectionFailed(url string, err error) *TMLError {
	return NewTMLError(
		"TML_NET_001",
		fmt.Sprintf("Failed to connect to Guardian: %s", url),
		CategoryNetwork,
		SeverityError,
	).WithContext("guardian_url", url).
		WithOriginal(err).
		WithRemediation("Check network connectivity and Guardian availability.")
}

// Always Memory Log Failed
func AlwaysMemoryLogFailed(reason string, err error) *TMLError {
	return NewTMLError(
		"TML_AM_001",
		fmt.Sprintf("Always Memory logging failed: %s", reason),
		CategoryAlwaysMemory,
		SeverityCritical,
	).WithOriginal(err).
		WithStackTrace().
		NeedsEscalation().
		WithRemediation("Ensure local storage is available and Guardian connection is stable.")
}

// Configuration Invalid
func ConfigurationInvalid(field, reason string) *TMLError {
	return NewTMLError(
		"TML_CFG_001",
		fmt.Sprintf("Invalid configuration for %s: %s", field, reason),
		CategoryConfiguration,
		SeverityError,
	).WithContext("field", field).
		WithContext("reason", reason)
}

// TEE Not Available
func TEENotAvailable() *TMLError {
	return NewTMLError(
		"TML_SEC_001",
		"Trusted Execution Environment (TEE) required but not available",
		CategorySecurity,
		SeverityCritical,
	).WithRemediation("Enable TEE support or adjust security requirements.")
}

// Indigenous Data Consent Missing
func IndigenousConsentMissing(dataType string) *TMLError {
	return NewTMLError(
		"TML_IND_001",
		fmt.Sprintf("Indigenous data sovereignty requires consent for: %s", dataType),
		CategoryIndigenous,
		SeverityCritical,
	).WithContext("data_type", dataType).
		NeedsEscalation().
		WithRemediation("Obtain proper consent before processing indigenous data.")
}

// Compliance Violation
func ComplianceViolation(framework, requirement string) *TMLError {
	return NewTMLError(
		"TML_CMP_001",
		fmt.Sprintf("Compliance violation: %s - %s", framework, requirement),
		CategoryCompliance,
		SeverityCritical,
	).WithContext("framework", framework).
		WithContext("requirement", requirement).
		NeedsEscalation()
}

// Helper Functions

// captureStackTrace captures the current stack trace
func captureStackTrace() []string {
	var traces []string
	for i := 2; ; i++ { // Skip this function and the caller
		pc, file, line, ok := runtime.Caller(i)
		if !ok {
			break
		}
		
		fn := runtime.FuncForPC(pc)
		if fn == nil {
			continue
		}
		
		trace := fmt.Sprintf("%s:%d %s", file, line, fn.Name())
		traces = append(traces, trace)
		
		if len(traces) >= 20 { // Limit stack trace depth
			break
		}
	}
	return traces
}

// generateTraceID generates a unique trace ID
func generateTraceID() string {
	return fmt.Sprintf("tml-%d-%d", time.Now().UnixNano(), runtime.NumGoroutine())
}

// generateSpanID generates a unique span ID
func generateSpanID() string {
	return fmt.Sprintf("span-%d", time.Now().UnixNano())
}

// IsRetryable determines if an error is retryable
func IsRetryable(err error) bool {
	if tmlErr, ok := err.(*TMLError); ok {
		switch tmlErr.Category {
		case CategoryNetwork, CategoryGuardian, CategoryStorage:
			return tmlErr.Severity < SeverityCritical
		case CategorySacredZero, CategoryDiscrimination:
			return false // Never retry Sacred Zero violations
		default:
			return tmlErr.Severity <= SeverityError
		}
	}
	return false
}

// IsFatal determines if an error is fatal
func IsFatal(err error) bool {
	if tmlErr, ok := err.(*TMLError); ok {
		return tmlErr.Severity == SeverityFatal
	}
	return false
}

// RequiresEscalation determines if an error requires escalation
func RequiresEscalation(err error) bool {
	if tmlErr, ok := err.(*TMLError); ok {
		return tmlErr.RequiresEscalation || tmlErr.Severity >= SeverityCritical
	}
	return false
}

// ErrorChain creates a chain of errors
type ErrorChain struct {
	Errors []*TMLError `json:"errors"`
}

// Add adds an error to the chain
func (ec *ErrorChain) Add(err *TMLError) {
	ec.Errors = append(ec.Errors, err)
}

// HasFatal checks if chain contains fatal error
func (ec *ErrorChain) HasFatal() bool {
	for _, err := range ec.Errors {
		if err.Severity == SeverityFatal {
			return true
		}
	}
	return false
}

// GetByCategory returns errors of specific category
func (ec *ErrorChain) GetByCategory(category ErrorCategory) []*TMLError {
	var filtered []*TMLError
	for _, err := range ec.Errors {
		if err.Category == category {
			filtered = append(filtered, err)
		}
	}
	return filtered
}

// Error implements error interface for ErrorChain
func (ec *ErrorChain) Error() string {
	if len(ec.Errors) == 0 {
		return "no errors"
	}
	
	var messages []string
	for _, err := range ec.Errors {
		messages = append(messages, err.Error())
	}
	
	return strings.Join(messages, "; ")
}
