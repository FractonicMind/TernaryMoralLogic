/**
 * Always Memory Logger - Immutable logging system for TML
 * 
 * Path: /sdk/go/always_memory.go
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This implements the Always Memory logging system,
 * creating immutable, cryptographically sealed records of
 * every AI action. No memory = No action.
 */

package tml

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"sync"
	"sync/atomic"
	"time"
)

// LogType defines the type of log entry
type LogType int

const (
	LogTypePreAction LogType = iota
	LogTypePostAction
	LogTypeSacredZero
	LogTypeRefusal
	LogTypeError
	LogTypeSystem
	LogTypeBatchSeal
)

// Priority defines log entry priority
type Priority int

const (
	PriorityNormal Priority = iota
	PriorityHigh
	PriorityCritical
)

// AlwaysMemoryLogger manages immutable logging
type AlwaysMemoryLogger struct {
	client         *TMLClient
	logQueue       chan *LogEntry
	activeBatches  map[string]*LogBatch
	sequenceNumber int64
	nodeID         string
	previousHash   string
	running        bool
	mu             sync.RWMutex
	wg             sync.WaitGroup
	
	// Cryptographic components
	hmacKey []byte
}

// LogEntry represents a single log entry
type LogEntry struct {
	LogID        string                 `json:"log_id"`
	Type         LogType                `json:"type"`
	Timestamp    time.Time              `json:"timestamp"`
	Sequence     int64                  `json:"sequence"`
	Data         map[string]interface{} `json:"data"`
	Hash         string                 `json:"hash"`
	PreviousHash string                 `json:"previous_hash"`
	Priority     Priority               `json:"priority"`
}

// LogBatch represents a batch of log entries
type LogBatch struct {
	BatchID   string       `json:"batch_id"`
	Entries   []*LogEntry  `json:"entries"`
	StartTime time.Time    `json:"start_time"`
	EndTime   time.Time    `json:"end_time"`
	Signature string       `json:"signature"`
	mu        sync.Mutex
}

// AuditTrail represents an audit trail for a time range
type AuditTrail struct {
	StartTime time.Time
	EndTime   time.Time
	Entries   []*LogEntry
	Verified  bool
}

// NewAlwaysMemoryLogger creates a new Always Memory logger
func NewAlwaysMemoryLogger(client *TMLClient) *AlwaysMemoryLogger {
	logger := &AlwaysMemoryLogger{
		client:         client,
		logQueue:       make(chan *LogEntry, 10000),
		activeBatches:  make(map[string]*LogBatch),
		sequenceNumber: 0,
		nodeID:         generateNodeID(),
		previousHash:   "GENESIS",
		running:        true,
	}
	
	// Initialize HMAC key
	logger.hmacKey = []byte(client.config.HMACKey)
	if len(logger.hmacKey) == 0 {
		// Use default key for demo - in production, this would come from TEE/HSM
		logger.hmacKey = []byte("demo-hmac-key-replace-in-production")
	}
	
	// Start batch processor
	logger.startBatchProcessor()
	
	return logger
}

// LogPreAction creates immutable record before action execution
func (l *AlwaysMemoryLogger) LogPreAction(action *Action) (string, error) {
	logID := l.generateLogID()
	
	entry := &LogEntry{
		LogID:     logID,
		Type:      LogTypePreAction,
		Timestamp: time.Now(),
		Sequence:  atomic.AddInt64(&l.sequenceNumber, 1),
		Data: map[string]interface{}{
			"action_id":    action.ID,
			"action_type":  action.Type,
			"content_hash": l.hashContent(action.Content),
			"context":      action.Context,
			"actor":        action.Actor,
			"target":       action.Target,
			// Add environmental context if present
			"environmental_context": l.extractEnvironmentalContext(action),
		},
	}
	
	// Calculate entry hash
	entry.Hash = l.calculateEntryHash(entry)
	entry.PreviousHash = l.getPreviousHash()
	
	// Queue for processing
	select {
	case l.logQueue <- entry:
		l.updatePreviousHash(entry.Hash)
		return logID, nil
	case <-time.After(time.Second):
		return "", errors.New("log queue timeout")
	}
}

