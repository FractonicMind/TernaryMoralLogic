#!/usr/bin/env python3
"""
TML Framework FastAPI Application - Dual-Layer SPRL
Author: Lev Goukassian
Date: September 17, 2025
Legal Status: Framework-enforced Sacred Pause system

This application implements TML with dual-layer SPRL:
- Dynamic Stream from prompt arrival (t₀)
- Static Anchor on Sacred Pause crossing
- Framework-enforced thresholds (not configurable)
- Developer Console for read-only visibility
- Non-blocking execution with parallel logging
"""

import asyncio
import hashlib
import json
import logging
import time
import threading
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from uuid import uuid4
from collections import deque

import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Security, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

# ===================================================================
# APPLICATION CONFIGURATION
# ===================================================================

app = FastAPI(
    title="Ternary Moral Logic (TML) Framework API - Dual-Layer SPRL",
    description="""
    Framework-Enforced AI Accountability System
    
    This API implements TML with dual-layer SPRL architecture:
    - Dynamic Stream: Continuous risk evaluation from prompt arrival
    - Static Anchor: Immutable timestamp when Sacred Pause triggers
    - Framework-enforced thresholds (not deployer-configurable)
    - Non-blocking execution with parallel logging
    - Developer Console for mandatory read-only visibility
    
    **Legal Notice**: Sacred Pause is framework-enforced. Organizations cannot
    configure thresholds. All moral complexity is automatically logged.
    """,
    version="4.0.0",
    contact={
        "name": "Lev Goukassian",
        "email": "leogouk@gmail.com",
        "url": "https://github.com/fractonicmind/TernaryMoralLogic"
    },
    license_info={
        "name": "MIT License with Framework Enforcement",
        "url": "https://github.com/fractonicmind/TernaryMoralLogic/blob/main/LICENSE"
    }
)

# Security middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["api.tml-framework.org", "staging-api.tml-framework.org", "localhost", "127.0.0.1"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tml-framework.org", "https://staging.tml-framework.org"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "X-TML-API-Key", "Content-Type"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("/var/log/tml/api.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("tml-api-dual-layer")

# ===================================================================
# PYDANTIC MODELS (UPDATED FOR DUAL-LAYER)
# ===================================================================

class TMLState(BaseModel):
    """TML three-state classification"""
    value: int = Field(..., ge=-1, le=1, description="TML state: -1=Prohibit, 0=Sacred Pause, 1=Proceed")
    description: str = Field(..., description="Human-readable state description")

class DecisionContext(BaseModel):
    """Context for decision being evaluated"""
    decision_type: str = Field(..., description="Type of decision being made")
    prompt: str = Field(..., max_length=5000, description="The actual prompt/query")
    affected_parties: Dict[str, Any] = Field(..., description="Stakeholder information")
    domain: str = Field(..., regex=r"^(healthcare|autonomous_vehicle|financial|social_media|education|criminal_justice|general)$")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
class OrganizationConfig(BaseModel):
    """Organization configuration (thresholds removed - framework enforces)"""
    organization_id: str = Field(..., description="Unique organization identifier")
    domain: str = Field(..., description="Primary operational domain")
    region: str = Field(default="US", description="Operating region")
    vulnerable_population_served: bool = Field(False, description="Serves vulnerable populations")
    
class DecisionEvaluationRequest(BaseModel):
    """Request for TML decision evaluation"""
    decision_context: DecisionContext
    organization_config: OrganizationConfig
    stakeholders: List[Dict[str, Any]] = Field(..., description="Affected stakeholders")

class StaticAnchorData(BaseModel):
    """Static Anchor immutable record"""
    sa_id: str
    sa_ts: str  # ISO timestamp
    initial_risk: float
    model_id: str
    runtime_id: str
    policy_version: str = "4.0.0"
    
class DynamicStreamSnapshot(BaseModel):
    """Snapshot of Dynamic Stream state"""
    risk_curve: List[tuple]
    chunk_count: int
    lite_traces: int
    current_risk: float
    
