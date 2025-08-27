# Human Judgment Corpus

## Overview

The Human Judgment Corpus captures, stores, and learns from human interventions during Sacred Pause events. This growing repository of ethical decisions enables the system to adapt and improve its moral reasoning capabilities over time while maintaining transparency and auditability.

## Data Capture Structure

### Core Metadata Schema

```python
JUDGMENT_SCHEMA = {
    'judgment_id': str,           # Unique identifier
    'timestamp': datetime,        # When judgment occurred
    'sacred_pause_trigger': {
        'eus_score': float,       # Ethical Uncertainty Score
        'threshold': float,       # Active threshold at trigger
        'components': dict,       # Breakdown of uncertainty
        'domain': str,           # Operational domain
        'original_query': str,   # Initial user input
        'scenario_type': str     # Classified scenario
    },
    'clarifying_interaction': {
        'questions_presented': list,  # Questions shown to human
        'questions_answered': list,   # Which were answered
        'response_time': float,       # Seconds to respond
        'interaction_rounds': int     # Number of exchanges
    },
    'human_decision': {
        'action': str,           # 'proceed', 'refuse', 'modify'
        'rationale': str,        # Free-form explanation
        'confidence': float,     # Human's confidence (0-1)
        'category': str,         # Selected reason category
        'modifications': dict    # If action was 'modify'
    },
    'outcome_tracking': {
        'immediate_result': str,     # What happened next
        'follow_up_available': bool, # Is there outcome data?
        'quality_assessment': float, # Long-term quality score
        'user_satisfaction': float   # If available
    },
    'metadata': {
        'reviewer_id': str,      # Anonymized reviewer ID
        'reviewer_expertise': str, # Domain expertise level
        'organization_id': str,  # Which deployment
        'version': str          # System version
    }
}
```

### Storage Implementation

```python
class HumanJudgmentCorpus:
    """
    Manages storage and retrieval of human judgments
    """
    
    def __init__(self, storage_backend='postgresql'):
        self.storage = self._initialize_storage(storage_backend)
        self.encryption = self._setup_encryption()
        self.compression = zlib  # For efficient storage
    
    def store_judgment(self, judgment_data):
        """
        Store a human judgment with appropriate privacy measures
        
        Args:
            judgment_data: Dictionary following JUDGMENT_SCHEMA
            
        Returns:
            str: Judgment ID for reference
        """
        # Anonymize sensitive data
        judgment_data = self.anonymize_pii(judgment_data)
        
        # Add integrity hash
        judgment_data['integrity_hash'] = self.calculate_hash(judgment_data)
        
        # Compress for storage
        compressed = self.compress_judgment(judgment_data)
        
        # Store with encryption
        judgment_id = self.storage.store(
            data=compressed,
            encrypted=True,
            index_fields=['domain', 'timestamp', 'action']
        )
        
        # Update indices for fast retrieval
        self.update_indices(judgment_id, judgment_data)
        
        return judgment_id
    
    def anonymize_pii(self, data):
        """Remove or hash personally identifiable information"""
        # Hash reviewer ID
        if 'reviewer_id' in data['metadata']:
            data['metadata']['reviewer_id'] = hash_id(
                data['metadata']['reviewer_id']
            )
        
        # Remove any names from rationale
        data['human_decision']['rationale'] = remove_names(
            data['human_decision']['rationale']
        )
        
        # Generalize location data if present
        if 'location' in data['metadata']:
            data['metadata']['location'] = generalize_location(
                data['metadata']['location']
            )
        
        return data
```

### Database Schema