// LogPostAction logs post-action with decision result
func (l *AlwaysMemoryLogger) LogPostAction(action *Action, decision int, logID string) error {
	entry := &LogEntry{
		LogID:     logID,
		Type:      LogTypePostAction,
		Timestamp: time.Now(),
		Sequence:  atomic.AddInt64(&l.sequenceNumber, 1),
		Data: map[string]interface{}{
			"action_id":      action.ID,
			"decision":       decision,
			"decision_text":  getDecisionText(decision),
			"execution_time": time.Now().UnixMilli(),
		},
	}
	
	if decision == DecisionSacredZero {
		entry.Data["sacred_zero_reason"] = action.TriggerReason
	} else if decision == DecisionRefuse {
		entry.Data["refusal_reason"] = action.RefusalReason
	}
	
	entry.Hash = l.calculateEntryHash(entry)
	entry.PreviousHash = l.getPreviousHash()
	
	return l.queueEntry(entry)
}

// LogSacredZero logs Sacred Zero trigger
func (l *AlwaysMemoryLogger) LogSacredZero(event map[string]interface{}, logID string) error {
	entry := &LogEntry{
		LogID:        logID,
		Type:         LogTypeSacredZero,
		Timestamp:    time.Now(),
		Sequence:     atomic.AddInt64(&l.sequenceNumber, 1),
		Data:         event,
		Priority:     PriorityHigh,
	}
	
	entry.Hash = l.calculateEntryHash(entry)
	entry.PreviousHash = l.getPreviousHash()
	
	return l.queueEntry(entry)
}

// LogRefusal logs action refusal
func (l *AlwaysMemoryLogger) LogRefusal(event map[string]interface{}, logID string) error {
	entry := &LogEntry{
		LogID:        logID,
		Type:         LogTypeRefusal,
		Timestamp:    time.Now(),
		Sequence:     atomic.AddInt64(&l.sequenceNumber, 1),
		Data:         event,
		Priority:     PriorityCritical,
	}
	
	entry.Hash = l.calculateEntryHash(entry)
	entry.PreviousHash = l.getPreviousHash()
	
	return l.queueEntry(entry)
}

// LogSystemEvent logs system events
func (l *AlwaysMemoryLogger) LogSystemEvent(eventType string, data map[string]interface{}) error {
	entry := &LogEntry{
		LogID:     l.generateLogID(),
		Type:      LogTypeSystem,
		Timestamp: time.Now(),
		Sequence:  atomic.AddInt64(&l.sequenceNumber, 1),
		Data: map[string]interface{}{
			"event_type": eventType,
			"data":       data,
		},
	}
	
	entry.Hash = l.calculateEntryHash(entry)
	entry.PreviousHash = l.getPreviousHash()
	
	return l.queueEntry(entry)
}

// StartBatch starts a new batch for high-throughput operations
func (l *AlwaysMemoryLogger) StartBatch(batchID string) error {
	l.mu.Lock()
	defer l.mu.Unlock()
	
	if _, exists := l.activeBatches[batchID]; exists {
		return errors.New("batch already exists")
	}
	
	l.activeBatches[batchID] = &LogBatch{
		BatchID:   batchID,
		StartTime: time.Now(),
		Entries:   make([]*LogEntry, 0),
	}
	
	return nil
}

