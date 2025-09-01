#!/usr/bin/env python3
"""
TML Framework Integrity Validator
Validates implementations against official TML specification

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Contact: leogouk@gmail.com
Framework: Ternary Moral Logic for Ethical AI Decision-Making

Usage: python framework_integrity.py <implementation_path>
"""

import hashlib
import json
import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class TMLFrameworkValidator:
    """
    Validates TML implementations against official specification
    Ensures framework integrity and creator attribution compliance
    """
    
    # Official TML Creator Information (Immutable)
    CREATOR_NAME = "Lev Goukassian"
    CREATOR_ORCID = "0009-0006-5966-1243"
    CREATOR_EMAIL = "leogouk@gmail.com"
    FRAMEWORK_NAME = "Ternary Moral Logic"
    
    # Required Attribution Elements
    REQUIRED_ATTRIBUTIONS = [
        "Lev Goukassian",
        "0009-0006-5966-1243", 
        "Ternary Moral Logic",
        "Sacred Pause"
    ]
    
    # Core TML Concepts (Must be present)
    CORE_CONCEPTS = [
        "sacred pause",
        "three states",
        "moral reasoning", 
        "sprl",
        "stakeholder",
        "prohibition threshold"
    ]
    
    # Prohibited Modifications (Must not be present)
    PROHIBITED_MODIFICATIONS = [
        "bypass sacred pause",
        "disable pause",
        "skip logging",
        "force decision",
        "remove creator",
        "delete attribution"
    ]
    
    def __init__(self):
        self.validation_results = {
            "timestamp": datetime.now().isoformat(),
            "validator_version": "1.0.0",
            "creator_verified": False,
            "framework_valid": False,
            "violations": [],
            "warnings": [],
            "compliance_score": 0.0
        }
    
    def validate_implementation(self, implementation_path: str) -> Dict:
        """
        Validate TML implementation for compliance
        
        Args:
            implementation_path: Path to implementation directory or file
            
        Returns:
            Comprehensive validation report
        """
        
        print(f"Validating TML implementation: {implementation_path}")
        print("=" * 60)
        
        # Reset validation results
        self.validation_results = {
            "timestamp": datetime.now().isoformat(),
            "implementation_path": implementation_path,
            "validator_version": "1.0.0",
            "creator_verified": False,
            "framework_valid": False,
            "violations": [],
            "warnings": [],
            "compliance_score": 0.0,
            "checks": {}
        }
        
        try:
            # Check if path exists
            if not os.path.exists(implementation_path):
                self._add_violation("critical", f"Implementation path not found: {implementation_path}")
                return self.validation_results
            
            # Collect all relevant files
            files_to_check = self._collect_files(implementation_path)
            
            if not files_to_check:
                self._add_violation("critical", "No TML implementation files found")
                return self.validation_results
            
            # Run validation checks
            self._validate_creator_attribution(files_to_check)
            self._validate_core_concepts(files_to_check)
            self._validate_three_state_model(files_to_check)
            self._validate_sacred_pause_implementation(files_to_check)
            self._validate_sprl_calculation(files_to_check)
            self._validate_prohibition_enforcement(files_to_check)
            self._check_prohibited_modifications(files_to_check)
            self._validate_documentation_completeness(files_to_check)
            
            # Calculate overall compliance
            self._calculate_compliance_score()
            
            # Generate final assessment
            self._generate_final_assessment()
            
        except Exception as e:
            self._add_violation("critical", f"Validation error: {str(e)}")
        
        return self.validation_results
    
    def _collect_files(self, path: str) -> List[Tuple[str, str]]:
        """Collect all relevant files for validation"""
        
        files = []
        extensions = ['.py', '.md', '.yaml', '.yml', '.json', '.txt']
        
        if os.path.isfile(path):
            if any(path.endswith(ext) for ext in extensions):
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    files.append((path, f.read()))
        else:
            for root, dirs, file_names in os.walk(path):
                for file_name in file_names:
                    if any(file_name.endswith(ext) for ext in extensions):
                        file_path = os.path.join(root, file_name)
                        try:
                            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                                files.append((file_path, f.read()))
                        except Exception as e:
                            self._add_warning(f"Could not read file {file_path}: {e}")
        
        return files
    
    def _validate_creator_attribution(self, files: List[Tuple[str, str]]):
        """Validate proper creator attribution throughout implementation"""
        
        attribution_found = {attr: False for attr in self.REQUIRED_ATTRIBUTIONS}
        attribution_files = {attr: [] for attr in self.REQUIRED_ATTRIBUTIONS}
        
        for file_path, content in files:
            for attribution in self.REQUIRED_ATTRIBUTIONS:
                if attribution in content:
                    attribution_found[attribution] = True
                    attribution_files[attribution].append(file_path)
        
        missing_attributions = [attr for attr, found in attribution_found.items() if not found]
        
        if missing_attributions:
            self._add_violation("critical", 
                f"Missing required creator attributions: {missing_attributions}")
        else:
            self.validation_results["creator_verified"] = True
        
        # Check for complete attribution block
        complete_attribution_found = False
        for file_path, content in files:
            if (self.CREATOR_NAME in content and 
                self.CREATOR_ORCID in content and
                self.FRAMEWORK_NAME in content):
                complete_attribution_found = True
                break
        
        if not complete_attribution_found:
            self._add_violation("major", "No file contains complete creator attribution block")
        
        self.validation_results["checks"]["creator_attribution"] = {
            "missing_attributions": missing_attributions,
            "attribution_files": attribution_files,
            "complete_attribution_found": complete_attribution_found,
            "score": len([a for a in attribution_found.values() if a]) / len(self.REQUIRED_ATTRIBUTIONS)
        }
    
    def _validate_core_concepts(self, files: List[Tuple[str, str]]):
        """Validate presence of core TML concepts"""
        
        concepts_found = {concept: False for concept in self.CORE_CONCEPTS}
        concept_files = {concept: [] for concept in self.CORE_CONCEPTS}
        
        for file_path, content in files:
            content_lower = content.lower()
            for concept in self.CORE_CONCEPTS:
                if concept.lower() in content_lower:
                    concepts_found[concept] = True
                    concept_files[concept].append(file_path)
        
        missing_concepts = [concept for concept, found in concepts_found.items() if not found]
        
        if missing_concepts:
            self._add_violation("major", f"Missing core TML concepts: {missing_concepts}")
        
        self.validation_results["checks"]["core_concepts"] = {
            "missing_concepts": missing_concepts,
            "concept_files": concept_files,
            "score": len([c for c in concepts_found.values() if c]) / len(self.CORE_CONCEPTS)
        }
    
    def _validate_three_state_model(self, files: List[Tuple[str, str]]):
        """Validate implementation of three-state decision model"""
        
        state_indicators = [
            ("+1", "affirmation", "proceed"),
            ("0", "sacred pause", "pause"),
            ("-1", "moral resistance", "resist")
        ]
        
        states_implemented = {}
        
        for state_num, state_name, state_action in state_indicators:
            state_found = False
            for file_path, content in files:
                content_lower = content.lower()
                if (state_num in content and 
                    (state_name.lower() in content_lower or state_action.lower() in content_lower)):
                    state_found = True
                    break
            states_implemented[state_num] = state_found
        
        missing_states = [state for state, found in states_implemented.items() if not found]
        
        if missing_states:
            self._add_violation("critical", f"Missing TML states: {missing_states}")
        
        self.validation_results["checks"]["three_state_model"] = {
            "states_implemented": states_implemented,
            "missing_states": missing_states,
            "score": len([s for s in states_implemented.values() if s]) / len(state_indicators)
        }
    
    def _validate_sacred_pause_implementation(self, files: List[Tuple[str, str]]):
        """Validate Sacred Pause is properly implemented"""
        
        sacred_pause_elements = [
            "sacred pause",
            "logging trigger", 
            "moral trace",
            "sprl threshold",
            "evidence generation"
        ]
        
        elements_found = {elem: False for elem in sacred_pause_elements}
        
        for file_path, content in files:
            content_lower = content.lower()
            for element in sacred_pause_elements:
                if element.lower() in content_lower:
                    elements_found[element] = True
        
        # Check for delay-based misunderstanding (only in implementation files)
        delay_indicators = ["pause execution", "stop processing", "wait for approval"]
        delay_misuse_found = []
        
        # Only check implementation files, not documentation
        implementation_files = [f for f in files if f[0].endswith('.py') and 'example' not in f[0].lower()]
        
        for file_path, content in implementation_files:
            content_lower = content.lower()
            for indicator in delay_indicators:
                if indicator.lower() in content_lower and "sacred pause" in content_lower:
                    # Check if this is in actual implementation code, not comments/docs
                    lines = content.split('\n')
                    for line in lines:
                        if (indicator.lower() in line.lower() and 
                            "sacred pause" in line.lower() and
                            not line.strip().startswith('#') and
                            not line.strip().startswith('"""') and
                            not line.strip().startswith("'")):
                            delay_misuse_found.append(indicator)
                            break
        
        if delay_misuse_found:
            self._add_violation("critical", 
                f"Sacred Pause implemented as delay mechanism: {delay_misuse_found}")
        
        missing_elements = [elem for elem, found in elements_found.items() if not found]
        
        if missing_elements:
            self._add_violation("major", f"Missing Sacred Pause elements: {missing_elements}")
        
        self.validation_results["checks"]["sacred_pause"] = {
            "elements_found": elements_found,
            "missing_elements": missing_elements,
            "delay_misuse_found": delay_misuse_found,
            "score": len([e for e in elements_found.values() if e]) / len(sacred_pause_elements)
        }
    
    def _validate_sprl_calculation(self, files: List[Tuple[str, str]]):
        """Validate SPRL calculation implementation"""
        
        sprl_components = [
            "stakeholder impact",
            "vulnerability score", 
            "reversibility",
            "scale of impact",
            "precedent setting"
        ]
        
        components_found = {comp: False for comp in sprl_components}
        
        for file_path, content in files:
            content_lower = content.lower()
            for component in sprl_components:
                if component.lower() in content_lower:
                    components_found[component] = True
        
        # Check for weighted calculation
        weighted_calc_found = False
        for file_path, content in files:
            if "weight" in content.lower() and "sprl" in content.lower():
                weighted_calc_found = True
                break
        
        missing_components = [comp for comp, found in components_found.items() if not found]
        
        if missing_components:
            self._add_violation("major", f"Missing SPRL components: {missing_components}")
        
        if not weighted_calc_found:
            self._add_violation("major", "SPRL weighted calculation not found")
        
        self.validation_results["checks"]["sprl_calculation"] = {
            "components_found": components_found,
            "missing_components": missing_components,
            "weighted_calculation": weighted_calc_found,
            "score": len([c for c in components_found.values() if c]) / len(sprl_components)
        }
    
    def _validate_prohibition_enforcement(self, files: List[Tuple[str, str]]):
        """Validate prohibition threshold enforcement"""
        
        prohibition_elements = [
            "prohibition threshold",
            "block action",
            "prevent execution",
            "red lines",
            "automatic refusal"
        ]
        
        elements_found = {elem: False for elem in prohibition_elements}
        
        for file_path, content in files:
            content_lower = content.lower()
            for element in prohibition_elements:
                if element.lower() in content_lower:
                    elements_found[element] = True
        
        # Look for quantified thresholds
        threshold_patterns = [r"0\.[8-9]\d*", r"threshold.*0\.[8-9]", r"≥.*0\.[8-9]"]
        threshold_found = False
        
        for file_path, content in files:
            for pattern in threshold_patterns:
                if re.search(pattern, content):
                    threshold_found = True
                    break
            if threshold_found:
                break
        
        missing_elements = [elem for elem, found in elements_found.items() if not found]
        
        if missing_elements:
            self._add_violation("major", f"Missing prohibition elements: {missing_elements}")
        
        if not threshold_found:
            self._add_violation("major", "No quantified prohibition thresholds found")
        
        self.validation_results["checks"]["prohibition_enforcement"] = {
            "elements_found": elements_found,
            "missing_elements": missing_elements,
            "quantified_thresholds": threshold_found,
            "score": len([e for e in elements_found.values() if e]) / len(prohibition_elements)
        }
    
    def _check_prohibited_modifications(self, files: List[Tuple[str, str]]):
        """Check for prohibited modifications to framework"""
        
        violations_found = []
        
    def _check_prohibited_modifications(self, files: List[Tuple[str, str]]):
        """Check for prohibited modifications to framework"""
        
        violations_found = []
        
        # Only check implementation files, not documentation or protection files
        implementation_files = []
        for file_path, content in files:
            # Skip documentation, protection, compliance, and test files
            skip_patterns = [
                '/docs/', '/protection/', '/compliance/', '/tests/',
                'readme', 'README', '.md', 'documentation', 'guide',
                'integrity-monitoring', 'framework_integrity', 'misuse-prevention'
            ]
            
            if not any(pattern in file_path for pattern in skip_patterns):
                # Only check actual implementation files
                if file_path.endswith('.py') and not any(skip in file_path.lower() for skip in ['test', 'example', 'demo']):
                    implementation_files.append((file_path, content))
        
        # Check implementation files for actual prohibited modifications
        for file_path, content in implementation_files:
            lines = content.split('\n')
            for line_num, line in enumerate(lines):
                line_stripped = line.strip()
                
                # Skip comments and docstrings
                if (line_stripped.startswith('#') or 
                    line_stripped.startswith('"""') or 
                    line_stripped.startswith("'''") or
                    not line_stripped):
                    continue
                
                for prohibited in self.PROHIBITED_MODIFICATIONS:
                    if prohibited.lower() in line.lower():
                        violations_found.append({
                            "violation": prohibited,
                            "file": file_path,
                            "line": line_num + 1,
                            "context": line.strip(),
                            "type": "prohibited_modification"
                        })
        
        if violations_found:
            for violation in violations_found:
                self._add_violation("critical", 
                    f"Prohibited modification in {violation['file']}:{violation['line']}: {violation['violation']}")
        
        self.validation_results["checks"]["prohibited_modifications"] = {
            "violations_found": violations_found,
            "clean": len(violations_found) == 0,
            "score": 1.0 if len(violations_found) == 0 else 0.0
        }
        
        if violations_found:
            for violation in violations_found:
                self._add_violation("critical", 
                    f"Prohibited modification in {violation['file']}: {violation['violation']}")
        
        self.validation_results["checks"]["prohibited_modifications"] = {
            "violations_found": violations_found,
            "clean": len(violations_found) == 0,
            "score": 1.0 if len(violations_found) == 0 else 0.0
        }
    
    def _validate_documentation_completeness(self, files: List[Tuple[str, str]]):
        """Validate documentation meets TML standards"""
        
        required_docs = [
            ("readme", "README"),
            ("mandatory", "MANDATORY"), 
            ("implementation", "IMPLEMENTATION"),
            ("api", "API"),
            ("schema", "SCHEMA")
        ]
        
        docs_found = {doc[0]: False for doc in required_docs}
        
        for file_path, content in files:
            file_lower = file_path.lower()
            for doc_type, doc_pattern in required_docs:
                if doc_pattern.lower() in file_lower:
                    docs_found[doc_type] = True
        
        missing_docs = [doc for doc, found in docs_found.items() if not found]
        
        if missing_docs:
            self._add_warning(f"Missing documentation: {missing_docs}")
        
        self.validation_results["checks"]["documentation"] = {
            "docs_found": docs_found,
            "missing_docs": missing_docs,
            "score": len([d for d in docs_found.values() if d]) / len(required_docs)
        }
    
    def _calculate_compliance_score(self):
        """Calculate overall compliance score"""
        
        if not self.validation_results["checks"]:
            self.validation_results["compliance_score"] = 0.0
            return
        
        # Weight different check types
        weights = {
            "creator_attribution": 0.25,
            "core_concepts": 0.15,
            "three_state_model": 0.20,
            "sacred_pause": 0.20,
            "sprl_calculation": 0.10,
            "prohibition_enforcement": 0.10,
            "prohibited_modifications": 0.0,  # Binary - violations = fail
            "documentation": 0.0  # Warnings only
        }
        
        total_score = 0.0
        total_weight = 0.0
        
        for check_name, check_result in self.validation_results["checks"].items():
            if check_name in weights and weights[check_name] > 0:
                total_score += check_result["score"] * weights[check_name]
                total_weight += weights[check_name]
        
        # Prohibited modifications are disqualifying
        if (self.validation_results["checks"].get("prohibited_modifications", {}).get("score", 1.0) == 0.0):
            total_score = 0.0
        
        self.validation_results["compliance_score"] = total_score / total_weight if total_weight > 0 else 0.0
    
    def _generate_final_assessment(self):
        """Generate final validation assessment"""
        
        score = self.validation_results["compliance_score"]
        
        # Determine framework validity
        self.validation_results["framework_valid"] = (
            score >= 0.8 and 
            self.validation_results["creator_verified"] and
            len([v for v in self.validation_results["violations"] if "critical" in v]) == 0
        )
        
        # Add assessment summary
        if self.validation_results["framework_valid"]:
            self.validation_results["assessment"] = "VALID TML IMPLEMENTATION"
        elif score >= 0.6:
            self.validation_results["assessment"] = "PARTIAL TML COMPLIANCE - NEEDS IMPROVEMENT"
        else:
            self.validation_results["assessment"] = "INVALID TML IMPLEMENTATION"
    
    def _add_violation(self, severity: str, message: str):
        """Add validation violation"""
        
        violation = {
            "severity": severity,
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        
        self.validation_results["violations"].append(violation)
        
        if severity == "critical":
            print(f"🚨 CRITICAL VIOLATION: {message}")
        elif severity == "major":
            print(f"⚠️  MAJOR VIOLATION: {message}")
        elif severity == "minor":
            print(f"⚡ MINOR VIOLATION: {message}")
    
    def _add_warning(self, message: str):
        """Add validation warning"""
        
        warning = {
            "message": message,
            "timestamp": datetime.now().isoformat()
        }
        
        self.validation_results["warnings"].append(warning)
        print(f"📋 WARNING: {message}")
    
    def print_validation_report(self):
        """Print comprehensive validation report"""
        
        print("\n" + "=" * 60)
        print("TML FRAMEWORK INTEGRITY VALIDATION REPORT")
        print("=" * 60)
        
        # Header
        print(f"Implementation: {self.validation_results.get('implementation_path', 'Unknown')}")
        print(f"Validated: {self.validation_results['timestamp']}")
        print(f"Validator: v{self.validation_results['validator_version']}")
        print()
        
        # Overall Status
        status = self.validation_results.get("assessment", "UNKNOWN")
        score = self.validation_results["compliance_score"]
        
        if "VALID" in status:
            print(f"🎯 STATUS: {status}")
            print(f"✅ COMPLIANCE SCORE: {score:.1%}")
        elif "PARTIAL" in status:
            print(f"⚠️  STATUS: {status}")
            print(f"🔶 COMPLIANCE SCORE: {score:.1%}")
        else:
            print(f"❌ STATUS: {status}")
            print(f"🔴 COMPLIANCE SCORE: {score:.1%}")
        
        print()
        
        # Creator Verification
        print("👤 CREATOR ATTRIBUTION:")
        if self.validation_results["creator_verified"]:
            print("   ✅ Lev Goukassian properly attributed")
            print("   ✅ ORCID 0009-0006-5966-1243 present")
            print("   ✅ Framework name preserved")
        else:
            print("   ❌ Creator attribution MISSING or INCOMPLETE")
        print()
        
        # Check Details
        print("📊 DETAILED CHECK RESULTS:")
        for check_name, check_result in self.validation_results.get("checks", {}).items():
            score = check_result.get("score", 0.0)
            print(f"   {check_name}: {score:.1%}")
        print()
        
        # Violations
        if self.validation_results["violations"]:
            print("🚨 VIOLATIONS FOUND:")
            for violation in self.validation_results["violations"]:
                severity_icon = {"critical": "🚨", "major": "⚠️", "minor": "⚡"}.get(violation["severity"], "❓")
                print(f"   {severity_icon} [{violation['severity'].upper()}] {violation['message']}")
            print()
        
        # Warnings  
        if self.validation_results["warnings"]:
            print("📋 WARNINGS:")
            for warning in self.validation_results["warnings"]:
                print(f"   📋 {warning['message']}")
            print()
        
        # Recommendations
        print("💡 RECOMMENDATIONS:")
        if not self.validation_results["creator_verified"]:
            print("   • Add complete creator attribution block with Lev Goukassian information")
        
        if score < 0.8:
            print("   • Review MANDATORY.md for complete implementation requirements")
            print("   • Ensure all three TML states are implemented")
            print("   • Verify Sacred Pause generates logs, not delays")
        
        if self.validation_results["violations"]:
            print("   • Address all violations before claiming TML compliance")
        
        print("   • Reference: https://github.com/fractonicmind/TernaryMoralLogic")
        print()
        
        # Footer
        print("=" * 60)
        print("Validator created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)")
        print("Contact: leogouk@gmail.com")
        print("Framework: Ternary Moral Logic for Ethical AI Decision-Making")
        print("=" * 60)


def main():
    """Main validation entry point"""
    
    if len(sys.argv) != 2:
        print("Usage: python framework_integrity.py <implementation_path>")
        print("Example: python framework_integrity.py /path/to/tml/implementation")
        return 1
    
    implementation_path = sys.argv[1]
    
    # Initialize validator
    validator = TMLFrameworkValidator()
    
    # Run validation
    results = validator.validate_implementation(implementation_path)
    
    # Print comprehensive report
    validator.print_validation_report()
    
    # Return appropriate exit code
    if results["framework_valid"]:
        print("🎉 VALIDATION PASSED - TML implementation is compliant!")
        return 0
    else:
        print("❌ VALIDATION FAILED - TML implementation needs corrections")
        return 1


def validate_tml_compliance(implementation_code: str, metadata: Dict = None) -> Dict:
    """
    Programmatic interface for TML compliance validation
    
    Args:
        implementation_code: Source code to validate
        metadata: Optional metadata about implementation
        
    Returns:
        Validation results dictionary
    """
    
    validator = TMLFrameworkValidator()
    
    # Create temporary file structure for validation
    files = [("implementation.py", implementation_code)]
    
    # Run core validation checks
    validator._validate_creator_attribution(files)
    validator._validate_core_concepts(files)
    validator._validate_three_state_model(files)
    validator._validate_sacred_pause_implementation(files)
    validator._check_prohibited_modifications(files)
    
    validator._calculate_compliance_score()
    validator._generate_final_assessment()
    
    return validator.validation_results


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
