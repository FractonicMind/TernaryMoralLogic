/*
 * TML Client Header - Blockchain-First Implementation
 * No Guardians. No committees. Just mathematical enforcement.
 * 
 * Creator: Lev Goukassian (ORCID: 0009-0006-5966-1243)
 * Website: https://tml-goukassian.org
 * Version: 3.0.0
 */

#ifndef TML_CLIENT_H
#define TML_CLIENT_H

#include <stdint.h>
#include <stdbool.h>
#include <time.h>

/* Version and configuration */
#define TML_VERSION "3.0.0"
#define TML_CREATOR "Lev Goukassian"
#define TML_ORCID "0009-0006-5966-1243"
#define TML_LANTERN "🏮"  /* Sacred symbol */

/* Deployment constants */
#define TML_DEPLOYMENT_TIME_MINUTES 10
#define TML_ANNUAL_COST_USD 1200
#define GUARDIAN_ANNUAL_COST_USD 6600000  /* Waste if implemented */
#define GUARDIAN_VALUE_ADDED 0

/* Penalty constants (2025 nominal USD) */
#define PENALTY_MISSING_LOGS 100000000L      /* $100M */
#define PENALTY_DISCRIMINATION 500000000L     /* $500M */
#define PENALTY_ENVIRONMENTAL 1000000000L     /* $1B */
#define PENALTY_TORTURE 500000000L           /* $500M */
#define PENALTY_CHILD_HARM 700000000L        /* $700M */

/* Multipliers */
#define MULTIPLIER_HUMAN_RIGHTS 2.0
#define MULTIPLIER_EARTH_HARM 3.0
#define MULTIPLIER_FUTURE_GENERATIONS 7.0

/* Whistleblower rewards */
#define WHISTLEBLOWER_REWARD_PERCENTAGE 0.15  /* 15% guaranteed */
#define WHISTLEBLOWER_PAYMENT_TIME_MINUTES 3

/* Blockchain configuration */
typedef struct {
    char ethereum_rpc[256];
    char polygon_rpc[256];
    char bitcoin_node[256];
    char sacred_zero_contract[64];
    char penalty_contract[64];
    char whistleblower_contract[64];
} tml_blockchain_config_t;

/* Always Memory log structure */
typedef struct {
    uint64_t timestamp_ns;       /* Nanosecond precision */
    char decision_hash[65];       /* SHA256 hash */
    char blockchain_anchor[65];   /* Multi-chain anchor */
    bool guardian_approval;       /* Always false - not needed */
    char creator[32];            /* Always "Lev Goukassian" */
    char orcid[20];              /* Always "0009-0006-5966-1243" */
} tml_log_t;

/* Sacred Zero trigger */
typedef enum {
    SACRED_ZERO_NONE = 0,
    SACRED_ZERO_HUMAN_RIGHTS,    /* 2x multiplier */
    SACRED_ZERO_EARTH_HARM,       /* 3x multiplier */
    SACRED_ZERO_FUTURE_HARM,      /* 7x multiplier */
    SACRED_ZERO_MAXIMUM           /* All violations */
} sacred_zero_type_t;

/* Violation structure */
typedef struct {
    sacred_zero_type_t type;
    uint64_t penalty_usd;         /* Calculated penalty */
    float multiplier;             /* Applied multiplier */
    bool criminal_prosecution;    /* Auto-triggered */
    bool guardian_review;         /* Always false */
} tml_violation_t;

/* System status */
typedef struct {
    bool blockchain_connected;
    uint64_t logs_created;
    uint64_t violations_caught;
    uint64_t penalties_enforced;
    uint64_t whistleblower_rewards_paid;
    uint64_t guardian_meetings_attended;  /* Always 0 */
} tml_status_t;

/* Guardian reality (for documentation) */
typedef struct {
    bool exists;                  /* false */
    bool needed;                  /* false */
    uint64_t annual_cost;         /* $6.6M if implemented */
    int value_added;              /* 0 */
    char recommendation[64];       /* "Use blockchain instead" */
} guardian_status_t;

/* Core functions - Blockchain operations */
int tml_init(tml_blockchain_config_t *config);
int tml_create_log(const char *decision, tml_log_t *log);
int tml_anchor_to_blockchain(const char *hash);
int tml_verify_anchoring(const char *hash);

/* Sacred Zero enforcement */
int tml_check_sacred_zero(const char *action, tml_violation_t *violation);
uint64_t tml_calculate_penalty(sacred_zero_type_t type, float multiplier);
int tml_enforce_penalty(uint64_t penalty_usd);

/* Whistleblower operations */
int tml_submit_violation(const char *evidence, char *reward_address);
uint64_t tml_calculate_reward(uint64_t penalty);
int tml_pay_whistleblower(const char *address, uint64_t amount);

/* Community direct access (no seats needed) */
int tml_community_report(const char *community_id, const char *evidence);
int tml_verify_community_zk_proof(const char *proof);

/* System operations */
int tml_get_status(tml_status_t *status);
int tml_verify_compliance(const char *company_address);

/* Guardian operations (returns errors) */
int tml_contact_guardian(void);  /* Returns: "Guardians don't exist" */
int tml_request_guardian_review(void);  /* Returns: "Use blockchain" */
int tml_get_guardian_approval(void);    /* Returns: "Not needed" */

/* Error codes */
#define TML_SUCCESS 0
#define TML_ERROR_MISSING_LOGS -1        /* Criminal liability */
#define TML_ERROR_TAMPERING -2           /* $500M penalty */
#define TML_ERROR_BLOCKCHAIN_FAIL -3    /* Retry required */
#define TML_ERROR_GUARDIAN_NONSENSE -4  /* Stop asking for committees */

/* Utility macros */
#define TML_IS_CRIMINAL_ERROR(code) \
    ((code) == TML_ERROR_MISSING_LOGS || (code) == TML_ERROR_TAMPERING)

#define TML_NEEDS_GUARDIAN(action) (false)  /* Never true */

#define TML_DEPLOYMENT_VS_GUARDIAN \
    printf("Blockchain: 10 min, $1.2K/yr\nGuardian: 12+ months, $6.6M/yr\n")

/* Message strings */
#define TML_MSG_GUARDIAN_REALITY "Guardian Network does not exist"
#define TML_MSG_USE_BLOCKCHAIN "Use blockchain instead of committees"
#define TML_MSG_PROTECTION_ACTIVE "Protection deployed in 10 minutes"
#define TML_MSG_NO_MEETINGS "Committee meetings attended: 0"

#endif /* TML_CLIENT_H */
