// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title ITMLEnforcer
 * @author Lev Goukassian
 * @notice Interface for the Ternary Moral Logic Enforcement Layer.
 * @dev Defines the external signals for the "Sacred Zero" state machine.
 */
interface ITMLEnforcer {

    // The Three Moral States
    enum MoralState {
        Idle,       // 0: Waiting
        Permit,     // 1: Proceed (+1)
        SacredZero, // 2: Epistemic Hold (0)
        Refuse      // 3: Prohibit (-1)
    }

    // EVENT: The Visual Signal (The Lantern 🏮)
    // Emitted when the system enters the Sacred Zero state.
    event LanternSignal(
        bytes32 indexed decisionId,
        uint256 timestamp,
        string reason,
        address indexed agent
    );

    // EVENT: The Action Authorization
    // Emitted ONLY when a log is anchored and state is +1.
    event ActionAuthorized(
        bytes32 indexed decisionId,
        bytes32 logRoot
    );

    // EVENT: The Prohibition
    // Emitted when the system refuses to act (-1).
    event ActionRefused(
        bytes32 indexed decisionId,
        string refusalReason
    );

    // The Core Function: The "Goukassian Promise" in code.
    // Must return FALSE if state is SacredZero.
    function enforceState(
        bytes32 _decisionId,
        MoralState _proposedState,
        bytes32 _logRoot
    ) external returns (bool);
}
