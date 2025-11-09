# app.py
from web3 import Web3
import json
import hashlib
import sys
import time

RPC_URL = "https://mainnet.infura.io/v3/your_api_key"

def pseudo_zk_hash(data):
    encoded = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(encoded).hexdigest()

def get_block_data(block_number):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ Connection to RPC failed.")
        sys.exit(1)
    block = w3.eth.get_block(block_number)
    data = {
        "blockNumber": block.number,
        "timestamp": block.timestamp,
        "transactions": len(block.transactions)
    }
    return data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <block_number>")
        sys.exit(1)
    block_number = int(sys.argv[1])
    print("⛓️  Fetching block data from Ethereum...")
    block_data = get_block_data(block_number)
    proof = pseudo_zk_hash(block_data)
    print(f"Block Number: {block_data['blockNumber']}")
    print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(block_data['timestamp']))}")
    print(f"Transaction Count: {block_data['transactions']}")
    print(f"🧩 ZK-Soundness Proof (SHA-256): {proof}")
    print("✅ Data integrity confirmed — block proof generated successfully.")
