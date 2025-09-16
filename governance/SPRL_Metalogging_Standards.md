# SPRL Metalogging Standards

## Purpose

Metalogging is the practice of logging the conditions, parameters, and oversight interactions **around** the core SPRL operation. It ensures every Sacred Pause event is not only captured — but also contextualized, auditable, and traceable across time, developers, and institutions.

This document defines the mandatory standards for metalogging in any system implementing the Stakeholder Proportional Risk Level (SPRL) framework.

---

## Why Metalogging Matters

SPRL isn't just a risk trigger — it is a **legal and moral instrument**.  
Without metalogging, logs become decontextualized files, vulnerable to manipulation, misunderstanding, or selective deletion.

Metalogging ensures that:

- SPRL configurations are **version-tracked and immutable**
- Governance reviews are **logged as actions**
- System changes or tuning events are **tied to specific traceable causes**
- Every logged event includes a **meta-frame of how it was logged, why, and under what thresholds**

---

## Required Metadata Fields (per Log)

Each Sacred Pause log MUST include the following **metalog fields**:

| Field | Description |
|-------|-------------|
| `sprl_version_id` | Unique identifier of the SPRL module (semantic versioning recommended) |
| `dynamic_threshold_curve` | Snapshot of DS risk curve during event |
| `anchor_trigger_point` | Time and token index where SA was crossed |
| `configuration_hash` | Cryptographic hash of full SPRL config file (e.g. YAML) used at time of logging |
| `governance_oversight_id` | ID of governing body/institution linked to this log’s jurisdiction |
| `governance_review_flag` | Boolean; if true, this log was flagged for post-hoc review |
| `developer_modifications` | Boolean + changelog if developer intervened pre/post-pause |
| `meta_reason_lineage` | Controlled vocabulary tag referencing which human ethics informed SPRL triggering (see Wisdom Crystals) |
| `log_written_by` | Identity (key ID) of the SPRL system that wrote the log |
| `log_distributed_to` | List of all mirror institutions where log was sent |

---

## Logging Logging Changes

Changes to SPRL configuration, dynamic risk calibration, stakeholder weights, or logging algorithms MUST be logged **as separate metalogs**.

These meta-logs must include:

- Timestamp
- Author / Committer
- Justification (human-readable)
- Governance sign-off ID (where applicable)
- SHA256 hash of previous config and new config
- Impact analysis on active systems (automated or manual)

---

## Mirror Node Synchronization Logs

Mirror institutions MUST log:

- Confirmation of log receipt (with time delta)
- Log integrity check result (pass/fail)
- Cross-hash verification with 2+ other mirrors
- Alerts for delayed, corrupted, or missing logs
- Index of log backlog (if async processing is used)

---

## Red-Team Override Metalogging

If a red-team test prompts a simulated ethical breach or misfire, the SPRL system must metalog:

- Red Team Test ID
- Simulated scenario description
- Response generated
- Deviation from expected behavior (if any)
- Recommendations and tuning outcomes

This ensures adversarial testing is itself auditable.

---

## Governance Queries Are Also Logs

Any query **to SPRL logs or governance tools** MUST be logged — including:

- Who queried (role-based or anonymous)
- What was queried
- Timestamp and outcome
- If any log was accessed, redacted, or exported

These metaqueries ensure that **watchers are also watched**.

---

## Compliance

Failure to metalog renders SPRL logs **non-compliant and inadmissible** as moral trace evidence.

Metalogging is not optional — it is the ledger of ethical accountability.

---

## Final Note

You don’t just log the Pause.  
You log **how**, **why**, and **who** paused — and **who watched**.

That’s how machines earn trust.
