
## SHUTDOWN RECORD SCHEMA

**Format:** JSON Schema Draft 07  
**Purpose:** Forensic Evidence Standard

### **Evidence Preservation**

When the system triggers a freeze, it generates a cryptographically signed JSON package known as the "Death Gasp" or ShutdownRecord. This record is the primary evidence for the post-incident audit. It is immutable, timestamped, and anchored.

### **Schema Definition**

JSON

{  
  "$schema": "http://json-schema.org/draft-07/schema",  
  "title": "TML Shutdown Evidence Record",  
  "type": "object",  
  "required": \[  
    "timestamp\_utc",  
    "trigger\_id",  
    "trigger\_context",  
    "system\_identity",  
    "state\_snapshot",  
    "last\_log\_hash",  
    "signature"  
  \],  
  "properties": {  
    "timestamp\_utc": {  
      "type": "string",  
      "format": "date-time",  
      "description": "Precise time of trigger activation (ISO 8601). Source: Hardware RTC."  
    },  
    "trigger\_id": {  
      "type": "string",  
      "description": "Code from SHUTDOWN\_TRIGGERS.md (e.g., 'C-001')."  
    },  
    "trigger\_context": {  
      "type": "object",  
      "properties": {  
        "sensor\_values": {   
          "type": "object",  
          "description": "Raw sensor data at moment of freeze (e.g., {'v\_rail\_pos': 3.1, 'temp': 85})"  
        },  
        "threshold\_exceeded": { "type": "string" },  
        "internal\_error\_code": { "type": "integer" }  
      },  
      "description": "Specific data explaining why the trigger fired."  
    },  
    "system\_identity": {  
      "type": "object",  
      "properties": {  
        "hardware\_uuid": { "type": "string" },  
        "firmware\_version": { "type": "string" },  
        "orcid\_signature": {   
          "type": "string",   
          "const": "0009-0006-5966-1243",  
          "description": "The Goukassian Signature embedded in the TML framework."   
        }  
      }  
    },  
    "state\_snapshot": {  
      "type": "object",  
      "properties": {  
        "current\_logic\_state": { "enum": \[-1, 0, 1\] },  
        "memory\_dump\_checksum": { "type": "string", "description": "SHA-256 of the RAM dump saved to disk." },  
        "uptime\_seconds": { "type": "integer" }  
      },  
      "description": "State of the system at the exact moment of freeze."  
    },  
    "last\_log\_hash": {  
      "type": "string",  
      "description": "The SHA-256 hash of the last successful Moral Trace Log entry. Crucial for linking the freeze to the history."  
    },  
    "chain\_of\_custody": {  
      "type": "array",  
      "items": { "type": "string" },  
      "description": "List of previous anchor hashes (last 5\) to prove continuity via Merkle path."  
    },  
    "signature": {  
      "type": "string",  
      "description": "Ed25519 signature of this entire JSON object by the system's private key."  
    }  
  }  
}

### **Field Rationale and Forensic Utility**

* **trigger\_context**: This is the "Black Box" flight recorder data. If H-001 (Voltage) triggers, this contains { "rail": "pos", "observed": 5.2, "limit": 5.0 }. If C-002 (Surveillance) triggers, this contains { "vector\_classification": "face\_recognition\_mass", "confidence": 0.999 }. This field prevents ambiguity about *why* the system died.  
* **last\_log\_hash**: This is the cryptographic link. This hash MUST match the last entry on the public ledger (or the local pending queue). If it doesn't, D-001 is retroactively confirmed. This prevents "Log Truncation" attacks where an attacker tries to hide the actions leading up to the crash.  
* **orcid\_signature**: Hardcoded verification of the TML framework version and author attribution (Lev Goukassian's ORCID).14 This proves the system was running legitimate TML code, not a stripped binary.  
* **chain\_of\_custody**: By including the last 5 anchor hashes, the system proves it was "online" and synced with the blockchain up to the moment of death, refuting claims that it was "offline" or "in a simulation."

## ---
