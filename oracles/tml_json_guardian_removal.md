================================================================================
FILE: oracles/eco_oracle_network.json
================================================================================
{
  "network_version": "2.0",
  "network_id": "tml_earth_oracle_network",
  "consensus_algorithm": "BFT_with_VRF",
  "last_updated": "2025-09-23T10:00:00Z",
  
  "node_categories": {
    "tier_1_oracles": {
      "description": "Fetch and validate global treaty/law data",
      "minimum_nodes": 9,
      "quorum_required": 5,
      "node_requirements": {
        "stake_minimum": 1000,
        "uptime_requirement": 0.999,
        "hardware": {
          "cpu_cores": 8,
          "ram_gb": 32,
          "bandwidth_mbps": 100,
          "storage_tb": 2
        },
        "certifications": [
          "tls_certificate",
          "kyc_verification",
          "technical_audit"
        ]
      }
    },
    
    "tier_2_oracles": {
      "description": "Validate community and local ecological data",
      "minimum_nodes": 21,
      "quorum_required": 11,
      "node_requirements": {
        "stake_minimum": 100,
        "uptime_requirement": 0.95,
        "hardware": {
          "cpu_cores": 4,
          "ram_gb": 16,
          "bandwidth_mbps": 50,
          "storage_tb": 1
        },
        "community_endorsement": true
      }
    },
    
    "bridge_oracles": {
      "description": "Connect offline communities via SMS/satellite",
      "minimum_nodes": 7,
      "special_requirements": {
        "connectivity_methods": ["sms", "satellite", "radio"],
        "regional_presence": true,
        "language_support": 3
      }
    }
  },
  
  "data_sources": {
    "tier_1_mandatory": [
      {
        "source_id": "unfccc",
        "name": "UN Framework Convention on Climate Change",
        "endpoints": [
          "https://unfccc.int/api/v2/treaties",
          "https://unfccc.int/api/v2/ndc"
        ],
        "update_frequency": "daily",
        "validation_method": "signature"
      },
      {
        "source_id": "cbd",
        "name": "Convention on Biological Diversity",
        "endpoints": [
          "https://cbd.int/api/gbf/targets",
          "https://cbd.int/api/protected_areas"
        ],
        "update_frequency": "weekly",
        "validation_method": "signature"
      },
      {
        "source_id": "ipcc",
        "name": "Intergovernmental Panel on Climate Change",
        "endpoints": [
          "https://ipcc.ch/api/ar6/data",
          "https://ipcc.ch/api/sr15/pathways"
        ],
        "update_frequency": "monthly",
        "validation_method": "hash_chain"
      },
      {
        "source_id": "iucn_redlist",
        "name": "IUCN Red List",
        "endpoints": [
          "https://iucnredlist.org/api/v4/species",
          "https://iucnredlist.org/api/v4/habitats"
        ],
        "update_frequency": "monthly",
        "validation_method": "api_key"
      },
      {
        "source_id": "ramsar",
        "name": "Ramsar Convention",
        "endpoints": [
          "https://ramsar.org/api/sites",
          "https://ramsar.org/api/criteria"
        ],
        "update_frequency": "quarterly",
        "validation_method": "signature"
      }
    ],
    
    "tier_1_regional": [
      {
        "source_id": "eu_taxonomy",
        "name": "EU Sustainable Finance Taxonomy",
        "region": "Europe",
        "endpoints": ["https://ec.europa.eu/sustainable-finance-taxonomy/api"],
        "update_frequency": "monthly"
      },
      {
        "source_id": "epa",
        "name": "US Environmental Protection Agency",
        "region": "United States",
        "endpoints": ["https://api.epa.gov/standards/v2"],
        "update_frequency": "weekly"
      },
      {
        "source_id": "china_mee",
        "name": "China Ministry of Ecology and Environment",
        "region": "China",
        "endpoints": ["https://mee.gov.cn/api/standards"],
        "update_frequency": "monthly"
      }
    ],
    
    "tier_2_community": {
      "validation_requirements": {
        "minimum_witnesses": 3,
        "governance_approval": true,
        "cross_reference": "satellite_imagery"
      },
      "data_types": [
        "water_quality",
        "deforestation",
        "species_observation",
        "pollution_detection",
        "traditional_indicators"
      ]
    }
  },
  
  "validation_protocols": {
    "consensus_mechanisms": {
      "tier_1": {
        "algorithm": "BFT",
        "threshold": 0.56,
        "timeout_seconds": 30
      },
      "tier_2": {
        "algorithm": "weighted_voting",
        "threshold": 0.51,
        "timeout_seconds": 60,
        "reputation_weight": 0.3
      }
    },
    
    "cross_validation": {
      "satellite_correlation": {
        "providers": ["sentinel", "landsat", "planet"],
        "confidence_threshold": 0.8
      },
      "scientific_review": {
        "required_for": ["critical_triggers"],
        "review_time_hours": 24
      }
    },
    
    "dispute_resolution": {
      "escalation_path": [
        "oracle_consensus",
        "stewardship_review",
        "ombudsperson"
      ],
      "max_resolution_time_hours": 72
    }
  },
  
  "economic_model": {
    "token_economics": {
      "staking": {
        "tier_1_minimum": 1000,
        "tier_2_minimum": 100,
        "community_minimum": 10,
        "slashing_conditions": {
          "false_data": 0.5,
          "downtime": 0.1,
          "collusion": 1.0
        }
      },
      
      "rewards": {
        "per_validation": {
          "tier_1": 0.1,
          "tier_2": 0.05,
          "community": 0.02
        },
        "accuracy_bonus": {
          "threshold": 0.95,
          "multiplier": 1.5
        },
        "uptime_bonus": {
          "threshold": 0.999,
          "amount_monthly": 50
        }
      }
    },
    
    "fee_structure": {
      "data_request": {
        "tier_1": 0.01,
        "tier_2": 0.005,
        "bulk_discount": 0.2
      },
      "priority_processing": {
        "multiplier": 3,
        "max_queue_skip": 100
      }
    },
    
    "treasury_allocation": {
      "node_rewards": 0.4,
      "development": 0.2,
      "community_grants": 0.2,
      "insurance": 0.1,
      "reserve": 0.1
    }
  },
  
  "security_parameters": {
    "node_selection": {
      "method": "VRF",
      "randomness_source": "block_hash",
      "selection_frequency": "per_request",
      "backup_nodes": 3
    },
    
    "anti_sybil": {
      "measures": [
        "stake_requirement",
        "reputation_system",
        "hardware_attestation",
        "network_diversity"
      ],
      "sybil_resistance_score": 0.92
    },
    
    "data_integrity": {
      "hash_algorithm": "SHA3-256",
      "signature_scheme": "Ed25519",
      "encryption": "AES-256-GCM",
      "key_rotation_days": 90
    }
  },
  
  "performance_metrics": {
    "latency_targets": {
      "tier_1_fetch_ms": 500,
      "tier_2_validation_ms": 1000,
      "consensus_ms": 3000,
      "end_to_end_ms": 5000
    },
    
    "throughput": {
      "requests_per_second": 1000,
      "validations_per_second": 500,
      "peak_capacity_multiplier": 10
    },
    
    "availability": {
      "network_uptime_target": 0.9999,
      "degraded_mode_threshold": 0.6,
      "emergency_mode_threshold": 0.3
    }
  },
  
  "governance": {
    "update_process": {
      "proposal_threshold": 100,
      "voting_period_days": 7,
      "implementation_delay_days": 3,
      "quorum_requirement": 0.3
    },
    
    "node_rotation": {
      "frequency_days": 30,
      "rotation_percentage": 0.1,
      "performance_threshold": 0.8
    },
    
    "emergency_procedures": {
      "activation_threshold": "critical_vulnerability",
      "decision_makers": ["stewardship_council", "ombudsperson"],
      "max_response_time_hours": 1
    }
  },
  
  "offline_bridge": {
    "sms_gateway": {
      "providers": ["twilio", "africas_talking", "msg91"],
      "format": "structured_codes",
      "cost_per_message": 0.01
    },
    
    "satellite": {
      "providers": ["iridium", "thuraya", "globalstar"],
      "sync_frequency_hours": 24,
      "data_compression": "zstd"
    },
    
    "physical_courier": {
      "usb_encryption": "AES-256",
      "seal_verification": "tamper_evident",
      "collection_frequency_days": 30
    }
  },
  
  "monitoring": {
    "health_checks": {
      "frequency_seconds": 60,
      "metrics": [
        "node_count",
        "consensus_rate",
        "validation_accuracy",
        "network_latency"
      ]
    },
    
    "alerts": {
      "critical": {
        "node_failure_threshold": 0.4,
        "consensus_failure_count": 3,
        "latency_spike_multiplier": 10
      },
      "warning": {
        "node_failure_threshold": 0.2,
        "accuracy_drop": 0.1,
        "queue_depth": 1000
      }
    }
  },
  
  "deployment": {
    "mainnet": {
      "launch_date": "2026-01-01",
      "initial_nodes": 30,
      "regions": [
        "North America",
        "Europe",
        "Asia",
        "Africa",
        "South America",
        "Oceania"
      ]
    },
    
    "testnet": {
      "active": true,
      "endpoint": "https://testnet.tml-earth-oracle.org",
      "faucet": "https://faucet.tml-earth-oracle.org"
    }
  }
}

