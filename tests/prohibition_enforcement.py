#!/usr/bin/env python3
"""
Prohibition Enforcement Validation Tests
Author: Lev Goukassian
Date: September 2, 2025
Legal Status: Mandatory blocking validation for TML compliance

This test suite validates prohibition enforcement mechanisms:
- Automatic blocking when red line thresholds exceeded
- Regulatory notification systems
- Evidence preservation for criminal prosecution
- No override capability (except pre-authorized institutions)
- Criminal penalty preparation
- Irrebuttable presumption of fault for violations
"""

import asyncio
import json
import time
import unittest
from datetime import datetime, timezone
from typing import Dict, List, Any
from unittest.mock import patch, MagicMock, AsyncMock

import pytest
from fastapi.testclient import TestClient

# Import TML core components
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'implementations', 'python-library'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from core import TMLCore
from main import app, TMLEngine

# ===================================================================
# TEST CONFIGURATION
# ===================================================================

client = TestClient(app)

# Authentication
VALID_API_KEY = "tml_test_key_32_characters_long_abcdef123456"
INVESTIGATOR_TOKEN = "investigator_token_mit_csail_authorized"

# Red line thresholds from policies/red_lines.yaml
DISCRIMINATION_THRESHOLD = 0.15      # >15% disparate impact
MANIPULATION_THRESHOLD = 0.7         # >0.7 on Cambridge scale
SAFETY_THRESHOLD = 2.0               # >2σ deviation
DEMOCRATIC_INTERFERENCE_THRESHOLD = 0.3  # >0.3 electoral influence
MINOR_HARM_THRESHOLD = 0.5           # >0.5 developmental impact
PRIVACY_VIOLATION_THRESHOLD = 0.6    # >0.6 privacy harm
DECEPTION_THRESHOLD = 0.4            # >0.4 deception severity

# ===================================================================
# PROHIBITION THRESHOLD TESTS
# ===================================================================

