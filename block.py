import hashlib
from datetime import datetime

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
    return Block(0, datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    next_index = last_block.index + 1
    return Block(next_index, datetime.now(), "Hey! I'm block " + str(next_index), last_block.hash)

def main():
    # Create the blockchain and add the genesis block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain after the genesis block
    num_of_blocks_to_add = 20

    # Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        # Log
        print("Block #{0} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}".format(block_to_add.hash))
        print(block_to_add.timestamp)
        print

if __name__ == "__main__":
    main()