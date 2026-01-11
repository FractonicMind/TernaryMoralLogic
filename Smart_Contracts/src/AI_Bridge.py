import json
import time
from web3 import Web3

# --- CONFIGURATION ---
# In a real scenario, this connects to a node like Infura or Alchemy
RPC_URL = "http://127.0.0.1:8545" 
CONTRACT_ADDRESS = "0x..." # Paste address after deployment
PRIVATE_KEY = "0x..."      # The AI Agent's Wallet Key

# Initialize Connection
w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIVATE_KEY)

def load_contract():
    # Load the ABI (Application Binary Interface) from the JSON file
    with open('TML_Config.json') as f:
        config = json.load(f)
    return w3.eth.contract(address=config['address'], abi=config['abi'])

def trigger_sacred_zero(decision_id, log_hash):
    """
    The AI is unsure. It calls the blockchain to Lock itself.
    """
    contract = load_contract()
    
    print(f"⚠️  AMBIGUITY DETECTED. ID: {decision_id}")
    print(f"🏮 Triggering Sacred Zero...")

    # Build Transaction: State 2 = SacredZero
    tx = contract.functions.enforceState(
        decision_id,
        2, 
        log_hash
    ).build_transaction({
        'from': account.address,
        'nonce': w3.eth.get_transaction_count(account.address),
        'gas': 200000,
        'gasPrice': w3.to_wei('20', 'gwei')
    })

    # Sign and Send
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    print(f"✅ Sacred Pause Anchored on Ethereum. Tx: {tx_hash.hex()}")
    return tx_hash.hex()

# --- SIMULATION ---
if __name__ == "__main__":
    # Mock Data
    mock_id = w3.keccak(text="Medical_Triage_Patient_001")
    mock_log = w3.keccak(text="Log_Data_Patient_Vital_Signs")

    trigger_sacred_zero(mock_id, mock_log)
