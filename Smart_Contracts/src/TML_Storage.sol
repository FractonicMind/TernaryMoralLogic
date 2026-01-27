// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TML_Storage
 * @dev Immutable storage for Moral Trace Logs.
 * Implements the "Always Memory" pattern.
 */
contract TML_Storage {

    struct MoralLog {
        uint256 timestamp;
        bytes32 actionHash;
        uint256 uncertaintyScore;
        int8 finalState;   // +1, 0, -1
        address agent;     // The AI Agent (wallet) that requested it
    }

    // Maps Trace ID -> Moral Log
    mapping(bytes32 => MoralLog) private logs;
    
    address public moralKernel;
    address public governance;

    modifier onlyKernel() {
        require(msg.sender == moralKernel, "TML_Storage: Only Kernel");
        _;
    }

    constructor() {
        governance = msg.sender;
    }

    function setMoralKernel(address _kernel) external {
        require(msg.sender == governance, "TML_Storage: Only Governance");
        moralKernel = _kernel;
    }

    /**
     * @dev Writes the moral decision to history.
     */
    function writeLog(bytes32 _traceId, bytes32 _actionHash, uint256 _score, int8 _state, address _agent) external onlyKernel {
        require(logs[_traceId].timestamp == 0, "TML_Storage: Trace ID collision");
        
        logs[_traceId] = MoralLog({
            timestamp: block.timestamp,
            actionHash: _actionHash,
            uncertaintyScore: _score,
            finalState: _state,
            agent: _agent
        });
    }

    function getLog(bytes32 _traceId) external view returns (MoralLog memory) {
        return logs[_traceId];
    }
}
