// Package tml provides blockchain-enforced AI accountability
//
// Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
package tml

import (
	"fmt"
	"os"
	"time"
)

// Config represents TML blockchain configuration
type Config struct {
	// Blockchain endpoints (required)
	Ethereum EthereumConfig `json:"ethereum"`
	Polygon  PolygonConfig  `json:"polygon"`
	Bitcoin  BitcoinConfig  `json:"bitcoin"`
	
	// Smart contracts (required)
	Contracts ContractsConfig `json:"contracts"`
	
	// Penalties (automatic enforcement)
	Penalties PenaltyConfig `json:"penalties"`
	
	// Whistleblower settings
	Whistleblower WhistleblowerConfig `json:"whistleblower"`
	
	// Stewardship Council settings (recommended enhancement)
	StewardshipCouncil StewardshipCouncilConfig `json:"stewardship_council,omitempty"`
	
	// System settings
	System SystemConfig `json:"system"`
}

// EthereumConfig for primary smart contract execution
type EthereumConfig struct {
	RPC      string `json:"rpc"`
	ChainID  int    `json:"chain_id"`
	GasPrice string `json:"gas_price"`
}

// PolygonConfig for high-speed anchoring
type PolygonConfig struct {
	RPC     string `json:"rpc"`
	ChainID int    `json:"chain_id"`
}

// BitcoinConfig for ultimate immutability
type BitcoinConfig struct {
	Node string `json:"node"`
	OTS  bool   `json:"opentimestamps"` // OpenTimestamps integration
}

// ContractsConfig holds smart contract addresses
type ContractsConfig struct {
	SacredZero    string `json:"sacred_zero"`
	Penalties     string `json:"penalties"`
	Whistleblower string `json:"whistleblower"`
	AlwaysMemory  string `json:"always_memory"`
}

// PenaltyConfig defines automatic penalties (2025 USD)
type PenaltyConfig struct {
	MissingLogs     int64   `json:"missing_logs"`      // $100M default
	Discrimination  int64   `json:"discrimination"`    // $500M default
	Environmental   int64   `json:"environmental"`     // $1B default
	Torture         int64   `json:"torture"`           // $500M default
	ChildHarm       int64   `json:"child_harm"`        // $700M default
	
	// Multipliers
	HumanRights       float64 `json:"human_rights_multiplier"`       // 2x
	EarthProtection   float64 `json:"earth_protection_multiplier"`   // 3x
	FutureGenerations float64 `json:"future_generations_multiplier"` // 7x
}

// WhistleblowerConfig for direct rewards
type WhistleblowerConfig struct {
	RewardPercentage  float64       `json:"reward_percentage"`   // 15%
	PaymentTime       time.Duration `json:"payment_time"`        // 3 minutes
	AnonymousReporting bool         `json:"anonymous_reporting"` // true
}

// StewardshipCouncilConfig (recommended enhancement)
type StewardshipCouncilConfig struct {
	Enabled              bool                       `json:"enabled"`
	Members              []StewardshipCouncilMember `json:"members"`
	SynchronizationAPI   string                     `json:"synchronization_api"`
	ValidationThreshold  int                        `json:"validation_threshold"`  // Number of confirmations required
}

// StewardshipCouncilMember represents a council member institution
type StewardshipCouncilMember struct {
	Role         string `json:"role"`          // e.g., "Technical Custodian"
	Institution  string `json:"institution"`   // e.g., "Electronic Frontier Foundation"
	PublicKey    string `json:"public_key"`
	EndpointURL  string `json:"endpoint_url"`
}

// SystemConfig for general settings
type SystemConfig struct {
	Creator         string        `json:"creator"`          // Lev Goukassian
	ORCID           string        `json:"orcid"`            // 0009-0006-5966-1243
	Version         string        `json:"version"`          // 3.0.0
	SacredSymbol    string        `json:"sacred_symbol"`    // 🏮
}

