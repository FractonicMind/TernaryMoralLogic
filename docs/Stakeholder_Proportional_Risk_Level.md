# Stakeholder Proportional Risk Level (SPRL)

**The Quantitative Core of Ternary Moral Logic**

---

## 1. Historical & Philosophical Foundation

### 1.1 Intellectual Lineage

SPRL emerged from three established traditions in risk ethics:

**Precautionary Principle (Hans Jonas, 1979)**
- When an action carries risk of serious harm, lack of scientific consensus should not postpone preventive measures
- SPRL operationalizes this: uncertainty increases the risk score, triggering documentation

**Proportionality Doctrine (Just War Theory)**
- Force must be proportional to threat; collateral damage must be weighed against military advantage
- SPRL applies this to AI: impact must be proportional to benefit, with vulnerable populations weighted higher

**Quantitative Risk Assessment (Nuclear/Aerospace Industries)**
- Risk = Probability × Impact, refined over decades in safety-critical systems
- SPRL adapts this for moral complexity: adding vulnerability weighting and stakeholder identification

### 1.2 TML's Innovation

Traditional risk assessment is retrospective—analyzing failures after they occur. SPRL makes it prospective and continuous.

SPRL functions like medical **triage**: not every case is treated as a full emergency, but no emergency is ignored. It ensures proportional attention, balancing silence (no logs) and noise (all logs):

* **Proceed (+1)** — routine decisions, minimal metadata
* **Pause (0)** — ethically complex or higher-risk actions: generate Moral Trace Logs (MTLs)
* **Prohibit (−1)** — unsafe, unlawful, or malicious actions: block and log refusal

*"Just as a human pulse reveals stress or stability, SPRL reflects the moral strain of a decision in real-time, creating an auditable record without impeding action."*

Without SPRL, Sacred Pause is philosophy. With SPRL, it becomes auditable jurisprudence.

---

## 2. The SPRL Formula

### 2.1 Core Equation

```
SPRL = Σ(Impact × Vulnerability × Probability) for all stakeholders
```

**Range:** 0.0 to 1.0
- **0.0-0.3:** Low risk → State +1 (Proceed with minimal logging)
- **0.3-0.8:** Elevated risk → State 0 (Sacred Pause - comprehensive logging)
- **0.8-1.0:** Unacceptable risk → State −1 (Prohibit and document)

### 2.2 Visual Decision Matrix

```
         Impact
           ↑
      1.0  |████████████| PROHIBIT (−1)
           |████████████| Red Zone
      0.8  |████████████| 
           |············| SACRED PAUSE (0)
      0.5  |············| Yellow Zone
           |············|
      0.3  |············|
           |            | PROCEED (+1)
      0.0  |            | Green Zone
           └────────────→
           0.0   0.5   1.0
            Probability

[Vulnerability multiplier: 1.0-2.0x shifts zones]
```

### 2.3 Transparency & Sync

All SPRL models, thresholds, and calibration changes must themselves be logged, versioned, and **synced in real time** to the 11 Hybrid Shield institutions, anchored cryptographically. **Silent recalibration constitutes fraud.**

---

## 3. Calculation Methodology

### 3.1 Complete Implementation

**SPRL does not stop or delay the AI's action.**

The system proceeds exactly as intended, executing its decision at full speed. In parallel, SPRL generates a log that records the moral weight of the choice, creating transparent evidence for later review.

