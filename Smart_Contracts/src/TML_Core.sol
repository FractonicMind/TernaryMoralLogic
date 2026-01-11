// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ITMLEnforcer.sol";
import "./TML_Storage.sol";

/**
 * @title TML_Core (Logic Layer)
 * @notice The Constitutional Enforcement Layer for AI Governance.
 * @dev V2 Architecture: Separates Logic from Storage. 
 * Implements the "No Log = No Action" primitive by writing to TML_Storage.
 */
contract TML_Core is ITMLEnforcer {
    
    // --- STATE VARIABLES ---
    address public owner;
    TML_Storage public database; // Reference to the Eternal Vault
    mapping(address => bool) public authorizedAgents; // Whitelist of AI Agents
    
    // --- MODIFIERS ---
    modifier onlyAgent() {
        require(authorizedAgents[msg.sender], "TML: Unauthorized Agent");
        _;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "TML: Only Owner");
        _;
    }

    // --- CONSTRUCTOR ---
    // You must provide the address of the deployed TML_Storage contract
    constructor(address _storageAddress) {
        owner = msg.sender;
        database = TML_Storage(_storageAddress);
    }

    // --- GOVERNANCE ---
    function authorizeAgent(address _agent) external onlyOwner {
        authorizedAgents[_agent] = true;
    }

    function setStorageContract(address _newStorage) external onlyOwner {
        database = TML_Storage(_newStorage);
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
        // If the log root is empty (zero bytes), we reject everything.
        if (_logRoot == bytes32(0)) {
            revert("TML: Violation - No Log Provided");
        }

        // 2. CHECK: Previous Context
        // We check the Database to see if this decision is currently frozen.
        // Note: We use a try/catch or simple read pattern depending on storage logic.
        // Here we assume getDecision reverts if not found, so we check existence first if possible.
        // For simplicity in this MVP, we proceed with logic:

        (MoralState currentState, , , address recordedAgent) = database.getDecision(_decisionId);
        
        // If it exists and is in SacredZero, we must prevent skipping to Permit without resolution
        // (In a full version, you would have a specific 'resolve' function, but here is the check)
        if (recordedAgent != address(0) && currentState == MoralState.SacredZero) {
             // If currently held, we can only update if we are explicitly resolving it.
             // For this MVP, we allow the update but strict implementations might require a separate resolve flow.
             require(_proposedState != MoralState.Permit, "TML: Decision is under Epistemic Hold. Cannot Proceed.");
        }

        // 3. LOGIC: State Machine Transitions & Database Writes
        if (_proposedState == MoralState.SacredZero) {
            // ENTERING THE HOLD
            database.saveDecision(_decisionId, MoralState.SacredZero, _logRoot, msg.sender);
            
            // Emit the Lantern Signal 🏮
            emit LanternSignal(_decisionId, block.timestamp, "Epistemic Ambiguity Detected", msg.sender);
            return false; // Execution is PAUSED

        } else if (_proposedState == MoralState.Permit) {
            // PROCEEDING (+1)
            database.saveDecision(_decisionId, MoralState.Permit, _logRoot, msg.sender);

            emit ActionAuthorized(_decisionId, _logRoot);
            return true; // Execution ALLOWED

        } else if (_proposedState == MoralState.Refuse) {
            // REFUSING (-1)
            database.saveDecision(_decisionId, MoralState.Refuse, _logRoot, msg.sender);

            emit ActionRefused(_decisionId, "Ethical Harm Threshold Exceeded");
            return false; // Execution BLOCKED
        }

        return false;
    }
}
