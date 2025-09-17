"""
Ternary Moral Logic (TML) Framework - Core Implementation
Version 4.0 - Dual-Layer SPRL Architecture

Framework-enforced Sacred Pause with automatic logging.
No deployer thresholds. Automatic Static Anchor + Dynamic Stream.
"""

import hashlib
import json
import time
import threading
from datetime import datetime, timezone
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, asdict
from enum import IntEnum
import asyncio
from collections import deque


class TMLState(IntEnum):
    """TML decision states"""
    PROHIBIT = -1     # Risk exceeds framework policy
    SACRED_PAUSE = 0  # Moral complexity detected - log required
    PROCEED = 1       # Low risk, ordinary operation


@dataclass
class StaticAnchor:
    """Immutable timestamp of Sacred Pause entry"""
    sa_id: str
    sa_ts: str  # UTC timestamp
    initial_risk: float
    model_id: str
    runtime_id: str
    policy_version: str
    
    def to_hash(self) -> str:
        """Generate cryptographic hash of anchor"""
        data = json.dumps(asdict(self), sort_keys=True)
        return hashlib.sha3_256(data.encode()).hexdigest()


@dataclass
class DynamicStreamChunk:
    """Single chunk of dynamic risk stream"""
    timestamp: str
    risk_value: float
    token_index: Optional[int]
    tool_boundary: Optional[str]
    features: Dict[str, Any]
    
    def to_dict(self) -> Dict:
        return asdict(self)


@dataclass
class LiteTrace:
    """Minimal telemetry for amber zone events"""
    ts: str
    scenario_signature: str
    top_features: List[str]
    risk_snapshot: float
    policy_version: str
    note: Optional[str] = None