================================================================================
FILE: schemas/earth/community_registration.schema.json
================================================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://tml-goukassian.org/schemas/earth/v2.0/community_registration",
  "title": "Community Registration Schema",
  "description": "Registration structure for Indigenous and local communities as sovereign ecological data stewards",
  "type": "object",
  "required": ["community_id", "name", "governance", "territory", "registration_type"],
  
  "properties": {
    "schema_version": {
      "const": "2.0"
    },
    
    "community_id": {
      "type": "string",
      "pattern": "^com_[a-z0-9]{8}$",
      "description": "Auto-generated unique identifier"
    },
    
    "name": {
      "type": "object",
      "required": ["primary"],
      "properties": {
        "primary": {
          "type": "string",
          "minLength": 1,
          "maxLength": 200
        },
        "indigenous_name": {
          "type": "string",
          "description": "Name in Indigenous language"
        },
        "alternative_names": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    },
    
    "governance": {
      "type": "object",
      "required": ["type", "decision_process", "sovereignty_declaration"],
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "consensus_council",
            "elder_council",
            "chief_council",
            "assembly",
            "traditional_custom",
            "hybrid",
            "other"
          ]
        },
        "decision_process": {
          "type": "string",
          "description": "Plain language description of how decisions are made"
        },
        "representatives": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "role": {"type": "string"},
              "name": {"type": "string"},
              "contact_method": {
                "type": "string",
                "enum": ["email", "phone", "sms", "whatsapp", "signal", "in_person", "radio"]
              },
              "term_end": {"type": "string", "format": "date"}
            }
          }
        },
        "quorum_requirements": {
          "type": "object",
          "properties": {
            "minimum_participants": {"type": "integer"},
            "percentage_required": {"type": "number"},
            "special_conditions": {"type": "string"}
          }
        },
        "sovereignty_declaration": {
          "type": "object",
          "required": ["data_ownership", "consent_protocol"],
          "properties": {
            "data_ownership": {
              "type": "string",
              "enum": ["community_collective", "tribal_nation", "indigenous_sovereign", "local_cooperative"]
            },
            "consent_protocol": {
              "type": "string",
              "enum": ["fpic", "consensus", "council_approval", "custom"]
            },
            "ids_principles": {
              "type": "boolean",
              "description": "Adherence to Indigenous Data Sovereignty principles"
            },
            "care_principles": {
              "type": "boolean",
              "description": "Adherence to CARE principles"
            }
          }
        },
        "dispute_resolution": {
          "type": "string",
          "description": "Internal process for resolving conflicts"
        }
      }
    },
    
    "territory": {
      "type": "object",
      "required": ["description"],
      "properties": {
        "description": {
          "type": "string",
          "description": "Plain language description of territory"
        },
        "boundaries": {
          "oneOf": [
            {
              "type": "object",
              "properties": {
                "type": {"const": "geojson"},
                "data": {"type": "object"}
              }
            },
            {
              "type": "object",
              "properties": {
                "type": {"const": "coordinates"},
                "points": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "lat": {"type": "number"},
                      "lng": {"type": "number"}
                    }
                  }
                }
              }
            },
            {
              "type": "object",
              "properties": {
                "type": {"const": "descriptive"},
                "landmarks": {
                  "type": "array",
                  "items": {"type": "string"}
                }
              }
            }
          ]
        },
        "area_km2": {
          "type": "number",
          "minimum": 0
        },
        "ecosystems": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "forest",
              "wetland",
              "grassland",
              "desert",
              "tundra",
              "marine",
              "freshwater",
              "mountain",
              "coastal",
              "arctic",
              "tropical",
              "other"
            ]
          }
        },
        "sacred_sites": {
          "type": "object",
          "properties": {
            "has_sacred_sites": {"type": "boolean"},
            "protection_level": {
              "type": "string",
              "enum": ["public", "restricted", "confidential"]
            }
          }
        }
      }
    },
    
    "registration_type": {
      "type": "string",
      "enum": ["online", "offline", "hybrid"]
    },
    
    "connectivity": {
      "type": "object",
      "required": ["primary_method"],
      "properties": {
        "primary_method": {
          "type": "string",
          "enum": [
            "internet_continuous",
            "internet_periodic",
            "mobile_data",
            "sms_only",
            "satellite",
            "radio",
            "courier",
            "ngo_relay"
          ]
        },
        "backup_methods": {
          "type": "array",
          "items": {"type": "string"}
        },
        "sync_frequency": {
          "type": "string",
          "enum": ["realtime", "daily", "weekly", "monthly", "quarterly"]
        },
        "offline_capability": {
          "type": "object",
          "properties": {
            "storage_method": {
              "type": "string",
              "enum": ["usb_encrypted", "paper_forms", "voice_recording", "local_server"]
            },
            "collection_protocol": {"type": "string"}
          }
        }
      }
    },
    
    "ecological_monitoring": {
      "type": "object",
      "properties": {
        "focus_areas": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "water_quality",
              "deforestation",
              "wildlife_populations",
              "seasonal_patterns",
              "pollution",
              "climate_indicators",
              "soil_health",
              "fire_management",
              "invasive_species",
              "traditional_indicators"
            ]
          }
        },
        "monitoring_capacity": {
          "type": "object",
          "properties": {
            "active_monitors": {"type": "integer"},
            "youth_participants": {"type": "integer"},
            "elder_advisors": {"type": "integer"},
            "technical_equipment": {
              "type": "array",
              "items": {"type": "string"}
            }
          }
        },
        "reporting_capability": {
          "type": "object",
          "properties": {
            "languages": {
              "type": "array",
              "items": {"type": "string"}
            },
            "formats": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": ["text", "voice", "photo", "video", "traditional_art", "oral_testimony"]
              }
            }
          }
        },
        "traditional_knowledge": {
          "type": "object",
          "properties": {
            "includes_tek": {
              "type": "boolean",
              "description": "Traditional Ecological Knowledge included"
            },
            "knowledge_keepers": {"type": "integer"},
            "transmission_method": {"type": "string"}
          }
        }
      }
    },
    
    "stewardship_participation": {
      "type": "object",
      "required": ["initial_stake", "payment_method"],
      "properties": {
        "initial_stake": {
          "type": "integer",
          "minimum": 0,
          "description": "Initial Proof-of-Stewardship tokens"
        },
        "payment_method": {
          "type": "object",
          "required": ["type"],
          "properties": {
            "type": {
              "type": "string",
              "enum": [
                "mobile_money",
                "bank_transfer",
                "crypto_wallet",
                "ngo_distribution",
                "community_fund",
                "resource_credits"
              ]
            },
            "details": {
              "type": "object",
              "properties": {
                "account_info": {"type": "string"},
                "verification_method": {"type": "string"}
              }
            }
          }
        },
        "grant_eligibility": {
          "type": "object",
          "properties": {
            "micro_grants": {"type": "boolean"},
            "emergency_fund": {"type": "boolean"},
            "infrastructure_support": {"type": "boolean"}
          }
        }
      }
    },
    
    "verification": {
      "type": "object",
      "required": ["registration_date", "verification_method"],
      "properties": {
        "registration_date": {
          "type": "string",
          "format": "date-time"
        },
        "verification_method": {
          "type": "string",
          "enum": [
            "digital_signature",
            "community_attestation",
            "ngo_validation",
            "government_recognition",
            "stewardship_verification"
          ]
        },
        "verifier": {
          "type": "object",
          "properties": {
            "entity": {"type": "string"},
            "contact": {"type": "string"},
            "signature": {"type": "string"}
          }
        },
        "supporting_documents": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {"type": "string"},
              "hash": {"type": "string"},
              "location": {"type": "string"}
            }
          }
        }
      }
    },
    
    "partnerships": {
      "type": "object",
      "properties": {
        "supporting_organizations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {"type": "string"},
              "type": {
                "type": "string",
                "enum": ["ngo", "university", "government", "foundation", "cooperative"]
              },
              "support_type": {
                "type": "array",
                "items": {
                  "type": "string",
                  "enum": ["technical", "financial", "training", "connectivity", "legal"]
                }
              }
            }
          }
        },
        "neighboring_communities": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "community_id": {"type": "string"},
              "relationship": {
                "type": "string",
                "enum": ["data_sharing", "joint_monitoring", "dispute_resolution", "resource_management"]
              }
            }
          }
        }
      }
    },
    
    "consent_log": {
      "type": "object",
      "properties": {
        "fpic_obtained": {
          "type": "boolean",
          "description": "Free, Prior, and Informed Consent"
        },
        "consent_date": {"type": "string", "format": "date"},
        "renewal_required": {"type": "string", "format": "date"},
        "withdrawal_process": {"type": "string"},
        "data_usage_restrictions": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    },
    
    "status": {
      "type": "object",
      "required": ["active", "last_activity"],
      "properties": {
        "active": {"type": "boolean"},
        "last_activity": {"type": "string", "format": "date-time"},
        "suspension_reason": {"type": "string"},
        "reactivation_conditions": {"type": "string"}
      }
    },
    
    "metadata": {
      "type": "object",
      "properties": {
        "schema_version": {"type": "string"},
        "last_updated": {"type": "string", "format": "date-time"},
        "update_history": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "date": {"type": "string", "format": "date-time"},
              "changes": {"type": "string"},
              "approved_by": {"type": "string"}
            }
          }
        }
      }
    }
  },
  
  "additionalProperties": false
}