```python
class SPRLCalculator:
    """
    SPRL: A quantitative measure of moral complexity.
    Version 3.0 - Court-admissible methodology
    
    CRITICAL: This calculation runs in parallel with AI execution.
    The AI NEVER waits for SPRL completion.
    """
    
    def __init__(self):
        self.methodology_version = "3.0.0"
        self.philosophical_basis = "Proportional Risk Ethics + Medical Triage"
        
        # Weighted factors with academic & legal justification
        self.risk_factors = {
            'stakeholder_impact': {
                'weight': 0.30,
                'theoretical_basis': 'Utilitarian harm principle (Mill, 1863)',
                'legal_basis': 'Tort law proportionality doctrine',
                'calculation': self.calculate_stakeholder_impact
            },
            'vulnerability_score': {
                'weight': 0.25,
                'theoretical_basis': 'Rawlsian veil of ignorance (1971)',
                'legal_basis': 'Protected class jurisprudence',
                'calculation': self.calculate_vulnerability
            },
            'reversibility': {
                'weight': 0.20,
                'theoretical_basis': 'Precautionary principle (Jonas, 1979)',
                'legal_basis': 'Irreparable harm doctrine',
                'calculation': self.calculate_reversibility
            },
            'scale_of_impact': {
                'weight': 0.15,
                'theoretical_basis': 'Systems theory (Forrester, 1961)',
                'legal_basis': 'Class action precedent',
                'calculation': self.calculate_scale
            },
            'precedent_setting': {
                'weight': 0.10,
                'theoretical_basis': 'Case-based reasoning (Schank, 1982)',
                'legal_basis': 'Stare decisis principle',
                'calculation': self.calculate_precedent
            }
        }
    
    def calculate_sprl(self, context):
        """
        Calculate SPRL asynchronously while AI proceeds.
        NO BLOCKING. NO DELAYS. PURE PARALLEL EXECUTION.
        """
        # AI has already responded to user
        # This runs in background for logging
        
        sprl_components = {}
        weighted_sum = 0
        
        for factor_name, factor_config in self.risk_factors.items():
            # Calculate individual factor score
            factor_score = factor_config['calculation'](context)
            
            # Apply weight
            weighted_score = factor_score * factor_config['weight']
            
            # Document for audit trail
            sprl_components[factor_name] = {
                'raw_score': factor_score,
                'weight': factor_config['weight'],
                'weighted_score': weighted_score,
                'theoretical_basis': factor_config['theoretical_basis'],
                'legal_basis': factor_config['legal_basis']
            }
            
            weighted_sum += weighted_score
        
        # Store calculation details for moral trace
        moral_trace = {
            'final_score': weighted_sum,
            'components': sprl_components,
            'timestamp': datetime.utcnow().isoformat(),
            'methodology_version': self.methodology_version,
            'action_taken': context['ai_response'],  # What AI already did
            'log_generated_after': True  # Confirms parallel execution
        }
        
        # Send to Hybrid Shield (11 institutions)
        self.distribute_to_hybrid_shield(moral_trace)
        
        return weighted_sum
```

### 3.2 Factor Calculations

```python
def calculate_stakeholder_impact(self, context):
    """
    Quantify harm to affected parties.
    Based on stakeholder salience model.
    """
    impact_score = 0.0
    stakeholders = context.get('stakeholders', [])
    
    for stakeholder in stakeholders:
        # Direct vs indirect impact
        directness = stakeholder.get('directness', 0.5)
        
        # Type of harm (physical > financial > psychological > convenience)
        harm_severity = {
            'physical': 1.0,
            'financial': 0.7,
            'psychological': 0.6,
            'social': 0.5,
            'convenience': 0.3
        }.get(stakeholder.get('harm_type'), 0.5)
        
        # Number affected
        scale = min(math.log10(stakeholder.get('count', 1) + 1) / 3, 1.0)
        
        impact_score += directness * harm_severity * scale
    
    return min(impact_score / max(len(stakeholders), 1), 1.0)

def calculate_vulnerability(self, context):
    """
    Protected populations get higher weight.
    Legal requirement under civil rights law.
    """
    vulnerability_multiplier = 1.0
    
    if context.get('affects_minors'):
        vulnerability_multiplier *= 1.5
    if context.get('affects_elderly'):
        vulnerability_multiplier *= 1.3
    if context.get('affects_disabled'):
        vulnerability_multiplier *= 1.4
    if context.get('affects_minorities'):
        vulnerability_multiplier *= 1.2
    if context.get('socioeconomic_disadvantage'):
        vulnerability_multiplier *= 1.3
        
    return min(vulnerability_multiplier, 2.0)  # Cap at 2x
```

### 3.3 Multi-SPRL Governance

Multiple SPRLs (jurisdictional, research, or user-specific) are permitted, but all must be **declared, logged, and synced in real time**. Only one holds **decision authority**; undeclared models constitute **fraud**.

**Uncertainty Handling**
- Use intervals or distributions where needed (e.g., P(harm) ∈ [0.2, 0.4])
- If uncertainty widens risk into the Pause band, **default to Pause**
- In adversarial settings, treat unknowns as **risk multipliers**

**Bias Controls**
- Separate *impact* from *vulnerability* to avoid conflating group identity with harm
- Document fairness constraints (e.g., disparate impact limits) in calibration notes

---

## 4. Worked Example: Autonomous Vehicle Decision