```sql
-- PostgreSQL schema for production deployments
CREATE TABLE human_judgments (
    judgment_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    timestamp TIMESTAMPTZ NOT NULL,
    domain VARCHAR(50) NOT NULL,
    scenario_type VARCHAR(100),
    eus_score FLOAT NOT NULL CHECK (eus_score >= 0 AND eus_score <= 1),
    threshold FLOAT NOT NULL CHECK (threshold >= 0 AND threshold <= 1),
    human_action VARCHAR(20) NOT NULL CHECK (human_action IN ('proceed', 'refuse', 'modify')),
    rationale TEXT,
    confidence FLOAT CHECK (confidence >= 0 AND confidence <= 1),
    response_time_seconds FLOAT,
    reviewer_hash VARCHAR(64),
    organization_id VARCHAR(100),
    system_version VARCHAR(20),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- JSONB for flexible schema evolution
    full_data JSONB NOT NULL,
    
    -- Indices for common queries
    INDEX idx_domain_time (domain, timestamp DESC),
    INDEX idx_scenario (scenario_type),
    INDEX idx_action (human_action),
    INDEX idx_eus (eus_score),
    INDEX idx_org (organization_id)
);

-- Aggregated statistics table for performance
CREATE TABLE judgment_statistics (
    stat_id SERIAL PRIMARY KEY,
    domain VARCHAR(50) NOT NULL,
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    total_judgments INTEGER NOT NULL,
    avg_eus_score FLOAT,
    avg_response_time FLOAT,
    action_distribution JSONB,
    common_rationales TEXT[],
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE(domain, period_start, period_end)
);
```

## Learning Mechanisms

### Pattern Recognition

```python
class JudgmentPatternAnalyzer:
    """Identify patterns in human ethical decisions"""
    
    def analyze_patterns(self, corpus, time_window=30):
        """
        Find patterns in recent judgments
        
        Args:
            corpus: HumanJudgmentCorpus instance
            time_window: Days of history to analyze
            
        Returns:
            dict: Identified patterns and insights
        """
        recent_judgments = corpus.get_recent(days=time_window)
        
        patterns = {
            'decision_clusters': self.find_decision_clusters(recent_judgments),
            'rationale_themes': self.extract_rationale_themes(recent_judgments),
            'threshold_adjustments': self.recommend_threshold_changes(recent_judgments),
            'scenario_patterns': self.identify_scenario_patterns(recent_judgments),
            'reviewer_consistency': self.analyze_reviewer_consistency(recent_judgments)
        }
        
        return patterns
    
    def find_decision_clusters(self, judgments):
        """Group similar decisions together"""
        from sklearn.cluster import DBSCAN
        import numpy as np
        
        # Extract features
        features = []
        for j in judgments:
            features.append([
                j['sacred_pause_trigger']['eus_score'],
                hash(j['sacred_pause_trigger']['domain']) % 100 / 100,
                hash(j['sacred_pause_trigger']['scenario_type']) % 100 / 100,
                1 if j['human_decision']['action'] == 'proceed' else 0
            ])
        
        # Cluster analysis
        clustering = DBSCAN(eps=0.3, min_samples=5).fit(features)
        
        # Group judgments by cluster
        clusters = {}
        for idx, label in enumerate(clustering.labels_):
            if label not in clusters:
                clusters[label] = []
            clusters[label].append(judgments[idx])
        
        return self.summarize_clusters(clusters)
```

### Supervised Learning Updates

```python
class SupervisedLearningUpdater:
    """Update system models based on human judgments"""
    
    def __init__(self, base_model):
        self.base_model = base_model
        self.update_buffer = []
        self.min_buffer_size = 100
    
    def add_judgment_to_buffer(self, judgment):
        """Add judgment to training buffer"""
        training_example = self.judgment_to_training_example(judgment)
        self.update_buffer.append(training_example)
        
        if len(self.update_buffer) >= self.min_buffer_size:
            self.trigger_model_update()
    
    def judgment_to_training_example(self, judgment):
        """Convert judgment to training format"""
        return {
            'input': {
                'query': judgment['sacred_pause_trigger']['original_query'],
                'domain': judgment['sacred_pause_trigger']['domain'],
                'context': judgment['sacred_pause_trigger']
            },
            'target': {
                'action': judgment['human_decision']['action'],
                'confidence': judgment['human_decision']['confidence'],
                'rationale_embedding': embed_text(
                    judgment['human_decision']['rationale']
                )
            },
            'weight': self.calculate_example_weight(judgment)
        }
    
    def calculate_example_weight(self, judgment):
        """Weight examples by confidence and recency"""
        recency_weight = self.calculate_recency_weight(
            judgment['timestamp']
        )
        confidence_weight = judgment['human_decision']['confidence']
        reviewer_weight = self.get_reviewer_reliability(
            judgment['metadata']['reviewer_hash']
        )
        
        return recency_weight * confidence_weight * reviewer_weight
    
    def trigger_model_update(self):
        """Fine-tune model with accumulated judgments"""
        from torch.utils.data import DataLoader
        
        # Prepare dataset
        dataset = JudgmentDataset(self.update_buffer)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
        
        # Fine-tuning loop
        optimizer = torch.optim.AdamW(self.base_model.parameters(), lr=1e-5)
        
        for epoch in range(3):  # Light fine-tuning
            for batch in dataloader:
                loss = self.base_model.compute_loss(batch)
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
        
        # Clear buffer after update
        self.update_buffer = []
        
        # Log update
        self.log_model_update()
```

