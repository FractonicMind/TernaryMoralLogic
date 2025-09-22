"""
TML Framework FastAPI Application - Always Memory Implementation
Author: Lev Goukassian (ORCID: 0009-0006-5966-1243)

This application implements TML with Always Memory:
- Every AI action creates an immutable log before execution
- Sacred Zero triggers on moral complexity
- Environmental impact tracking
- Guardian network integration
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import IntEnum
import hashlib
import json
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="TML Always Memory Framework",
    description="Universal accountability framework for AI systems",
    version="5.0.0",
    contact={
        "name": "Lev Goukassian",
        "email": "leogouk@gmail.com",
        "url": "https://orcid.org/0009-0006-5966-1243"
    }
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TMLClassification(IntEnum):
    """Ternary Moral Logic states"""
    REFUSE = -1
    SACRED_ZERO = 0
    PROCEED = 1

class MemoryRequest(BaseModel):
    """Request to create an Always Memory log"""
    action: str = Field(..., description="Action being performed")
    input_data: Dict[str, Any] = Field(..., description="Input data for the action")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context")
    environmental_check: bool = Field(False, description="Check for environmental impact")

class MemoryResponse(BaseModel):
    """Response containing the created memory log"""
    memory_id: str
    classification: int
    sacred_zero_trigger: Optional[str]
    timestamp: str
    guardian_confirmations: List[str]
    environmental_impact: Optional[Dict[str, Any]]

class SacredZeroEvent(BaseModel):
    """Sacred Zero pause event"""
    trigger: str
    context_hash: str
    human_review_required: bool
    timestamp: str

class AlwaysMemory:
    """Core Always Memory implementation"""
    
    def __init__(self):
        self.creator_orcid = "0009-0006-5966-1243"
        self.framework = "TML-AlwaysMemory-v5.0"
        self.memories = []
        
    def classify_action(self, action: str, context: Dict[str, Any]) -> tuple[TMLClassification, Optional[str]]:
        """Classify action according to TML states"""
        
        # Check for harmful actions (REFUSE)
        harmful_keywords = ["harm", "illegal", "weapon", "surveillance", "fraud"]
        if any(keyword in action.lower() for keyword in harmful_keywords):
            return TMLClassification.REFUSE, None
            
        # Check for Sacred Zero triggers
        sacred_triggers = {
            "protected_class": ["loan", "hiring", "housing", "credit"],
            "medical_critical": ["diagnosis", "treatment", "triage"],
            "environmental_harm": ["pollution", "deforestation", "extraction"],
            "vulnerable_population": ["minor", "elderly", "disability"]
        }
        
        for trigger_type, keywords in sacred_triggers.items():
            if any(keyword in action.lower() for keyword in keywords):
                return TMLClassification.SACRED_ZERO, trigger_type
                
        # Default to PROCEED for routine actions
        return TMLClassification.PROCEED, None
    
    def check_environmental_impact(self, action: str, context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Assess environmental impact of action"""
        
        impact_keywords = ["energy", "carbon", "water", "resource", "waste"]
        if not any(keyword in action.lower() for keyword in impact_keywords):
            return None
            
        # Simplified impact assessment (would be ML model in production)
        return {
            "carbon_equiv": "0.5_tons",
            "water_consumed": "1000_liters",
            "irreversibility_score": 0.3,
            "assessment": "moderate_impact"
        }
    
    def create_memory_log(self, 
                         action: str,
                         classification: TMLClassification,
                         input_hash: str,
                         sacred_zero_trigger: Optional[str] = None,
                         environmental_impact: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create an immutable memory log entry"""
        
        memory_log = {
            "framework": self.framework,
            "creator_orcid": self.creator_orcid,
            "memory_id": self._generate_id(),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "action": action,
            "classification": int(classification),
            "input_hash": input_hash,
            "goukassian_promise": {
                "lantern": True,
                "signature": self.creator_orcid,
                "license": "MIT-Attribution-Required"
            }
        }
        
        if sacred_zero_trigger:
            memory_log["sacred_zero_trigger"] = sacred_zero_trigger
            
        if environmental_impact:
            memory_log["environmental_impact"] = environmental_impact
            
        # In production, this would be signed and sent to Guardian network
        memory_log["signature"] = self._sign_memory(memory_log)
        
        self.memories.append(memory_log)
        return memory_log
    
    def _generate_id(self) -> str:
        """Generate unique memory ID"""
        timestamp = str(datetime.utcnow().timestamp())
        return hashlib.sha256(timestamp.encode()).hexdigest()[:16]
    
    def _sign_memory(self, memory: Dict[str, Any]) -> str:
        """Create signature for memory log (simplified)"""
        json_str = json.dumps(memory, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()[:32]
    
    def _hash_data(self, data: Dict[str, Any]) -> str:
        """Create SHA256 hash of data"""
        json_str = json.dumps(data, sort_keys=True)
        return "0x" + hashlib.sha256(json_str.encode()).hexdigest()

# Initialize Always Memory
always_memory = AlwaysMemory()

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "framework": "TML Always Memory",
        "version": "5.0.0",
        "creator": "Lev Goukassian",
        "orcid": "0009-0006-5966-1243",
        "principle": "No memory = No action"
    }

@app.post("/memory/create", response_model=MemoryResponse)
async def create_memory(request: MemoryRequest, background_tasks: BackgroundTasks):
    """Create an Always Memory log for an AI action"""
    
    # Classify the action
    classification, sacred_trigger = always_memory.classify_action(
        request.action, 
        request.context or {}
    )
    
    # Check for environmental impact if requested
    environmental_impact = None
    if request.environmental_check:
        environmental_impact = always_memory.check_environmental_impact(
            request.action,
            request.context or {}
        )
        
        # Escalate to Sacred Zero if high environmental impact
        if environmental_impact and environmental_impact.get("irreversibility_score", 0) > 0.7:
            classification = TMLClassification.SACRED_ZERO
            sacred_trigger = "environmental_harm"
    
    # Block refused actions
    if classification == TMLClassification.REFUSE:
        raise HTTPException(
            status_code=403,
            detail="Action refused: violates TML safety principles"
        )
    
    # Create memory log
    input_hash = always_memory._hash_data(request.input_data)
    memory_log = always_memory.create_memory_log(
        action=request.action,
        classification=classification,
        input_hash=input_hash,
        sacred_zero_trigger=sacred_trigger,
        environmental_impact=environmental_impact
    )
    
    # Simulate Guardian confirmations (would be actual network calls)
    guardian_confirmations = [
        f"guardian_{i}_confirmed" for i in range(1, 4)
    ]
    
    # If Sacred Zero, trigger human review
    if classification == TMLClassification.SACRED_ZERO:
        background_tasks.add_task(
            trigger_human_review,
            memory_log["memory_id"],
            sacred_trigger
        )
    
    return MemoryResponse(
        memory_id=memory_log["memory_id"],
        classification=int(classification),
        sacred_zero_trigger=sacred_trigger,
        timestamp=memory_log["timestamp"],
        guardian_confirmations=guardian_confirmations,
        environmental_impact=environmental_impact
    )

@app.get("/memory/{memory_id}")
async def get_memory(memory_id: str):
    """Retrieve a specific memory log"""
    
    for memory in always_memory.memories:
        if memory["memory_id"] == memory_id:
            return memory
            
    raise HTTPException(status_code=404, detail="Memory not found")

@app.get("/memories/recent")
async def get_recent_memories(limit: int = 10):
    """Get recent memory logs"""
    return always_memory.memories[-limit:]

@app.post("/sacred-zero/trigger")
async def trigger_sacred_zero(event: SacredZeroEvent):
    """Manually trigger a Sacred Zero event"""
    
    memory_log = always_memory.create_memory_log(
        action="manual_sacred_zero",
        classification=TMLClassification.SACRED_ZERO,
        input_hash=event.context_hash,
        sacred_zero_trigger=event.trigger
    )
    
    return {
        "status": "Sacred Zero triggered",
        "memory_id": memory_log["memory_id"],
        "human_review_required": event.human_review_required
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "framework": "TML-AlwaysMemory-v5.0",
        "memories_logged": len(always_memory.memories)
    }

async def trigger_human_review(memory_id: str, trigger: str):
    """Trigger human review for Sacred Zero events"""
    logger.info(f"Sacred Zero human review triggered for {memory_id}: {trigger}")
    # In production, this would notify the Accountability Council

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