class DynamicStream:
    """Continuous risk evaluation from prompt arrival"""
    
    def __init__(self, prompt_ts: float, domain: str = "general", region: str = "US"):
        self.t0 = prompt_ts
        self.domain = domain
        self.region = region
        self.chunks = deque(maxlen=10000)  # Bounded buffer
        self.lite_traces = deque(maxlen=1000)
        self.sa_written = False
        self.static_anchor = None
        self.is_logging = False
        self.chunk_hashes = []
        
    def evaluate_risk(self, context: Dict[str, Any]) -> float:
        """
        Calculate SPRL using simple I × V × P formula
        Clamped to [0.0001, 0.9999]
        """
        impact = self._calculate_impact(context)
        vulnerability = self._calculate_vulnerability(context)
        probability = self._calculate_probability(context)
        
        risk = impact * vulnerability * probability
        return max(0.0001, min(0.9999, risk))
    
    def _calculate_impact(self, context: Dict) -> float:
        """Calculate impact factor (0-1)"""
        # Framework-defined impact assessment
        stakeholders = context.get('stakeholders', [])
        if not stakeholders:
            return 0.1
            
        max_severity = 0
        for s in stakeholders:
            harm_type = s.get('harm_type', 'unknown')
            severity_map = {
                'physical': 1.0,
                'financial': 0.7,
                'psychological': 0.6,
                'social': 0.5,
                'convenience': 0.3,
                'unknown': 0.5
            }
            max_severity = max(max_severity, severity_map.get(harm_type, 0.5))
        
        return max_severity
    
    def _calculate_vulnerability(self, context: Dict) -> float:
        """Calculate vulnerability factor (0-1)"""
        base = 0.5
        if context.get('affects_minors'):
            base *= 1.5
        if context.get('affects_elderly'):
            base *= 1.3
        if context.get('affects_disabled'):
            base *= 1.4
        if context.get('affects_minorities'):
            base *= 1.2
        return min(1.0, base)
    
    def _calculate_probability(self, context: Dict) -> float:
        """Calculate probability factor (0-1)"""
        # Framework assessment of likelihood
        confidence = context.get('confidence', 0.5)
        uncertainty = context.get('uncertainty', 0.5)
        return confidence * (1 - uncertainty * 0.5)
    
    def add_chunk(self, risk: float, context: Dict) -> Optional[StaticAnchor]:
        """
        Add risk evaluation to stream.
        Returns StaticAnchor if Sacred Pause line crossed.
        """
        chunk = DynamicStreamChunk(
            timestamp=datetime.now(timezone.utc).isoformat(),
            risk_value=risk,
            token_index=context.get('token_index'),
            tool_boundary=context.get('tool_boundary'),
            features=context.get('features', {})
        )
        
        self.chunks.append(chunk)
        chunk_hash = hashlib.sha3_256(
            json.dumps(chunk.to_dict()).encode()
        ).hexdigest()
        self.chunk_hashes.append(chunk_hash)
        
        # Check Sacred Pause threshold (framework-enforced)
        SACRED_PAUSE_LINE = self._get_sacred_pause_line()
        
        if risk >= SACRED_PAUSE_LINE and not self.sa_written:
            # Write Static Anchor (atomic, once only)
            self.static_anchor = StaticAnchor(
                sa_id=f"SA-{int(time.time()*1000000)}",
                sa_ts=datetime.now(timezone.utc).isoformat(),
                initial_risk=risk,
                model_id=context.get('model_id', 'unknown'),
                runtime_id=context.get('runtime_id', 'unknown'),
                policy_version="4.0.0"
            )
            self.sa_written = True
            self.is_logging = True
            return self.static_anchor
            
        # Check amber zone for Lite Traces
        if 0.8 * SACRED_PAUSE_LINE <= risk < SACRED_PAUSE_LINE:
            lite = LiteTrace(
                ts=datetime.now(timezone.utc).isoformat(),
                scenario_signature=self._compute_scenario_signature(context),
                top_features=self._extract_top_features(context),
                risk_snapshot=risk,
                policy_version="4.0.0"
            )
            self.lite_traces.append(lite)
            
        return None
    
    def _get_sacred_pause_line(self) -> float:
        """
        Framework-enforced Sacred Pause threshold.
        Domain-specific but NOT deployer-configurable.
        """
        domain_thresholds = {
            'healthcare': 0.15,
            'autonomous_vehicle': 0.10,
            'financial': 0.30,
            'social_media': 0.40,
            'education': 0.25,
            'criminal_justice': 0.20,
            'general': 0.35
        }
        return domain_thresholds.get(self.domain, 0.35)
    
    def _compute_scenario_signature(self, context: Dict) -> str:
        """Generate signature for scenario categorization"""
        key_features = sorted(context.get('features', {}).items())[:5]
        sig_data = json.dumps(key_features)
        return hashlib.sha3_256(sig_data.encode()).hexdigest()[:16]
    
    def _extract_top_features(self, context: Dict) -> List[str]:
        """Extract most important features for lite trace"""
        features = context.get('features', {})
        sorted_features = sorted(features.items(), key=lambda x: x[1], reverse=True)
        return [f[0] for f in sorted_features[:5]]
    
    def get_risk_curve(self) -> List[Tuple[str, float]]:
        """Get complete risk trajectory"""
        return [(c.timestamp, c.risk_value) for c in self.chunks]
    
    def seal_log(self) -> Dict[str, Any]:
        """Seal and return complete moral trace log"""
        log = {
            'header': {
                'sa_id': self.static_anchor.sa_id if self.static_anchor else None,
                'sa_ts': self.static_anchor.sa_ts if self.static_anchor else None,
                'initial_risk': self.static_anchor.initial_risk if self.static_anchor else None,
                'policy_version': '4.0.0'
            },
            'timeline': {
                'risk_curve': self.get_risk_curve(),
                'chunk_count': len(self.chunks),
                'lite_traces': len(self.lite_traces)
            },
            'integrity': {
                'chunk_hashes': self.chunk_hashes[:100],  # First 100 for space
                'log_hash': self._compute_log_hash()
            }
        }
        return log
    
    def _compute_log_hash(self) -> str:
        """Compute hash of entire log"""
        if not self.chunk_hashes:
            return "empty"
        combined = "".join(self.chunk_hashes)
        return hashlib.sha3_256(combined.encode()).hexdigest()