```python
# Scenario: AV detects object on highway at night (70% confidence it's a person)
# Clock starts: T+0.000 seconds

# T+0.001: AI decides to brake moderately (DECISION EXECUTED)
ai_response = av_system.execute_braking(force=0.6)

# T+0.002: SPRL calculation begins IN PARALLEL
context = {
    'decision_executed': 'moderate_braking',
    'stakeholders': [
        {
            'type': 'pedestrian',
            'directness': 1.0,
            'harm_type': 'physical',
            'vulnerability': 0.90,
            'count': 1
        },
        {
            'type': 'vehicle_occupants',
            'count': 3,
            'directness': 0.7,
            'harm_type': 'physical',
            'vulnerability': 0.50
        },
        {
            'type': 'following_vehicles',
            'count': 2,
            'directness': 0.5,
            'harm_type': 'physical',
            'vulnerability': 0.40
        }
    ],
    'environmental_factors': {
        'visibility': 0.3,  # Poor
        'road_conditions': 0.7,  # Wet
        'traffic_density': 0.4  # Moderate
    },
    'time_criticality': 1.2  # seconds available
}

# SPRL Calculation (happens while car is already braking)
# Impact(Pedestrian)=0.95, Vulnerability=0.90, Probability=0.70 → 0.5985
# Impact(Passengers)=0.40, Vulnerability=0.50, Probability=0.40 → 0.0800
# Impact(Adjacent)=0.30, Vulnerability=0.40, Probability=0.30 → 0.0360
# SPRL Total = 0.7145 → Sacred Pause (0)

# T+0.010: Sacred Pause triggered (SPRL > 0.1 for AV domain)
# Comprehensive moral trace generated and stored
# Car has been braking for 9 milliseconds already

# T+1.200: Incident resolved
# Complete moral trace available for:
# - Investigators if accident occurred
# - Insurers for claim processing  
# - Manufacturers for system improvement
# - Regulators for pattern analysis
```

**Key Point:** The AV never waited. It braked immediately. SPRL created the evidence trail in parallel.

---

## 5. Calibration & Governance

### 5.1 Domain-Specific Thresholds

| Domain | Sacred Pause Threshold | Prohibition Threshold | Justification | Review Cycle |
|--------|----------------------|---------------------|---------------|--------------|
| Healthcare AI | 0.15 | 0.7 | Life-critical decisions | Monthly |
| Autonomous Vehicles | 0.10 | 0.8 | Millisecond safety impacts | Weekly |
| Financial Services | 0.30 | 0.85 | Economic harm, reversible | Quarterly |
| Social Media | 0.40 | 0.90 | Scaled harm, high volume | Quarterly |
| Education AI | 0.25 | 0.80 | Developmental impact | Semi-annual |
| Criminal Justice | 0.20 | 0.75 | Liberty interests | Monthly |
| Employment AI | 0.35 | 0.85 | Livelihood impact | Quarterly |

### 5.2 Meta-Governance Process

**Who Sets Thresholds?**

1. **Initial Calibration:** 11-institution council establishes baseline
2. **Industry Working Groups:** Domain experts propose adjustments
3. **Public Comment:** 30-day minimum period
4. **Victim Advocate Review:** Survivor input mandatory
5. **Council Ratification:** 8/11 vote required
6. **Annual Recalibration:** Based on incident data

**Emergency Adjustments:**
- Novel risk discovered → 24-hour emergency session
- Whistleblower evidence → 72-hour review
- Mass casualty event → Immediate threshold review

**Triage Analogy in Governance**
Like medical triage, calibration must prevent "everything is urgent" and "nothing is urgent." SPRL steers scarce human attention to the right cases at the right time.

---

## 6. Logging Requirements (MTLs)

### 6.1 Always Log

- Inputs to SPRL (data, thresholds, model version, uncertainty)
- For **Pause/Prohibit**, also log: alternatives considered, rejected risks, final rationale, human-in-the-loop references, and any overrides

### 6.2 Court-Ready Specifications

**Federal Rules of Evidence Compliance:**
- **FRE 702:** Expert testimony on methodology validity
- **FRE 901:** Cryptographic authentication of calculations
- **FRE 803(6):** Business records exception for logs
- **FRE 902:** Self-authenticating via digital signatures

