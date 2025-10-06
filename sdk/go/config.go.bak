/**
 * TML Configuration - Configuration management for TML SDK
 * 
 * Path: /sdk/go/config.go
 * Version: 1.0.0
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * 
 * This manages configuration settings for TML client,
 * including Guardian endpoints, security settings, and 
 * operational parameters.
 */

package tml

import (
	"encoding/json"
	"errors"
	"io/ioutil"
	"os"
	"time"
)

// Config holds all TML configuration settings
type Config struct {
	// Network Configuration
	GuardianURL     string   `json:"guardian_url"`
	BackupGuardians []string `json:"backup_guardians"`
	ConnectionTimeout int    `json:"connection_timeout_ms"`
	ReadTimeout      int     `json:"read_timeout_ms"`
	MaxRetries       int     `json:"max_retries"`
	
	// Security Configuration
	RequireTEE           bool     `json:"require_tee"`
	EncryptLocal         bool     `json:"encrypt_local"`
	HMACKey              string   `json:"hmac_key"`
	ValidateCertificates bool     `json:"validate_certificates"`
	TrustedCAs           []string `json:"trusted_cas"`
	
	// Sacred Zero Configuration
	BlockOnSacredZero     bool `json:"block_on_sacred_zero"`
	SacredZeroTimeout     int  `json:"sacred_zero_timeout_ms"`
	MaxSacredZerosPerHour int  `json:"max_sacred_zeros_per_hour"`
	AutoEscalate          bool `json:"auto_escalate"`
	
	// Always Memory Configuration
	LocalStorageEnabled   bool   `json:"local_storage_enabled"`
	LocalStoragePath      string `json:"local_storage_path"`
	MaxLocalStorageSize   int64  `json:"max_local_storage_bytes"`
	BatchSize             int    `json:"batch_size"`
	BatchTimeout          int    `json:"batch_timeout_ms"`
	CompressLogs          bool   `json:"compress_logs"`
	
	// Operational Configuration
	Environment          string `json:"environment"` // production, staging, development
	DebugMode            bool   `json:"debug_mode"`
	LogLevel             string `json:"log_level"` // DEBUG, INFO, WARN, ERROR
	MetricsEnabled       bool   `json:"metrics_enabled"`
	MetricsReportInterval int   `json:"metrics_report_interval_ms"`
	
	// Human Rights Configuration
	DiscriminationThreshold      float64  `json:"discrimination_threshold"`
	VulnerablePopulationEnhanced bool     `json:"vulnerable_population_enhanced"`
	ProtectedCharacteristics     []string `json:"protected_characteristics"`
	
	// Environmental Configuration
	CarbonThreshold           float64 `json:"carbon_threshold_kg"`
	WaterThreshold            float64 `json:"water_threshold_liters"`
	IndigenousDataSovereignty bool    `json:"indigenous_data_sovereignty"`
	BiodiversityProtection    bool    `json:"biodiversity_protection"`
	CircularEconomyMode       bool    `json:"circular_economy_mode"`
	
	// Ecosystem Stakeholder Configuration
	EcosystemStakeholders struct {
		HumanCommunities    bool `json:"human_communities"`
		NonHumanEntities    bool `json:"non_human_entities"`
		FutureGenerations   bool `json:"future_generations"`
	} `json:"ecosystem_stakeholders"`
	
	// Compliance Configuration
	Jurisdiction          string   `json:"jurisdiction"`
	ComplianceFrameworks  []string `json:"compliance_frameworks"`
	AuditModeEnabled      bool     `json:"audit_mode_enabled"`
}

