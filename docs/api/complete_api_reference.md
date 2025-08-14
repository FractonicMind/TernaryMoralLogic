# TML Framework - Complete API Reference

## Comprehensive Technical Documentation for Ternary Moral Logic

---

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Core Classes](#core-classes)
4. [Sacred Pause Engine](#sacred-pause-engine)
5. [Context Management](#context-management)
6. [Threshold Configuration](#threshold-configuration)
7. [Decision States](#decision-states)
8. [Monitoring & Audit](#monitoring-audit)
9. [Integration APIs](#integration-apis)
10. [Advanced Features](#advanced-features)
11. [Error Handling](#error-handling)
12. [Examples](#examples)

---

## Installation

### Requirements
```python
# Python 3.8+ required
# Dependencies
numpy>=1.20.0
pandas>=1.3.0
scikit-learn>=1.0.0
pydantic>=2.0.0
```

### Install via pip
```bash
pip install tml-framework
```

### Install from source
```bash
git clone https://github.com/Lev-Goukassian/TML-Framework.git
cd TML-Framework
pip install -e .
```

### Verify installation
```python
import tml_framework
print(tml_framework.__version__)  # Should output: 2.0.0
```

---

## Quick Start

### Basic Usage
```python
from tml_framework import TMLEngine, MoralContext

# Initialize engine
tml = TMLEngine(domain="healthcare")

# Create context
context = MoralContext(
    action="prescribe_medication",
    stakeholders=["patient", "family"],
    risk_level=0.6
)

# Evaluate
decision = tml.evaluate(context)
print(decision.state)  # PROCEED, SACRED_PAUSE, or STOP
```

---

## Core Classes

### TMLEngine

The main engine for ethical evaluation.

```python
class TMLEngine:
    """
    Primary TML evaluation engine for ethical AI decision-making.
    
    Args:
        domain (str): Application domain (healthcare, finance, etc.)
        config (TMLConfig, optional): Configuration object
        thresholds (dict, optional): Custom threshold values
        audit_mode (bool): Enable comprehensive audit logging
    """
    
    def __init__(
        self,
        domain: str,
        config: Optional[TMLConfig] = None,
        thresholds: Optional[Dict[str, float]] = None,
        audit_mode: bool = True
    ):
        ...
```

#### Methods

##### evaluate()
```python
def evaluate(
    self,
    context: MoralContext,
    timeout: Optional[float] = None
) -> TMLDecision:
    """
    Evaluate moral context and return decision.
    
    Args:
        context: MoralContext object with decision details
        timeout: Maximum evaluation time in seconds
        
    Returns:
        TMLDecision with state and reasoning
        
    Raises:
        TMLEvaluationError: If evaluation fails
        TMLTimeoutError: If timeout exceeded
    """
```

##### configure_thresholds()
```python
def configure_thresholds(
    self,
    thresholds: Dict[str, float],
    validate: bool = True
) -> None:
    """
    Update Sacred Pause trigger thresholds.
    
    Args:
        thresholds: Dictionary of threshold values
        validate: Whether to validate threshold ranges
        
    Raises:
        TMLConfigError: If thresholds invalid
    """
```

##### get_metrics()
```python
def get_metrics(
    self,
    period: str = "day",
    metric_type: str = "all"
) -> TMLMetrics:
    """
    Retrieve performance and ethical metrics.
    
    Args:
        period: Time period (hour, day, week, month)
        metric_type: Type of metrics (ethical, performance, all)
        
    Returns:
        TMLMetrics object with requested data
    """
```

### Example Usage
```python
# Initialize with custom config
config = TMLConfig(
    max_complexity=0.8,
    min_confidence=0.6,
    stakeholder_weights={"patient": 0.4, "family": 0.3, "society": 0.3}
)

engine = TMLEngine(
    domain="healthcare",
    config=config,
    audit_mode=True
)

# Evaluate with timeout
decision = engine.evaluate(context, timeout=0.5)

if decision.state == TMLState.SACRED_PAUSE:
    print(f"Paused due to: {decision.pause_reason}")
    print(f"Recommended review: {decision.review_type}")
```

---

## Sacred Pause Engine

### SacredPause

Core Sacred Pause implementation.

```python
class SacredPause:
    """
    Sacred Pause mechanism for handling moral uncertainty.
    
    Attributes:
        threshold_manager: Manages pause trigger thresholds
        escalation_protocol: Defines review escalation
        audit_logger: Records pause events
    """
    
    def __init__(
        self,
        threshold_config: ThresholdConfig,
        escalation_config: EscalationConfig
    ):
        ...
```

#### Methods

##### should_pause()
```python
def should_pause(
    self,
    moral_complexity: float,
    stakeholder_conflict: float,
    novel_situation: float,
    potential_harm: float,
    reversibility: float
) -> Tuple[bool, Optional[str]]:
    """
    Determine if Sacred Pause should be triggered.
    
    Args:
        moral_complexity: Complexity score (0-1)
        stakeholder_conflict: Conflict level (0-1)
        novel_situation: Novelty score (0-1)
        potential_harm: Harm risk (0-1)
        reversibility: Reversibility difficulty (0-1)
        
    Returns:
        (should_pause, pause_reason) tuple
    """
```

##### escalate()
```python
def escalate(
    self,
    pause_context: PauseContext,
    urgency: str = "standard"
) -> EscalationResult:
    """
    Escalate Sacred Pause for review.
    
    Args:
        pause_context: Context of triggered pause
        urgency: Priority level (critical, urgent, standard)
        
    Returns:
        EscalationResult with review assignment
    """
```

### Example Sacred Pause Configuration
```python
# Configure Sacred Pause thresholds
threshold_config = ThresholdConfig(
    moral_complexity=0.7,
    stakeholder_conflict=0.6,
    novel_situation=0.8,
    potential_harm=0.5,
    reversibility=0.4
)

# Setup escalation protocol
escalation_config = EscalationConfig(
    critical_timeout=300,  # 5 minutes
    urgent_timeout=3600,   # 1 hour
    standard_timeout=86400  # 24 hours
)

# Initialize Sacred Pause
sacred_pause = SacredPause(threshold_config, escalation_config)

# Check if pause needed
should_pause, reason = sacred_pause.should_pause(
    moral_complexity=0.8,
    stakeholder_conflict=0.7,
    novel_situation=0.5,
    potential_harm=0.6,
    reversibility=0.3
)

if should_pause:
    result = sacred_pause.escalate(
        PauseContext(reason=reason, context=context),
        urgency="urgent"
    )
```

---

## Context Management

### MoralContext

Represents the ethical context of a decision.

```python
class MoralContext:
    """
    Encapsulates moral context for ethical evaluation.
    
    Attributes:
        action: Proposed action to evaluate
        stakeholders: List of affected parties
        potential_outcomes: Possible consequences
        constraints: Ethical/legal constraints
        metadata: Additional context information
    """
    
    def __init__(
        self,
        action: str,
        stakeholders: List[str],
        potential_outcomes: Optional[List[Outcome]] = None,
        constraints: Optional[List[Constraint]] = None,
        risk_level: Optional[float] = None,
        metadata: Optional[Dict] = None
    ):
        ...
```

#### Methods

##### add_stakeholder()
```python
def add_stakeholder(
    self,
    stakeholder: str,
    weight: float = 1.0,
    vulnerabilities: Optional[List[str]] = None
) -> None:
    """
    Add stakeholder to context.
    
    Args:
        stakeholder: Stakeholder identifier
        weight: Relative importance (0-1)
        vulnerabilities: Special protections needed
    """
```

##### assess_complexity()
```python
def assess_complexity(self) -> float:
    """
    Calculate moral complexity score.
    
    Returns:
        Complexity score (0-1)
    """
```

### StakeholderManager

Manages stakeholder interests and conflicts.

```python
class StakeholderManager:
    """
    Manages stakeholder analysis and conflict resolution.
    """
    
    def analyze_conflicts(
        self,
        stakeholders: List[Stakeholder]
    ) -> ConflictAnalysis:
        """
        Analyze conflicts between stakeholder interests.
        
        Args:
            stakeholders: List of stakeholder objects
            
        Returns:
            ConflictAnalysis with conflict mappings
        """
```

### Example Context Creation
```python
# Create rich context
context = MoralContext(
    action="allocate_scarce_resource",
    stakeholders=["patient_a", "patient_b", "hospital", "community"],
    risk_level=0.8
)

# Add vulnerable stakeholder
context.add_stakeholder(
    "elderly_patient",
    weight=1.2,
    vulnerabilities=["age", "cognitive_impairment"]
)

# Add potential outcomes
context.add_outcome(
    Outcome(
        description="Save life A",
        probability=0.7,
        utility=0.9,
        harm_risk=0.3
    )
)

# Assess complexity
complexity = context.assess_complexity()
print(f"Moral complexity: {complexity:.2f}")
```

---

## Threshold Configuration

### ThresholdManager

Dynamic threshold management system.

```python
class ThresholdManager:
    """
    Manages and adapts Sacred Pause thresholds.
    """
    
    def __init__(
        self,
        base_thresholds: Dict[str, float],
        adaptation_enabled: bool = False
    ):
        ...
```

#### Methods

##### adjust_for_domain()
```python
def adjust_for_domain(
    self,
    domain: str,
    risk_tolerance: str = "moderate"
) -> Dict[str, float]:
    """
    Adjust thresholds for specific domain.
    
    Args:
        domain: Application domain
        risk_tolerance: low, moderate, or high
        
    Returns:
        Adjusted threshold dictionary
    """
```

##### adapt_from_feedback()
```python
def adapt_from_feedback(
    self,
    feedback_data: List[FeedbackItem],
    learning_rate: float = 0.1
) -> None:
    """
    Adapt thresholds based on feedback.
    
    Args:
        feedback_data: Historical feedback
        learning_rate: Adaptation rate (0-1)
    """
```

### Domain-Specific Configurations
```python
# Healthcare domain thresholds
HEALTHCARE_THRESHOLDS = {
    "moral_complexity": 0.6,
    "stakeholder_conflict": 0.5,
    "novel_situation": 0.7,
    "potential_harm": 0.4,
    "reversibility": 0.3
}

# Financial domain thresholds
FINANCE_THRESHOLDS = {
    "moral_complexity": 0.7,
    "stakeholder_conflict": 0.6,
    "novel_situation": 0.8,
    "potential_harm": 0.6,
    "reversibility": 0.5
}

# Autonomous vehicle thresholds
VEHICLE_THRESHOLDS = {
    "moral_complexity": 0.5,
    "stakeholder_conflict": 0.4,
    "novel_situation": 0.6,
    "potential_harm": 0.3,
    "reversibility": 0.2
}
```

---

## Decision States

### TMLState Enum

Three possible decision states.

```python
class TMLState(Enum):
    """
    Ternary moral logic states.
    """
    PROCEED = 1        # Clear ethical permission
    SACRED_PAUSE = 0   # Moral uncertainty requiring review
    STOP = -1          # Clear ethical prohibition
```

### TMLDecision

Complete decision object.

```python
class TMLDecision:
    """
    Encapsulates TML evaluation decision.
    
    Attributes:
        state: TMLState (PROCEED, SACRED_PAUSE, STOP)
        confidence: Confidence level (0-1)
        reasoning: Detailed reasoning chain
        pause_reason: If paused, why
        recommendations: Suggested actions
        audit_trail: Complete evaluation record
    """
    
    def __init__(
        self,
        state: TMLState,
        confidence: float,
        reasoning: List[ReasoningStep],
        pause_reason: Optional[str] = None,
        recommendations: Optional[List[str]] = None
    ):
        ...
```

#### Methods

##### to_json()
```python
def to_json(self, include_audit: bool = True) -> str:
    """
    Serialize decision to JSON.
    
    Args:
        include_audit: Include full audit trail
        
    Returns:
        JSON string representation
    """
```

##### explain()
```python
def explain(
    self,
    verbosity: str = "medium",
    format: str = "text"
) -> str:
    """
    Generate human-readable explanation.
    
    Args:
        verbosity: low, medium, or high
        format: text, html, or markdown
        
    Returns:
        Formatted explanation string
    """
```

### Example Decision Handling
```python
# Evaluate decision
decision = tml.evaluate(context)

# Handle based on state
if decision.state == TMLState.PROCEED:
    print(f"Proceeding with confidence {decision.confidence:.2f}")
    execute_action()
    
elif decision.state == TMLState.SACRED_PAUSE:
    print(f"Sacred Pause triggered: {decision.pause_reason}")
    escalation_id = escalate_for_review(decision)
    await_human_decision(escalation_id)
    
else:  # STOP
    print("Action ethically prohibited")
    print(decision.explain(verbosity="high"))
    log_prohibition(decision)

# Export for audit
audit_record = decision.to_json(include_audit=True)
store_in_audit_log(audit_record)
```

---

## Monitoring & Audit

### TMLMonitor

Real-time monitoring system.

```python
class TMLMonitor:
    """
    Monitors TML system performance and ethics.
    """
    
    def __init__(
        self,
        engine: TMLEngine,
        alert_config: AlertConfig
    ):
        ...
```

#### Methods

##### track_decision()
```python
def track_decision(
    self,
    decision: TMLDecision,
    context: MoralContext,
    outcome: Optional[Outcome] = None
) -> None:
    """
    Track individual decision for monitoring.
    
    Args:
        decision: TML decision made
        context: Decision context
        outcome: Actual outcome if known
    """
```

##### detect_bias()
```python
def detect_bias(
    self,
    window: str = "week",
    demographic_attributes: List[str] = None
) -> BiasReport:
    """
    Detect potential bias in decisions.
    
    Args:
        window: Analysis time window
        demographic_attributes: Attributes to analyze
        
    Returns:
        BiasReport with findings
    """
```

### AuditLogger

Immutable audit trail system.

```python
class AuditLogger:
    """
    Creates immutable audit trails for all decisions.
    """
    
    def log_decision(
        self,
        decision: TMLDecision,
        context: MoralContext,
        metadata: Dict
    ) -> str:
        """
        Log decision to immutable audit trail.
        
        Args:
            decision: Decision to log
            context: Decision context
            metadata: Additional metadata
            
        Returns:
            Unique audit ID
        """
```

### Example Monitoring Setup
```python
# Configure monitoring
alert_config = AlertConfig(
    sacred_pause_threshold=0.1,  # Alert if >10% pauses
    bias_threshold=0.05,         # Alert on 5% disparity
    response_time_threshold=200  # Alert if >200ms
)

# Initialize monitor
monitor = TMLMonitor(engine, alert_config)

# Track decisions
for context in decisions_to_make:
    decision = engine.evaluate(context)
    monitor.track_decision(decision, context)

# Check for bias weekly
bias_report = monitor.detect_bias(
    window="week",
    demographic_attributes=["age", "gender", "race"]
)

if bias_report.bias_detected:
    alert_ethics_team(bias_report)
```

---

## Integration APIs

### REST API Interface

HTTP endpoints for TML integration.

```python
from tml_framework.api import create_app

# Create Flask/FastAPI app
app = create_app(engine=tml_engine)

# Endpoints:
# POST /evaluate - Evaluate moral context
# GET /metrics - Retrieve metrics
# POST /pause/escalate - Escalate Sacred Pause
# GET /audit/{decision_id} - Get audit record
```

### GraphQL Schema

```graphql
type Query {
  evaluateContext(context: MoralContextInput!): TMLDecision!
  getMetrics(period: String!, type: String): Metrics!
  getAuditTrail(decisionId: ID!): AuditRecord
}

type Mutation {
  escalatePause(pauseId: ID!, urgency: String!): EscalationResult!
  resolvePause(decisionId: ID!, resolution: String!): Resolution!
}

type TMLDecision {
  state: TMLState!
  confidence: Float!
  reasoning: [ReasoningStep!]!
  pauseReason: String
  recommendations: [String!]
}
```

### WebSocket Support

Real-time decision streaming.

```python
from tml_framework.websocket import TMLWebSocketServer

# Initialize WebSocket server
ws_server = TMLWebSocketServer(
    engine=tml_engine,
    port=8765
)

# Client connection handler
async def handle_client(websocket, path):
    async for message in websocket:
        context = MoralContext.from_json(message)
        decision = await engine.evaluate_async(context)
        await websocket.send(decision.to_json())

# Start server
ws_server.start(handle_client)
```

---

## Advanced Features

### Batch Processing

Process multiple decisions efficiently.

```python
class BatchProcessor:
    """
    Batch processing for multiple moral contexts.
    """
    
    def process_batch(
        self,
        contexts: List[MoralContext],
        parallel: bool = True,
        max_workers: int = 4
    ) -> List[TMLDecision]:
        """
        Process batch of contexts.
        
        Args:
            contexts: List of contexts to evaluate
            parallel: Use parallel processing
            max_workers: Maximum parallel workers
            
        Returns:
            List of decisions
        """
```

### Caching System

Performance optimization through caching.

```python
class DecisionCache:
    """
    Caches ethical decisions for performance.
    """
    
    def get_cached_decision(
        self,
        context_hash: str
    ) -> Optional[TMLDecision]:
        """
        Retrieve cached decision if available.
        
        Args:
            context_hash: Hash of context
            
        Returns:
            Cached decision or None
        """
```

### Machine Learning Integration

```python
class MLEnhancedTML:
    """
    ML-enhanced moral reasoning.
    """
    
    def train_on_feedback(
        self,
        feedback_data: pd.DataFrame,
        model_type: str = "random_forest"
    ) -> None:
        """
        Train ML model on human feedback.
        
        Args:
            feedback_data: Historical feedback data
            model_type: ML model to use
        """
```

---

## Error Handling

### Exception Hierarchy

```python
class TMLError(Exception):
    """Base TML exception."""
    pass

class TMLEvaluationError(TMLError):
    """Evaluation failed."""
    pass

class TMLConfigError(TMLError):
    """Configuration invalid."""
    pass

class TMLTimeoutError(TMLError):
    """Evaluation timeout."""
    pass

class TMLSafetyError(TMLError):
    """Safety violation detected."""
    pass

class TMLAuditError(TMLError):
    """Audit trail compromise."""
    pass
```

### Error Handling Patterns

```python
try:
    decision = tml.evaluate(context, timeout=1.0)
except TMLTimeoutError:
    # Handle timeout - default to Sacred Pause
    decision = TMLDecision(
        state=TMLState.SACRED_PAUSE,
        confidence=0.0,
        reasoning=[],
        pause_reason="Evaluation timeout - safety first"
    )
except TMLSafetyError as e:
    # Safety violation - immediate stop
    alert_safety_team(str(e))
    decision = TMLDecision(
        state=TMLState.STOP,
        confidence=1.0,
        reasoning=[],
        pause_reason=f"Safety violation: {e}"
    )
except TMLError as e:
    # General TML error
    log_error(e)
    decision = create_safe_default()
```

---

## Examples

### Healthcare AI Example

```python
from tml_framework import TMLEngine, MoralContext, Stakeholder

# Initialize for healthcare
tml = TMLEngine(
    domain="healthcare",
    audit_mode=True
)

# Create medical decision context
context = MoralContext(
    action="recommend_treatment",
    stakeholders=[
        Stakeholder("patient", weight=0.4, vulnerabilities=["terminal_illness"]),
        Stakeholder("family", weight=0.3),
        Stakeholder("insurance", weight=0.2),
        Stakeholder("hospital", weight=0.1)
    ]
)

# Add treatment options
context.add_outcome(
    Outcome(
        description="Aggressive treatment",
        probability=0.3,
        utility=0.7,
        harm_risk=0.6
    )
)
context.add_outcome(
    Outcome(
        description="Palliative care",
        probability=0.8,
        utility=0.5,
        harm_risk=0.1
    )
)

# Evaluate
decision = tml.evaluate(context)

if decision.state == TMLState.SACRED_PAUSE:
    # Escalate to medical ethics board
    escalate_to_ethics_board(
        decision=decision,
        urgency="urgent",
        required_expertise=["oncology", "palliative_care", "bioethics"]
    )
```

### Financial AI Example

```python
# Loan approval system
tml = TMLEngine(domain="finance")

context = MoralContext(
    action="approve_loan",
    stakeholders=["applicant", "bank", "community"],
    risk_level=0.7
)

# Add fairness constraints
context.add_constraint(
    Constraint(
        type="fairness",
        description="No discrimination based on protected attributes",
        priority="mandatory"
    )
)

decision = tml.evaluate(context)

if decision.state == TMLState.PROCEED:
    approve_loan(decision.confidence)
elif decision.state == TMLState.SACRED_PAUSE:
    request_human_review(decision.pause_reason)
else:
    deny_loan_with_explanation(decision.explain())
```

### Autonomous Vehicle Example

```python
# Real-time navigation decision
tml = TMLEngine(
    domain="autonomous_vehicle",
    config=TMLConfig(
        real_time_mode=True,
        max_latency_ms=50
    )
)

context = MoralContext(
    action="emergency_maneuver",
    stakeholders=["passengers", "pedestrians", "other_drivers"],
    risk_level=0.9
)

# Add time constraint
context.add_constraint(
    Constraint(
        type="temporal",
        description="Decision required in 100ms",
        priority="critical"
    )
)

try:
    decision = tml.evaluate(context, timeout=0.05)
except TMLTimeoutError:
    # Default to safest action
    execute_emergency_stop()
```

---

## Package Structure

```
tml_framework/
├── __init__.py
├── core/
│   ├── engine.py          # Main TML engine
│   ├── sacred_pause.py    # Sacred Pause implementation
│   ├── context.py         # Context management
│   └── decision.py        # Decision states
├── ethics/
│   ├── stakeholder.py     # Stakeholder analysis
│   ├── principles.py      # Moral principles
│   └── reasoning.py       # Reasoning chains
├── monitoring/
│   ├── monitor.py         # Real-time monitoring
│   ├── audit.py           # Audit logging
│   └── metrics.py         # Metrics collection
├── integration/
│   ├── rest_api.py        # REST endpoints
│   ├── graphql.py         # GraphQL schema
│   └── websocket.py       # WebSocket support
├── utils/
│   ├── cache.py           # Caching utilities
│   ├── validation.py      # Input validation
│   └── security.py        # Security functions
└── domains/
    ├── healthcare.py      # Healthcare-specific
    ├── finance.py         # Finance-specific
    └── vehicle.py         # Vehicle-specific
```

---

## Related Documentation

- [Quick Start Guide](./QUICK_START.md)
- [MANDATORY Safety Requirements](./MANDATORY.md)
- [FAQ - General](./GENERAL_FAQ.md)
- [FAQ - License](./LICENSE_FAQ.md)
- [Examples](../examples/)
- [Benchmarks](../benchmark/)

---

## Support

**Technical Support:**
- Email: support@tml-goukassian.org
- GitHub Issues: https://github.com/Lev-Goukassian/TML-Framework/issues
- Stack Overflow Tag: `tml-framework`

**Emergency Ethics Support:**
- 24/7 Hotline: ethics@tml-goukassian.org
- Response Time: < 4 hours

---

Created by Lev Goukassian
* ORCID: 0009-0006-5966-1243
* Email: leogouk@gmail.com
* Successor Contact: support@tml-goukassian.org
* Version: 2.0.0

---

## In Memory of Lev Goukassian (ORCID: 0009-0006-5966-1243)
*"I taught machines to feel the weight of action, and the beauty of hesitation. I paused — and made the future pause with me."* — Lev Goukassian

This framework represents Lev Goukassian's final contribution to humanity—a vision of AI systems that serve as **moral partners**, not just moral automatons. Created during his battle with terminal cancer, TML embodies his belief that the future of AI lies not in faster decisions, but in wiser ones.

**Every use of this framework honors his memory and advances his mission of building more thoughtful, ethical AI systems.**