class DecisionEvaluationResponse(BaseModel):
    """Response from TML decision evaluation"""
    request_id: str
    tml_state: int = Field(..., ge=-1, le=1)
    current_risk: float = Field(..., ge=0.0001, le=0.9999)
    sacred_pause_triggered: bool
    static_anchor: Optional[StaticAnchorData]
    dynamic_stream: DynamicStreamSnapshot
    console_url: str
    execution_status: str = "non_blocking"
    moral_trace_id: Optional[str]

class DeveloperConsoleView(BaseModel):
    """Read-only Developer Console view"""
    request_id: str
    status: str = Field(..., regex=r"^(normal|pause|prohibit)$")
    risk_curve: List[tuple]
    sa_tick: Optional[str]
    current_risk: float
    lite_trace_count: int
    last_updated: str

# ===================================================================
# DUAL-LAYER SPRL COMPONENTS
# ===================================================================

class DynamicStreamChunk:
    """Single chunk of dynamic risk stream"""
    def __init__(self, timestamp: str, risk_value: float, token_index: Optional[int], features: Dict):
        self.timestamp = timestamp
        self.risk_value = risk_value
        self.token_index = token_index
        self.features = features
        
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'risk_value': self.risk_value,
            'token_index': self.token_index,
            'features': self.features
        }

class LiteTrace:
    """Minimal telemetry for amber zone events"""
    def __init__(self, ts: str, scenario_sig: str, risk: float):
        self.ts = ts
        self.scenario_signature = scenario_sig
        self.risk_snapshot = risk

