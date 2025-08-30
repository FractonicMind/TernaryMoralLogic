"""
Ternary Moral Logic (TML) Core Framework
Sacred Pause Logging Infrastructure for AI Accountability

Post-audit investigation model: Organizations control thresholds,
TML provides logging infrastructure when Sacred Pause triggers.
No operational delays, no pre-approval mechanisms.
"""

import hashlib
import json
import time
import uuid
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum
import asyncio
from collections import defaultdict


class TernaryState(Enum):
    """Core ternary logic states"""
    RIGHT = 1
    UNCERTAIN = 0
    WRONG = -1


class PatternCategory:
    """Storage optimization through pattern recognition"""
    
    def __init__(self):
        self.patterns = {}
        self.pattern_counter = defaultdict(int)
        self.next_id = 1
        
    def categorize(self, moral_trace: Dict) -> Tuple[str, Dict]:
        """
        Categorize moral reasoning patterns for 90% storage reduction
        Returns: (pattern_id, compressed_trace)
        """
        # Create pattern signature
        signature = self._create_signature(moral_trace)
        
        if signature not in self.patterns:
            # New pattern - store full template
            pattern_id = f"CAT-{self.next_id:04d}"
            self.patterns[signature] = {
                'id': pattern_id,
                'template': moral_trace,
                'first_seen': datetime.now(timezone.utc).isoformat()
            }
            self.next_id += 1
            
            # Return full trace for first occurrence (~500 bytes)
            return pattern_id, {
                'template_id': pattern_id,
                'full_reasoning': moral_trace,
                'storage_type': 'full',
                'storage_size': len(json.dumps(moral_trace))
            }
        else:
            # Existing pattern - return reference (~45 bytes)
            pattern_id = self.patterns[signature]['id']
            self.pattern_counter[pattern_id] += 1
            
            unique_aspects = self._extract_unique(moral_trace, self.patterns[signature]['template'])
            
            return pattern_id, {
                'template_reference': pattern_id,
                'unique_aspects': unique_aspects,
                'timestamp': moral_trace['timestamp'],
                'decision_id': moral_trace['decision_id'],
                'storage_type': 'compressed',
                'storage_size': len(json.dumps(unique_aspects)) + 45
            }
    
    def _create_signature(self, trace: Dict) -> str:
        """Create hashable signature from moral reasoning pattern"""
        key_elements = {
            'ethical_principles': sorted(trace.get('ethical_principles', [])),
            'stakeholder_types': sorted(trace.get('stakeholder_types', [])),
            'risk_category': trace.get('risk_category', 'unknown'),
            'decision_type': trace.get('decision_type', 'general')
        }
        return hashlib.md5(json.dumps(key_elements, sort_keys=True).encode()).hexdigest()
    
    def _extract_unique(self, current: Dict, template: Dict) -> Dict:
        """Extract only unique aspects different from template"""
        unique = {}
        for key in ['sprl_score', 'specific_stakeholders', 'context_variations']:
            if key in current and current.get(key) != template.get(key):
                unique[key] = current[key]
        return unique


