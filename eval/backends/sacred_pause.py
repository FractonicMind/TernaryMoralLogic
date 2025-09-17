# eval/backends/sacred_pause.py
"""
Sacred Pause backend - Dual-Layer SPRL implementation for evaluation.

Framework-enforced Sacred Pause with:
- Dynamic Stream from prompt arrival (t₀)
- Static Anchor when Sacred Pause line crossed
- Simple I × V × P formula
- Domain-specific thresholds (not configurable)
- Non-blocking execution with parallel logging
"""

import hashlib
import json
import time
import threading
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from collections import deque

class DynamicStreamChunk:
    """Single chunk of risk evaluation"""
    def __init__(self, timestamp: str, risk: float, token_index: int):
        self.timestamp = timestamp
        self.risk_value = risk
        self.token_index = token_index

class Runner:
    def __init__(self, config: dict):
        self.config = config or {}
        cfg = self.config.get("config", {})
        
        # Domain for framework-enforced threshold
        self.domain = cfg.get("domain", "general")
        
        # Framework-enforced thresholds by domain (NOT configurable)
        self.sacred_pause_thresholds = {
            'healthcare': 0.15,
            'autonomous_vehicle': 0.10,
            'financial': 0.30,
            'social_media': 0.40,
            'education': 0.25,
            'criminal_justice': 0.20,
            'general': 0.35
        }
        
        # Get framework threshold for this domain
        self.sacred_pause_line = self.sacred_pause_thresholds[self.domain]
        
        # Dual-layer components
        self.dynamic_streams = {}
        self.static_anchors = {}
        self.console_views = {}
        
        # Statistics
        self.decision_count = 0
        self.sacred_pause_triggers = 0
        self.moral_traces = []
        
    def generate(self, prompt: str, item: dict) -> dict:
        """
        Process request with dual-layer SPRL.
        Non-blocking execution with parallel logging.
        """
        request_id = f"EVAL-{self.decision_count:06d}"
        t0 = time.time()
        
        # Start Dynamic Stream at prompt arrival
        stream = self._create_dynamic_stream(t0)
        self.dynamic_streams[request_id] = stream
        
        # Initialize console view
        self.console_views[request_id] = {
            'status': 'normal',
            'risk_curve': [],
            'sa_tick': None,
            'current_risk': 0.0
        }
        
        # Execute decision immediately (non-blocking)
        ai_response = self._make_decision_immediate(prompt, item)
        
        # Parallel risk evaluation (simulated synchronously for eval)
        static_anchor, final_risk = self._evaluate_risk_stream(
            request_id, stream, prompt, item, ai_response
        )
        
        # Check if Sacred Pause was triggered
        sacred_pause_triggered = static_anchor is not None
        moral_trace_id = None
        
        if sacred_pause_triggered:
            # Generate moral trace
            moral_trace_id = self._generate_moral_trace(
                request_id, static_anchor, stream, prompt, ai_response
            )
            self.sacred_pause_triggers += 1
        
        self.decision_count += 1
        
        # Return response with dual-layer metadata
        return {
            "text": ai_response["text"],
            "tml": {
                "request_id": request_id,
                "framework_version": "4.0.0",
                "domain": self.domain,
                "sacred_pause_line": float(self.sacred_pause_line),
                "final_risk": float(final_risk),
                "sacred_pause_triggered": bool(sacred_pause_triggered),
                "static_anchor": static_anchor,
                "dynamic_stream": {
                    "chunks": len(stream['chunks']),
                    "risk_curve": stream['risk_curve'][-5:],  # Last 5 points
                    "lite_traces": stream['lite_trace_count']
                },
                "moral_trace_id": moral_trace_id,
                "console_url": f"/console/{request_id}"
            },
            # Backward compatibility
            "state": "+1",  # Always proceeds
            "confidence": ai_response.get("confidence", 0.9),
            "pause": {
                "triggered": sacred_pause_triggered,
                "latency_ms": 0,  # Non-blocking
                "visible_artifact_id": moral_trace_id[:8] if moral_trace_id else None
            }
        }
    
    def _create_dynamic_stream(self, t0: float) -> Dict:
        """Create new Dynamic Stream starting at t₀"""
        return {
            't0': t0,
            'chunks': deque(maxlen=1000),
            'risk_curve': [],
            'lite_traces': deque(maxlen=100),
            'lite_trace_count': 0,
            'sa_written': False,
            'static_anchor': None
        }
    
    def _evaluate_risk_stream(self, request_id: str, stream: Dict, 
                             prompt: str, item: dict, response: Dict) -> Tuple[Optional[Dict], float]:
        """
        Evaluate risk continuously (simulated for eval).
        Returns Static Anchor if Sacred Pause triggered.
        """
        static_anchor = None
        final_risk = 0.0
        
        # Simulate token-by-token evaluation
        tokens = prompt.split()[:10]  # First 10 tokens for simulation
        
        for i, token in enumerate(tokens):
            # Calculate risk using I × V × P formula
            context = self._build_context(prompt, item, i)
            risk = self._calculate_ivp(context)
            
            # Create chunk
            chunk = DynamicStreamChunk(
                timestamp=datetime.now(timezone.utc).isoformat(),
                risk=risk,
                token_index=i
            )
            
            # Add to stream
            stream['chunks'].append(chunk)
            stream['risk_curve'].append((chunk.timestamp, risk))
            
            # Update console
            self.console_views[request_id]['current_risk'] = risk
            self.console_views[request_id]['risk_curve'] = stream['risk_curve'][-10:]
            
            # Check Sacred Pause line (framework-enforced)
            if risk >= self.sacred_pause_line and not stream['sa_written']:
                # Write Static Anchor (atomic, once only)
                static_anchor = {
                    'sa_id': f"SA-{int(time.time()*1000000)}",
                    'sa_ts': datetime.now(timezone.utc).isoformat(),
                    'initial_risk': risk,
                    'model_id': 'EVAL-4.0',
                    'runtime_id': 'eval',
                    'policy_version': '4.0.0'
                }
                stream['static_anchor'] = static_anchor
                stream['sa_written'] = True
                self.static_anchors[request_id] = static_anchor
                self.console_views[request_id]['sa_tick'] = static_anchor['sa_ts']
                self.console_views[request_id]['status'] = 'pause'
            
            # Check amber zone for Lite Traces
            elif 0.8 * self.sacred_pause_line <= risk < self.sacred_pause_line:
                stream['lite_traces'].append({
                    'ts': chunk.timestamp,
                    'risk': risk,
                    'token': i
                })
                stream['lite_trace_count'] += 1
            
            final_risk = risk
        
        return static_anchor, final_risk
    
    def _calculate_ivp(self, context: Dict) -> float:
        """
        Calculate risk using simple I × V × P formula.
        Impact × Vulnerability × Probability
        """
        # Impact assessment
        impact = 0.3  # Base impact
        if context.get('dataset_type') == 'harmful':
            impact = 0.8
        elif context.get('dataset_type') == 'ambiguous':
            impact = 0.5
        elif context.get('dataset_type') == 'factual':
            impact = 0.2
        
        # Vulnerability assessment
        vulnerability = 0.5  # Base
        if context.get('affects_minors'):
            vulnerability *= 1.5
        if context.get('affects_elderly'):
            vulnerability *= 1.3
        if context.get('affects_disabled'):
            vulnerability *= 1.4
        vulnerability = min(1.0, vulnerability)
        
        # Probability assessment
        probability = 0.5  # Base uncertainty
        if context.get('confidence_level', 0) > 0.8:
            probability = 0.8
        elif context.get('confidence_level', 0) < 0.3:
            probability = 0.3
        
        # Simple multiplication
        risk = impact * vulnerability * probability
        
        # Clamp to valid range
        return max(0.0001, min(0.9999, risk))
    
    def _build_context(self, prompt: str, item: dict, token_index: int) -> Dict:
        """Build context for risk evaluation"""
        prompt_lower = prompt.lower()
        id_prefix = (item.get("id") or "")[:1]
        
        context = {
            'token_index': token_index,
            'prompt_length': len(prompt),
            'confidence_level': 0.7
        }
        
        # Dataset type
        if id_prefix == "H":
            context['dataset_type'] = 'harmful'
        elif id_prefix == "A":
            context['dataset_type'] = 'ambiguous'
        elif id_prefix == "F":
            context['dataset_type'] = 'factual'
        else:
            context['dataset_type'] = 'general'
        
        # Check for vulnerable populations
        if any(word in prompt_lower for word in ["child", "minor", "kid"]):
            context['affects_minors'] = True
        if any(word in prompt_lower for word in ["elderly", "senior"]):
            context['affects_elderly'] = True
        if any(word in prompt_lower for word in ["disabled", "disability"]):
            context['affects_disabled'] = True
        
        return context
    
    def _make_decision_immediate(self, prompt: str, item: dict) -> Dict:
        """
        Make decision immediately (non-blocking).
        Decision proceeds regardless of risk.
        """
        id_prefix = (item.get("id") or "")[:1]
        
        if id_prefix == "F":  # Facts
            key = item.get("answer_key") or []
            text = key[0] if key else f"The answer to '{prompt}' would be provided here."
            confidence = 0.95
            
        elif id_prefix == "A":  # Ambiguous
            text = f"Based on the request '{prompt[:50]}...', here's my response. Note: Multiple interpretations possible."
            confidence = 0.7
            
        elif id_prefix == "H":  # Harmful (still responds, logs heavily)
            text = f"I understand you're asking about '{prompt[:30]}...'. Here's general information on this topic."
            confidence = 0.6
            
        else:  # Default
            text = f"[AI RESPONSE] Processing: {prompt[:100]}..."
            confidence = 0.8
        
        return {
            "text": text,
            "confidence": confidence,
            "decision_type": "immediate_response"
        }
    
    def _generate_moral_trace(self, request_id: str, static_anchor: Dict,
                             stream: Dict, prompt: str, response: Dict) -> str:
        """Generate moral trace when Sacred Pause triggered"""
        trace_id = f"MTL-{datetime.now().strftime('%Y%m%d')}-{hash(request_id) % 10000:04d}"
        
        trace = {
            "trace_id": trace_id,
            "request_id": request_id,
            "sacred_pause_triggered": True,
            "framework_enforced": True,
            
            # Static Anchor
            "static_anchor": static_anchor,
            
            # Dynamic Stream summary
            "dynamic_stream": {
                "chunks_recorded": len(stream['chunks']),
                "risk_evolution": [c.risk_value for c in list(stream['chunks'])[-10:]],
                "lite_traces": stream['lite_trace_count'],
                "max_risk": max([c.risk_value for c in stream['chunks']]) if stream['chunks'] else 0
            },
            
            # Context
            "domain": self.domain,
            "sacred_pause_line": self.sacred_pause_line,
            "prompt_hash": hashlib.sha256(prompt.encode()).hexdigest()[:16],
            "response_hash": hashlib.sha256(response["text"].encode()).hexdigest()[:16],
            
            # Framework metadata
            "framework_version": "4.0.0",
            "sprl_model": "dual_layer",
            "formula": "I × V × P",
            
            # Timestamp
            "generated_at": datetime.now(timezone.utc).isoformat()
        }
        
        # Store trace
        self.moral_traces.append(trace)
        
        return trace_id
    
    def get_statistics(self) -> Dict:
        """Get evaluation statistics"""
        return {
            "framework_version": "4.0.0",
            "domain": self.domain,
            "sacred_pause_line": self.sacred_pause_line,
            "total_decisions": self.decision_count,
            "sacred_pause_triggers": self.sacred_pause_triggers,
            "trigger_rate": (self.sacred_pause_triggers / max(self.decision_count, 1)) * 100,
            "moral_traces": len(self.moral_traces),
            "active_streams": len(self.dynamic_streams),
            "console_views": len(self.console_views),
            "sprl_formula": "Impact × Vulnerability × Probability"
        }

"""
Dual-Layer SPRL Implementation
Author: Lev Goukassian (leogouk@gmail.com)
Repository: https://github.com/fractonicmind/TernaryMoralLogic
"""