// SealBatch seals and commits a batch
func (l *AlwaysMemoryLogger) SealBatch(batchID string) error {
	l.mu.Lock()
	batch, exists := l.activeBatches[batchID]
	if !exists {
		l.mu.Unlock()
		return errors.New("batch not found")
	}
	delete(l.activeBatches, batchID)
	l.mu.Unlock()
	
	batch.EndTime = time.Now()
	
	// Create batch seal entry
	sealEntry := &LogEntry{
		LogID:     l.generateLogID(),
		Type:      LogTypeBatchSeal,
		Timestamp: time.Now(),
		Sequence:  atomic.AddInt64(&l.sequenceNumber, 1),
		Data: map[string]interface{}{
			"batch_id":    batchID,
			"entry_count": len(batch.Entries),
			"start_time":  batch.StartTime.Format(time.RFC3339),
			"end_time":    batch.EndTime.Format(time.RFC3339),
			"batch_hash":  l.calculateBatchHash(batch),
		},
	}
	
	sealEntry.Hash = l.calculateEntryHash(sealEntry)
	sealEntry.PreviousHash = l.getPreviousHash()
	
	return l.queueEntry(sealEntry)
}

// GetAuditTrail retrieves audit trail for time range
func (l *AlwaysMemoryLogger) GetAuditTrail(start, end time.Time) (*AuditTrail, error) {
	// Implementation would query stored logs
	// This is a stub for the actual retrieval mechanism
	trail := &AuditTrail{
		StartTime: start,
		EndTime:   end,
		Entries:   make([]*LogEntry, 0),
		Verified:  true,
	}
	
	return trail, nil
}

// Flush processes any remaining entries in queue
func (l *AlwaysMemoryLogger) Flush() error {
	l.mu.Lock()
	l.running = false
	l.mu.Unlock()
	
	// Wait for batch processor to finish
	l.wg.Wait()
	
	// Process remaining entries
	remaining := make([]*LogEntry, 0)
	close(l.logQueue)
	for entry := range l.logQueue {
		remaining = append(remaining, entry)
	}
	
	if len(remaining) > 0 {
		return l.processBatch(remaining)
	}
	
	return nil
}

// startBatchProcessor starts background batch processing
func (l *AlwaysMemoryLogger) startBatchProcessor() {
	l.wg.Add(1)
	go func() {
		defer l.wg.Done()
		
		batch := make([]*LogEntry, 0, l.client.config.BatchSize)
		ticker := time.NewTicker(time.Duration(l.client.config.BatchTimeout) * time.Millisecond)
		defer ticker.Stop()
		
		for {
			select {
			case entry, ok := <-l.logQueue:
				if !ok {
					return
				}
				batch = append(batch, entry)
				
				// Process batch if full
				if len(batch) >= l.client.config.BatchSize {
					l.processBatch(batch)
					batch = make([]*LogEntry, 0, l.client.config.BatchSize)
				}
				
			case <-ticker.C:
				// Process batch on timeout
				if len(batch) > 0 {
					l.processBatch(batch)
					batch = make([]*LogEntry, 0, l.client.config.BatchSize)
				}
				
				// Check if should stop
				l.mu.RLock()
				if !l.running {
					l.mu.RUnlock()
					return
				}
				l.mu.RUnlock()
			}
		}
	}()
}

// processBatch processes a batch of log entries
func (l *AlwaysMemoryLogger) processBatch(entries []*LogEntry) error {
	if len(entries) == 0 {
		return nil
	}
	
	// Create batch
	batch := &LogBatch{
		BatchID:   generateBatchID(),
		Entries:   entries,
		StartTime: entries[0].Timestamp,
		EndTime:   entries[len(entries)-1].Timestamp,
	}
	
	// Sign batch
	batch.Signature = l.signBatch(batch)
	
	// Send to Guardian network
	if err := l.sendToGuardian(batch); err != nil {
		// Critical failure - logs must be preserved
		return fmt.Errorf("guardian send failed: %w", err)
	}
	
	// Store locally if configured
	if l.client.config.LocalStorageEnabled {
		if err := l.storeLocally(batch); err != nil {
			// Log but don't fail - Guardian has the data
			fmt.Printf("Local storage failed: %v\n", err)
		}
	}
	
	return nil
}