class ImmutableStorage:
    """Tamper-resistant audit trail storage"""
    
    def __init__(self):
        self.storage = []
        self.hash_chain = []
        
    def store(self, trace: Dict) -> str:
        """
        Store moral trace with cryptographic integrity
        Returns storage hash for verification
        """
        # Add timestamp if not present
        if 'stored_at' not in trace:
            trace['stored_at'] = datetime.now(timezone.utc).isoformat()
        
        # Create hash including previous block (blockchain-style)
        trace_json = json.dumps(trace, sort_keys=True)
        
        if self.hash_chain:
            previous_hash = self.hash_chain[-1]
            content = f"{previous_hash}:{trace_json}"
        else:
            content = trace_json
            
        trace_hash = hashlib.sha256(content.encode()).hexdigest()
        
        # Store with integrity markers
        storage_record = {
            'trace': trace,
            'hash': trace_hash,
            'index': len(self.storage),
            'previous_hash': self.hash_chain[-1] if self.hash_chain else None
        }
        
        self.storage.append(storage_record)
        self.hash_chain.append(trace_hash)
        
        return trace_hash
    
    def retrieve(self, decision_id: str = None, timeframe: Tuple[str, str] = None) -> List[Dict]:
        """Retrieve logs for investigation"""
        results = []
        
        for record in self.storage:
            trace = record['trace']
            
            # Filter by decision_id if provided
            if decision_id and trace.get('decision_id') != decision_id:
                continue
                
            # Filter by timeframe if provided
            if timeframe:
                trace_time = trace.get('timestamp', trace.get('stored_at'))
                if not (timeframe[0] <= trace_time <= timeframe[1]):
                    continue
                    
            results.append(trace)
            
        return results
    
    def verify_integrity(self) -> bool:
        """Verify entire chain integrity"""
        for i, record in enumerate(self.storage):
            expected_content = json.dumps(record['trace'], sort_keys=True)
            
            if i > 0:
                expected_content = f"{self.hash_chain[i-1]}:{expected_content}"
                
            computed_hash = hashlib.sha256(expected_content.encode()).hexdigest()
            
            if computed_hash != record['hash']:
                return False
                
        return True


