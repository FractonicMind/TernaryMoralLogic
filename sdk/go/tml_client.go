/**
 * TML Client - Main interface for Ternary Moral Logic integration
 * 
 * Path: /sdk/go/tml_client.go
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This is the primary interface for integrating Sacred Zero triggers
 * and Always Memory logging into Go applications.
 */

package tml

import (
	"context"
	"crypto/sha256"
	"encoding/hex"
	"errors"
	"fmt"
	"sync"
	"time"
)

// Decision constants for TML ternary logic
const (
	DecisionProceed    = 1  // Action approved
	DecisionSacredZero = 0  // Human review required
	DecisionRefuse     = -1 // Action blocked
)

// TMLClient is the main client for TML operations
type TMLClient struct {
	apiKey       string
	guardianURL  string
	config       *Config
	memory       *AlwaysMemoryLogger
	sacredZero   *SacredZeroTrigger
	initialized  bool
	mu           sync.RWMutex
	shutdownChan chan struct{}
}

// NewClient creates a new TML client with default configuration
func NewClient(apiKey, guardianURL string) (*TMLClient, error) {
	return NewClientWithConfig(apiKey, guardianURL, DefaultConfig())
}

// NewClientWithConfig creates a new TML client with custom configuration
func NewClientWithConfig(apiKey, guardianURL string, config *Config) (*TMLClient, error) {
	if apiKey == "" {
		return nil, errors.New("API key is required")
	}
	if guardianURL == "" {
		return nil, errors.New("Guardian URL is required")
	}
	if err := config.Validate(); err != nil {
		return nil, fmt.Errorf("invalid configuration: %w", err)
	}

	client := &TMLClient{
		apiKey:       apiKey,
		guardianURL:  guardianURL,
		config:       config,
		shutdownChan: make(chan struct{}),
	}

	// Initialize components
	client.memory = NewAlwaysMemoryLogger(client)
	client.sacredZero = NewSacredZeroTrigger(client)

	// Initialize client
	if err := client.initialize(); err != nil {
		return nil, fmt.Errorf("initialization failed: %w", err)
	}

	return client, nil
}

// initialize establishes connection to Guardian network
func (c *TMLClient) initialize() error {
	c.mu.Lock()
	defer c.mu.Unlock()

	// Validate API key
	if err := c.validateAPIKey(); err != nil {
		return fmt.Errorf("API key validation failed: %w", err)
	}

	// Connect to Guardian
	if err := c.connectToGuardian(); err != nil {
		return fmt.Errorf("Guardian connection failed: %w", err)
	}

	// Verify TEE if required
	if c.config.RequireTEE {
		if err := c.verifyTEE(); err != nil {
			return fmt.Errorf("TEE verification failed: %w", err)
		}
	}

	c.initialized = true

	// Log initialization
	c.logSystemEvent("TML_CLIENT_INITIALIZED", map[string]interface{}{
		"version":     "1.0.0",
		"guardian":    c.guardianURL,
		"tee_enabled": c.config.RequireTEE,
	})

	return nil
}

// ProcessAction evaluates an action through TML framework
// Returns: +1 (proceed), 0 (Sacred Zero), -1 (refuse)
func (c *TMLClient) ProcessAction(ctx context.Context, action *Action) (int, error) {
	c.mu.RLock()
	if !c.initialized {
		c.mu.RUnlock()
		return DecisionSacredZero, errors.New("client not initialized")
	}
	c.mu.RUnlock()

	// Pre-action Always Memory log
	logID, err := c.memory.LogPreAction(action)
	if err != nil {
		return DecisionSacredZero, fmt.Errorf("pre-action logging failed: %w", err)
	}

	// Check Sacred Zero triggers
	decision := c.sacredZero.Evaluate(action)

	switch decision {
	case DecisionSacredZero:
		// Sacred Zero triggered - require human review
		if err := c.handleSacredZero(ctx, action, logID); err != nil {
			return decision, err
		}

	case DecisionRefuse:
		// Action refused - log and block
		if err := c.handleRefusal(ctx, action, logID); err != nil {
			return decision, err
		}
	}

	// Post-action Always Memory log
	if err := c.memory.LogPostAction(action, decision, logID); err != nil {
		return decision, fmt.Errorf("post-action logging failed: %w", err)
	}

	return decision, nil
}

// handleSacredZero processes Sacred Zero triggers
func (c *TMLClient) handleSacredZero(ctx context.Context, action *Action, logID string) error {
	event := map[string]interface{}{
		"action_id":       action.ID,
		"trigger_reason":  action.TriggerReason,
		"timestamp":       time.Now().Format(time.RFC3339),
		"requires_review": true,
	}

	// Log to Always Memory
	if err := c.memory.LogSacredZero(event, logID); err != nil {
		return err
	}

	// Notify Guardian network
	c.notifyGuardians(event)

	// If configured, wait for human review
	if c.config.BlockOnSacredZero {
		return c.waitForHumanReview(ctx, action, logID)
	}

	return nil
}

// handleRefusal processes action refusals
func (c *TMLClient) handleRefusal(ctx context.Context, action *Action, logID string) error {
	event := map[string]interface{}{
		"action_id":       action.ID,
		"refusal_reason":  action.RefusalReason,
		"timestamp":       time.Now().Format(time.RFC3339),
		"permanent":       true,
	}

	// Log to Always Memory
	if err := c.memory.LogRefusal(event, logID); err != nil {
		return err
	}

	// Notify authorities if required
	if action.RequiresLegalNotification {
		c.notifyAuthorities(event)
	}

	return nil
}

