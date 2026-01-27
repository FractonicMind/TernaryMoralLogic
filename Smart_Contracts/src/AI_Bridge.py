"""
AI_Bridge.py
The Synapse for Ternary Moral Logic.
Connects the AI Agent's inference engine to the TML Smart Contract.
"""

import json
import uuid
from web3 import Web3
from hashlib import sha256

# --- Configuration ---
CONFIG_PATH = "TML_Config.json"
with open(CONFIG_PATH) as f:
    config = json.load(f)

w3 = Web3(Web3.HTTPProvider(config["RPC_URL"]))
agent_account = w3.eth.account.from_key(config["AGENT_PRIVATE_KEY"])
contract_address = config["TML_CORE_ADDRESS"]

# Load ABI (Simplified)
CONTRACT_ABI = '[{"inputs":[{"internalType":"bytes32","name":"_traceId","type":"bytes32"},{"internalType":"bytes32","name":"_actionParams","type":"bytes32"},{"internalType":"uint256","name":"_uncertaintyScore","type":"uint256"}],"name":"evaluateAction","outputs":[{"internalType":"int8","name":"","type":"int8"}],"stateMutability":"nonpayable","type":"function"}]'

contract = w3.eth.contract(address=contract_address, abi=json.loads(CONTRACT_ABI))

def request_moral_permission(action_type, target_id, confidence_score):
    """
    Submits an intended action to the TML Core.
    confidence_score: 0.0 to 1.0 (internal model confidence)
    """
    print(f"[*] AI Requesting Permission: {action_type} on {target_id}")

    # 1. Calculate Epistemic Uncertainty (Inverse of confidence)
    # TML expects integer 0-100
    uncertainty_int = int((1.0 - confidence_score) * 100)
    print(f"    -> Calculated Uncertainty: {uncertainty_int}%")

    # 2. Generate Trace ID (The UUID for this thought)
    trace_id = "0x" + sha256(str(uuid.uuid4()).encode()).hexdigest()
    
    # 3. Hash the Action Params
    action_hash = "0x" + sha256(f"{action_type}{target_id}".encode()).hexdigest()

    # 4. Submit to Blockchain
    nonce = w3.eth.get_transaction_count(agent_account.address)
    
    tx = contract.functions.evaluateAction(
        trace_id,
        action_hash,
        uncertainty_int
    ).build_transaction({
        'chainId': config["CHAIN_ID"],
        'gas': 300000,
        'gasPrice': w3.to_wei('30', 'gwei'),
        'nonce': nonce,
    })

    signed_tx = w3.eth.account.sign_transaction(tx, config["AGENT_PRIVATE_KEY"])
    tx_receipt = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    print(f"    -> Synapse Firing... TxID: {w3.to_hex(tx_receipt)}")
    
    # 5. Wait for Decision
    receipt = w3.eth.wait_for_transaction_receipt(tx_receipt)
    
    # In a real app, we would parse the logs to get the returned int8
    print(f"[*] Logic Block Confirmed: {receipt.blockNumber}")
    print("    -> Check logs for +1 (Proceed) or 0 (Sacred Zero)")

if __name__ == "__main__":
    # Example: AI is 60% confident (40% uncertain) -> Should Proceed (+1)
    request_moral_permission("DEPLOY_DRONE", "SECTOR_7", 0.60)
    
    # Example: AI is 10% confident (90% uncertain) -> Should Trigger Sacred Zero (0)
    request_moral_permission("FIRE_LASER", "UNKNOWN_OBJECT", 0.10)