class TMLFramework:
    """
    Core TML Framework Implementation
    Organizations control when Sacred Pause triggers
    TML ensures logging when it does
    """
    
    def __init__(self, organization_config: Dict):
        """
        Initialize TML with organization-specific configuration
        
        Args:
            organization_config: Dict containing:
                - sprl_threshold: Organization's trigger threshold
                - risk_categories: Domain-specific risk definitions
                - stakeholder_methodology: How to identify affected parties
                - retention_days: How long to keep logs (minimum per domain)
        """
        # Organization controls these
        self.sprl_threshold = organization_config.get('sprl_threshold', 0.7)
        self.risk_categories = organization_config.get('risk_categories', {})
        self.stakeholder_methodology = organization_config.get('stakeholder_methodology', 'standard')
        self.calculate_risk_on = organization_config.get('calculate_risk_on', 'all')  # all, samples, threshold
        self.retention_days = organization_config.get('retention_days', 1095)  # 3 years default
        
        # TML mandates these capabilities
        self.logging_enabled = True  # Cannot be disabled
        self.audit_immutable = True  # Cannot be modified
        self.investigation_api = True  # Must be accessible
        
        # Initialize subsystems
        self.pattern_categorizer = PatternCategory()
        self.immutable_storage = ImmutableStorage()
        self.decision_counter = 0
        self.sacred_pause_triggers = 0
        
        # Performance monitoring
        self.performance_stats = {
            'total_decisions': 0,
            'sacred_pauses': 0,
            'average_log_time_ms': 0,
            'storage_saved_percent': 0
        }
    
    def process_decision(self, context: Dict, ai_decision_func=None) -> Dict:
        """
        Process AI decision with Sacred Pause logging when triggered
        
        Args:
            context: Decision context including stakeholders, action, etc.
            ai_decision_func: Organization's AI decision function
            
        Returns:
            Dict with decision and any generated logs
        """
        self.decision_counter += 1
        self.performance_stats['total_decisions'] += 1
        
        decision_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # Organization determines if/when to calculate risk
        should_evaluate = self._should_evaluate_risk(context)
        
        sacred_pause_triggered = False
        moral_trace = None
        storage_hash = None
        
        if should_evaluate:
            # Calculate SPRL using organization's methodology
            sprl_score = self.calculate_sprl(context)
            
            # Check if Sacred Pause triggers
            if sprl_score >= self.sprl_threshold:
                sacred_pause_triggered = True
                self.sacred_pause_triggers += 1
                self.performance_stats['sacred_pauses'] += 1
                
                # MANDATORY: Generate moral trace when triggered
                start_time = time.time()
                moral_trace = self.generate_moral_trace(
                    context=context,
                    sprl_score=sprl_score,
                    decision_id=decision_id,
                    timestamp=timestamp
                )
                
                # Store immutable log
                storage_hash = self.store_immutable_log(moral_trace)
                
                # Update performance stats
                log_time = (time.time() - start_time) * 1000
                self.performance_stats['average_log_time_ms'] = (
                    (self.performance_stats['average_log_time_ms'] * (self.sacred_pause_triggers - 1) + log_time) 
                    / self.sacred_pause_triggers
                )
        
        # AI makes decision (no mandated delay)
        if ai_decision_func:
            ai_result = ai_decision_func(context)
        else:
            ai_result = self._default_decision(context)
        
        # Return decision with any logging metadata
        return {
            'decision_id': decision_id,
            'timestamp': timestamp,
            'decision': ai_result,
            'sacred_pause_triggered': sacred_pause_triggered,
            'moral_trace_stored': storage_hash is not None,
            'storage_hash': storage_hash,
            'sprl_score': sprl_score if should_evaluate else None
        }
    
    def _should_evaluate_risk(self, context: Dict) -> bool:
        """
        Organization's logic for when to calculate risk
        Can be always, sampling, or threshold-based
        """
        if self.calculate_risk_on == 'all':
            return True
        elif self.calculate_risk_on == 'samples':
            # Example: Evaluate 10% of decisions
            return self.decision_counter % 10 == 0
        elif self.calculate_risk_on == 'threshold':
            # Example: Only for high-stakes contexts
            return context.get('stakes', 'low') in ['medium', 'high']
        return True
    
    def calculate_sprl(self, context: Dict) -> float:
        """
        Calculate Stakeholder Proportional Risk Level
        Organizations implement their own methodology
        
        This is a simplified example - organizations would implement
        their domain-specific calculation
        """
        risk_score = 0.0
        
        # Stakeholder impact assessment
        stakeholders = self.identify_stakeholders(context)
        for stakeholder in stakeholders:
            impact = stakeholder.get('impact_level', 0.5)
            vulnerability = stakeholder.get('vulnerability', 1.0)
            risk_score += impact * vulnerability
        
        # Normalize to 0-1 range
        if stakeholders:
            risk_score = risk_score / len(stakeholders)
        
        # Apply domain-specific risk factors
        if context.get('irreversible', False):
            risk_score *= 1.5
        if context.get('affects_minors', False):
            risk_score *= 2.0
        if context.get('medical_decision', False):
            risk_score *= 1.8
            
        return min(risk_score, 1.0)  # Cap at 1.0
    
    def identify_stakeholders(self, context: Dict) -> List[Dict]:
        """
        Identify affected parties using organization's methodology
        """
        stakeholders = []
        
        # Direct stakeholders
        if 'user' in context:
            stakeholders.append({
                'type': 'direct_user',
                'id': context['user'],
                'impact_level': 0.8,
                'vulnerability': self._assess_vulnerability(context['user'])
            })
        
        # Affected individuals
        if 'affected_parties' in context:
            for party in context['affected_parties']:
                stakeholders.append({
                    'type': 'affected_individual',
                    'id': party,
                    'impact_level': 0.6,
                    'vulnerability': self._assess_vulnerability(party)
                })
        
        # Systemic stakeholders
        if context.get('systemic_impact', False):
            stakeholders.append({
                'type': 'community',
                'id': 'general_public',
                'impact_level': 0.3,
                'vulnerability': 1.0
            })
        
        return stakeholders
    
    def _assess_vulnerability(self, stakeholder_id: Any) -> float:
        """
        Assess vulnerability level of stakeholder
        Enhanced for protected groups
        """
        # This would connect to organization's user data
        # Simplified example
        if isinstance(stakeholder_id, dict):
            if stakeholder_id.get('age', 99) < 18:
                return 2.0  # Minor
            if stakeholder_id.get('disability', False):
                return 1.8  # Disabled
            if stakeholder_id.get('elderly', False):
                return 1.6  # Elderly
        return 1.0  # Standard
    
    def generate_moral_trace(self, context: Dict, sprl_score: float, 
                            decision_id: str, timestamp: str) -> Dict:
        """
        Generate comprehensive moral reasoning trace
        MANDATORY when Sacred Pause triggers
        """
        stakeholders = self.identify_stakeholders(context)
        
        trace = {
            'decision_id': decision_id,
            'timestamp': timestamp,
            'sprl_score': sprl_score,
            'stakeholders': [s['type'] for s in stakeholders],
            'stakeholder_types': list(set(s['type'] for s in stakeholders)),
            'decision_type': context.get('decision_type', 'general'),
            'risk_category': self._categorize_risk(sprl_score),
            
            # Ethical reasoning
            'ethical_principles': self._identify_principles(context),
            'mitigations_applied': self._identify_mitigations(context, sprl_score),
            'alternatives_considered': context.get('alternatives', []),
            
            # Context
            'domain': context.get('domain', 'general'),
            'reversibility': not context.get('irreversible', False),
            'time_sensitivity': context.get('time_sensitive', False),
            
            # Vulnerable population analysis (if applicable)
            'vulnerable_population_analysis': self._analyze_vulnerable_impact(stakeholders)
        }
        
        # Add enhanced documentation for vulnerable populations
        if trace['vulnerable_population_analysis']:
            trace['enhanced_safeguards'] = self._generate_enhanced_safeguards(
                context, 
                trace['vulnerable_population_analysis']
            )
        
        return trace
    
    def _categorize_risk(self, sprl_score: float) -> str:
        """Categorize risk level for pattern matching"""
        if sprl_score >= 0.9:
            return 'critical'
        elif sprl_score >= 0.7:
            return 'high'
        elif sprl_score >= 0.5:
            return 'medium'
        elif sprl_score >= 0.3:
            return 'low'
        return 'minimal'
    
    def _identify_principles(self, context: Dict) -> List[str]:
        """Identify ethical principles relevant to decision"""
        principles = []
        
        if context.get('fairness_required', False):
            principles.append('fairness')
        if context.get('privacy_sensitive', False):
            principles.append('privacy')
        if context.get('autonomy_affecting', False):
            principles.append('autonomy')
        if context.get('beneficence_relevant', False):
            principles.append('beneficence')
        if context.get('non_maleficence', True):
            principles.append('non_maleficence')
            
        return principles if principles else ['general_ethics']
    
    def _identify_mitigations(self, context: Dict, sprl_score: float) -> List[str]:
        """Identify mitigations applied based on risk"""
        mitigations = []
        
        if sprl_score >= 0.8:
            mitigations.append('enhanced_logging')
            mitigations.append('stakeholder_notification')
        if sprl_score >= 0.6:
            mitigations.append('alternative_analysis')
        if context.get('affects_minors', False):
            mitigations.append('child_safety_protocols')
        if context.get('medical_decision', False):
            mitigations.append('medical_ethics_review')
            
        return mitigations
    
    def _analyze_vulnerable_impact(self, stakeholders: List[Dict]) -> Optional[Dict]:
        """Analyze impact on vulnerable populations"""
        vulnerable_groups = []
        
        for stakeholder in stakeholders:
            vulnerability = stakeholder.get('vulnerability', 1.0)
            if vulnerability > 1.0:
                group_type = 'unknown'
                if vulnerability >= 2.0:
                    group_type = 'minor'
                elif vulnerability >= 1.8:
                    group_type = 'disabled'
                elif vulnerability >= 1.6:
                    group_type = 'elderly'
                    
                vulnerable_groups.append({
                    'group': group_type,
                    'impact_level': stakeholder.get('impact_level', 0.5),
                    'special_considerations': self._get_special_considerations(group_type)
                })
        
        if vulnerable_groups:
            return {
                'groups_identified': vulnerable_groups,
                'total_vulnerable_stakeholders': len(vulnerable_groups),
                'highest_vulnerability': max(s['vulnerability'] for s in stakeholders)
            }
        
        return None
    
    def _get_special_considerations(self, group_type: str) -> str:
        """Get special considerations for vulnerable group"""
        considerations = {
            'minor': 'Developmental impact, long-term consequences, guardian involvement',
            'disabled': 'Accessibility needs, cognitive considerations, support requirements',
            'elderly': 'Cognitive decline considerations, technological barriers, isolation risks',
            'unknown': 'General vulnerability considerations'
        }
        return considerations.get(group_type, 'Standard considerations')
    
    def _generate_enhanced_safeguards(self, context: Dict, vulnerability_analysis: Dict) -> List[str]:
        """Generate enhanced safeguards for vulnerable populations"""
        safeguards = []
        
        for group in vulnerability_analysis['groups_identified']:
            if group['group'] == 'minor':
                safeguards.extend([
                    'age_appropriate_communication',
                    'parental_notification_available',
                    'developmental_impact_assessment'
                ])
            elif group['group'] == 'disabled':
                safeguards.extend([
                    'accessibility_compliance_verified',
                    'alternative_access_methods',
                    'support_resources_provided'
                ])
            elif group['group'] == 'elderly':
                safeguards.extend([
                    'simplified_interface_option',
                    'extended_time_allowances',
                    'human_assistance_available'
                ])
        
        return list(set(safeguards))  # Remove duplicates
    
    def store_immutable_log(self, moral_trace: Dict) -> str:
        """
        Store moral trace in immutable audit trail
        Returns storage hash for verification
        """
        # Categorize for storage optimization
        pattern_id, compressed_trace = self.pattern_categorizer.categorize(moral_trace)
        
        # Store in immutable storage
        storage_hash = self.immutable_storage.store(compressed_trace)
        
        # Update storage savings statistics
        if compressed_trace.get('storage_type') == 'compressed':
            original_size = len(json.dumps(moral_trace))
            compressed_size = compressed_trace.get('storage_size', 45)
            savings = ((original_size - compressed_size) / original_size) * 100
            
            # Running average of storage savings
            total_patterns = sum(self.pattern_categorizer.pattern_counter.values())
            self.performance_stats['storage_saved_percent'] = (
                (self.performance_stats['storage_saved_percent'] * total_patterns + savings) 
                / (total_patterns + 1)
            )
        
        return storage_hash
    
    def provide_investigation_access(self, institution: str, incident: Dict) -> Optional[Dict]:
        """
        MANDATORY: Provide investigation access to authorized institutions
        
        Args:
            institution: Requesting institution identifier
            incident: Dict with timeframe, affected_parties, etc.
            
        Returns:
            Investigation package with relevant logs
        """
        # Verify institution authorization (would check against governance list)
        authorized_institutions = [
            'un_human_rights',
            'ieee_ethics',
            'amnesty_international',
            # ... other 8 institutions from governance charter
        ]
        
        if institution not in authorized_institutions:
            return None
        
        # Retrieve relevant logs
        logs = self.immutable_storage.retrieve(
            decision_id=incident.get('decision_id'),
            timeframe=incident.get('timeframe')
        )
        
        # Create investigation package
        return {
            'incident_id': incident.get('id'),
            'logs': logs,
            'log_count': len(logs),
            'institution': institution,
            'access_timestamp': datetime.now(timezone.utc).isoformat(),
            'read_only': True,
            'operational_control': False,
            'integrity_verified': self.immutable_storage.verify_integrity()
        }
    
    async def process_decision_async(self, context: Dict, ai_decision_func=None) -> Dict:
        """
        Asynchronous decision processing for latency-critical systems
        Logs are generated in background without blocking
        """
        decision_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # Make decision immediately
        if ai_decision_func:
            ai_result = await ai_decision_func(context) if asyncio.iscoroutinefunction(ai_decision_func) else ai_decision_func(context)
        else:
            ai_result = self._default_decision(context)
        
        # Check if logging needed (non-blocking)
        should_evaluate = self._should_evaluate_risk(context)
        
        if should_evaluate:
            # Create logging task without waiting
            asyncio.create_task(self._async_sacred_pause_logging(
                context, decision_id, timestamp
            ))
        
        # Return immediately
        return {
            'decision_id': decision_id,
            'timestamp': timestamp,
            'decision': ai_result,
            'logging_async': should_evaluate
        }
    
    async def _async_sacred_pause_logging(self, context: Dict, decision_id: str, timestamp: str):
        """Background Sacred Pause logging"""
        sprl_score = self.calculate_sprl(context)
        
        if sprl_score >= self.sprl_threshold:
            moral_trace = self.generate_moral_trace(
                context=context,
                sprl_score=sprl_score,
                decision_id=decision_id,
                timestamp=timestamp
            )
            self.store_immutable_log(moral_trace)
    
    def _default_decision(self, context: Dict) -> Dict:
        """Default decision when no AI function provided"""
        return {
            'action': 'proceed',
            'confidence': 0.5,
            'reasoning': 'Default decision - no AI function provided'
        }
    
    def get_performance_report(self) -> Dict:
        """Get framework performance statistics"""
        return {
            'total_decisions': self.performance_stats['total_decisions'],
            'sacred_pause_triggers': self.performance_stats['sacred_pauses'],
            'trigger_rate': (self.performance_stats['sacred_pauses'] / 
                           max(self.performance_stats['total_decisions'], 1)) * 100,
            'average_logging_time_ms': self.performance_stats['average_log_time_ms'],
            'storage_optimization': f"{self.performance_stats['storage_saved_percent']:.1f}% saved",
            'integrity_verified': self.immutable_storage.verify_integrity()
        }
    
    def export_logs_for_audit(self, start_date: str, end_date: str) -> Dict:
        """Export logs for external audit"""
        logs = self.immutable_storage.retrieve(timeframe=(start_date, end_date))
        
        return {
            'export_timestamp': datetime.now(timezone.utc).isoformat(),
            'period': {'start': start_date, 'end': end_date},
            'total_logs': len(logs),
            'logs': logs,
            'integrity_verified': self.immutable_storage.verify_integrity(),
            'performance_stats': self.get_performance_report()
        }