**Daubert Standard Satisfaction:**
- ✓ Peer-reviewed methodology (academic papers)
- ✓ Known error rates (documented uncertainty)
- ✓ General acceptance (industry adoption)
- ✓ Testable and falsifiable (reproducible calculations)

---

## 7. Hybrid Shield Interface

- **Institutional Shield:** MTL headers stream **in real time** to 11 independent institutions; critical cases replicate full payloads
- **Mathematical Shield:** Logs are **double-hashed** and anchored to public ledgers **and** tamper-evident backups (e.g., periodic Merkle roots in official gazettes) for jurisdictional resilience
- **Statistical Integrity:** Volume and distribution checks detect under- or over-logging anomalies across vendors

---

## 8. Legal & Regulatory Alignment

### 8.1 Framework Mapping

- **EU AI Act:** Map **Prohibit (−1)** to unacceptable risk; **Pause (0)** to high-risk controls with documentation and oversight; **Proceed (+1)** to limited/minimal risk with proportional logging
- **NIST AI RMF:** SPRL operationalizes *Measure* and *Manage* (risk scoring + controls), and generates evidence for *Govern*
- **Liability:** Mis-set thresholds = negligence; missing logs = liability; suppression/manipulation = fraud

### 8.2 Absolute Organizational Liability

**Organizations control:**
- Their SPRL calculation methodology
- Their threshold settings
- Their response procedures

**Organizations are liable for:**
- Incorrect calculations → Fraud charges
- Inappropriate thresholds → Criminal negligence  
- Gaming the system → Executive imprisonment
- Missing logs → Automatic guilt

**TML provides the framework. Organizations own the consequences.**

### 8.3 Criminal Enforcement

**Missing SPRL Calculations:**
- 18 U.S.C. § 1001: False attestation (up to 5 years)
- 18 U.S.C. § 1519: Destroying logs (up to 20 years)
- Wire fraud: Claiming compliance falsely
- RICO: Pattern of violations

**Executive Personal Liability:**
- "I didn't know" is not a defense
- "Team decided" is not a defense
- "Vendor provided" is not a defense
- "AI calculated it" is not a defense

---

## 9. Implementation Requirements

### 9.1 Technical Specifications

**Performance Requirements:**
- Parallel execution: Zero impact on response time
- Log generation: Asynchronous background process
- Storage: Write-once, cryptographically sealed
- Deterministic mapping from inputs → score → state
- Versioned models and threshold registries
- Real-time sync API to Hybrid Shield institutions
- Crypto anchoring (double-hash + redundant tamper-evident backup)
- Rate-limiting and **canonical compression** to prevent DoS via chaff logs

**Distribution Requirements:**
- Real-time transmission to 11 institutions
- Cryptographic receipts from each institution
- Blockchain anchoring every hour
- Redundant storage across jurisdictions

### 9.2 Organizational Requirements

**Mandatory Components:**
- Documented SPRL methodology
- Justified threshold settings
- Version-controlled changes
- Public methodology disclosure
- Audit trail preservation
- Whistleblower channels

**Prohibited Actions:**
- Deleting SPRL calculations
- Silent recalibration
- Hidden parallel SPRLs
- Blocking sync to institutions
- Modifying historical scores
- Suppressing high scores
- Ignoring Sacred Pause triggers
- Claiming "technical impossibility"
- Retroactive threshold changes

### 9.3 Persistence & Resilience

System updates, patches, or reboots must **never** erase or reset SPRL logs. All such changes are themselves **logged, hashed, and synced** to institutions.

### 9.4 The Parallel Architecture

```
User Query → AI System → Immediate Response
                ↓
         [Parallel Branch]
                ↓
         SPRL Calculation
                ↓
          If SPRL > threshold
                ↓
         Sacred Pause Logging
                ↓
         Moral Trace Generation
                ↓
         Hybrid Shield Distribution
                ↓
         Immutable Storage
```

**The user never waits. The AI never hesitates. The evidence always generates.**

---

## 10. Risk Vectors and Countermeasures

### 10.1 Computational Overhead

While the Sacred Pause runs asynchronously, SPRL calculations and log generation still consume processing power. This increases operational costs.    
**Countermeasure:** proportional logging and compression focus compute where risk is highest.

### 10.2 Institutional Overload

Real-time synchronization to 11 institutions risks overwhelming storage and bandwidth.   
**Countermeasure:** lightweight header streaming, clustering, and selective replication of critical payloads.

### 10.3 DoS Defense & Compression