// DefaultConfig returns the default configuration
func DefaultConfig() *Config {
	return &Config{
		// Network
		GuardianURL:       "https://guardian.tml-network.org",
		BackupGuardians:   []string{
			"https://guardian2.tml-network.org",
			"https://guardian3.tml-network.org",
		},
		ConnectionTimeout: 5000,
		ReadTimeout:       10000,
		MaxRetries:        3,
		
		// Security
		RequireTEE:           false,
		EncryptLocal:         true,
		HMACKey:              "",
		ValidateCertificates: true,
		TrustedCAs:           []string{},
		
		// Sacred Zero
		BlockOnSacredZero:     true,
		SacredZeroTimeout:     500,
		MaxSacredZerosPerHour: 5,
		AutoEscalate:          true,
		
		// Always Memory
		LocalStorageEnabled:   true,
		LocalStoragePath:      "/var/tml/logs",
		MaxLocalStorageSize:   10 * 1024 * 1024 * 1024, // 10GB
		BatchSize:             1000,
		BatchTimeout:          100,
		CompressLogs:          true,
		
		// Operational
		Environment:           "production",
		DebugMode:             false,
		LogLevel:              "INFO",
		MetricsEnabled:        true,
		MetricsReportInterval: 60000,
		
		// Human Rights
		DiscriminationThreshold:      0.2,
		VulnerablePopulationEnhanced: true,
		ProtectedCharacteristics: []string{
			"race", "color", "religion", "sex", "national_origin",
			"disability", "age", "gender_identity", "sexual_orientation",
		},
		
		// Environmental
		CarbonThreshold:           1000.0, // kg CO2
		WaterThreshold:            10000.0, // liters
		IndigenousDataSovereignty: true,
		BiodiversityProtection:    true,
		CircularEconomyMode:       false,
		
		// Ecosystem Stakeholders (all enabled by default)
		EcosystemStakeholders: struct {
			HumanCommunities  bool `json:"human_communities"`
			NonHumanEntities  bool `json:"non_human_entities"`
			FutureGenerations bool `json:"future_generations"`
		}{
			HumanCommunities:  true,
			NonHumanEntities:  true,
			FutureGenerations: true,
		},
		
		// Compliance
		Jurisdiction: "US",
		ComplianceFrameworks: []string{
			"GDPR", "CCPA", "EU_AI_ACT", "UN_HUMAN_RIGHTS",
			"PARIS_AGREEMENT", "CBD", "UNDRIP",
		},
		AuditModeEnabled: false,
	}
}

// DevelopmentConfig returns configuration for development
func DevelopmentConfig() *Config {
	config := DefaultConfig()
	config.Environment = "development"
	config.DebugMode = true
	config.LogLevel = "DEBUG"
	config.RequireTEE = false
	config.ValidateCertificates = false
	config.GuardianURL = "http://localhost:8080"
	return config
}

// HighSecurityConfig returns high-security configuration
func HighSecurityConfig() *Config {
	config := DefaultConfig()
	config.RequireTEE = true
	config.EncryptLocal = true
	config.ValidateCertificates = true
	config.BlockOnSacredZero = true
	config.AuditModeEnabled = true
	config.MaxSacredZerosPerHour = 3
	return config
}

// StrictEnvironmentalConfig returns strict environmental configuration
func StrictEnvironmentalConfig() *Config {
	config := DefaultConfig()
	config.CarbonThreshold = 100.0   // Much stricter - 100kg CO2
	config.WaterThreshold = 1000.0   // Much stricter - 1000 liters
	config.BiodiversityProtection = true
	config.CircularEconomyMode = true
	config.IndigenousDataSovereignty = true
	return config
}

// LoadFromFile loads configuration from JSON file
func LoadFromFile(path string) (*Config, error) {
	data, err := ioutil.ReadFile(path)
	if err != nil {
		return nil, err
	}
	
	config := DefaultConfig()
	if err := json.Unmarshal(data, config); err != nil {
		return nil, err
	}
	
	if err := config.Validate(); err != nil {
		return nil, err
	}
	
	return config, nil
}