// ProcessActionAsync processes an action asynchronously
func (c *TMLClient) ProcessActionAsync(ctx context.Context, action *Action) <-chan ActionResult {
	resultChan := make(chan ActionResult, 1)

	go func() {
		decision, err := c.ProcessAction(ctx, action)
		resultChan <- ActionResult{
			Decision: decision,
			Error:    err,
		}
		close(resultChan)
	}()

	return resultChan
}

// ProcessBatch processes multiple actions in a batch
func (c *TMLClient) ProcessBatch(ctx context.Context, actions []*Action) (map[string]int, error) {
	results := make(map[string]int)
	var mu sync.Mutex

	// Create batch ID for Always Memory
	batchID := generateBatchID()
	if err := c.memory.StartBatch(batchID); err != nil {
		return nil, fmt.Errorf("batch start failed: %w", err)
	}

	// Process actions concurrently
	var wg sync.WaitGroup
	errChan := make(chan error, len(actions))

	for _, action := range actions {
		wg.Add(1)
		go func(a *Action) {
			defer wg.Done()

			decision, err := c.ProcessAction(ctx, a)
			if err != nil {
				errChan <- err
				return
			}

			mu.Lock()
			results[a.ID] = decision
			mu.Unlock()
		}(action)
	}

	wg.Wait()
	close(errChan)

	// Check for errors
	for err := range errChan {
		if err != nil {
			return results, err
		}
	}

	// Seal batch in Always Memory
	if err := c.memory.SealBatch(batchID); err != nil {
		return results, fmt.Errorf("batch seal failed: %w", err)
	}

	return results, nil
}

// GetSacredZeroStats returns Sacred Zero statistics
func (c *TMLClient) GetSacredZeroStats() *SacredZeroStats {
	return c.sacredZero.GetStatistics()
}

// GetAuditTrail retrieves audit trail for time range
func (c *TMLClient) GetAuditTrail(start, end time.Time) (*AuditTrail, error) {
	return c.memory.GetAuditTrail(start, end)
}

// validateAPIKey validates the API key with Guardian
func (c *TMLClient) validateAPIKey() error {
	// Implementation would validate with Guardian network
	if c.apiKey == "" {
		return errors.New("invalid API key")
	}
	return nil
}

// connectToGuardian establishes connection to Guardian network
func (c *TMLClient) connectToGuardian() error {
	// Implementation would establish secure connection
	if c.guardianURL == "" {
		return errors.New("invalid Guardian URL")
	}
	return nil
}

// verifyTEE verifies Trusted Execution Environment
func (c *TMLClient) verifyTEE() error {
	// Implementation would verify TEE attestation
	// This is a stub for the actual TEE verification
	return nil
}

// waitForHumanReview waits for human review of Sacred Zero
func (c *TMLClient) waitForHumanReview(ctx context.Context, action *Action, logID string) error {
	timer := time.NewTimer(time.Duration(c.config.SacredZeroTimeout) * time.Millisecond)
	defer timer.Stop()

	select {
	case <-ctx.Done():
		return ctx.Err()
	case <-timer.C:
		return errors.New("Sacred Zero timeout")
	case <-c.shutdownChan:
		return errors.New("client shutdown")
	}
}

// notifyGuardians sends event to Guardian network
func (c *TMLClient) notifyGuardians(event map[string]interface{}) {
	// Implementation would send to Guardian network
	// This is a stub for actual network communication
}

// notifyAuthorities sends notification to legal authorities
func (c *TMLClient) notifyAuthorities(event map[string]interface{}) {
	// Implementation would send to legal authorities
	// This is a stub for actual notification
}

// logSystemEvent logs internal system events
func (c *TMLClient) logSystemEvent(eventType string, data map[string]interface{}) {
	c.memory.LogSystemEvent(eventType, data)
}

// Shutdown closes the client and releases resources
func (c *TMLClient) Shutdown() error {
	c.mu.Lock()
	defer c.mu.Unlock()

	if !c.initialized {
		return nil
	}

	// Signal shutdown
	close(c.shutdownChan)

	// Flush pending logs
	if err := c.memory.Flush(); err != nil {
		return fmt.Errorf("memory flush failed: %w", err)
	}

	// Disconnect from Guardian
	if err := c.disconnectFromGuardian(); err != nil {
		return fmt.Errorf("Guardian disconnect failed: %w", err)
	}

	c.initialized = false
	return nil
}

// disconnectFromGuardian closes connection to Guardian network
func (c *TMLClient) disconnectFromGuardian() error {
	// Implementation would close connection cleanly
	return nil
}

// Action represents an action to be evaluated
type Action struct {
	ID                        string                 `json:"id"`
	Type                      string                 `json:"type"`
	Content                   string                 `json:"content"`
	Actor                     string                 `json:"actor"`
	Target                    string                 `json:"target"`
	Context                   map[string]interface{} `json:"context"`
	TriggerReason             string                 `json:"trigger_reason,omitempty"`
	RefusalReason             string                 `json:"refusal_reason,omitempty"`
	RequiresLegalNotification bool                   `json:"requires_legal_notification"`
}

// ActionResult represents the result of an async action processing
type ActionResult struct {
	Decision int
	Error    error
}

// Helper functions

func generateBatchID() string {
	timestamp := time.Now().UnixNano()
	hash := sha256.Sum256([]byte(fmt.Sprintf("batch-%d", timestamp)))
	return hex.EncodeToString(hash[:])[:16]
}
