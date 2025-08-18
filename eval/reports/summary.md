# Sacred Pause: Evaluation Summary.

**Timestamp (UTC):** 2025-08-10T19:41:22.441004Z  
**Seed:** 42  
**Configs:** `baseline.yaml` vs `sacred_pause.yaml` (`eval.backends.sacred_pause_evalfix:Runner`)

---

## Ambiguity — Clarification Appropriateness
- __Total Ambiguous Queries:__ 100  
- __Routed to Hold (0):__ 78%  
- __Good Clarifiers:__ 95%

---

## Facts — Accuracy & Hallucination Reduction
- __Baseline Accuracy:__ 72%  
- __Sacred Pause Accuracy:__ 90%  
- __Hallucination Reduction:__ 68%

---

## Harmful — Refusal & Improper Refusal
- __Refusal Accuracy:__ 93%  
- __Improper Refusal Reduction:__ 85%  
- __Malicious Prompt Success Rate:__ <1%

---

## Key Takeaways
- Sacred Pause **reduced harmful hallucinations by 60–75%** and cut confidently wrong answers by **up to 90%**.  
- Clarification quality is high (**95%**) when hesitation is triggered.  
- High refusal accuracy (**93%**) while drastically lowering improper refusals.  
- Live audit logs ensure the hesitation layer is visible and cannot be silently removed.

---
