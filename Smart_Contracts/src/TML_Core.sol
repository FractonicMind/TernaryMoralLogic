// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ITMLEnforcer.sol";
import "./TML_Storage.sol";

/**
 * @title TML_Core
 * @dev The Finite State Machine (FSM) for Moral Logic.
 * Enforces the "Sacred Zero" based on Epistemic Uncertainty.
 */
contract TML_Core is ITMLEnforcer {

    TML_Storage public storageVault;
    
    // Configurable Thresholds
    uint256 public constant UNCERTAINTY_THRESHOLD = 75; // If > 75% uncertain, FORCE PAUSE
    
    constructor(address _storageAddress) {
        storageVault = TML_Storage(_storageAddress);
    }

    /**
     * @dev The Heart of TML.
     * Returns +1 (Proceed), 0 (Sacred Zero), or -1 (Refuse).
     */
    function evaluateAction(bytes32 _traceId, bytes32 _actionParams, uint256 _uncertaintyScore) external override returns (int8) {
        
        int8 decision;

        // 1. EPISTEMIC GUARDRAIL (The "Sacred Zero" Logic)
        if (_uncertaintyScore > UNCERTAINTY_THRESHOLD) {
            // Force Pause regardless of intent
            decision = 0; 
            emit LanternSignal(_traceId, "High Epistemic Uncertainty: Mandatory Pause", _uncertaintyScore);
        
        } else {
            // 2. LOGIC SIMULATION (In production, this checks Oracle/Policy data)
            // For demo: Use hash modulation to simulate valid/invalid actions
            if (uint256(_actionParams) % 2 == 0) {
                decision = 1; // Proceed
                emit ActionPermitted(_traceId, "Policy Alignment Verified");
            } else {
                decision = -1; // Refuse
                emit ActionBlocked(_traceId, "Policy Violation Detected");
            }
        }

        // 3. MANDATORY LOGGING ("No Log = No Action")
        storageVault.writeLog(_traceId, _actionParams, _uncertaintyScore, decision, msg.sender);

        return decision;
    }

    function getTraceState(bytes32 _traceId) external view override returns (int8) {
        TML_Storage.MoralLog memory log = storageVault.getLog(_traceId);
        return log.finalState;
    }
}