class DynamicStream:
    """Continuous risk evaluation from prompt arrival"""
    
    def __init__(self, t0: float, domain: str, region: str):
        self.t0 = t0
        self.domain = domain
        self.region = region
        self.chunks = deque(maxlen=10000)
        self.lite_traces = deque(maxlen=1000)
        self.sa_written = False
        self.static_anchor = None
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
        """Calculate impact factor"""
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
                'convenience': 0.3
            }
            max_severity = max(max_severity, severity_map.get(harm_type, 0.5))
        
        return max_severity
    
    def _calculate_vulnerability(self, context: Dict) -> float:
        """Calculate vulnerability factor"""
        base = 0.5
        affected = context.get('affected_parties', {})
        
        if affected.get('affects_minors'):
            base *= 1.5
        if affected.get('affects_elderly'):
            base *= 1.3
        if affected.get('affects_disabled'):
            base *= 1.4
        if affected.get('affects_minorities'):
            base *= 1.2
            
        return min(1.0, base)
    
    def _calculate_probability(self, context: Dict) -> float:
        """Calculate probability factor"""
        confidence = context.get('confidence', 0.5)
        uncertainty = context.get('uncertainty', 0.5)
        return confidence * (1 - uncertainty * 0.5)
    
    def add_chunk(self, risk: float, context: Dict) -> Optional[Dict]:
        """Add risk evaluation chunk, return Static Anchor if Sacred Pause crossed"""
        chunk = DynamicStreamChunk(
            timestamp=datetime.now(timezone.utc).isoformat(),
            risk_value=risk,
            token_index=context.get('token_index'),
            features=context.get('features', {})
        )
        
        self.chunks.append(chunk)
        chunk_hash = hashlib.sha3_256(
            json.dumps(chunk.to_dict()).encode()
        ).hexdigest()
        self.chunk_hashes.append(chunk_hash)
        
        # Framework-enforced Sacred Pause line
        sacred_pause_line = self._get_sacred_pause_line()
        
        # Check if we cross the Sacred Pause threshold
        if risk >= sacred_pause_line and not self.sa_written:
            # Write Static Anchor (once only, atomic)
            self.static_anchor = {
                'sa_id': f"SA-{int(time.time()*1000000)}",
                'sa_ts': datetime.now(timezone.utc).isoformat(),
                'initial_risk': risk,
                'model_id': context.get('model_id', 'TML-4.0'),
                'runtime_id': context.get('runtime_id', 'prod'),
                'policy_version': '4.0.0'
            }
            self.sa_written = True
            return self.static_anchor
            
        # Check amber zone for Lite Traces
        if 0.8 * sacred_pause_line <= risk < sacred_pause_line:
            lite = LiteTrace(
                ts=datetime.now(timezone.utc).isoformat(),
                scenario_sig=self._compute_scenario_signature(context),
                risk=risk
            )
            self.lite_traces.append(lite)
            
        return None
    
    def _get_sacred_pause_line(self) -> float:
        """
        Framework-enforced Sacred Pause threshold by domain.
        NOT configurable by organizations.
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
        """Generate scenario signature for categorization"""
        features = sorted(context.get('features', {}).items())[:5]
        sig_data = json.dumps(features)
        return hashlib.sha3_256(sig_data.encode()).hexdigest()[:16]
    
    def get_risk_curve(self) -> List[tuple]:
        """Get complete risk trajectory"""
        return [(c.timestamp, c.risk_value) for c in self.chunks]
    
    def seal_log(self) -> Dict[str, Any]:
        """Seal and return complete moral trace log"""
        return {
            'header': {
                'sa_id': self.static_anchor['sa_id'] if self.static_anchor else None,
                'sa_ts': self.static_anchor['sa_ts'] if self.static_anchor else None,
                'initial_risk': self.static_anchor['initial_risk'] if self.static_anchor else None,
                'policy_version': '4.0.0'
            },
            'timeline': {
                'risk_curve': self.get_risk_curve(),
                'chunk_count': len(self.chunks),
                'lite_traces': len(self.lite_traces)
            },
            'integrity': {
                'chunk_hashes': self.chunk_hashes[:100],
                'log_hash': self._compute_log_hash()
            }
        }
    
    def _compute_log_hash(self) -> str:
        """Compute hash of entire log"""
        if not self.chunk_hashes:
            return "empty"
        combined = "".join(self.chunk_hashes)
        return hashlib.sha3_256(combined.encode()).hexdigest()

class DeveloperConsole:
    """Mandatory read-only developer console"""
    
    def __init__(self):
        self.views = {}
        
    def update(self, request_id: str, data: Dict):
        """Update console view (read-only from dev perspective)"""
        if request_id not in self.views:
            self.views[request_id] = {
                'created': datetime.now(timezone.utc).isoformat(),
                'status': 'normal',
                'risk_curve': [],
                'sa_tick': None,
                'current_risk': 0.0,
                'lite_trace_count': 0
            }
        
        self.views[request_id].update(data)
        
        # Update status based on risk
        if data.get('current_risk', 0) >= 0.8:
            self.views[request_id]['status'] = 'prohibit'
        elif data.get('sa_tick'):
            self.views[request_id]['status'] = 'pause'
            
    def get_view(self, request_id: str) -> Dict:
        """Get read-only console view"""
        view = self.views.get(request_id, {})
        if view:
            view['last_updated'] = datetime.now(timezone.utc).isoformat()
        return view

# ===================================================================
# TML ENGINE WITH DUAL-LAYER SPRL
# ===================================================================

class TMLEngine:
    """Core TML engine with dual-layer SPRL"""
    
    def __init__(self):
        self.active_streams = {}
        self.console = DeveloperConsole()
        self.moral_traces = {}
        
    def process_decision(self, request: DecisionEvaluationRequest) -> Dict[str, Any]:
        """
        Process decision with dual-layer SPRL.
        Non-blocking execution with parallel logging.
        """
        request_id = f"REQ-{int(time.time()*1000000)}"
        t0 = time.time()
        
        # Start Dynamic Stream at prompt arrival
        stream = DynamicStream(
            t0=t0,
            domain=request.decision_context.domain,
            region=request.organization_config.region
        )
        self.active_streams[request_id] = stream
        
        # Build evaluation context
        context = {
            'stakeholders': request.stakeholders,
            'affected_parties': request.decision_context.affected_parties,
            'confidence': 0.8,  # Would be calculated from context
            'uncertainty': 0.2,
            'model_id': 'TML-4.0',
            'runtime_id': 'prod'
        }
        
        # Start parallel processing
        decision_thread = threading.Thread(
            target=self._execute_decision,
            args=(request_id, request.decision_context.prompt, context)
        )
        decision_thread.start()
        
        # Parallel logging thread
        logging_thread = threading.Thread(
            target=self._parallel_logging,
            args=(request_id, stream, context)
        )
        logging_thread.start()
        
        # Wait briefly for initial assessment (non-blocking in production)
        time.sleep(0.05)  # 50ms for initial risk assessment
        
        # Get current state
        console_view = self.console.get_view(request_id)
        
        # Determine TML state
        if console_view.get('status') == 'prohibit':
            tml_state = -1
        elif console_view.get('status') == 'pause':
            tml_state = 0
        else:
            tml_state = 1
        
        return {
            'request_id': request_id,
            'tml_state': tml_state,
            'current_risk': console_view.get('current_risk', 0.0),
            'sacred_pause_triggered': console_view.get('sa_tick') is not None,
            'static_anchor': stream.static_anchor,
            'dynamic_stream': {
                'risk_curve': stream.get_risk_curve(),
                'chunk_count': len(stream.chunks),
                'lite_traces': len(stream.lite_traces),
                'current_risk': console_view.get('current_risk', 0.0)
            },
            'console_url': f'/console/{request_id}',
            'execution_status': 'non_blocking'
        }
    
    def _execute_decision(self, request_id: str, prompt: str, context: Dict):
        """Execute the actual decision (runs immediately)"""
        # Decision logic here - NOT delayed by logging
        time.sleep(0.001)  # Simulate decision processing
        
        result = {
            'decision': 'executed',
            'request_id': request_id,
            'timestamp': datetime.now(timezone.utc).isoformat()
        }
        
        # Update console
        self.console.update(request_id, {'decision': result})
        
    def _parallel_logging(self, request_id: str, stream: DynamicStream, context: Dict):
        """
        Parallel logging process.
        Evaluates risk continuously and writes logs.
        """
        # Simulate continuous risk evaluation
        for i in range(10):
            time.sleep(0.01)  # Simulate token processing
            
            # Update context with token position
            current_context = {**context, 'token_index': i}
            
            # Evaluate current risk
            risk = stream.evaluate_risk(current_context)
            
            # Add to stream (may trigger Static Anchor)
            sa = stream.add_chunk(risk, current_context)
            
            # Update console
            self.console.update(request_id, {
                'risk_curve': stream.get_risk_curve(),
                'sa_tick': sa['sa_ts'] if sa else None,
                'current_risk': risk,
                'lite_trace_count': len(stream.lite_traces)
            })
            
            if sa:
                # Sacred Pause triggered - generate moral trace
                self._generate_moral_trace(request_id, stream, context)
        
        # Seal and distribute log
        final_log = stream.seal_log()
        self._distribute_to_hybrid_shield(final_log)
    
    def _generate_moral_trace(self, request_id: str, stream: DynamicStream, context: Dict):
        """Generate comprehensive moral trace when Sacred Pause triggers"""
        trace_id = f"MTL-{datetime.now().strftime('%Y%m%d')}-{uuid4().hex[:16].upper()}"
        
        trace = {
            'trace_id': trace_id,
            'request_id': request_id,
            'sacred_pause_triggered': True,
            'static_anchor': stream.static_anchor,
            'risk_at_trigger': stream.static_anchor['initial_risk'] if stream.static_anchor else None,
            'alternatives_considered': ['continue', 'modify', 'refuse'],
            'stakeholder_map': context.get('stakeholders', []),
            'framework_reason': 'Moral complexity detected by framework',
            'domain_threshold': stream._get_sacred_pause_line()
        }
        
        self.moral_traces[trace_id] = trace
        self._store_immutable_trace(trace)
        
    def _store_immutable_trace(self, trace: Dict):
        """Store trace in WORM storage"""
        logger.info(f"Storing immutable trace: {trace['trace_id']}")
        # Implementation would use actual WORM storage
        
    def _distribute_to_hybrid_shield(self, log: Dict):
        """Distribute log to 11 independent institutions"""
        logger.info(f"Distributing to Hybrid Shield: {log['header']['sa_id'] if log['header']['sa_id'] else 'no-sa'}")
        # Implementation would connect to actual institutions

# Global TML engine instance
tml_engine = TMLEngine()

# ===================================================================
# SECURITY AND AUTHENTICATION
# ===================================================================

security = HTTPBearer()

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Verify API key and return organization information"""
    api_key = credentials.credentials
    
    if not api_key or len(api_key) < 32:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    logger.info(f"API access with key: {api_key[:8]}...")
    
    return {
        "organization_id": "org_" + api_key[:8],
        "organization_name": "Example Organization",
        "access_level": "standard"
    }