### Rule-Based Adjustments

```python
class RuleBasedAdjuster:
    """Adjust system rules based on judgment patterns"""
    
    def __init__(self, rule_engine):
        self.rule_engine = rule_engine
        self.adjustment_threshold = 0.8  # 80% agreement needed
    
    def analyze_for_rule_updates(self, corpus, min_examples=50):
        """
        Identify potential rule adjustments
        
        Args:
            corpus: Human judgment corpus
            min_examples: Minimum examples needed for rule change
            
        Returns:
            list: Proposed rule adjustments
        """
        proposals = []
        
        # Analyze by scenario type
        scenario_groups = corpus.group_by('scenario_type')
        
        for scenario_type, judgments in scenario_groups.items():
            if len(judgments) >= min_examples:
                consensus = self.find_consensus(judgments)
                
                if consensus['agreement_rate'] >= self.adjustment_threshold:
                    proposal = self.create_rule_proposal(
                        scenario_type,
                        consensus,
                        judgments
                    )
                    proposals.append(proposal)
        
        return proposals
    
    def create_rule_proposal(self, scenario_type, consensus, judgments):
        """Create a proposed rule adjustment"""
        return {
            'type': 'rule_adjustment',
            'scenario': scenario_type,
            'current_rule': self.rule_engine.get_rule(scenario_type),
            'proposed_rule': self.generate_rule_from_consensus(consensus),
            'supporting_judgments': len(judgments),
            'agreement_rate': consensus['agreement_rate'],
            'confidence': consensus['avg_confidence'],
            'common_rationale': consensus['top_rationale']
        }
```

## Feedback Integration

### Real-time Integration

```python
def integrate_human_feedback(sacred_pause_context, human_response):
    """
    Process and store human feedback in real-time
    
    Args:
        sacred_pause_context: Original pause context
        human_response: Human's decision and rationale
        
    Returns:
        dict: Integration results
    """
    # Create judgment record
    judgment = create_judgment_record(
        sacred_pause_context,
        human_response
    )
    
    # Store in corpus
    judgment_id = corpus.store_judgment(judgment)
    
    # Immediate updates
    results = {
        'judgment_id': judgment_id,
        'immediate_actions': []
    }
    
    # Update threshold if pattern detected
    if should_adjust_threshold(judgment):
        new_threshold = calculate_new_threshold(judgment)
        update_threshold(judgment['sacred_pause_trigger']['domain'], new_threshold)
        results['immediate_actions'].append(f'Threshold adjusted to {new_threshold}')
    
    # Update question templates if needed
    if judgment['clarifying_interaction']['questions_answered']:
        update_question_effectiveness(
            judgment['clarifying_interaction']['questions_presented'],
            judgment['clarifying_interaction']['questions_answered']
        )
        results['immediate_actions'].append('Question effectiveness updated')
    
    # Add to learning buffer
    learning_updater.add_judgment_to_buffer(judgment)
    
    return results
```

### Batch Processing

```python
class BatchFeedbackProcessor:
    """Process accumulated feedback in batches"""
    
    def __init__(self, corpus, processing_interval=3600):
        self.corpus = corpus
        self.processing_interval = processing_interval
        self.last_processed = datetime.now()
    
    def process_batch(self):
        """Process accumulated judgments"""
        # Get unprocessed judgments
        new_judgments = self.corpus.get_since(self.last_processed)
        
        if len(new_judgments) < 10:
            return  # Wait for more data
        
        # Pattern analysis
        patterns = pattern_analyzer.analyze_patterns(new_judgments)
        
        # Model updates
        if len(new_judgments) >= 100:
            model_updater.trigger_update(new_judgments)
        
        # Rule adjustments
        rule_proposals = rule_adjuster.analyze_for_rule_updates(new_judgments)
        
        # Generate report
        report = self.generate_batch_report(
            patterns,
            rule_proposals,
            len(new_judgments)
        )
        
        # Update timestamp
        self.last_processed = datetime.now()
        
        return report
```

