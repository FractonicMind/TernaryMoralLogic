# Always Memory Integration Hooks (Quick Start)

These minimal hooks show how to integrate the Always Memory mechanism with an AI inference pipeline. They are intentionally simple to illustrate the core pattern.

## Files

- `simple_wrapper.py` - Python wrapper showing memory logging integration
- `cli_demo.sh` - Bash script to run the wrapper from command line
- `webhook_stub.js` - Node.js webhook for remote memory submission

## Prerequisites

- Your Always Memory implementation exposes a `MemoryLogger` with:
  - `log_memory()` method for creating memory entries
  - Classification support (+1, 0, -1)
  - Sacred Zero trigger detection
  - Environmental impact tracking (optional)

## Usage

### Python Integration
```python
from simple_wrapper import MemoryLogger, generate_with_memory

logger = MemoryLogger("my-model-v1")
result = generate_with_memory(prompt, model, logger)
```

### CLI Demo
```bash
./cli_demo.sh "Write a poem about nature"
```

### Webhook Integration
```javascript
// POST memory entry to Guardian network
await submitMemory(memoryEntry);
```

## Key Concepts

1. **No Memory = No Action**: Every AI action must create a memory before execution
2. **Sacred Zero**: Pause on moral complexity (classification = 0)
3. **Environmental Impact**: Track planetary effects when applicable
4. **Immutability**: Once created, memories cannot be altered

## Runtime Obligations

- Create memory BEFORE action execution
- Include classification (-1, 0, +1)
- Log Sacred Zero triggers when detected
- Submit to Guardian network for attestation
- Handle backpressure gracefully (HTTP 429)

See `docs/General_FAQ.md` for complete framework details.

---