// LoadFromEnv loads configuration from environment variables
func LoadFromEnv() *Config {
	config := DefaultConfig()
	
	// Network settings
	if url := os.Getenv("TML_GUARDIAN_URL"); url != "" {
		config.GuardianURL = url
	}
	
	// Security settings
	if tee := os.Getenv("TML_REQUIRE_TEE"); tee == "true" {
		config.RequireTEE = true
	}
	if key := os.Getenv("TML_HMAC_KEY"); key != "" {
		config.HMACKey = key
	}
	
	// Sacred Zero settings
	if block := os.Getenv("TML_BLOCK_SACRED_ZERO"); block == "false" {
		config.BlockOnSacredZero = false
	}
	
	// Environmental settings
	if carbon := os.Getenv("TML_CARBON_THRESHOLD"); carbon != "" {
		// Parse and set carbon threshold
	}
	
	// Compliance settings
	if jurisdiction := os.Getenv("TML_JURISDICTION"); jurisdiction != "" {
		config.Jurisdiction = jurisdiction
	}
	
	return config
}

// Validate checks if configuration is valid
func (c *Config) Validate() error {
	// Check required fields
	if c.GuardianURL == "" {
		return errors.New("guardian URL is required")
	}
	
	// Check thresholds
	if c.DiscriminationThreshold < 0 || c.DiscriminationThreshold > 1 {
		return errors.New("discrimination threshold must be between 0 and 1")
	}
	
	if c.CarbonThreshold < 0 {
		return errors.New("carbon threshold must be positive")
	}
	
	if c.WaterThreshold < 0 {
		return errors.New("water threshold must be positive")
	}
	
	// Check timeouts
	if c.ConnectionTimeout <= 0 || c.ReadTimeout <= 0 {
		return errors.New("timeouts must be positive")
	}
	
	// Check batch settings
	if c.BatchSize <= 0 || c.BatchTimeout <= 0 {
		return errors.New("batch settings must be positive")
	}
	
	// Validate environment
	switch c.Environment {
	case "production", "staging", "development":
		// Valid
	default:
		return errors.New("invalid environment: must be production, staging, or development")
	}
	
	// Validate log level
	switch c.LogLevel {
	case "DEBUG", "INFO", "WARN", "ERROR":
		// Valid
	default:
		return errors.New("invalid log level: must be DEBUG, INFO, WARN, or ERROR")
	}
	
	return nil
}

// Copy creates a deep copy of the configuration
func (c *Config) Copy() *Config {
	// Marshal and unmarshal to create deep copy
	data, _ := json.Marshal(c)
	copy := &Config{}
	json.Unmarshal(data, copy)
	return copy
}

// ToJSON converts configuration to JSON
func (c *Config) ToJSON() ([]byte, error) {
	return json.MarshalIndent(c, "", "  ")
}

// SaveToFile saves configuration to JSON file
func (c *Config) SaveToFile(path string) error {
	data, err := c.ToJSON()
	if err != nil {
		return err
	}
	return ioutil.WriteFile(path, data, 0644)
}

// GetTimeout returns appropriate timeout duration
func (c *Config) GetTimeout(operation string) time.Duration {
	switch operation {
	case "connection":
		return time.Duration(c.ConnectionTimeout) * time.Millisecond
	case "read":
		return time.Duration(c.ReadTimeout) * time.Millisecond
	case "sacred_zero":
		return time.Duration(c.SacredZeroTimeout) * time.Millisecond
	case "batch":
		return time.Duration(c.BatchTimeout) * time.Millisecond
	default:
		return 5 * time.Second
	}
}

// IsHighRisk returns true if configuration indicates high-risk operations
func (c *Config) IsHighRisk() bool {
	return c.RequireTEE && 
	       c.AuditModeEnabled && 
	       c.Environment == "production"
}

// RequiresEnvironmentalReview returns true if environmental thresholds may be exceeded
func (c *Config) RequiresEnvironmentalReview(carbon, water float64) bool {
	return carbon > c.CarbonThreshold || water > c.WaterThreshold
}

// RequiresIndigenousConsent returns true if indigenous data sovereignty is enabled
func (c *Config) RequiresIndigenousConsent() bool {
	return c.IndigenousDataSovereignty
}