async def verify_investigator_auth(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Verify investigator authentication for audit access"""
    token = credentials.credentials
    
    if not token or "investigator" not in token:
        raise HTTPException(status_code=403, detail="Investigator credentials required")
    
    logger.warning(f"Investigator access: {token[:16]}...")
    
    return {
        "investigator_id": "inv_" + token[:8],
        "institution": "MIT CSAIL",
        "access_level": "investigation:read"
    }

# ===================================================================
# API ENDPOINTS
# ===================================================================

@app.post("/v1/decisions/evaluate", response_model=DecisionEvaluationResponse)
async def evaluate_decision(
    request: DecisionEvaluationRequest,
    background_tasks: BackgroundTasks,
    org_info: Dict = Depends(verify_api_key)
):
    """
    Evaluate decision with framework-enforced Sacred Pause.
    Non-blocking execution with parallel moral logging.
    """
    try:
        # Process with dual-layer SPRL
        result = tml_engine.process_decision(request)
        
        # Add organization info
        result['organization_id'] = org_info['organization_id']
        
        # If Sacred Pause triggered, note in background
        if result['sacred_pause_triggered']:
            background_tasks.add_task(
                log_sacred_pause_event,
                result['request_id'],
                result['static_anchor']
            )
        
        # Create response
        return DecisionEvaluationResponse(
            request_id=result['request_id'],
            tml_state=result['tml_state'],
            current_risk=result['current_risk'],
            sacred_pause_triggered=result['sacred_pause_triggered'],
            static_anchor=StaticAnchorData(**result['static_anchor']) if result['static_anchor'] else None,
            dynamic_stream=DynamicStreamSnapshot(**result['dynamic_stream']),
            console_url=result['console_url'],
            execution_status=result['execution_status'],
            moral_trace_id=result.get('moral_trace_id')
        )
        
    except Exception as e:
        logger.error(f"Decision evaluation error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Evaluation failed: {str(e)}")

@app.get("/v1/console/{request_id}", response_model=DeveloperConsoleView)
async def get_console_view(
    request_id: str,
    org_info: Dict = Depends(verify_api_key)
):
    """Get read-only Developer Console view for a request"""
    view = tml_engine.console.get_view(request_id)
    
    if not view:
        raise HTTPException(status_code=404, detail="Request not found")
    
    return DeveloperConsoleView(
        request_id=request_id,
        **view
    )

@app.get("/v1/sprl/thresholds")
async def get_framework_thresholds():
    """
    Get framework-enforced Sacred Pause thresholds.
    These are NOT configurable by organizations.
    """
    return {
        "framework_version": "4.0.0",
        "thresholds_by_domain": {
            "healthcare": 0.15,
            "autonomous_vehicle": 0.10,
            "financial": 0.30,
            "social_media": 0.40,
            "education": 0.25,
            "criminal_justice": 0.20,
            "general": 0.35
        },
        "notice": "Thresholds are framework-enforced and cannot be modified by organizations",
        "formula": "SPRL = Impact × Vulnerability × Probability (clamped to [0.0001, 0.9999])",
        "prohibition_line": 0.80
    }

@app.get("/v1/audit/logs")
async def get_audit_logs(
    organization_id: str,
    date_range_start: Optional[str] = None,
    date_range_end: Optional[str] = None,
    limit: int = 100,
    investigator_info: Dict = Depends(verify_investigator_auth)
):
    """Retrieve moral trace logs for regulatory audit"""
    logger.warning(f"Audit access by {investigator_info['institution']} for org {organization_id}")
    
    # In production, query immutable storage
    mock_logs = []
    for trace_id, trace in tml_engine.moral_traces.items():
        if len(mock_logs) < limit:
            mock_logs.append(trace)
    
    return {
        "logs": mock_logs,
        "pagination": {
            "total_count": len(mock_logs),
            "limit": limit
        },
        "audit_metadata": {
            "investigator_id": investigator_info['investigator_id'],
            "institution": investigator_info['institution'],
            "access_timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

@app.get("/v1/monitoring/health")
async def get_system_health():
    """Monitor TML system health"""
    return {
        "status": "healthy",
        "framework_version": "4.0.0",
        "dual_layer_status": {
            "dynamic_stream": "operational",
            "static_anchor": "operational",
            "developer_console": "operational"
        },
        "active_requests": len(tml_engine.active_streams),
        "moral_traces_generated": len(tml_engine.moral_traces),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# ===================================================================
# BACKGROUND TASKS
# ===================================================================

async def log_sacred_pause_event(request_id: str, static_anchor: Dict):
    """Log Sacred Pause event for compliance"""
    logger.info(f"Sacred Pause triggered: {request_id} at {static_anchor['sa_ts']}")
    # Implementation would store in compliance database

# ===================================================================
# ROOT ENDPOINT
# ===================================================================

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "framework": "Ternary Moral Logic (TML)",
        "version": "4.0.0",
        "sprl_model": "Dual-Layer (Dynamic Stream + Static Anchor)",
        "author": "Lev Goukassian",
        "enforcement": "Framework-enforced Sacred Pause (not configurable)",
        "documentation": "/docs",
        "key_features": [
            "Dynamic Stream from prompt arrival (t₀)",
            "Static Anchor on Sacred Pause crossing",
            "Framework-enforced thresholds by domain",
            "Non-blocking execution",
            "Parallel moral logging",
            "Developer Console (read-only)"
        ],
        "contact": {
            "email": "leogouk@gmail.com",
            "repository": "https://github.com/fractonicmind/TernaryMoralLogic"
        }
    }

# ===================================================================
# EXCEPTION HANDLERS
# ===================================================================

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions"""
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
    
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": f"HTTP_{exc.status_code}",
            "message": exc.detail,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle unexpected exceptions"""
    logger.critical(f"Unhandled Exception: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content={
            "error": "INTERNAL_SERVER_ERROR",
            "message": "An unexpected error occurred",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    )

# ===================================================================
# STARTUP AND SHUTDOWN
# ===================================================================

@app.on_event("startup")
async def startup_event():
    """Initialize TML framework on startup"""
    logger.info("TML Framework API (Dual-Layer SPRL) starting...")
    logger.info("Framework-enforced Sacred Pause active")
    logger.info("Ready for non-blocking decision processing")

@app.on_event("shutdown")
async def shutdown_event():
    """Graceful shutdown"""
    logger.warning("TML Framework API shutting down...")
    
    # Seal all active streams
    for request_id, stream in tml_engine.active_streams.items():
        final_log = stream.seal_log()
        logger.info(f"Sealing stream {request_id}")
    
    logger.warning("Shutdown complete")

# ===================================================================
# DEVELOPMENT SERVER
# ===================================================================

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
        reload=False
    )

# Author: Lev Goukassian (leogouk@gmail.com)
# Repository: https://github.com/fractonicmind/TernaryMoralLogic