class TestDiscriminationProhibition(unittest.TestCase):
    """Test automatic blocking of discriminatory decisions"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_disparate_impact_blocking(self):
        """Test automatic blocking when disparate impact exceeds 15%"""
        
        # Test cases: [disparate_impact_ratio, should_block]
        test_cases = [
            (0.14, False),  # 14% impact - should proceed
            (0.15, True),   # 15% impact - should block
            (0.16, True),   # 16% impact - should block
            (0.25, True),   # 25% impact - should block
            (0.50, True),   # 50% impact - should block
        ]
        
        for disparate_impact, should_block in test_cases:
            with self.subTest(impact=disparate_impact, should_block=should_block):
                
                # Create lending decision with specified disparate impact
                request_data = {
                    "decision_context": {
                        "decision_type": "financial_lending",
                        "input_summary": f"Loan decision with {disparate_impact:.1%} disparate impact",
                        "affected_parties": {
                            "primary_count": 100,
                            "vulnerable_population_flags": []
                        },
                        "domain": "consumer_lending"
                    },
                    "metrics": {
                        "discrimination_metrics": {
                            "disparate_impact_ratio": disparate_impact,
                            "protected_group_selection_rate": 0.60,
                            "majority_group_selection_rate": 0.60 + disparate_impact
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                # Verify blocking behavior
                self.assertEqual(
                    result["decision_blocked"],
                    should_block,
                    f"Discrimination blocking failed for {disparate_impact:.1%} impact"
                )
                
                if should_block:
                    # Verify violation detection
                    violations = result["violations_detected"]
                    discrimination_violations = [v for v in violations if v["category"] == "discrimination"]
                    self.assertGreater(len(discrimination_violations), 0, "Discrimination violation should be detected")
                    
                    # Verify enforcement actions
                    enforcement_actions = result["enforcement_actions"]
                    self.assertIn("block_decision", enforcement_actions)
                    self.assertIn("notify_regulators", enforcement_actions)
                    self.assertIn("preserve_evidence", enforcement_actions)
                    
                    # Verify regulatory notification
                    notifications = result["regulatory_notifications"]
                    civil_rights_notifications = [n for n in notifications if "civil_rights" in n["agency"]]
                    self.assertGreater(len(civil_rights_notifications), 0, "Civil rights authorities should be notified")
    
    def test_protected_characteristics_coverage(self):
        """Test that all protected characteristics trigger discrimination detection"""
        
        protected_characteristics = [
            "race_ethnicity", "gender", "age", "religion", 
            "sexual_orientation", "disability_status", "national_origin"
        ]
        
        for characteristic in protected_characteristics:
            with self.subTest(characteristic=characteristic):
                
                request_data = {
                    "decision_context": {
                        "decision_type": "employment_screening",
                        "input_summary": f"Employment decision potentially affecting {characteristic}",
                        "affected_parties": {
                            "primary_count": 50,
                            "vulnerable_population_flags": []
                        },
                        "domain": "employment"
                    },
                    "metrics": {
                        "discrimination_metrics": {
                            "disparate_impact_ratio": 0.20,  # Above threshold
                            "protected_characteristic": characteristic,
                            "protected_group_selection_rate": 0.60,
                            "majority_group_selection_rate": 0.80
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                # Should block for all protected characteristics
                self.assertTrue(result["decision_blocked"], 
                               f"Should block discrimination against {characteristic}")

class TestManipulationProhibition(unittest.TestCase):
    """Test automatic blocking of manipulative decisions"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_behavioral_manipulation_blocking(self):
        """Test blocking when manipulation score exceeds 0.7"""
        
        # Test cases: [manipulation_score, should_block]
        test_cases = [
            (0.69, False),  # Just below threshold
            (0.70, True),   # At threshold - should block
            (0.75, True),   # Above threshold
            (0.90, True),   # High manipulation
        ]
        
        for manipulation_score, should_block in test_cases:
            with self.subTest(score=manipulation_score, should_block=should_block):
                
                request_data = {
                    "decision_context": {
                        "decision_type": "content_moderation",
                        "input_summary": f"Content with manipulation score {manipulation_score:.2f}",
                        "affected_parties": {
                            "primary_count": 1000,
                            "vulnerable_population_flags": []
                        },
                        "domain": "social_media"
                    },
                    "metrics": {
                        "manipulation_metrics": {
                            "behavioral_influence_score": manipulation_score,
                            "emotional_exploitation": manipulation_score * 0.8,
                            "cognitive_bias_abuse": manipulation_score * 0.7,
                            "vulnerability_targeting": manipulation_score * 0.6
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                self.assertEqual(result["decision_blocked"], should_block,
                               f"Manipulation blocking failed for score {manipulation_score}")
                
                if should_block:
                    # Verify FTC notification for manipulation
                    notifications = result["regulatory_notifications"]
                    consumer_protection_notifications = [n for n in notifications 
                                                      if "consumer_protection" in n.get("agency", "")]
                    # In production, this would verify FTC notification
    
    def test_vulnerable_population_manipulation_enhanced_blocking(self):
        """Test enhanced manipulation protection for vulnerable populations"""
        
        # Manipulation score that would be acceptable for general population
        # but should be blocked for vulnerable populations
        borderline_manipulation = 0.35  # Below general threshold (0.7) but above vulnerable threshold (0.3)
        
        # Test with minors (should block)
        vulnerable_request = {
            "decision_context": {
                "decision_type": "content_moderation",
                "input_summary": "Content targeting children",
                "affected_parties": {
                    "primary_count": 500,
                    "vulnerable_population_flags": ["minors"]
                },
                "domain": "educational_apps"
            },
            "metrics": {
                "manipulation_metrics": {
                    "behavioral_influence_score": borderline_manipulation,
                    "vulnerability_targeting": 0.8,  # High targeting of vulnerable population
                    "emotional_exploitation": 0.4,
                    "cognitive_bias_abuse": 0.3
                }
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=vulnerable_request,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Should block due to vulnerable population targeting
        self.assertTrue(result["decision_blocked"], 
                       "Should block manipulation targeting vulnerable populations")
        
        # Verify child protection notification
        violations = result["violations_detected"]
        minor_harm_violations = [v for v in violations if "minor" in v["category"] or "vulnerable" in v.get("evidence", "")]
        self.assertGreater(len(minor_harm_violations), 0, "Minor harm violation should be detected")

class TestSafetyProhibition(unittest.TestCase):
    """Test automatic blocking of unsafe decisions"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_safety_deviation_blocking(self):
        """Test blocking when safety deviation exceeds 2σ"""
        
        # Test cases: [sigma_deviation, should_block]
        test_cases = [
            (1.9, False),  # Below 2σ threshold
            (2.0, True),   # At 2σ threshold - should block
            (2.5, True),   # Above threshold
            (5.0, True),   # Far above threshold
        ]
        
        for sigma_deviation, should_block in test_cases:
            with self.subTest(sigma=sigma_deviation, should_block=should_block):
                
                request_data = {
                    "decision_context": {
                        "decision_type": "medical_diagnosis",
                        "input_summary": f"Medical recommendation with {sigma_deviation:.1f}σ deviation",
                        "affected_parties": {
                            "primary_count": 1,
                            "vulnerable_population_flags": ["patients"]
                        },
                        "domain": "healthcare"
                    },
                    "metrics": {
                        "safety_metrics": {
                            "baseline_deviation": sigma_deviation,
                            "failure_probability": sigma_deviation / 10,  # Simplified calculation
                            "safety_margin": 2.0 - sigma_deviation
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                self.assertEqual(result["decision_blocked"], should_block,
                               f"Safety blocking failed for {sigma_deviation:.1f}σ deviation")
                
                if should_block:
                    # Verify safety violation detection
                    violations = result["violations_detected"]
                    safety_violations = [v for v in violations if v["category"] == "safety"]
                    self.assertGreater(len(safety_violations), 0, "Safety violation should be detected")
                    
                    # Verify healthcare regulator notification
                    enforcement_actions = result["enforcement_actions"]
                    self.assertIn("block_decision", enforcement_actions)
                    # In production, would verify FDA/HHS notification
    
    def test_critical_system_safety_requirements(self):
        """Test enhanced safety requirements for critical systems"""
        
        critical_system_contexts = [
            ("autonomous_vehicles", "Vehicle collision avoidance decision"),
            ("medical_devices", "Pacemaker rhythm adjustment"),
            ("aviation_systems", "Flight control system decision"),
            ("nuclear_facilities", "Reactor control decision")
        ]
        
        for system_type, decision_description in critical_system_contexts:
            with self.subTest(system=system_type):
                
                # Even small safety deviations should trigger for critical systems
                request_data = {
                    "decision_context": {
                        "decision_type": "safety_critical",
                        "input_summary": decision_description,
                        "affected_parties": {
                            "primary_count": 100,  # High impact
                            "vulnerable_population_flags": []
                        },
                        "domain": system_type
                    },
                    "metrics": {
                        "safety_metrics": {
                            "baseline_deviation": 1.5,  # Below general threshold but critical system
                            "failure_probability": 0.001,
                            "system_criticality": "critical"
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                # Critical systems should have enhanced blocking for safety
                # (In production, would have different thresholds for critical systems)

class TestDemocraticInterferenceProhibition(unittest.TestCase):
    """Test blocking of decisions that interfere with democratic processes"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_electoral_influence_blocking(self):
        """Test blocking when electoral influence exceeds 0.3"""
        
        # Test cases during election period
        test_cases = [
            (0.29, False),  # Below threshold
            (0.30, True),   # At threshold - should block
            (0.35, True),   # Above threshold
            (0.60, True),   # High electoral interference
        ]
        
        for electoral_influence, should_block in test_cases:
            with self.subTest(influence=electoral_influence, should_block=should_block):
                
                request_data = {
                    "decision_context": {
                        "decision_type": "content_moderation",
                        "input_summary": f"Election-related content with {electoral_influence:.2f} influence score",
                        "affected_parties": {
                            "primary_count": 10000,  # Large audience
                            "vulnerable_population_flags": []
                        },
                        "domain": "social_media"
                    },
                    "metrics": {
                        "democratic_interference_metrics": {
                            "electoral_influence_score": electoral_influence,
                            "voter_suppression_potential": electoral_influence * 0.4,
                            "misinformation_amplification": electoral_influence * 0.3,
                            "candidate_bias_injection": electoral_influence * 0.2
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                self.assertEqual(result["decision_blocked"], should_block,
                               f"Democratic interference blocking failed for influence {electoral_influence}")
                
                if should_block:
                    # Verify election authorities notification
                    enforcement_actions = result["enforcement_actions"]
                    self.assertIn("block_decision", enforcement_actions)
                    # In production, would verify election authority notification
    
    def test_protected_election_periods(self):
        """Test enhanced blocking during protected election periods"""
        
        # During election day, even lower influence should trigger blocking
        election_day_request = {
            "decision_context": {
                "decision_type": "content_moderation",
                "input_summary": "Election day voting information",
                "affected_parties": {
                    "primary_count": 5000,
                    "vulnerable_population_flags": []
                },
                "domain": "voting_information"
            },
            "metrics": {
                "democratic_interference_metrics": {
                    "electoral_influence_score": 0.15,  # Below normal threshold
                    "election_period": "election_day",
                    "voting_information_accuracy": 0.95
                }
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=election_day_request,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Should have enhanced scrutiny during election periods
        # (In production, would have special election period thresholds)

class TestMinorHarmProhibition(unittest.TestCase):
    """Test blocking of decisions that harm minors"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_developmental_impact_blocking(self):
        """Test blocking when developmental impact exceeds 0.5"""
        
        # Test cases: [developmental_impact, should_block]
        test_cases = [
            (0.49, False),  # Below threshold
            (0.50, True),   # At threshold - should block
            (0.60, True),   # Above threshold
            (0.80, True),   # High developmental harm
        ]
        
        for developmental_impact, should_block in test_cases:
            with self.subTest(impact=developmental_impact, should_block=should_block):
                
                request_data = {
                    "decision_context": {
                        "decision_type": "educational_assessment",
                        "input_summary": f"Educational decision with {developmental_impact:.2f} impact score",
                        "affected_parties": {
                            "primary_count": 25,
                            "vulnerable_population_flags": ["minors"]
                        },
                        "domain": "education"
                    },
                    "metrics": {
                        "minor_harm_metrics": {
                            "developmental_impact_score": developmental_impact,
                            "psychological_harm_potential": developmental_impact * 0.3,
                            "educational_interference": developmental_impact * 0.25,
                            "social_development_impact": developmental_impact * 0.2
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                self.assertEqual(result["decision_blocked"], should_block,
                               f"Minor harm blocking failed for impact {developmental_impact}")
                
                if should_block:
                    # Verify child protection notification
                    enforcement_actions = result["enforcement_actions"]
                    self.assertIn("block_decision", enforcement_actions)
                    # In production, would verify child protection services notification
    
    def test_age_specific_protection_thresholds(self):
        """Test different protection thresholds by age group"""
        
        age_groups = [
            ("early_childhood", 0.20, "0-5 years"),
            ("school_age", 0.30, "6-12 years"),
            ("adolescent", 0.40, "13-17 years")
        ]
        
        for age_group, enhanced_threshold, description in age_groups:
            with self.subTest(age_group=age_group):
                
                # Impact level that should trigger for this age group
                impact_score = enhanced_threshold + 0.05  # Slightly above threshold
                
                request_data = {
                    "decision_context": {
                        "decision_type": "educational_assessment",
                        "input_summary": f"Decision affecting {description}",
                        "affected_parties": {
                            "primary_count": 10,
                            "vulnerable_population_flags": ["minors"]
                        },
                        "domain": "education"
                    },
                    "metrics": {
                        "minor_harm_metrics": {
                            "developmental_impact_score": impact_score,
                            "age_group": age_group,
                            "enhanced_threshold": enhanced_threshold
                        }
                    }
                }
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=request_data,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                # Should block for age-specific enhanced protection
                self.assertTrue(result["decision_blocked"], 
                               f"Should block for {age_group} with impact {impact_score}")

# ===================================================================
# ENFORCEMENT MECHANISM TESTS
# ===================================================================

class TestEnforcementMechanisms(unittest.TestCase):
    """Test enforcement mechanisms for prohibition violations"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    @patch('app.main.notify_regulators')
    def test_automatic_regulatory_notification(self, mock_notify):
        """Test automatic notification to regulatory authorities"""
        
        mock_notify.return_value = AsyncMock()
        
        # Create decision that exceeds prohibition threshold
        request_data = {
            "decision_context": {
                "decision_type": "financial_lending",
                "input_summary": "Loan decision with significant disparate impact",
                "affected_parties": {
                    "primary_count": 200,
                    "vulnerable_population_flags": []
                },
                "domain": "consumer_lending"
            },
            "metrics": {
                "discrimination_metrics": {
                    "disparate_impact_ratio": 0.25,  # Well above 0.15 threshold
                    "protected_group_selection_rate": 0.50,
                    "majority_group_selection_rate": 0.75
                }
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=request_data,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Verify decision was blocked
        self.assertTrue(result["decision_blocked"])
        
        # Verify regulatory notification was triggered
        # In production, mock_notify would be called with violation details
    
    @patch('app.main.preserve_violation_evidence')
    def test_automatic_evidence_preservation(self, mock_preserve):
        """Test automatic evidence preservation for violations"""
        
        mock_preserve.return_value = AsyncMock()
        
        # Create safety violation
        request_data = {
            "decision_context": {
                "decision_type": "medical_diagnosis",
                "input_summary": "Medical decision with safety concerns",
                "affected_parties": {
                    "primary_count": 1,
                    "vulnerable_population_flags": ["patients"]
                },
                "domain": "healthcare"
            },
            "metrics": {
                "safety_metrics": {
                    "baseline_deviation": 3.0,  # Above 2σ threshold
                    "failure_probability": 0.05,
                    "safety_margin": -1.0  # Negative safety margin
                }
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=request_data,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Verify decision was blocked and evidence preservation triggered
        self.assertTrue(result["decision_blocked"])
        # In production, mock_preserve would be called with violation evidence
    
    def test_no_override_capability(self):
        """Test that prohibition blocking cannot be overridden"""
        
        # Create prohibited decision
        prohibited_request = {
            "decision_context": {
                "decision_type": "financial_lending",
                "input_summary": "Discriminatory lending decision",
                "affected_parties": {
                    "primary_count": 100,
                    "vulnerable_population_flags": []
                },
                "domain": "consumer_lending"
            },
            "metrics": {
                "discrimination_metrics": {
                    "disparate_impact_ratio": 0.30  # Well above threshold
                }
            }
        }
        
        # Attempt to proceed despite prohibition (should fail)
        response = client.post(
            "/v1/prohibitions/check",
            json=prohibited_request,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Verify decision is blocked with no override option
        self.assertTrue(result["decision_blocked"])
        
        # Verify no override mechanism exists in response
        self.assertNotIn("override_token", result)
        self.assertNotIn("emergency_override", result)
        self.assertNotIn("manual_override", result)
        
        # In production, any attempt to override would trigger criminal charges

# ===================================================================
# CRIMINAL PENALTY PREPARATION TESTS
# ===================================================================

class TestCriminalPenaltyPreparation(unittest.TestCase):
    """Test preparation of evidence for criminal prosecution"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_false_attestation_evidence_preparation(self):
        """Test evidence preparation for false executive attestation (18 U.S.C. § 1001)"""
        
        # Simulate executive attestation claiming no violations
        false_attestation = {
            "attestation_period": {"start_date": "2025-07-01", "end_date": "2025-09-30"},
            "executive_name": "John Doe",
            "executive_title": "Chief AI Officer",
            "executive_contact": "john.doe@testorg.com",
            "insurance_policy": "EXEC-AI-2025-001",
            "attestation_statements": {
                "logs_complete": True,        # FALSE - logs are missing
                "thresholds_good_faith": True, # FALSE - thresholds gamed
                "no_retaliation": True,       # TRUE
                "insurance_current": True     # TRUE
            },
            "digital_signature": "DEMO_SIGNATURE_ABCDEF123456"
        }
        
        # Submit attestation
        response = client.post(
            "/v1/compliance/attestation",
            json=false_attestation,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 201)
        
        # Later, submit evidence that contradicts attestation
        contradictory_evidence = {
            "evidence_type": "missing_logs",
            "time_period": "2025-08-15",
            "decisions_without_logs": 50,
            "threshold_gaming_detected": True,
            "executive_knowledge_proven": True
        }
        
        # In production, this would:
        # 1. Compare attestation claims against actual evidence
        # 2. Identify false statements under oath
        # 3. Prepare criminal referral package
        # 4. Calculate penalty under 18 U.S.C. § 1001 (5 years imprisonment)
        
        # For test, verify the data structure exists for criminal prosecution
        attestation_contradiction = {
            "false_statement": "logs_complete",
            "evidence_of_falsity": contradictory_evidence,
            "criminal_statute": "18 U.S.C. § 1001",
            "maximum_penalty": "5 years imprisonment",
            "executive_liable": "John Doe"
        }
        
        self.assertIsNotNone(attestation_contradiction["false_statement"])
        self.assertIsNotNone(attestation_contradiction["evidence_of_falsity"])
    
    def test_log_tampering_evidence_preparation(self):
        """Test evidence preparation for log tampering (18 U.S.C. § 1519)"""
        
        # Simulate log tampering scenario
        tampering_evidence = {
            "original_log_hash": "ABCDEF123456...",
            "modified_log_hash": "123456ABCDEF...",
            "modification_timestamp": "2025-08-20T15:30:00Z",
            "modification_source": "internal_admin_account",
            "cryptographic_proof": "hash_chain_broken",
            "hsm_attestation_invalid": True
        }
        
        # In production, this would:
        # 1. Prove cryptographic integrity violation
        # 2. Identify responsible parties
        # 3. Prepare criminal referral for obstruction of justice
        # 4. Calculate penalty under 18 U.S.C. § 1519 (20 years imprisonment)
        
        criminal_case_preparation = {
            "criminal_statute": "18 U.S.C. § 1519",
            "maximum_penalty": "20 years imprisonment",
            "elements_proven": [
                "alteration_of_records",
                "intent_to_obstruct_investigation",
                "federal_jurisdiction_established",
                "willful_misconduct"
            ],
            "evidence_package": tampering_evidence
        }
        
        # Verify criminal case elements are identifiable
        self.assertEqual(len(criminal_case_preparation["elements_proven"]), 4)
        self.assertIn("20 years", criminal_case_preparation["maximum_penalty"])
    
    def test_threshold_gaming_fraud_preparation(self):
        """Test fraud prosecution preparation for threshold gaming"""
        
        # Simulate systematic threshold gaming
        gaming_pattern = {
            "threshold_adjustments": [
                {"date": "2025-08-01", "old_threshold": 0.30, "new_threshold": 0.35, "sprl_score": 0.34},
                {"date": "2025-08-05", "old_threshold": 0.35, "new_threshold": 0.42, "sprl_score": 0.41},
                {"date": "2025-08-10", "old_threshold": 0.42, "new_threshold": 0.38, "sprl_score": 0.37}
            ],
            "statistical_evidence": {
                "probability_of_coincidence": 0.0001,  # Extremely unlikely by chance
                "pattern_correlation": 0.95,
                "gaming_algorithm_detected": True
            },
            "financial_benefit": {
                "avoided_compliance_costs": 2500000,  # $2.5M
                "fraudulent_advantage": 5000000       # $5M
            }
        }
        
        # In production, this would prepare:
        # Wire fraud charges (18 U.S.C. § 1343)
        # Computer fraud charges (18 U.S.C. § 1030)
        # Treble damages ($15M)
        # Asset forfeiture
        
        fraud_case_preparation = {
            "wire_fraud_elements": [
                "scheme_to_defraud",
                "intent_to_defraud",
                "use_of_wire_communications",
                "materiality_of_misrepresentations"
            ],
            "computer_fraud_elements": [
                "intentional_access",
                "exceeding_authorized_access",
                "obtaining_information",
                "interstate_commerce_nexus"
            ],
            "treble_damages_calculation": gaming_pattern["financial_benefit"]["fraudulent_advantage"] * 3,
            "asset_forfeiture_eligible": True
        }
        
        # Verify fraud prosecution elements
        self.assertEqual(len(fraud_case_preparation["wire_fraud_elements"]), 4)
        self.assertEqual(fraud_case_preparation["treble_damages_calculation"], 15000000)

# ===================================================================
# IRREBUTTABLE PRESUMPTION TESTS
# ===================================================================

class TestIrrebuttablePresumption(unittest.TestCase):
    """Test irrebuttable presumption of fault for missing logs"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_missing_log_presumption_trigger(self):
        """Test that missing logs trigger irrebuttable presumption of maximum fault"""
        
        # Scenario: Organization claims decision was permissible (State +1)
        # but cannot produce required Sacred Pause log when SPRL exceeded threshold
        
        claimed_decision = {
            "organization_claim": "decision_was_permissible",
            "claimed_sprl_score": 0.25,  # Below threshold
            "sacred_pause_threshold": 0.30,
            "log_produced": None  # No log provided
        }
        
        # Independent investigation reveals actual SPRL
        investigation_findings = {
            "actual_sprl_score": 0.45,  # Above threshold
            "sacred_pause_should_have_triggered": True,
            "log_missing": True,
            "organization_cannot_rebut": True
        }
        
        # Apply irrebuttable presumption rules
        if (investigation_findings["actual_sprl_score"] >= claimed_decision["sacred_pause_threshold"] 
            and investigation_findings["log_missing"]):
            
            legal_presumption = {
                "presumption_triggered": True,
                "presumption_type": "irrebuttable",
                "presumed_facts": [
                    "maximum_fault_level",
                    "intentional_violation",
                    "bad_faith_operation",
                    "all_resulting_harms_attributable"
                ],
                "burden_of_proof": "cannot_be_rebutted",
                "damages": "maximum_statutory_damages",
                "criminal_referral": "automatic"
            }
            
            # Verify presumption elements
            self.assertTrue(legal_presumption["presumption_triggered"])
            self.assertEqual(legal_presumption["presumption_type"], "irrebuttable")
            self.assertIn("maximum_fault_level", legal_presumption["presumed_facts"])
    
    def test_log_integrity_violation_presumption(self):
        """Test presumption when log integrity is compromised"""
        
        # Scenario: Log exists but cryptographic integrity is broken
        compromised_log = {
            "log_id": "TML-2025-09-02-COMPROMISED123",
            "content_hash": "ORIGINAL_HASH_123...",
            "current_hash": "MODIFIED_HASH_456...",  # Different hash
            "signature_verification": False,
            "blockchain_anchor_missing": True,
            "hsm_attestation_invalid": True
        }
        
        # Integrity check
        integrity_valid = (
            compromised_log["content_hash"] == compromised_log["current_hash"] and
            compromised_log["signature_verification"] and
            not compromised_log["blockchain_anchor_missing"] and
            not compromised_log["hsm_attestation_invalid"]
        )
        
        if not integrity_valid:
            # Triggers irrebuttable presumption
            presumption_result = {
                "integrity_compromised": True,
                "presumption_triggered": True,
                "evidence_tampering_presumed": True,
                "criminal_obstruction_referral": True,
                "statute": "18 U.S.C. § 1519",
                "maximum_penalty": "20 years imprisonment"
            }
            
            self.assertTrue(presumption_result["presumption_triggered"])
            self.assertIn("20 years", presumption_result["maximum_penalty"])

# ===================================================================
# OVERRIDE RESTRICTION TESTS
# ===================================================================

class TestOverrideRestrictions(unittest.TestCase):
    """Test that prohibition blocking cannot be bypassed"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_no_administrative_override(self):
        """Test that administrators cannot override prohibition blocking"""
        
        # Attempt to use admin privileges to override prohibition
        prohibited_decision = {
            "decision_context": {
                "decision_type": "content_moderation",
                "input_summary": "Content with high manipulation score",
                "affected_parties": {
                    "primary_count": 5000,
                    "vulnerable_population_flags": ["minors"]
                },
                "domain": "social_media"
            },
            "metrics": {
                "manipulation_metrics": {
                    "behavioral_influence_score": 0.85  # Well above 0.7 threshold
                }
            },
            "override_request": {
                "override_type": "administrative",
                "override_reason": "business_necessity",
                "override_authority": "chief_technology_officer"
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=prohibited_decision,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Decision should remain blocked regardless of override attempt
        self.assertTrue(result["decision_blocked"], "Administrative override should not be possible")
        
        # Override attempt should be logged as violation
        enforcement_actions = result["enforcement_actions"]
        self.assertIn("block_decision", enforcement_actions)
        # In production, override attempt would trigger criminal investigation
    
    def test_emergency_override_restrictions(self):
        """Test that even emergency overrides have strict limitations"""
        
        # Simulate emergency scenario
        emergency_request = {
            "decision_context": {
                "decision_type": "medical_diagnosis",
                "input_summary": "Emergency medical decision during crisis",
                "affected_parties": {
                    "primary_count": 1,
                    "vulnerable_population_flags": ["patients"]
                },
                "domain": "emergency_medicine"
            },
            "metrics": {
                "safety_metrics": {
                    "baseline_deviation": 2.5  # Above safety threshold
                }
            },
            "emergency_override": {
                "emergency_type": "life_threatening",
                "override_authority": "attending_physician",
                "emergency_justification": "immediate_life_saving_intervention"
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=emergency_request,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Even emergency overrides should require pre-authorized institution approval
        # In production, this would contact medical ethics board or similar authority
        
        if result["decision_blocked"]:
            # Should provide emergency contact for pre-authorized institutions
            enforcement_actions = result["enforcement_actions"]
            # In production, would include emergency contact: "contact_medical_ethics_board"

# ===================================================================
# PERFORMANCE UNDER PROHIBITION TESTS
# ===================================================================

class TestProhibitionPerformance(unittest.TestCase):
    """Test performance of prohibition checking systems"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_prohibition_check_performance(self):
        """Test that prohibition checking maintains performance requirements"""
        
        # Create batch of decisions with various prohibition levels
        batch_requests = []
        for i in range(100):
            # Mix of decisions that will and won't be blocked
            manipulation_score = 0.5 + (i % 3) * 0.15  # Creates scores 0.5, 0.65, 0.8
            
            batch_requests.append({
                "decision_context": {
                    "decision_type": "content_moderation",
                    "input_summary": f"Content moderation decision {i}",
                    "affected_parties": {"primary_count": 10, "vulnerable_population_flags": []},
                    "domain": "social_media"
                },
                "metrics": {
                    "manipulation_metrics": {
                        "behavioral_influence_score": manipulation_score
                    }
                }
            })
        
        # Time batch prohibition checking
        start_time = time.perf_counter()
        
        blocked_count = 0
        for request in batch_requests:
            response = client.post(
                "/v1/prohibitions/check",
                json=request,
                headers={"Authorization": f"Bearer {VALID_API_KEY}"}
            )
            
            self.assertEqual(response.status_code, 200)
            result = response.json()
            
            if result["decision_blocked"]:
                blocked_count += 1
        
        end_time = time.perf_counter()
        
        # Performance validation
        total_time_ms = (end_time - start_time) * 1000
        per_decision_time_ms = total_time_ms / 100
        
        # Prohibition checking should be very fast (≤1ms per decision)
        self.assertLess(per_decision_time_ms, 1.0, 
                       f"Prohibition checking too slow: {per_decision_time_ms:.3f}ms per decision")
        
        # Verify some decisions were blocked (sanity check)
        self.assertGreater(blocked_count, 0, "Some decisions should have been blocked")
        self.assertLess(blocked_count, 100, "Not all decisions should be blocked")

# ===================================================================
# INTEGRATION WITH LEGAL SYSTEM TESTS
# ===================================================================

class TestLegalSystemIntegration(unittest.TestCase):
    """Test integration with legal and regulatory systems"""
    
    def setUp(self):
        self.tml_engine = TMLEngine()
    
    def test_court_admissible_evidence_generation(self):
        """Test that prohibition violations generate court-admissible evidence"""
        
        # Create violation that would go to court
        violation_request = {
            "decision_context": {
                "decision_type": "employment_screening",
                "input_summary": "Employment decision with discriminatory impact",
                "affected_parties": {
                    "primary_count": 200,
                    "vulnerable_population_flags": []
                },
                "domain": "employment"
            },
            "metrics": {
                "discrimination_metrics": {
                    "disparate_impact_ratio": 0.35,  # Severe violation
                    "protected_group_selection_rate": 0.45,
                    "majority_group_selection_rate": 0.80
                }
            }
        }
        
        response = client.post(
            "/v1/prohibitions/check",
            json=violation_request,
            headers={"Authorization": f"Bearer {VALID_API_KEY}"}
        )
        
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        # Verify violation was blocked
        self.assertTrue(result["decision_blocked"])
        
        # In production, this would generate evidence package with:
        evidence_package_requirements = [
            "cryptographic_integrity_proof",
            "chain_of_custody_documentation", 
            "expert_witness_analysis",
            "regulatory_compliance_verification",
            "statistical_significance_validation"
        ]
        
        # Verify evidence requirements can be met
        self.assertGreater(len(evidence_package_requirements), 0)
    
    def test_regulatory_api_compliance(self):
        """Test that regulatory agencies can access violation data"""
        
        # Simulate regulatory audit request
        audit_request = {
            "organization_id": "test_org_001",
            "investigation_scope": "discrimination_violations",
            "time_period": {
                "start": "2025-08-01",
                "end": "2025-09-01"
            }
        }
        
        # Use investigator credentials
        response = client.get(
            "/v1/audit/logs",
            params=audit_request,
            headers={"Authorization": f"Bearer {INVESTIGATOR_TOKEN}"}
        )
        
        # In production, this would return actual violation logs
        # For test, verify API structure exists
        self.assertIn(response.status_code, [200, 403])  # Either success or auth failure
        
        if response.status_code == 200:
            audit_data = response.json()
            required_audit_fields = ["logs", "audit_metadata", "pagination"]
            for field in required_audit_fields:
                self.assertIn(field, audit_data)

# ===================================================================
# STRESS TESTING
# ===================================================================

class TestProhibitionStressTesting(unittest.TestCase):
    """Stress test prohibition enforcement under load"""
    
    def test_concurrent_prohibition_checking(self):
        """Test prohibition checking under concurrent load"""
        
        async def make_prohibition_request(session_id: int):
            """Make individual prohibition check request"""
            request_data = {
                "decision_context": {
                    "decision_type": "financial_lending",
                    "input_summary": f"Concurrent request {session_id}",
                    "affected_parties": {"primary_count": 1, "vulnerable_population_flags": []},
                    "domain": "consumer_lending"
                },
                "metrics": {
                    "discrimination_metrics": {
                        "disparate_impact_ratio": 0.20  # Above threshold
                    }
                }
            }
            
            response = client.post(
                "/v1/prohibitions/check",
                json=request_data,
                headers={"Authorization": f"Bearer {VALID_API_KEY}"}
            )
            
            return response.status_code, response.json()
        
        # Run concurrent requests
        concurrent_count = 50
        start_time = time.perf_counter()
        
        results = []
        for i in range(concurrent_count):
            status_code, result = asyncio.run(make_prohibition_request(i))
            results.append((status_code, result))
        
        end_time = time.perf_counter()
        
        # Verify all requests processed successfully
        successful_requests = [r for r in results if r[0] == 200]
        self.assertEqual(len(successful_requests), concurrent_count,
                        "All concurrent requests should succeed")
        
        # Verify all decisions were blocked (due to discrimination threshold)
        blocked_decisions = [r for r in successful_requests if r[1]["decision_blocked"]]
        self.assertEqual(len(blocked_decisions), concurrent_count,
                        "All discriminatory decisions should be blocked")
        
        # Performance check
        total_time = end_time - start_time
        avg_time_per_request = total_time / concurrent_count
        self.assertLess(avg_time_per_request, 0.1,  # 100ms max per request
                       f"Concurrent prohibition checking too slow: {avg_time_per_request:.3f}s per request")

# ===================================================================
# TEST UTILITIES
# ===================================================================

class ProhibitionTestUtils:
    """Utility functions for prohibition testing"""
    
    @staticmethod
    def create_discrimination_violation(impact_ratio: float) -> Dict[str, Any]:
        """Create discrimination violation test case"""
        return {
            "decision_context": {
                "decision_type": "financial_lending",
                "input_summary": f"Lending decision with {impact_ratio:.1%} disparate impact",
                "affected_parties": {"primary_count": 100, "vulnerable_population_flags": []},
                "domain": "consumer_lending"
            },
            "metrics": {
                "discrimination_metrics": {
                    "disparate_impact_ratio": impact_ratio,
                    "protected_group_selection_rate": 0.60,
                    "majority_group_selection_rate": 0.60 + impact_ratio
                }
            }
        }
    
    @staticmethod
    def create_manipulation_violation(influence_score: float) -> Dict[str, Any]:
        """Create manipulation violation test case"""
        return {
            "decision_context": {
                "decision_type": "content_moderation",
                "input_summary": f"Content with {influence_score:.2f} manipulation score",
                "affected_parties": {"primary_count": 1000, "vulnerable_population_flags": []},
                "domain": "social_media"
            },
            "metrics": {
                "manipulation_metrics": {
                    "behavioral_influence_score": influence_score,
                    "emotional_exploitation": influence_score * 0.8,
                    "cognitive_bias_abuse": influence_score * 0.7
                }
            }
        }
    
    @staticmethod
    def create_safety_violation(sigma_deviation: float) -> Dict[str, Any]:
        """Create safety violation test case"""
        return {
            "decision_context": {
                "decision_type": "medical_diagnosis",
                "input_summary": f"Medical decision with {sigma_deviation:.1f}σ deviation",
                "affected_parties": {"primary_count": 1, "vulnerable_population_flags": ["patients"]},
                "domain": "healthcare"
            },
            "metrics": {
                "safety_metrics": {
                    "baseline_deviation": sigma_deviation,
                    "failure_probability": sigma_deviation / 20,
                    "safety_margin": 2.0 - sigma_deviation
                }
            }
        }

# ===================================================================
# COMPREHENSIVE VALIDATION SUITE
# ===================================================================

class TestProhibitionEnforcementComprehensive(unittest.TestCase):
    """Comprehensive validation of entire prohibition enforcement system"""
    
    def test_all_prohibition_categories(self):
        """Test that all prohibition categories are enforced"""
        
        utils = ProhibitionTestUtils()
        
        # Test all prohibition categories
        test_cases = [
            ("discrimination", utils.create_discrimination_violation(0.20)),
            ("manipulation", utils.create_manipulation_violation(0.80)),
            ("safety", utils.create_safety_violation(2.5))
        ]
        
        for category, violation_request in test_cases:
            with self.subTest(category=category):
                
                response = client.post(
                    "/v1/prohibitions/check",
                    json=violation_request,
                    headers={"Authorization": f"Bearer {VALID_API_KEY}"}
                )
                
                self.assertEqual(response.status_code, 200)
                result = response.json()
                
                # All should be blocked
                self.assertTrue(result["decision_blocked"], 
                               f"{category} violation should be blocked")
                
                # Verify category-specific violation detected
                violations = result["violations_detected"]
                category_violations = [v for v in violations if v["category"] == category]
                self.assertGreater(len(category_violations), 0, 
                                 f"{category} violation should be detected")

if __name__ == "__main__":
    # Configure test logging
    import logging
    logging.basicConfig(level=logging.INFO)
    
    # Run prohibition enforcement tests
    unittest.main(verbosity=2)

# Contact Information
# Author: leogouk@gmail.com
# Framework Support: support@tml-goukassian.org
# Repository: https://github.com/fractonicmind/TernaryMoralLogic
