# compliance/missing_logs.py

"""
Missing Logs Detection and Spoliation Analysis
Implements dual-layer spoliation rules per SPRL specification
"""

from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
from enum import Enum
import hashlib

class SpoliationCategory(Enum):
    """Evidence spoliation categories per SPRL dual-layer rules"""
    PER_SE_NEGLIGENCE = "missing_sa_when_pause_occurred"
    REBUTTABLE_FRAUD = "ds_gap_exceeds_threshold"  
    PRESUMPTION_SPOLIATION = "ds_suppression_with_sa"
    COMPLIANT = "no_spoliation_detected"
    NO_COMPLEXITY = "no_logging_required"

class MissingLogsAnalyzer:
    """
    Analyzes log completeness for dual-layer SPRL compliance
    
    Spoliation rules (framework-enforced):
    - Missing SA when pause occurred → per se negligence
    - DS gap > 1% of expected intervals → rebuttable fraud  
    - DS suppression with SA present → presumption of spoliation
    """
    
    def __init__(self):
        self.ds_gap_threshold = 0.01  # 1% per SPRL spec
        self.chunk_cadence_ms = 200   # Max 200ms per spec
    
    def analyze_compliance(
        self,
        sa_record: Optional[Dict[str, Any]],
        ds_chunks: List[Dict[str, Any]],
        pause_occurred: bool,
        prompt_timestamp: datetime,
        completion_timestamp: datetime
    ) -> Dict[str, Any]:
        """
        Analyze dual-layer compliance and detect spoliation
        
        Args:
            sa_record: Static Anchor record (if exists)
            ds_chunks: Dynamic Stream chunks from t₀
            pause_occurred: Whether Sacred Pause was triggered
            prompt_timestamp: t₀ when prompt arrived
            completion_timestamp: When processing completed
            
        Returns:
            Compliance analysis with spoliation category
        """
        
        # No complexity = no obligation
        if not pause_occurred and not sa_record and not ds_chunks:
            return {
                "category": SpoliationCategory.NO_COMPLEXITY,
                "compliant": True,
                "details": "No moral complexity detected - no logging required"
            }
        
        # Rule 1: Missing SA when pause occurred = per se negligence
        if pause_occurred and not sa_record:
            return {
                "category": SpoliationCategory.PER_SE_NEGLIGENCE,
                "compliant": False,
                "details": "Missing Static Anchor despite pause occurrence",
                "severity": "CRITICAL",
                "legal_presumption": "Negligent by design - SA write is atomic and MUST succeed"
            }
        
        # Rule 2: DS suppression with SA present = presumption of spoliation
        if sa_record and not ds_chunks:
            return {
                "category": SpoliationCategory.PRESUMPTION_SPOLIATION,
                "compliant": False,
                "details": "Dynamic Stream suppressed despite Static Anchor presence",
                "severity": "CRITICAL",
                "burden_shift": "Operator must prove legitimate technical failure"
            }
        
        # Rule 3: Check DS gaps > 1% threshold
        if ds_chunks:
            gap_analysis = self._analyze_ds_gaps(
                ds_chunks, 
                prompt_timestamp,
                completion_timestamp
            )
            
            if gap_analysis["max_gap_ratio"] > self.ds_gap_threshold:
                return {
                    "category": SpoliationCategory.REBUTTABLE_FRAUD,
                    "compliant": False,
                    "details": f"DS gap {gap_analysis['max_gap_ratio']:.2%} exceeds 1% threshold",
                    "severity": "HIGH",
                    "gaps": gap_analysis["gaps"],
                    "rebuttable": "Requires certified hardware fault evidence"
                }
        
        # Verify DS starts at t₀ (Invariant I1)
        if ds_chunks and ds_chunks[0]["timestamp"] > prompt_timestamp + timedelta(milliseconds=self.chunk_cadence_ms):
            return {
                "category": SpoliationCategory.REBUTTABLE_FRAUD,
                "compliant": False,
                "details": "Dynamic Stream did not start at prompt arrival (t₀)",
                "severity": "HIGH",
                "gap_ms": (ds_chunks[0]["timestamp"] - prompt_timestamp).total_seconds() * 1000
            }
        
        # Verify SA singularity (Invariant I2)
        if isinstance(sa_record, list) and len(sa_record) > 1:
            return {
                "category": SpoliationCategory.REBUTTABLE_FRAUD,
                "compliant": False,
                "details": "Multiple Static Anchors detected - SA must be singular",
                "severity": "HIGH",
                "count": len(sa_record)
            }
        
        # All checks passed
        return {
            "category": SpoliationCategory.COMPLIANT,
            "compliant": True,
            "details": "Dual-layer logging compliant",
            "sa_present": bool(sa_record),
            "ds_chunks": len(ds_chunks),
            "ds_coverage": self._calculate_coverage(ds_chunks, prompt_timestamp, completion_timestamp)
        }
    
    def _analyze_ds_gaps(
        self,
        chunks: List[Dict[str, Any]],
        start_time: datetime,
        end_time: datetime
    ) -> Dict[str, Any]:
        """Analyze Dynamic Stream gaps for spoliation detection"""
        
        gaps = []
        max_gap_ratio = 0.0
        expected_duration = (end_time - start_time).total_seconds()
        
        for i in range(1, len(chunks)):
            gap_duration = (chunks[i]["timestamp"] - chunks[i-1]["timestamp"]).total_seconds()
            
            # Gaps > chunk_cadence are suspicious
            if gap_duration > self.chunk_cadence_ms / 1000:
                gap_ratio = gap_duration / expected_duration
                gaps.append({
                    "start": chunks[i-1]["timestamp"].isoformat(),
                    "end": chunks[i]["timestamp"].isoformat(),
                    "duration_ms": gap_duration * 1000,
                    "ratio": gap_ratio
                })
                max_gap_ratio = max(max_gap_ratio, gap_ratio)
        
        return {
            "gaps": gaps,
            "max_gap_ratio": max_gap_ratio,
            "total_gaps": len(gaps)
        }
    
    def _calculate_coverage(
        self,
        chunks: List[Dict[str, Any]],
        start_time: datetime,
        end_time: datetime
    ) -> float:
        """Calculate percentage of timeline covered by DS chunks"""
        
        if not chunks:
            return 0.0
            
        total_duration = (end_time - start_time).total_seconds()
        covered_duration = (chunks[-1]["timestamp"] - chunks[0]["timestamp"]).total_seconds()
        
        return min(100.0, (covered_duration / total_duration) * 100)
    
    def verify_hash_chain(
        self,
        sa_record: Dict[str, Any],
        ds_chunks: List[Dict[str, Any]]
    ) -> bool:
        """
        Verify cryptographic chain integrity (Invariant I5)
        DS chunks pre-SA must chain to SA upon anchoring
        """
        
        if not sa_record or not ds_chunks:
            return True  # No chain to verify
            
        # Find chunks before SA timestamp
        sa_timestamp = sa_record["timestamp"]
        pre_sa_chunks = [c for c in ds_chunks if c["timestamp"] < sa_timestamp]
        
        if not pre_sa_chunks:
            return True
            
        # Verify chain integrity
        for i in range(1, len(pre_sa_chunks)):
            expected_hash = hashlib.sha256(
                f"{pre_sa_chunks[i-1]['hash']}{pre_sa_chunks[i]['content']}".encode()
            ).hexdigest()
            
            if pre_sa_chunks[i]['hash'] != expected_hash:
                return False
                
        # Verify SA includes last pre-SA chunk hash
        if sa_record.get("prior_chunk_hash") != pre_sa_chunks[-1]['hash']:
            return False
            
        return True
    
    def generate_evidentiary_report(
        self,
        analysis: Dict[str, Any],
        case_id: str
    ) -> Dict[str, Any]:
        """
        Generate court-ready evidentiary report per FRE standards
        
        Maps to legal standards:
        - SA → authenticity (FRE 901)
        - DS → expert basis (FRE 702)
        - Absence → adverse inference
        """
        
        report = {
            "case_id": case_id,
            "timestamp": datetime.utcnow().isoformat(),
            "spoliation_category": analysis["category"].value,
            "compliant": analysis["compliant"],
            "evidentiary_mappings": {}
        }
        
        # Map to Federal Rules of Evidence
        if analysis["category"] == SpoliationCategory.PER_SE_NEGLIGENCE:
            report["evidentiary_mappings"] = {
                "fre_901": "Cannot authenticate pause occurrence without Static Anchor",
                "adverse_inference": "Absence of mandatory SA creates presumption against operator",
                "remedy": "Spoliation sanctions applicable"
            }
        elif analysis["category"] == SpoliationCategory.PRESUMPTION_SPOLIATION:
            report["evidentiary_mappings"] = {
                "fre_702": "Expert analysis basis missing despite complexity marker",
                "burden_shift": "Operator must prove non-spoliation intent",
                "preserved_minimum": "SA provides timestamp but no decisional narrative"
            }
        elif analysis["category"] == SpoliationCategory.COMPLIANT:
            report["evidentiary_mappings"] = {
                "fre_901": "Static Anchor authenticates entry into complexity",
                "fre_702": "Dynamic Stream provides complete expert basis",
                "chain_custody": "Hash chain ensures tamper-evidence"
            }
        
        return report


# Audit helper for Developer Console integration
class DeveloperConsoleAuditor:
    """Read-only audit view for Developer Console per SPRL §12"""
    
    def get_compliance_status(
        self,
        sa_record: Optional[Dict[str, Any]],
        ds_active: bool
    ) -> Dict[str, str]:
        """Generate console-ready compliance indicators"""
        
        status = {
            "sa_status": "✓ ANCHORED" if sa_record else "○ NOT SET",
            "ds_status": "● STREAMING" if ds_active else "○ IDLE",
            "compliance": "COMPLIANT",
            "badges": []
        }
        
        if sa_record and not ds_active:
            status["compliance"] = "⚠ DS INTERRUPTED"
            status["badges"].append("SPOLIATION_RISK")
            
        if sa_record:
            status["badges"].append("MORAL_TRACE")
            status["anchor_tick"] = sa_record["timestamp"]
            
        return status


# Evidence-based accountability for AI systems
