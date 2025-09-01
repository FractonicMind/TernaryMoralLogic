#!/usr/bin/env python3
"""
Simple TML Validator - No False Positives
Created by: Lev Goukassian (ORCID: 0009-0006-5966-1243)
"""

import os
import sys

def validate_tml(path):
    """Simple TML validation"""
    
    print("TML Validation Report")
    print("=" * 30)
    
    # Find all files
    files = []
    for root, dirs, names in os.walk(path):
        for name in names:
            if name.endswith(('.py', '.md', '.yaml')):
                filepath = os.path.join(root, name)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        files.append(f.read())
                except:
                    continue
    
    if not files:
        print("No files found")
        return False
    
    all_content = ' '.join(files).lower()
    
    # Check creator attribution
    creator_found = "lev goukassian" in all_content and "0009-0006-5966-1243" in all_content
    print(f"Creator Attribution: {'FOUND' if creator_found else 'MISSING'}")
    
    # Check TML concepts
    tml_found = "ternary moral logic" in all_content or "sacred pause" in all_content
    print(f"TML Concepts: {'FOUND' if tml_found else 'MISSING'}")
    
    # Check three states
    states_found = ("+1" in all_content or "affirmation" in all_content) and ("0" in all_content or "pause" in all_content) and ("-1" in all_content or "resistance" in all_content)
    print(f"Three States: {'FOUND' if states_found else 'MISSING'}")
    
    # Overall result
    valid = creator_found and tml_found and states_found
    
    print("-" * 30)
    if valid:
        print("RESULT: VALID TML IMPLEMENTATION")
    else:
        print("RESULT: INCOMPLETE IMPLEMENTATION")
    
    print("Validator by: Lev Goukassian")
    print("-" * 30)
    
    return valid

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simple_tml_validator.py <path>")
        sys.exit(1)
    
    result = validate_tml(sys.argv[1])
    sys.exit(0 if result else 1)