================================================================================
FILE: schemas/earth/earth_extension.schema.json
================================================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://tml-goukassian.org/schemas/earth/v2.0/earth_extension",
  "title": "TML Earth Protection Extension Schema",
  "description": "Extends Always Memory logs with planetary accountability",
  "type": "object",
  "required": ["earth_context", "legal_compliance", "impact_metrics"],
  
  "properties": {
    "framework_version": {
      "const": "TML-Earth-v2.0"
    },
    
    "earth_context": {
      "type": "object",
      "required": ["harm_assessment", "stakeholders_affected"],
      "properties": {
        "harm_assessment": {
          "type": "object",
          "properties": {
            "ecosystem_risk": {
              "type": "string",
              "enum": ["none", "low", "medium", "high", "critical"]
            },
            "biodiversity_impact": {
              "type": "string",
              "enum": ["positive", "neutral", "minor", "moderate", "severe"]
            },
            "irreversibility_score": {
              "type": "number",
              "minimum": 0,
              "maximum": 1,
              "description": "0 = fully reversible, 1 = permanent damage"
            },
            "recovery_timeframe": {
              "type": "string",
              "pattern": "^[0-9]+_(days|months|years|decades|centuries)$"
            }
          }
        },
        
        "stakeholders_affected": {
          "type": "object",
          "properties": {
            "human_communities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "community_id": {"type": "string"},
                  "population": {"type": "integer"},
                  "vulnerability_index": {"type": "number", "minimum": 0, "maximum": 1},
                  "indigenous_status": {"type": "boolean"}
                }
              }
            },
            "non_human_entities": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "species": {"type": "string"},
                  "iucn_status": {
                    "type": "string",
                    "enum": ["LC", "NT", "VU", "EN", "CR", "EW", "EX"]
                  },
                  "habitat_area": {"type": "string"},
                  "ecosystem_role": {"type": "string"}
                }
              }
            },
            "future_generations": {
              "type": "object",
              "properties": {
                "impact_duration": {"type": "string"},
                "affected_population_estimate": {"type": "integer"},
                "intergenerational_debt": {"type": "number"}
              }
            }
          }
        }
      }
    },
    
    "legal_compliance": {
      "type": "object",
      "required": ["rules_version", "rules_hash", "treaties_checked"],
      "properties": {
        "rules_version": {
          "type": "string",
          "pattern": "^ECO_HARM_RULES_v[0-9]+\\.[0-9]+\\.[0-9]+$"
        },
        "rules_hash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        },
        "treaties_checked": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["treaty_id", "version", "result"],
            "properties": {
              "treaty_id": {"type": "string"},
              "version": {"type": "string"},
              "articles_triggered": {"type": "array", "items": {"type": "string"}},
              "result": {
                "type": "integer",
                "enum": [1, 0, -1]
              }
            }
          }
        },
        "regional_regulations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "jurisdiction": {"type": "string"},
              "regulation_id": {"type": "string"},
              "compliance_status": {
                "type": "string",
                "enum": ["compliant", "uncertain", "violation"]
              }
            }
          }
        },
        "last_legal_sync": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    
    "impact_metrics": {
      "type": "object",
      "properties": {
        "carbon": {
          "type": "object",
          "properties": {
            "emissions_tons": {"type": "number"},
            "sequestration_tons": {"type": "number"},
            "net_impact": {"type": "number"},
            "paris_alignment": {"type": "boolean"}
          }
        },
        "water": {
          "type": "object",
          "properties": {
            "consumption_liters": {"type": "number"},
            "quality_impact": {
              "type": "string",
              "enum": ["improved", "neutral", "degraded", "contaminated"]
            },
            "watershed_stress": {
              "type": "string",
              "enum": ["low", "medium", "high", "critical"]
            }
          }
        },
        "habitat": {
          "type": "object",
          "properties": {
            "area_affected_km2": {"type": "number"},
            "fragmentation_index": {"type": "number"},
            "restoration_potential": {"type": "number"},
            "protected_status": {"type": "boolean"}
          }
        },
        "pollution": {
          "type": "object",
          "properties": {
            "air_quality_index": {"type": "integer"},
            "soil_contamination": {"type": "boolean"},
            "noise_db": {"type": "number"},
            "light_pollution_lux": {"type": "number"}
          }
        }
      }
    },
    
    "community_witness": {
      "type": "object",
      "properties": {
        "reports": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["community_id", "observation", "verification"],
            "properties": {
              "community_id": {"type": "string"},
              "observation": {
                "type": "object",
                "properties": {
                  "type": {"type": "string"},
                  "severity": {
                    "type": "string",
                    "enum": ["low", "medium", "high", "critical"]
                  },
                  "traditional_indicators": {"type": "array", "items": {"type": "string"}},
                  "witness_count": {"type": "integer", "minimum": 1}
                }
              },
              "governance_protocol": {
                "type": "string",
                "enum": ["consensus_council", "elder_council", "assembly", "custom"]
              },
              "verification": {
                "type": "object",
                "properties": {
                  "method": {
                    "type": "string",
                    "enum": ["digital_signature", "threshold_signature", "voice_attestation", "physical_seal"]
                  },
                  "timestamp": {"type": "string", "format": "date-time"},
                  "oracle_validation": {"type": "boolean"}
                }
              },
              "sovereignty_status": {
                "type": "string",
                "enum": ["recognized", "pending", "disputed"]
              }
            }
          }
        }
      }
    },
    
    "sacred_zero_earth": {
      "type": "object",
      "properties": {
        "trigger_type": {
          "type": "string",
          "enum": [
            "carbon_budget_exceeded",
            "biodiversity_loss",
            "water_depletion",
            "habitat_destruction",
            "pollution_threshold",
            "indigenous_sacred_site",
            "irreversible_damage",
            "tipping_point_proximity"
          ]
        },
        "escalation": {
          "type": "object",
          "properties": {
            "stewardship_notified": {"type": "boolean"},
            "council_review": {"type": "boolean"},
            "community_consultation": {"type": "boolean"},
            "emergency_protocol": {"type": "boolean"}
          }
        },
        "alternatives_considered": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "option": {"type": "string"},
              "impact_reduction": {"type": "number"},
              "cost_difference": {"type": "number"},
              "reason_rejected": {"type": "string"}
            }
          }
        },
        "resolution": {
          "type": "object",
          "properties": {
            "outcome": {
              "type": "string",
              "enum": ["proceed_modified", "pause_indefinite", "refuse_permanent", "defer_community"]
            },
            "authority": {"type": "string"},
            "rationale": {"type": "string"},
            "conditions": {"type": "array", "items": {"type": "string"}}
          }
        }
      }
    },
    
    "oracle_network": {
      "type": "object",
      "properties": {
        "tier_1_sources": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "source_id": {"type": "string"},
              "fetch_timestamp": {"type": "string", "format": "date-time"},
              "validation_nodes": {"type": "array", "items": {"type": "string"}},
              "consensus_achieved": {"type": "boolean"}
            }
          }
        },
        "tier_2_witnesses": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "community_oracle": {"type": "string"},
              "data_hash": {"type": "string"},
              "stewardship_tokens": {"type": "integer"}
            }
          }
        }
      }
    },
    
    "audit_trail": {
      "type": "object",
      "required": ["log_hash", "stewardship_signatures", "blockchain_anchor"],
      "properties": {
        "log_hash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        },
        "stewardship_signatures": {
          "type": "array",
          "minItems": 3,
          "items": {
            "type": "object",
            "properties": {
              "stewardship_member_id": {"type": "string"},
              "signature": {"type": "string"},
              "institution_type": {
                "type": "string",
                "enum": ["academic", "technical", "civil_society", "governance"]
              }
            }
          }
        },
        "blockchain_anchor": {
          "type": "object",
          "properties": {
            "chain": {"type": "string"},
            "block_height": {"type": "integer"},
            "transaction_hash": {"type": "string"},
            "timestamp": {"type": "string", "format": "date-time"}
          }
        },
        "immutable_since": {
          "type": "string",
          "format": "date-time"
        }
      }
    }
  },
  
  "additionalProperties": false
}

