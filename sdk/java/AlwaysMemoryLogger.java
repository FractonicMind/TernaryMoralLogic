/**
 * Always Memory Logger - Immutable logging system for TML
 * 
 * Path: /sdk/java/AlwaysMemoryLogger.java
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This class implements the Always Memory logging system,
 * creating immutable, cryptographically sealed records of
 * every AI action. No memory = No action.
 */

package org.tml.sdk;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicLong;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class AlwaysMemoryLogger {
    
    private final TMLClient client;
    private final BlockingQueue<LogEntry> logQueue;
    private final Map<String, LogBatch> activeBatches;
    private final AtomicLong sequenceNumber;
    private final String nodeId;
    private volatile boolean running = true;
    
    // Cryptographic components
    private final MessageDigest sha256;
    private final Mac hmac;
    private String previousHash = "GENESIS";
    
    // Batch configuration
    private static final int BATCH_SIZE = 1000;
    private static final long BATCH_TIMEOUT_MS = 100;
    
    public AlwaysMemoryLogger(TMLClient client) {
        this.client = client;
        this.logQueue = new LinkedBlockingQueue<>();
        this.activeBatches = new HashMap<>();
        this.sequenceNumber = new AtomicLong(0);
        this.nodeId = generateNodeId();
        
        try {
            this.sha256 = MessageDigest.getInstance("SHA-256");
            this.hmac = Mac.getInstance("HmacSHA256");
            initializeHMAC();
        } catch (NoSuchAlgorithmException e) {
            throw new TMLException("Cryptographic initialization failed", e);
        }
        
        // Start batch processing thread
        startBatchProcessor();
    }
    
    /**
     * Log pre-action - creates immutable record before action execution
     * Returns log ID for correlation
     */
    public String logPreAction(TMLAction action) {
        String logId = generateLogId();
        
        LogEntry entry = new LogEntry();
        entry.setLogId(logId);
        entry.setType(LogType.PRE_ACTION);
        entry.setTimestamp(Instant.now());
        entry.setSequence(sequenceNumber.incrementAndGet());
        
        // Create action snapshot
        Map<String, Object> data = new HashMap<>();
        data.put("action_id", action.getId());
        data.put("action_type", action.getType());
        data.put("content_hash", hashContent(action.getContent()));
        data.put("context", action.getContext());
        data.put("actor", action.getActor());
        data.put("target", action.getTarget());
        entry.setData(data);
        
        // Calculate entry hash
        entry.setHash(calculateEntryHash(entry));
        entry.setPreviousHash(previousHash);
        
        // Queue for batch processing
        try {
            logQueue.put(entry);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new TMLException("Failed to queue log entry", e);
        }
        
        return logId;
    }
    
    /**
     * Log post-action with decision result
     */
    public void logPostAction(TMLAction action, int decision, String logId) {
        LogEntry entry = new LogEntry();
        entry.setLogId(logId);
        entry.setType(LogType.POST_ACTION);
        entry.setTimestamp(Instant.now());
        entry.setSequence(sequenceNumber.incrementAndGet());
        
        Map<String, Object> data = new HashMap<>();
        data.put("action_id", action.getId());
        data.put("decision", decision);
        data.put("decision_text", getDecisionText(decision));
        data.put("execution_time_ms", System.currentTimeMillis());
        
        if (decision == 0) {
            data.put("sacred_zero_reason", action.getTriggerReason());
        } else if (decision == -1) {
            data.put("refusal_reason", action.getRefusalReason());
        }
        
        entry.setData(data);
        entry.setHash(calculateEntryHash(entry));
        entry.setPreviousHash(previousHash);
        
        queueEntry(entry);
    }
    
    /**
     * Log Sacred Zero trigger
     */
    public void logSacredZero(Map<String, Object> event, String logId) {
        LogEntry entry = new LogEntry();
        entry.setLogId(logId);
        entry.setType(LogType.SACRED_ZERO);
        entry.setTimestamp(Instant.now());
        entry.setSequence(sequenceNumber.incrementAndGet());
        entry.setData(event);
        entry.setHash(calculateEntryHash(entry));
        entry.setPreviousHash(previousHash);
        
        // Sacred Zero logs get priority
        entry.setPriority(Priority.HIGH);
        
        queueEntry(entry);
    }
    
    /**
     * Log action refusal
     */
    public void logRefusal(Map<String, Object> event, String logId) {
        LogEntry entry = new LogEntry();
        entry.setLogId(logId);
        entry.setType(LogType.REFUSAL);
        entry.setTimestamp(Instant.now());
        entry.setSequence(sequenceNumber.incrementAndGet());
        entry.setData(event);
        entry.setHash(calculateEntryHash(entry));
        entry.setPreviousHash(previousHash);
        
        // Refusals are critical
        entry.setPriority(Priority.CRITICAL);
        
        queueEntry(entry);
    }
    
    /**
     * Log error condition
     */
    public void logError(TMLAction action, Exception error, String logId) {
        LogEntry entry = new LogEntry();
        entry.setLogId(logId);
        entry.setType(LogType.ERROR);
        entry.setTimestamp(Instant.now());
        entry.setSequence(sequenceNumber.incrementAndGet());
        
        Map<String, Object> data = new HashMap<>();
        data.put("action_id", action.getId());
        data.put("error_type", error.getClass().getName());
        data.put("error_message", error.getMessage());
        data.put("stack_trace", getStackTrace(error));
        entry.setData(data);
        
        entry.setHash(calculateEntryHash(entry));
        entry.setPreviousHash(previousHash);
        entry.setPriority(Priority.HIGH);
        
        queueEntry(entry);
    }
    
    /**
     * Log system event
     */
    public void logSystemEvent(String type, Map<String, String> data) {
        LogEntry entry = new LogEntry();
        entry.setLogId(generateLogId());
        entry.setType(LogType.SYSTEM);
        entry.setTimestamp(Instant.now());
        entry.setSequence(sequenceNumber.incrementAndGet());
        
        Map<String, Object> eventData = new HashMap<>();
        eventData.put("event_type", type);
        eventData.putAll(data);
        entry.setData(eventData);
        
        entry.setHash(calculateEntryHash(entry));
        entry.setPreviousHash(previousHash);
        
        queueEntry(entry);
    }
    
    /**
     * Start a new batch for high-throughput operations
     */
    public void startBatch(String batchId) {
        LogBatch batch = new LogBatch(batchId);
        batch.setStartTime(Instant.now());
        activeBatches.put(batchId, batch);
    }
    
    /**
     * Seal and commit a batch
     */
    public void sealBatch(String batchId) {
        LogBatch batch = activeBatches.remove(batchId);
        if (batch != null) {
            batch.setEndTime(Instant.now());
            
            // Create batch seal entry
            LogEntry sealEntry = new LogEntry();
            sealEntry.setLogId(generateLogId());
            sealEntry.setType(LogType.BATCH_SEAL);
            sealEntry.setTimestamp(Instant.now());
            sealEntry.setSequence(sequenceNumber.incrementAndGet());
            
            Map<String, Object> sealData = new HashMap<>();
            sealData.put("batch_id", batchId);
            sealData.put("entry_count", batch.getEntryCount());
            sealData.put("start_time", batch.getStartTime().toString());
            sealData.put("end_time", batch.getEndTime().toString());
            sealData.put("batch_hash", batch.calculateBatchHash());
            sealEntry.setData(sealData);
            
            sealEntry.setHash(calculateEntryHash(sealEntry));
            sealEntry.setPreviousHash(previousHash);
            
            queueEntry(sealEntry);
        }
    }
    
    /**
     * Get audit trail for time range
     */
    public AuditTrail getAuditTrail(String startTime, String endTime) {
        // Implementation would query stored logs
        AuditTrail trail = new AuditTrail();
        trail.setStartTime(startTime);
        trail.setEndTime(endTime);
        // Would populate with actual entries from storage
        return trail;
    }
    
    /**
     * Flush pending logs
     */
    public void flush() {
        // Process any remaining entries in queue
        List<LogEntry> remaining = new ArrayList<>();
        logQueue.drainTo(remaining);
        if (!remaining.isEmpty()) {
            processBatch(remaining);
        }
    }
    
    /**
     * Calculate hash for entry
     */
    private String calculateEntryHash(LogEntry entry) {
        try {
            String content = entry.getLogId() + 
                           entry.getType() + 
                           entry.getTimestamp() + 
                           entry.getData().toString() +
                           previousHash;
            
            byte[] hash = sha256.digest(content.getBytes());
            return bytesToHex(hash);
        } catch (Exception e) {
            throw new TMLException("Hash calculation failed", e);
        }
    }
    
    /**
     * Hash content for privacy
     */
    private String hashContent(String content) {
        if (content == null) return "NULL";
        byte[] hash = sha256.digest(content.getBytes());
        return bytesToHex(hash);
    }
    
    /**
     * Initialize HMAC with key
     */
    private void initializeHMAC() {
        try {
            // In production, this would use a secure key from TEE/HSM
            String key = client.getConfig().getHMACKey();
            SecretKeySpec keySpec = new SecretKeySpec(key.getBytes(), "HmacSHA256");
            hmac.init(keySpec);
        } catch (Exception e) {
            throw new TMLException("HMAC initialization failed", e);
        }
    }
    
    /**
     * Start background batch processor
     */
    private void startBatchProcessor() {
        Thread processor = new Thread(() -> {
            List<LogEntry> batch = new ArrayList<>();
            long lastBatchTime = System.currentTimeMillis();
            
            while (running) {
                try {
                    // Wait for entries with timeout
                    LogEntry entry = logQueue.poll(10, java.util.concurrent.TimeUnit.MILLISECONDS);
                    
                    if (entry != null) {
                        batch.add(entry);
                        
                        // Update previous hash
                        previousHash = entry.getHash();
                    }
                    
                    // Check if batch should be processed
                    long now = System.currentTimeMillis();
                    boolean shouldProcess = batch.size() >= BATCH_SIZE ||
                                          (batch.size() > 0 && now - lastBatchTime > BATCH_TIMEOUT_MS);
                    
                    if (shouldProcess && !batch.isEmpty()) {
                        processBatch(new ArrayList<>(batch));
                        batch.clear();
                        lastBatchTime = now;
                    }
                    
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    break;
                } catch (Exception e) {
                    // Log processing error but continue
                    System.err.println("Batch processing error: " + e.getMessage());
                }
            }
        });
        
        processor.setName("TML-AlwaysMemory-Processor");
        processor.setDaemon(true);
        processor.start();
    }
    
    /**
     * Process a batch of log entries
     */
    private void processBatch(List<LogEntry> entries) {
        if (entries.isEmpty()) return;
        
        try {
            // Create batch wrapper
            LogBatch batch = new LogBatch(generateBatchId());
            batch.setEntries(entries);
            batch.setStartTime(entries.get(0).getTimestamp());
            batch.setEndTime(entries.get(entries.size() - 1).getTimestamp());
            
            // Sign batch
            String batchSignature = signBatch(batch);
            batch.setSignature(batchSignature);
            
            // Send to Guardian network
            sendToGuardian(batch);
            
            // Store locally if configured
            if (client.getConfig().isLocalStorageEnabled()) {
                storeLocally(batch);
            }
            
        } catch (Exception e) {
            // Critical failure - should never lose logs
            throw new TMLException("Failed to process log batch", e);
        }
    }
    
    /**
     * Sign batch with HMAC
     */
    private String signBatch(LogBatch batch) {
        try {
            String batchData = batch.calculateBatchHash();
            byte[] signature = hmac.doFinal(batchData.getBytes());
            return bytesToHex(signature);
        } catch (Exception e) {
            throw new TMLException("Batch signing failed", e);
        }
    }
    
    /**
     * Send batch to Guardian network
     */
    private void sendToGuardian(LogBatch batch) {
        // Implementation would send to Guardian nodes
        // This is a stub for the actual network communication
    }
    
    /**
     * Store batch locally
     */
    private void storeLocally(LogBatch batch) {
        // Implementation would persist to local storage
        // This is a stub for the actual storage mechanism
    }
    
    /**
     * Queue entry for processing
     */
    private void queueEntry(LogEntry entry) {
        try {
            logQueue.put(entry);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new TMLException("Failed to queue log entry", e);
        }
    }
    
    // Utility methods
    
    private String generateLogId() {
        return String.format("%s-%d-%s", 
            nodeId, 
            sequenceNumber.get(),
            UUID.randomUUID().toString().substring(0, 8));
    }
    
    private String generateBatchId() {
        return String.format("batch-%s-%d", 
            nodeId,
            System.currentTimeMillis());
    }
    
    private String generateNodeId() {
        return "node-" + UUID.randomUUID().toString().substring(0, 8);
    }
    
    private String getDecisionText(int decision) {
        switch (decision) {
            case 1: return "PROCEED";
            case 0: return "SACRED_ZERO";
            case -1: return "REFUSE";
            default: return "UNKNOWN";
        }
    }
    
    private String getStackTrace(Exception e) {
        StringBuilder sb = new StringBuilder();
        for (StackTraceElement element : e.getStackTrace()) {
            sb.append(element.toString()).append("\n");
        }
        return sb.toString();
    }
    
    private String bytesToHex(byte[] bytes) {
        StringBuilder result = new StringBuilder();
        for (byte b : bytes) {
            result.append(String.format("%02x", b));
        }
        return result.toString();
    }
    
    /**
     * Shutdown logger
     */
    public void shutdown() {
        running = false;
        flush();
    }
}
