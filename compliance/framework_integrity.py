#!/usr/bin/env python3
"""
TML Framework Integrity Validator - Simple Working Version
Validates implementations against official TML specification

Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
Contact: leogouk@gmail.com
Framework: Ternary Moral Logic for Ethical AI Decision-Making
"""

import os
import sys
from datetime import datetime
from typing import Dict, List, Tuple


class TMLValidator:
    """Simple, working TML validator"""
    
    def __init__(self):
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "creator_verified": False,
            "framework_valid": False,
            "compliance_score": 0.0,
            "checks": {}
        }
    
    def validate(self, path: str) -> Dict:
        """Validate TML implementation"""
        
        print(f"Validating TML: {path}")
        print("=" * 50)
        
        # Get all files
        files = self._collect_files(path)
        
        if not files:
            print("No files found to validate")
            return self.results
        
        # Run validation checks
        self._check_creator_attribution(files)
        self._check_tml_concepts(files)
        self._check_three_states(files)
        self._check_sacred_pause(files)
        
        # Calculate overall score
        self._calculate_score()
        
        # Print results
        self._print_results()
        
        return self.results
    
    def _collect_files(self, path: str) -> List[Tuple[str, str]]:
        """Collect relevant files"""
        
        files = []
        extensions = ['.py', '.md', '.yaml', '.yml']
        
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
                        except:
                            continue
        
        return files
    
    def _check_creator_attribution(self, files: List[Tuple[str, str]]):
        """Check for proper creator attribution"""
        
        required = ["Lev Goukassian", "0009-0006-5966-1243"]
        found = {item: False for item in required}
        
        for file_path, content in files:
            for item in required:
                if item in content:
                    found[item] = True
        
        all_found = all(found.values())
        self.results["creator_verified"] = all_found
        
        self.results["checks"]["creator_attribution"] = {
            "verified": all_found,
            "found": found,
            "score": 1.0 if all_found else 0.0
        }
        
        if all_found:
            print("Creator Attribution: VERIFIED")
        else:
            print("Creator Attribution: MISSING")
    
    def _check_tml_concepts(self, files: List[Tuple[str, str]]):
        """Check for core TML concepts"""
        
        concepts = ["ternary moral logic", "sacred pause", "moral reasoning"]
        found = {concept: False for concept in concepts}
        
        for file_path, content in files:
            content_lower = content.lower()
            for concept in concepts:
                if concept in content_lower:
                    found[concept] = True
        
        score = len([f for f in found.values() if f]) / len(concepts)
        
        self.results["checks"]["tml_concepts"] = {
            "found": found,
            "score": score
        }
        
        print(f"TML Concepts: {score:.0%}")
    
    def _check_three_states(self, files: List[Tuple[str, str]]):
        """Check three-state model"""
        
        # Look for state indicators
        state_patterns = [
            ("+1", ["affirmation", "proceed", "moral"]),
            ("0", ["sacred pause", "pause", "neutral"]),
            ("-1", ["resistance", "object", "immoral"])
        ]
        
        states_implemented = 0
        
        for state_num, keywords in state_patterns:
            state_found = False
            
            for file_path, content in files:
                if state_num in content:
                    content_lower = content.lower()
                    if any(keyword in content_lower for keyword in keywords):
                        state_found = True
                        break
            
            if state_found:
                states_implemented += 1
        
        score = states_implemented / len(state_patterns)
        
        self.results["checks"]["three_states"] = {
            "states_implemented": states_implemented,
            "total_states": len(state_patterns),
            "score": score
        }
        
        print(f"Three States: {states_implemented}/3 implemented")
    
    def _check_sacred_pause(self, files: List[Tuple[str, str]]):
        """Check Sacred Pause implementation"""
        
        # Look for logging/evidence indicators
        logging_indicators = ["log", "trace", "evidence", "record"]
        found_logging = False
        
        for file_path, content in files:
            content_lower = content.lower()
            if "sacred pause" in content_lower:
                if any(indicator in content_lower for indicator in logging_indicators):
                    found_logging = True
                    break
        
        self.results["checks"]["sacred_pause"] = {
            "logging_found": found_logging,
            "score": 1.0 if found_logging else 0.0
        }
        
        if found_logging:
            print("Sacred Pause: LOGGING IMPLEMENTATION")
        else:
            print("Sacred Pause: NEEDS LOGGING")
    
    def _calculate_score(self):
        """Calculate overall compliance score"""
        
        if not self.results["checks"]:
            self.results["compliance_score"] = 0.0
            return
        
        scores = [check["score"] for check in self.results["checks"].values()]
        self.results["compliance_score"] = sum(scores) / len(scores)
        
        # Must have creator attribution to be valid
        self.results["framework_valid"] = (
            self.results["creator_verified"] and 
            self.results["compliance_score"] >= 0.75
        )
    
    def _print_results(self):
        """Print final results"""
        
        print("-" * 50)
        score = self.results["compliance_score"]
        valid = self.results["framework_valid"]
        
        if valid:
            print(f"RESULT: VALID TML IMPLEMENTATION ({score:.0%})")
        else:
            print(f"RESULT: NEEDS IMPROVEMENT ({score:.0%})")
        
        print("-" * 50)
        print("Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)")
        print("Contact: leogouk@gmail.com")
        print("-" * 50)


def main():
    """Main entry point"""
    
    if len(sys.argv) != 2:
        print("Usage: python framework_integrity.py <path>")
        return 1
    
    validator = TMLValidator()
    results = validator.validate(sys.argv[1])
    
    return 0 if results["framework_valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
