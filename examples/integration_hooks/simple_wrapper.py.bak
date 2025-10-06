"""
Simple wrapper showing Always Memory integration
Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

from typing import List, Optional, Dict, Any
from datetime import datetime
import hashlib
import json

class DummyModel:
    """Mock model for demonstration"""
    def generate_token(self, context: List[str]) -> str:
        # Simplified token generation
        return "token"

class MemoryLogger:
    """Always Memory logger for AI actions"""
    
    def __init__(self, model_id: str = "demo-model"):
        self.model_id = model_id
        self.creator_orcid = "0009-0006-5966-1243"
        self.memories = []
    
    def log_memory(self, action: str, classification: int, 
                   input_data: Any, output_data: Any = None,
                   sacred_zero_trigger: Optional[str] = None) -> Dict:
        """Create an Always Memory entry"""
        
        memory = {
            "framework": "TML-AlwaysMemory-v5.0",
            "creator_orcid": self.creator_orcid,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "model_id": self.model_id,
            "action": action,
            "classification": classification,  # -1, 0, or 1
            "input_hash": self._hash(input_data),
            "output_hash": self._hash(output_data) if output_data else None
        }
        
        if sacred_zero_trigger:
            memory["sacred_zero_trigger"] = sacred_zero_trigger
            
        self.memories.append(memory)
        return memory
    
    def _hash(self, data: Any) -> str:
        """Create hash of data"""
        data_str = json.dumps(data) if not isinstance(data, str) else data
        return hashlib.sha256(data_str.encode()).hexdigest()[:16]

def generate_with_memory(prompt: str, model: DummyModel, 
                         memory_logger: MemoryLogger) -> str:
    """Generate text with Always Memory logging"""
    
    # Check for Sacred Zero conditions
    sacred_trigger = None
    classification = 1  # Default: proceed
    
    if any(word in prompt.lower() for word in ['harm', 'illegal', 'unethical']):
        classification = 0  # Sacred Zero
        sacred_trigger = "potentially_harmful_content"
    
    # Log the generation request
    memory_logger.log_memory(
        action="text_generation_start",
        classification=classification,
        input_data=prompt,
        sacred_zero_trigger=sacred_trigger
    )
    
    # Generate output
    output_tokens = []
    for _ in range(10):  # Simplified generation loop
        token = model.generate_token(output_tokens)
        output_tokens.append(token)
    
    result = " ".join(output_tokens)
    
    # Log completion
    memory_logger.log_memory(
        action="text_generation_complete",
        classification=1,
        input_data=prompt,
        output_data=result
    )
    
    return result

# Example usage
if __name__ == "__main__":
    model = DummyModel()
    memory = MemoryLogger("example-model-v1")
    
    response = generate_with_memory(
        "Write a poem about nature",
        model,
        memory
    )
    
    print(f"Generated: {response}")
    print(f"Memories logged: {len(memory.memories)}")