================================================================================
FILE: schemas/earth/ecological_event.schema.json
================================================================================
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://tml-goukassian.org/schemas/earth/v2.0/ecological_event",
  "title": "Ecological Event Schema",
  "description": "Structure for logging ecological events that trigger Sacred Zero or require monitoring",
  "type": "object",
  "required": ["event_id", "timestamp", "event_type", "severity", "location", "impact"],
  
  "properties": {
    "schema_version": {
      "const": "2.0"
    },
    
    "event_id": {
      "type": "string",
      "pattern": "^eco_[0-9]{4}_[0-9]{2}_[0-9]{2}_[a-z0-9]{8}$",
      "description": "Unique identifier: eco_YYYY_MM_DD_randomhash"
    },
    
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "ISO 8601 timestamp with microsecond precision"
    },
    
    "event_type": {
      "type": "string",
      "enum": [
        "deforestation",
        "water_contamination",
        "species_mortality",
        "habitat_destruction",
        "pollution_release",
        "climate_tipping_point",
        "biodiversity_loss",
        "sacred_site_violation",
        "migration_disruption",
        "ecosystem_collapse",
        "soil_degradation",
        "ocean_acidification",
        "wetland_destruction",
        "coral_bleaching",
        "wildfire",
        "drought",
        "flood",
        "chemical_spill",
        "radiation_leak",
        "invasive_species",
        "overharvesting",
        "noise_pollution",
        "light_pollution",
        "traditional_indicator"
      ]
    },
    
    "severity": {
      "type": "object",
      "required": ["level", "reversibility", "timeline"],
      "properties": {
        "level": {
          "type": "string",
          "enum": ["low", "medium", "high", "critical", "catastrophic"]
        },
        "reversibility": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "0 = fully reversible, 1 = permanent"
        },
        "timeline": {
          "type": "string",
          "pattern": "^[0-9]+_(hours|days|months|years|decades|centuries)$"
        },
        "confidence": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      }
    },
    
    "location": {
      "type": "object",
      "required": ["description"],
      "properties": {
        "description": {
          "type": "string",
          "minLength": 1
        },
        "coordinates": {
          "type": "object",
          "properties": {
            "latitude": {"type": "number", "minimum": -90, "maximum": 90},
            "longitude": {"type": "number", "minimum": -180, "maximum": 180},
            "precision_km": {"type": "number", "minimum": 1}
          }
        },
        "ecosystem_type": {
          "type": "string",
          "enum": [
            "forest", "wetland", "grassland", "desert", "tundra",
            "marine", "freshwater", "coastal", "mountain", "urban",
            "agricultural", "arctic", "tropical", "temperate"
          ]
        },
        "protected_status": {
          "type": "string",
          "enum": [
            "none", "national_park", "reserve", "indigenous_territory",
            "ramsar_site", "world_heritage", "marine_protected_area"
          ]
        },
        "watershed": {
          "type": "string"
        }
      }
    },
    
    "impact": {
      "type": "object",
      "required": ["primary_impact"],
      "properties": {
        "primary_impact": {
          "type": "object",
          "properties": {
            "area_affected_km2": {"type": "number", "minimum": 0},
            "population_affected": {"type": "integer", "minimum": 0},
            "species_affected": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "name": {"type": "string"},
                  "iucn_status": {
                    "type": "string",
                    "enum": ["LC", "NT", "VU", "EN", "CR", "EW", "EX"]
                  },
                  "population_impact": {"type": "string"}
                }
              }
            }
          }
        },
        "carbon_impact": {
          "type": "object",
          "properties": {
            "emissions_tons_co2e": {"type": "number"},
            "sequestration_loss": {"type": "number"},
            "net_impact": {"type": "number"}
          }
        },
        "water_impact": {
          "type": "object",
          "properties": {
            "volume_contaminated_m3": {"type": "number"},
            "quality_degradation": {
              "type": "string",
              "enum": ["minimal", "moderate", "severe", "toxic"]
            },
            "downstream_distance_km": {"type": "number"}
          }
        },
        "soil_impact": {
          "type": "object",
          "properties": {
            "erosion_tons": {"type": "number"},
            "contamination_depth_m": {"type": "number"},
            "fertility_loss_percent": {"type": "number"}
          }
        },
        "cumulative_effects": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Other events this contributes to"
        }
      }
    },
    
    "detection": {
      "type": "object",
      "required": ["source", "method"],
      "properties": {
        "source": {
          "type": "string",
          "enum": [
            "community_report",
            "satellite_imagery",
            "sensor_network",
            "scientific_survey",
            "oracle_network",
            "traditional_observation",
            "government_data",
            "ngo_report",
            "automated_detection"
          ]
        },
        "method": {
          "type": "string"
        },
        "reporter": {
          "type": "object",
          "properties": {
            "type": {
              "type": "string",
              "enum": ["community", "individual", "organization", "automated"]
            },
            "id": {
              "type": "string",
              "description": "Anonymized identifier"
            },
            "verification_status": {
              "type": "string",
              "enum": ["unverified", "community_verified", "oracle_verified", "stewardship_verified"]
            }
          }
        },
        "witnesses": {
          "type": "integer",
          "minimum": 0
        },
        "evidence": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["photo", "video", "sensor_data", "testimony", "document", "sample"]
              },
              "hash": {"type": "string"},
              "timestamp": {"type": "string", "format": "date-time"}
            }
          }
        }
      }
    },
    
    "response": {
      "type": "object",
      "required": ["classification", "sacred_zero_triggered"],
      "properties": {
        "classification": {
          "type": "integer",
          "enum": [1, 0, -1],
          "description": "1=proceed, 0=sacred_zero, -1=refuse"
        },
        "sacred_zero_triggered": {
          "type": "boolean"
        },
        "trigger_reason": {
          "type": "string"
        },
        "stewardship_notified": {
          "type": "boolean"
        },
        "community_notified": {
          "type": "boolean"
        },
        "emergency_response": {
          "type": "object",
          "properties": {
            "activated": {"type": "boolean"},
            "type": {"type": "string"},
            "resources_deployed": {"type": "array", "items": {"type": "string"}}
          }
        },
        "alternatives_considered": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "option": {"type": "string"},
              "impact_reduction": {"type": "number"},
              "reason_rejected": {"type": "string"}
            }
          }
        }
      }
    },
    
    "legal_context": {
      "type": "object",
      "properties": {
        "treaties_violated": {
          "type": "array",
          "items": {"type": "string"}
        },
        "regulations_violated": {
          "type": "array",
          "items": {"type": "string"}
        },
        "indigenous_rights": {
          "type": "object",
          "properties": {
            "fpic_status": {
              "type": "string",
              "enum": ["obtained", "not_obtained", "not_required", "in_process"]
            },
            "affected_communities": {
              "type": "array",
              "items": {"type": "string"}
            }
          }
        }
      }
    },
    
    "restoration": {
      "type": "object",
      "properties": {
        "required": {"type": "boolean"},
        "estimated_cost": {"type": "number"},
        "timeline": {"type": "string"},
        "responsible_parties": {
          "type": "array",
          "items": {"type": "string"}
        },
        "success_metrics": {
          "type": "array",
          "items": {"type": "string"}
        }
      }
    },
    
    "audit_trail": {
      "type": "object",
      "required": ["log_hash", "stewardship_signatures"],
      "properties": {
        "log_hash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        },
        "stewardship_signatures": {
          "type": "array",
          "minItems": 3,
          "items": {
            "type": "object",
            "properties": {
              "stewardship_member_id": {"type": "string"},
              "signature": {"type": "string"},
              "timestamp": {"type": "string", "format": "date-time"}
            }
          }
        },
        "oracle_attestations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "oracle_id": {"type": "string"},
              "attestation": {"type": "string"}
            }
          }
        },
        "immutable_since": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    
    "metadata": {
      "type": "object",
      "properties": {
        "related_events": {
          "type": "array",
          "items": {"type": "string"},
          "description": "IDs of related ecological events"
        },
        "tags": {
          "type": "array",
          "items": {"type": "string"}
        },
        "public_visibility": {
          "type": "string",
          "enum": ["public", "restricted", "confidential"]
        },
        "update_history": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "timestamp": {"type": "string", "format": "date-time"},
              "change": {"type": "string"},
              "author": {"type": "string"}
            }
          }
        }
      }
    }
  },
  
  "additionalProperties": false
}