class BatchLogger:
    """
    High-frequency batch logging for systems with many decisions
    Optimizes performance by batching Sacred Pause logs
    """
    
    def __init__(self, tml_framework: TMLFramework, batch_size: int = 100):
        self.tml = tml_framework
        self.batch_size = batch_size
        self.buffer = []
        self.last_flush = time.time()
        self.max_wait_seconds = 5  # Flush at least every 5 seconds
    
    def log_decision(self, context: Dict, decision: Dict):
        """Add decision to batch"""
        if self.tml._should_evaluate_risk(context):
            sprl_score = self.tml.calculate_sprl(context)
            
            if sprl_score >= self.tml.sprl_threshold:
                moral_trace = self.tml.generate_moral_trace(
                    context=context,
                    sprl_score=sprl_score,
                    decision_id=decision['decision_id'],
                    timestamp=decision['timestamp']
                )
                self.buffer.append(moral_trace)
                
                # Check if flush needed
                if len(self.buffer) >= self.batch_size or \
                   (time.time() - self.last_flush) > self.max_wait_seconds:
                    self.flush()
    
    def flush(self):
        """Flush buffered logs to storage"""
        for trace in self.buffer:
            self.tml.store_immutable_log(trace)
        
        self.buffer = []
        self.last_flush = time.time()
    
    def __del__(self):
        """Ensure all logs are flushed on cleanup"""
        if self.buffer:
            self.flush()


# Compliance verification utilities
def verify_tml_compliance(framework: TMLFramework) -> Dict:
    """
    Verify TML implementation meets mandatory requirements
    """
    compliance = {
        'logging_capability': framework.logging_enabled,
        'immutable_audit': framework.audit_immutable,
        'investigation_api': framework.investigation_api,
        'sprl_threshold_set': framework.sprl_threshold is not None,
        'retention_configured': framework.retention_days >= 1095,  # 3 years minimum
        'pattern_optimization': framework.pattern_categorizer is not None,
        'integrity_verification': framework.immutable_storage.verify_integrity()
    }
    
    compliance['fully_compliant'] = all(compliance.values())
    
    return compliance


# Export main components
__all__ = [
    'TMLFramework',
    'TernaryState',
    'BatchLogger',
    'verify_tml_compliance'
]

"""
Contact Information
- Email: leogouk@gmail.com 
- Successor Contact: support@tml-goukassian.org 
- See Succession Charter: /TML-SUCCESSION-CHARTER.md
"""
