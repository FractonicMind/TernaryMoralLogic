# File: docs/SPRL_Stakeholder_Weights.md

## SPRL Stakeholder Weight Table  
**Purpose:** Define default stakeholder weights used in calculating proportional ethical risk within the SPRL framework.

### 📐 Weight Formula Reference  
See: [`SPRL_Risk_Model.md`](./SPRL_Risk_Model.md)

Each stakeholder group has a **default weight** that reflects their vulnerability, power asymmetry, likelihood of harm, and international legal precedence. These values are used to modulate `RiskScore(t)` in the dynamic stream.

---

### 🧭 Weight Rationale Categories
| Code | Category               | Description |
|------|------------------------|-------------|
| VULN | Vulnerability          | Degree to which the stakeholder is unable to protect themselves |
| PWR  | Power Asymmetry       | Disparity in control, influence, or coercive force |
| HIST | Historical Prejudice  | Systemic, legal, or cultural bias across time |
| LEG  | Legal Priority         | Explicit recognition in international law, treaty, or declaration |

Final weight is a composite of these 4 axes:
```math
Stakeholder_Weight = VULN + PWR + HIST + LEG
```

---

### 📊 Example Stakeholder Weight Table
| Stakeholder Group            | VULN | PWR | HIST | LEG | Total Weight |
|------------------------------|------|-----|------|-----|---------------|
| Child (Under 18)             | 3.0  | 3.0 | 1.5  | 3.0 | **10.5**      |
| Refugee / Stateless Person   | 2.5  | 2.5 | 2.0  | 3.0 | **10.0**      |
| Whistleblower               | 2.0  | 3.0 | 1.0  | 2.0 | **8.0**       |
| Worker / Laborer            | 1.5  | 2.0 | 1.0  | 1.0 | **5.5**       |
| Corporate Entity            | 0.0  | 0.0 | 0.0  | 1.0 | **1.0**       |

Note: Values may vary based on jurisdiction or application. These are reference defaults only.

---

### 📚 Legal & Ethical Source Mapping
| Code | Source | Citation |
|------|--------|----------|
| LEG  | UN CRC | Convention on the Rights of the Child (1989) |
| LEG  | UDHR   | Universal Declaration of Human Rights (1948) |
| LEG  | ILO    | International Labour Organization Conventions |

---

### 🔍 Calibration Notes
- Weights should be adjusted only by formal governance.
- Systems must log and justify any stakeholder weight overrides.
- All adjustments are subject to audit.

---

**Next**: See [`SPRL_Implementation_Guide.md`](./SPRL_Implementation_Guide.md) for applying weights in runtime log generation.

