// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ITMLEnforcer.sol";

/**
 * @title TML_Core
 * @notice The Constitutional Enforcement Layer for AI Governance.
 * @dev Implements the "No Log = No Action" primitive.
 */
contract TML_Core is ITMLEnforcer {
    
    // --- STATE VARIABLES ---
    address public owner;
    mapping(address => bool) public authorizedAgents; // Whitelist of AI Agents
    
    // The "Memory" of the system
    struct DecisionRecord {
        MoralState currentState;
        bytes32 logRoot;
        uint256 timestamp;
        bool isFinalized;
    }
    
    // Maps a Decision Hash (ID) to its Record
    mapping(bytes32 => DecisionRecord) public decisions;

    // --- MODIFIERS ---
    modifier onlyAgent() {
        require(authorizedAgents[msg.sender], "TML: Unauthorized Agent");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    // --- GOVERNANCE ---
    function authorizeAgent(address _agent) external {
        require(msg.sender == owner, "Only Owner");
        authorizedAgents[_agent] = true;
    }

    // --- THE CORE LOGIC ---
    
    /**
     * @notice The primary enforcement function.
     * @param _decisionId The unique hash of the decision context.
     * @param _proposedState The state the AI wants to enter (Permit/Refuse/SacredZero).
     * @param _logRoot The Merkle Root of the Moral Trace Log.
     */
    function enforceState(
        bytes32 _decisionId,
        MoralState _proposedState,
        bytes32 _logRoot
    ) external override onlyAgent returns (bool) {
        
        // 1. CHECK: No Log = No Action
        // If the log root is empty (zero bytes), we reject everything except Idle.
        if (_logRoot == bytes32(0)) {
            revert("TML: Violation - No Log Provided");
        }

        // 2. LOGIC: State Machine Transitions
        if (_proposedState == MoralState.SacredZero) {
            // ENTERING THE HOLD
            decisions[_decisionId] = DecisionRecord({
                currentState: MoralState.SacredZero,
                logRoot: _logRoot,
                timestamp: block.timestamp,
                isFinalized: false
            });
            
            // Emit the Lantern Signal 🏮
            emit LanternSignal(_decisionId, block.timestamp, "Epistemic Ambiguity Detected", msg.sender);
            return false; // Execution is PAUSED

        } else if (_proposedState == MoralState.Permit) {
            // PROCEEDING (+1)
            // Verify we are not currently in a locked Sacred Zero state without resolution
            require(decisions[_decisionId].currentState != MoralState.SacredZero, "TML: Cannot bypass Sacred Zero");

            decisions[_decisionId] = DecisionRecord({
                currentState: MoralState.Permit,
                logRoot: _logRoot,
                timestamp: block.timestamp,
                isFinalized: true
            });

            emit ActionAuthorized(_decisionId, _logRoot);
            return true; // Execution ALLOWED

        } else if (_proposedState == MoralState.Refuse) {
            // REFUSING (-1)
            decisions[_decisionId] = DecisionRecord({
                currentState: MoralState.Refuse,
                logRoot: _logRoot,
                timestamp: block.timestamp,
                isFinalized: true
            });

            emit ActionRefused(_decisionId, "Ethical Harm Threshold Exceeded");
            return false; // Execution BLOCKED
        }

        return false;
    }
}