// DefaultConfig returns production-ready configuration
func DefaultConfig() *Config {
	return &Config{
		Ethereum: EthereumConfig{
			RPC:      "https://eth-mainnet.public-rpc.com",
			ChainID:  1,
			GasPrice: "auto",
		},
		Polygon: PolygonConfig{
			RPC:     "https://polygon-rpc.com",
			ChainID: 137,
		},
		Bitcoin: BitcoinConfig{
			Node: "https://blockchain.info",
			OTS:  true,
		},
		Contracts: ContractsConfig{
			SacredZero:    "0xSACRED...",
			Penalties:     "0xPENALTY...",
			Whistleblower: "0xWHISTLE...",
			AlwaysMemory:  "0xMEMORY...",
		},
		Penalties: PenaltyConfig{
			MissingLogs:       100_000_000,
			Discrimination:    500_000_000,
			Environmental:     1_000_000_000,
			Torture:           500_000_000,
			ChildHarm:         700_000_000,
			HumanRights:       2.0,
			EarthProtection:   3.0,
			FutureGenerations: 7.0,
		},
		Whistleblower: WhistleblowerConfig{
			RewardPercentage:   0.15,
			PaymentTime:        3 * time.Minute,
			AnonymousReporting: true,
		},
		StewardshipCouncil: StewardshipCouncilConfig{
			Enabled: false, // Can be enabled as recommended enhancement
			Members: []StewardshipCouncilMember{
				{
					Role:        "Technical Custodian",
					Institution: "Electronic Frontier Foundation",
					PublicKey:   "",
					EndpointURL: "",
				},
				{
					Role:        "Human Rights Enforcement Partner",
					Institution: "Amnesty International",
					PublicKey:   "",
					EndpointURL: "",
				},
				{
					Role:        "Earth Protection Enforcement Partner",
					Institution: "Indigenous Environmental Network",
					PublicKey:   "",
					EndpointURL: "",
				},
				{
					Role:        "AI Ethics Research Partner",
					Institution: "MIT Media Lab",
					PublicKey:   "",
					EndpointURL: "",
				},
				{
					Role:        "Memorial Fund Administrator",
					Institution: "Memorial Sloan Kettering Cancer Center",
					PublicKey:   "",
					EndpointURL: "",
				},
				{
					Role:        "Community Representative",
					Institution: "Elected by stakeholder community",
					PublicKey:   "",
					EndpointURL: "",
				},
			},
			ValidationThreshold: 4, // Require 4 of 6 confirmations
		},
		System: SystemConfig{
			Creator:        "Lev Goukassian",
			ORCID:          "0009-0006-5966-1243",
			Version:        "3.0.0",
			SacredSymbol:   "🏮",
		},
	}
}

// LoadConfig loads configuration from environment
func LoadConfig() (*Config, error) {
	cfg := DefaultConfig()
	
	// Override with environment variables if set
	if rpc := os.Getenv("TML_ETHEREUM_RPC"); rpc != "" {
		cfg.Ethereum.RPC = rpc
	}
	
	if rpc := os.Getenv("TML_POLYGON_RPC"); rpc != "" {
		cfg.Polygon.RPC = rpc
	}
	
	// Check for Stewardship Council configuration
	if os.Getenv("TML_ENABLE_STEWARDSHIP_COUNCIL") == "true" {
		cfg.StewardshipCouncil.Enabled = true
	}
	
	return cfg, nil
}

// Validate ensures configuration is correct
func (c *Config) Validate() error {
	// Required: Blockchain endpoints
	if c.Ethereum.RPC == "" {
		return fmt.Errorf("Ethereum RPC required for smart contracts")
	}
	
	if c.Polygon.RPC == "" {
		return fmt.Errorf("Polygon RPC required for fast anchoring")
	}
	
	// Validate penalties are set
	if c.Penalties.MissingLogs < 100_000_000 {
		return fmt.Errorf("Missing logs penalty must be >= $100M for deterrence")
	}
	
	// Ensure whistleblower rewards are sufficient
	if c.Whistleblower.RewardPercentage < 0.15 {
		return fmt.Errorf("Whistleblower rewards must be >= 15%%")
	}
	
	// Validate Stewardship Council configuration if enabled
	if c.StewardshipCouncil.Enabled {
		if len(c.StewardshipCouncil.Members) < 6 {
			return fmt.Errorf("Stewardship Council requires 6 member institutions")
		}
		
		for _, member := range c.StewardshipCouncil.Members {
			if member.PublicKey == "" || member.EndpointURL == "" {
				return fmt.Errorf("All Stewardship Council members require public key and endpoint")
			}
		}
	}
	
	return nil
}

// GetStewardshipCouncilInfo returns information about the Stewardship Council
func (c *Config) GetStewardshipCouncilInfo() string {
	if !c.StewardshipCouncil.Enabled {
		return "Stewardship Council: Not currently enabled (can be activated as recommended enhancement)"
	}
	
	info := "Stewardship Council Configuration:\n"
	info += fmt.Sprintf("  Members: %d institutions\n", len(c.StewardshipCouncil.Members))
	info += fmt.Sprintf("  Validation Threshold: %d of %d confirmations\n", 
		c.StewardshipCouncil.ValidationThreshold, len(c.StewardshipCouncil.Members))
	
	info += "\nCouncil Members:\n"
	for _, member := range c.StewardshipCouncil.Members {
		info += fmt.Sprintf("  - %s: %s\n", member.Role, member.Institution)
	}
	
	return info
}
