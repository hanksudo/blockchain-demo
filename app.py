import hashlib
import json
from datetime import datetime

import requests
from flask import Flask, request

node = Flask(__name__)

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdigest()


def create_genesis_block():
    # Manually construct a block with `index zero` and arbitrary `previous hash`
    return Block(0, datetime.now(), {
        "proof-of-work": 9,
        "transactions": None
    }, "0")

def next_block(last_block):
    next_index = last_block.index + 1
    return Block(next_index, datetime.now(), "Hey! I'm block " + str(next_index), last_block.hash)


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Store url data of every other node in the network so that we can communicate with them
peer_nodes = []

# Store the transactions this node has in a list.
node_transactions = []

@node.route("/txion", methods=["POST"])
def transaction():
    # Extract transaction data
    new_txion = request.get_json()
    # Add transaction to list
    node_transactions.append(new_txion)

    # Log
    print("New transaction")
    print("FROM: {}".format(new_txion["from"]))
    print("TO: {}".format(new_txion["to"]))
    print("AMOUNT: {}\n".format(new_txion["amount"]))

    return "Transaction submission successful\n"

miner_address = "d41d8cd98-random-miner-address-f00b204e9"

def proof_of_work(last_proof):
    # Create a variable that we will use to find our next proof of work
    incrementor = last_proof + 1

    # Keep incrementing the incrementor until it's equal to a number divisible by 9
    # and the proof of work of the previous block in the chain
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    # Once that number is found, we can return it as a proof of our work
    return incrementor

@node.route("/mine", methods=["GET"])
def mine():
    # Get the last proof of work
    last_block = blockchain[len(blockchain) - 1]
    last_proof = last_block.data["proof-of-work"]

    # Find the proof of work for the current block being mined
    # Note: program will hang here until a new proof of work is found
    proof = proof_of_work(last_proof)

    # Once we find a valid proof of work, we know we can mine a block
    # so we reward the miner by adding a transaction
    node_transactions.append({
        "from": "network",
        "to": miner_address,
        "amount": 1
    })

    # Now we can gather the data needed to create the new block
    new_block_data = {
        "proof-of-work": proof,
        "transactions": node_transactions
    }
    new_block_index = last_block.index + 1
    new_block_timestamp = datetime.now()
    last_block_hash = last_block.hash

    # Empty transaction list
    node_transactions[:] = []

    # Now create the new block!
    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )

    blockchain.append(mined_block)

    return json.dumps({
        "index": new_block_index,
        "timestamp": str(new_block_timestamp),
        "data": new_block_data,
        "hash": last_block_hash
    }) + "\n"

@node.route("/blocks", methods=["GET"])
def get_blocks():
    return json.dumps(list({
        "index": str(block.index),
        "timestamp": str(block.timestamp),
        "data": str(block.data),
        "hash": block.hash
    } for block in blockchain))

def find_new_chains():
    # Get the blockchains of every other node
    other_chains = []
    for node_url in peer_nodes:
        # Get chains
        block = requests.get(node_url + "/blocks").json()
        other_chains.append(block)
    return other_chains

def consensus():
    # Get blocks from other nodes
    other_chains = find_new_chains()
    # If our chain not longest, then we store the longest chain
    longest_chain = blockchain
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain

    blockchain = longest_chain