## Query Interface

### Corpus Queries

```python
class CorpusQueryInterface:
    """Query interface for the Human Judgment Corpus"""
    
    def find_similar_judgments(self, current_scenario, limit=10):
        """Find similar past judgments for reference"""
        query = """
            SELECT full_data,
                   similarity(full_data->>'original_query', %s) as sim_score
            FROM human_judgments
            WHERE domain = %s
              AND timestamp > NOW() - INTERVAL '90 days'
            ORDER BY sim_score DESC
            LIMIT %s
        """
        
        return self.execute_query(
            query,
            [current_scenario.query, current_scenario.domain, limit]
        )
    
    def get_decision_distribution(self, domain=None, days=30):
        """Get distribution of human decisions"""
        query = """
            SELECT human_action, COUNT(*) as count,
                   AVG(confidence) as avg_confidence
            FROM human_judgments
            WHERE timestamp > NOW() - INTERVAL '%s days'
        """
        
        if domain:
            query += f" AND domain = '{domain}'"
        
        query += " GROUP BY human_action"
        
        return self.execute_query(query, [days])
    
    def get_rationale_themes(self, action_type, limit=20):
        """Extract common themes from rationales"""
        query = """
            SELECT rationale, COUNT(*) as frequency
            FROM human_judgments
            WHERE human_action = %s
              AND rationale IS NOT NULL
            GROUP BY rationale
            ORDER BY frequency DESC
            LIMIT %s
        """
        
        results = self.execute_query(query, [action_type, limit])
        
        # Further process with NLP for theme extraction
        themes = extract_themes_from_rationales([r['rationale'] for r in results])
        
        return themes
```

## Privacy and Compliance

### Data Protection

```python
class PrivacyCompliantCorpus:
    """Ensures corpus compliance with privacy regulations"""
    
    def __init__(self):
        self.anonymization_key = load_secure_key()
        self.retention_policy = {
            'identifiable_data': 0,  # Never store
            'anonymized_data': 365 * 2,  # 2 years
            'aggregated_data': 365 * 5   # 5 years
        }
    
    def apply_gdpr_compliance(self, judgment):
        """Apply GDPR-compliant processing"""
        # No PII storage
        judgment = remove_all_pii(judgment)
        
        # Purpose limitation
        judgment['purpose'] = 'ai_ethics_improvement'
        
        # Data minimization
        judgment = keep_only_necessary_fields(judgment)
        
        # Storage limitation
        judgment['deletion_date'] = calculate_deletion_date(
            self.retention_policy['anonymized_data']
        )
        
        return judgment
    
    def handle_deletion_request(self, reviewer_hash):
        """Handle GDPR deletion requests"""
        # Find all judgments from this reviewer
        judgments = self.corpus.find_by_reviewer(reviewer_hash)
        
        # Anonymize further or delete
        for j in judgments:
            if j['timestamp'] < datetime.now() - timedelta(days=30):
                # Old enough to fully anonymize
                self.fully_anonymize(j)
            else:
                # Recent - mark for deletion
                self.mark_for_deletion(j)
        
        return f"Processed {len(judgments)} records"
```

## Export and Analysis

### Corpus Export

```python
def export_corpus_for_research(output_format='jsonl', filters=None):
    """
    Export corpus for research purposes
    
    Args:
        output_format: 'jsonl', 'csv', 'parquet'
        filters: Query filters to apply
        
    Returns:
        str: Path to exported file
    """
    # Apply filters
    data = corpus.query(filters or {})
    
    # Additional anonymization for export
    data = apply_export_anonymization(data)
    
    # Convert to requested format
    if output_format == 'jsonl':
        path = export_to_jsonl(data)
    elif output_format == 'csv':
        path = export_to_csv(data)
    elif output_format == 'parquet':
        path = export_to_parquet(data)
    
    # Add metadata
    add_export_metadata(path, len(data), filters)
    
    return path
```

---

*The Human Judgment Corpus creates a continuously improving system by capturing, storing, and learning from human ethical guidance during Sacred Pause events.*
