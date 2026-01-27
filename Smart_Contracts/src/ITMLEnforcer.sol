// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ITMLEnforcer
 * @dev Interface for the Ternary Moral Logic Enforcement Layer.
 * Defines the strict Tri-State return values for ethical auditing.
 */
interface ITMLEnforcer {

    // The Tri-State Moral Logic
    // +1: PROCEED (Ethically Clear)
    //  0: SACRED_ZERO (Epistemic Hold / Ambiguity / Pause)
    // -1: REFUSE (Ethically Blocked / Harm Detected)
    enum MoralState { REFUSE, SACRED_ZERO, PROCEED }

    event LanternSignal(bytes32 indexed traceId, string reason, uint256 uncertaintyScore);
    event ActionPermitted(bytes32 indexed traceId, string actionType);
    event ActionBlocked(bytes32 indexed traceId, string reason);

    /**
     * @dev Core ethical evaluation function.
     * @param _traceId Unique UUID for the decision event (from the AI).
     * @param _actionParams Hash of the proposed action parameters.
     * @param _uncertaintyScore 0-100 integer representing AI confidence (Epistemic Uncertainty).
     * @return int8 The Tri-State decision (+1, 0, -1).
     */
    function evaluateAction(bytes32 _traceId, bytes32 _actionParams, uint256 _uncertaintyScore) external returns (int8);

    /**
     * @dev Check the current state of a specific moral trace.
     */
    function getTraceState(bytes32 _traceId) external view returns (int8);
}