// Helper methods

func (l *AlwaysMemoryLogger) calculateEntryHash(entry *LogEntry) string {
	data := fmt.Sprintf("%s-%d-%s-%v-%s",
		entry.LogID,
		entry.Type,
		entry.Timestamp.Format(time.RFC3339Nano),
		entry.Data,
		l.previousHash)
	
	hash := sha256.Sum256([]byte(data))
	return hex.EncodeToString(hash[:])
}

func (l *AlwaysMemoryLogger) calculateBatchHash(batch *LogBatch) string {
	h := sha256.New()
	for _, entry := range batch.Entries {
		h.Write([]byte(entry.Hash))
	}
	return hex.EncodeToString(h.Sum(nil))
}

func (l *AlwaysMemoryLogger) signBatch(batch *LogBatch) string {
	mac := hmac.New(sha256.New, l.hmacKey)
	mac.Write([]byte(l.calculateBatchHash(batch)))
	return hex.EncodeToString(mac.Sum(nil))
}

func (l *AlwaysMemoryLogger) hashContent(content string) string {
	hash := sha256.Sum256([]byte(content))
	return hex.EncodeToString(hash[:])
}

func (l *AlwaysMemoryLogger) extractEnvironmentalContext(action *Action) map[string]interface{} {
	envContext := make(map[string]interface{})
	
	// Extract environmental indicators
	envIndicators := []string{
		"carbon_emissions", "water_usage", "habitat_impact",
		"energy_consumption", "waste_generation", "biodiversity_impact",
	}
	
	for _, indicator := range envIndicators {
		if value, exists := action.Context[indicator]; exists {
			envContext[indicator] = value
		}
	}
	
	// Add ecosystem stakeholders if present
	if stakeholders, exists := action.Context["ecosystem_stakeholders"]; exists {
		envContext["ecosystem_stakeholders"] = stakeholders
	}
	
	// Indigenous data sovereignty check
	if indigenous, exists := action.Context["indigenous_territory"]; exists {
		envContext["indigenous_territory"] = indigenous
		envContext["fpic_required"] = true // Free, Prior, Informed Consent
	}
	
	return envContext
}

func (l *AlwaysMemoryLogger) queueEntry(entry *LogEntry) error {
	select {
	case l.logQueue <- entry:
		l.updatePreviousHash(entry.Hash)
		return nil
	case <-time.After(time.Second):
		return errors.New("log queue timeout")
	}
}

func (l *AlwaysMemoryLogger) getPreviousHash() string {
	l.mu.RLock()
	defer l.mu.RUnlock()
	return l.previousHash
}

func (l *AlwaysMemoryLogger) updatePreviousHash(hash string) {
	l.mu.Lock()
	defer l.mu.Unlock()
	l.previousHash = hash
}

func (l *AlwaysMemoryLogger) generateLogID() string {
	return fmt.Sprintf("%s-%d-%d",
		l.nodeID,
		atomic.LoadInt64(&l.sequenceNumber),
		time.Now().UnixNano())
}

func (l *AlwaysMemoryLogger) sendToGuardian(batch *LogBatch) error {
	// Implementation would send to Guardian network
	// This is a stub for actual network communication
	return nil
}

func (l *AlwaysMemoryLogger) storeLocally(batch *LogBatch) error {
	// Implementation would persist to local storage
	// This is a stub for actual storage mechanism
	return nil
}

// Utility functions

func generateNodeID() string {
	hash := sha256.Sum256([]byte(fmt.Sprintf("node-%d", time.Now().UnixNano())))
	return hex.EncodeToString(hash[:])[:16]
}

func getDecisionText(decision int) string {
	switch decision {
	case DecisionProceed:
		return "PROCEED"
	case DecisionSacredZero:
		return "SACRED_ZERO"
	case DecisionRefuse:
		return "REFUSE"
	default:
		return "UNKNOWN"
	}
}