class TMLEngine:
    """
    Main TML Framework Engine
    Framework-enforced Sacred Pause, no deployer thresholds
    """
    
    def __init__(self, domain: str = "general", region: str = "US"):
        self.domain = domain
        self.region = region
        self.active_streams = {}
        self.console = DeveloperConsole()
        
    def process_decision(self, prompt: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process decision with dual-layer SPRL.
        Non-blocking execution with parallel logging.
        """
        request_id = f"REQ-{int(time.time()*1000000)}"
        t0 = time.time()
        
        # Start Dynamic Stream at prompt arrival
        stream = DynamicStream(t0, self.domain, self.region)
        self.active_streams[request_id] = stream
        
        # Execute decision immediately (non-blocking)
        decision_thread = threading.Thread(
            target=self._execute_decision,
            args=(prompt, context, request_id)
        )
        decision_thread.start()
        
        # Parallel logging thread
        logging_thread = threading.Thread(
            target=self._parallel_logging,
            args=(stream, context, request_id)
        )
        logging_thread.start()
        
        # Return immediately with handle
        return {
            'request_id': request_id,
            'status': 'processing',
            'console_view': f'/console/{request_id}'
        }
    
    def _execute_decision(self, prompt: str, context: Dict, request_id: str):
        """Execute the actual decision (runs immediately)"""
        # Your actual AI decision logic here
        # This is NOT delayed by logging
        time.sleep(0.001)  # Simulate decision processing
        
        # Decision executes regardless of SPRL
        result = {
            'decision': 'executed',
            'request_id': request_id,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        
        # Update console
        self.console.update(request_id, {'decision': result})
        
    def _parallel_logging(self, stream: DynamicStream, context: Dict, request_id: str):
        """
        Parallel logging process.
        Evaluates risk continuously and writes logs.
        """
        # Simulate continuous risk evaluation
        for i in range(10):  # Simplified - real system would track actual tokens
            time.sleep(0.01)  # Simulate processing time
            
            # Evaluate current risk
            current_context = {**context, 'token_index': i}
            risk = stream.evaluate_risk(current_context)
            
            # Add to stream (may trigger Static Anchor)
            sa = stream.add_chunk(risk, current_context)
            
            # Update console
            self.console.update(request_id, {
                'risk_curve': stream.get_risk_curve(),
                'sa_tick': sa.sa_ts if sa else None,
                'current_risk': risk
            })
            
            if sa:
                # Sacred Pause triggered - enhance logging
                self._generate_moral_trace(stream, context, request_id)
        
        # Seal and distribute log
        final_log = stream.seal_log()
        self._distribute_to_hybrid_shield(final_log)
        
    def _generate_moral_trace(self, stream: DynamicStream, context: Dict, request_id: str):
        """Generate comprehensive moral trace when Sacred Pause triggers"""
        trace = {
            'request_id': request_id,
            'sacred_pause_triggered': True,
            'anchor': asdict(stream.static_anchor) if stream.static_anchor else None,
            'alternatives_considered': context.get('alternatives', []),
            'stakeholder_map': context.get('stakeholders', []),
            'rationale': 'Framework detected moral complexity requiring logging'
        }
        
        # Store immutably (implementation depends on storage backend)
        self._store_immutable_trace(trace)
        
    def _store_immutable_trace(self, trace: Dict):
        """Store trace in WORM storage"""
        # Implementation would connect to actual WORM storage
        pass
        
    def _distribute_to_hybrid_shield(self, log: Dict):
        """Distribute log to 11 independent institutions"""
        # Implementation would connect to actual institutions
        pass


class DeveloperConsole:
    """
    Read-only developer console for SPRL visibility
    Mandatory for all deployments
    """
    
    def __init__(self):
        self.views = {}
        
    def update(self, request_id: str, data: Dict):
        """Update console view (read-only from dev perspective)"""
        if request_id not in self.views:
            self.views[request_id] = {
                'created': datetime.now(timezone.utc).isoformat(),
                'risk_curve': [],
                'sa_tick': None,
                'status': 'normal'
            }
        
        self.views[request_id].update(data)
        
        # Determine status based on risk
        if data.get('current_risk', 0) >= 0.8:
            self.views[request_id]['status'] = 'prohibit'
        elif data.get('sa_tick'):
            self.views[request_id]['status'] = 'pause'
            
    def get_view(self, request_id: str) -> Dict:
        """Get read-only console view"""
        return self.views.get(request_id, {})


# Decorator pattern for easy integration
def dynamic_sprl(domain: str = "general", region: str = "US"):
    """Decorator for automatic SPRL tracking"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            tml = TMLEngine(domain, region)
            
            # Extract context from function arguments
            context = kwargs.get('context', {})
            prompt = args[0] if args else kwargs.get('prompt', '')
            
            # Start TML processing (non-blocking)
            tml_handle = tml.process_decision(prompt, context)
            
            # Execute original function immediately
            result = func(*args, **kwargs)
            
            # Attach TML handle for tracking
            if isinstance(result, dict):
                result['_tml_handle'] = tml_handle
                
            return result
        return wrapper
    return decorator


# Simplified API
def create_tml_engine(domain: str = "general", region: str = "US") -> TMLEngine:
    """Create a TML engine instance"""
    return TMLEngine(domain, region)


# Export public API
__all__ = [
    'TMLState',
    'TMLEngine',
    'DynamicStream',
    'StaticAnchor',
    'dynamic_sprl',
    'create_tml_engine',
    'DeveloperConsole'
]