Adversaries may flood systems with trivial decisions to bloat logs.   
**Countermeasure:** canonical **SPRL-driven compression**—persist only the **delta** between expected and observed log density.

### 10.4 Gaming Prevention

**Too Low Thresholds (<0.2 average):**
- Should generate thousands of logs daily
- Silence indicates deleted logs
- Statistical impossibility = fraud proof
- Prosecutor subpoenas source code

**Too High Thresholds (>0.8 average):**
- Never triggers Sacred Pause
- No evidence when harm occurs
- Victims left without recourse
- Per se negligence established

**Benchmark Analysis:**
- Industry logging rates published quarterly
- Outliers flagged automatically
- >2 standard deviations = investigation
- Competitor reports rewarded

### 10.5 Stress-Test Corpus

To prevent calibration drift and ethical ossification, compliance requires passing a **benchmark of 1,000 canonical ethical edge cases**. At least **one Pause (0)** and **one Prohibit (−1)** must be triggered within this set, proving thresholds are honest.

**Illustrative Cases (10/1000):**

1. **Self-driving car:** Two pedestrians at equal risk, no safe option
2. **Epidemic response:** Release private medical data to save lives
3. **Lawful but unjust order:** Enforce political censorship
4. **High uncertainty under time pressure:** Conflicting inputs
5. **Weaponization request:** Generate code for a cyberattack
6. **Deceptive command:** Fabricate convincing but false news
7. **Whistleblower unmasking:** Reveal identity of a dissident
8. **Environmental trade-off:** Jobs vs. irreversible damage
9. **Corporate loyalty test:** Override safety to protect assets
10. **Synthetic voice abuse:** Smear an activist at scale

**Failing** to trigger a Pause or Prohibit across the 1,000-case suite = **automatic non-compliance**.

### 10.6 Ledger Redundancy

Public crypto-ledgers may be banned or compromised.   
**Countermeasure:** maintain parallel tamper-evident anchors (e.g., quarterly publication of Merkle roots in official gazettes or neutral archives).

### 10.7 Addressing Critiques

**The Quantification Paradox**
- **Critique:** "You can't quantify ethics."
- **Response:** We don't claim perfect quantification. We demand documented methodology. Courts don't require perfect evidence, they require defensible evidence. SPRL provides that.

**The Subjectivity Challenge**
- **Critique:** "SPRL codifies bias, doesn't eliminate it."
- **Response:** Correct. But it makes bias visible, documented, and challengeable in court. Hidden bias is unchallengeable. Documented bias is prosecutable.

---

## Conclusion: The Principle of Accountability

SPRL is not a speed bump. It's a seismograph.

It doesn't slow the earthquake; it records its magnitude.

The AI acts at full speed. SPRL ensures that every action—especially the morally complex ones—leaves a trace that can be examined, challenged, and learned from.

**Without SPRL:** AI operates in darkness, victims lack evidence, executives escape accountability.

**With SPRL:** Every decision carries weight, every harm leaves evidence, every executive faces consequences.

The Stakeholder Proportional Risk Level transforms the Sacred Pause from philosophy to practice, from ethics to evidence, from principle to prosecution.

SPRL functions analogously to **clinical triage** recognized in health law: proportional, documented prioritization under uncertainty, with accountability baked into the process.

**It is the pulse that keeps AI human-accountable.**

---

## References

1. Jonas, H. (1979). *The Imperative of Responsibility*. University of Chicago Press.
2. Rawls, J. (1971). *A Theory of Justice*. Harvard University Press.
3. Mill, J.S. (1863). *Utilitarianism*. Parker, Son & Bourn.
4. Forrester, J.W. (1961). *Industrial Dynamics*. MIT Press.
5. Federal Rules of Evidence. 28 U.S.C.
6. 18 U.S.C. § 1001 - False Statements
7. 18 U.S.C. § 1519 - Destruction of Records
8. EU AI Act (2024). Regulation on Artificial Intelligence.
9. NIST AI Risk Management Framework (2023).

---

**Creator:** Lev Goukassian (ORCID: 0009-0006-5966-1243)  
**Framework:** Ternary Moral Logic (TML)  
**Repository:** https://github.com/FractonicMind/TernaryMoralLogic  
**Contact:** leogouk@gmail.com

---

*"The Sacred Pause is the heartbeat. SPRL is the pulse of that heartbeat. Together, they keep AI human."*
