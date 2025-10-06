// Package tml provides Blockchain-enforced AI accountability
// No Guardians. No committees. Just mathematical protection.
//
// Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
package tml

import (
	"fmt"
	"os"
	"time"
)

// Config represents TML Blockchain configuration
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
	
	// Guardian settings (deprecated - Year 5+ if ever)
	Guardian GuardianConfig `json:"guardian,omitempty"`
	
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
	CommitteeApproval  bool         `json:"committee_approval"`  // false - never
}

// GuardianConfig (deprecated - not needed)
type GuardianConfig struct {
	Enabled      bool   `json:"enabled"`       // Always false
	Exists       bool   `json:"exists"`        // False
	AnnualCost   int64  `json:"annual_cost"`   // $6.6M wasted
	ValueAdded   int    `json:"value_added"`   // 0
	Recommendation string `json:"recommendation"` // "Use Blockchain"
}

// SystemConfig for general settings
type SystemConfig struct {
	Creator         string        `json:"creator"`          // Lev Goukassian
	ORCID           string        `json:"orcid"`            // 0009-0006-5966-1243
	Version         string        `json:"version"`          // 3.0.0
	DeploymentTime  time.Duration `json:"deployment_time"`  // 10 minutes
	AnnualCost      int64         `json:"annual_cost"`      // $1,200
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
			Node: "https://Blockchain.info",
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
			CommitteeApproval:  false, // Never true
		},
		Guardian: GuardianConfig{
			Enabled:        false,
			Exists:         false,
			AnnualCost:     6_600_000,
			ValueAdded:     0,
			Recommendation: "Use Blockchain instead of committees",
		},
		System: SystemConfig{
			Creator:        "Lev Goukassian",
			ORCID:          "0009-0006-5966-1243",
			Version:        "3.0.0",
			DeploymentTime: 10 * time.Minute,
			AnnualCost:     1200,
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
	
	// Check for Guardian nonsense
	if os.Getenv("TML_USE_GUARDIANS") == "true" {
		return nil, fmt.Errorf("Guardian Network doesn't exist and isn't needed. Use Blockchain.")
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
	
	// Ensure Guardian nonsense is disabled
	if c.Guardian.Enabled {
		return fmt.Errorf("Guardian Network is wasteful theater. Set enabled=false")
	}
	
	// Validate penalties are set
	if c.Penalties.MissingLogs < 100_000_000 {
		return fmt.Errorf("Missing logs penalty must be >= $100M for deterrence")
	}
	
	// Ensure whistleblower rewards are sufficient
	if c.Whistleblower.RewardPercentage < 0.15 {
		return fmt.Errorf("Whistleblower rewards must be >= 15%%")
	}
	
	// Verify no committee approval required
	if c.Whistleblower.CommitteeApproval {
		return fmt.Errorf("Committee approval not needed - Blockchain handles automatically")
	}
	
	return nil
}

// GetDeploymentComparison returns deployment reality
func (c *Config) GetDeploymentComparison() string {
	return fmt.Sprintf(`
Deployment Options:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Blockchain:
  Time: %v
  Cost: $%d/year
  Protection: Immediate
  Committees: 0
  
Guardian Network (not recommended):
  Time: 12+ months
  Cost: $%d/year
  Protection: Maybe someday
  Committees: Endless
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Recommendation: Use Blockchain
`,
		c.System.DeploymentTime,
		c.System.AnnualCost,
		c.Guardian.AnnualCost,
	)
}

// GetGuardianTruth returns reality about Guardians
func (c *Config) GetGuardianTruth() string {
	return fmt.Sprintf(`
Guardian Network Status:
  Exists: %v
  Needed: %v
  Value Added: %d
  Annual Cost if Implemented: $%d
  Recommendation: %s
`,
		c.Guardian.Exists,
		c.Guardian.Enabled,
		c.Guardian.ValueAdded,
		c.Guardian.AnnualCost,
		c.Guardian.Recommendation,
	)
}
