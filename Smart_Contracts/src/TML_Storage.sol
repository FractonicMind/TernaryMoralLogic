// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ITMLEnforcer.sol";

/**
 * @title TML_Storage
 * @notice The Eternal Database for Ternary Moral Logic.
 * @dev Separates data from logic. If TML_Core is replaced/upgraded, 
 * this contract REMAINS, preserving the Moral Trace Logs forever.
 */
contract TML_Storage {

    // --- DATA STRUCTURES ---
    struct DecisionRecord {
        ITMLEnforcer.MoralState currentState;
        bytes32 logRoot;
        uint256 timestamp;
        address agent; // Who made the decision?
        bool exists;
    }

    // --- STATE VARIABLES ---
    address public owner;
    address public latestCoreContract; // The only contract allowed to write
    
    // The Immutable History
    mapping(bytes32 => DecisionRecord) public history;

    // --- EVENTS ---
    event CoreContractUpdated(address indexed newCore);

    // --- MODIFIERS ---
    modifier onlyOwner() {
        require(msg.sender == owner, "Storage: Only Owner");
        _;
    }

    modifier onlyCore() {
        require(msg.sender == latestCoreContract, "Storage: Only Core Logic can write");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    // --- CONFIGURATION ---
    /**
     * @notice Point this storage to the valid Logic contract.
     * @dev Allows upgrading the logic without losing data.
     */
    function setCoreContract(address _newCore) external onlyOwner {
        latestCoreContract = _newCore;
        emit CoreContractUpdated(_newCore);
    }

    // --- WRITE FUNCTIONS (Restricted) ---
    
    function saveDecision(
        bytes32 _decisionId,
        ITMLEnforcer.MoralState _state,
        bytes32 _logRoot,
        address _agent
    ) external onlyCore {
        history[_decisionId] = DecisionRecord({
            currentState: _state,
            logRoot: _logRoot,
            timestamp: block.timestamp,
            agent: _agent,
            exists: true
        });
    }

    // --- READ FUNCTIONS (Public) ---
    
    function getDecision(bytes32 _decisionId) external view returns (
        ITMLEnforcer.MoralState, 
        bytes32, 
        uint256, 
        address
    ) {
        require(history[_decisionId].exists, "Storage: Decision not found");
        DecisionRecord memory r = history[_decisionId];
        return (r.currentState, r.logRoot, r.timestamp, r.agent);
    }
}
