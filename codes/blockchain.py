"""
blockchain.py

This module contains the Blockchain class and demonstrates its usage.

Author: Peyman Kh
Date: 2024-07-12
"""

import datetime as date
from block import Block


class Blockchain:
    """
    A class used to represent the Blockchain.

    Attributes:
        - chain: The list of blocks in the blockchain.
    """

    def __init__(self) -> None:
        """
        Initializes the blockchain with the genesis block.
        """
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block() -> Block:
        """
        Creates the genesis block.

        Returns:
            - Block: The genesis block.
        """
        # Create the genesis block with index 0, current timestamp, a dummy transaction, and previous hash of 0
        return Block(0, "0", Block.format_timestamp(date.datetime.now()), "Genesis Block")

    def get_last_block(self) -> Block:
        """
        Retrieves the last block in the blockchain.

        Returns:
            - Block: The last block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, transactions: str) -> None:
        """
        Adds a new block to the blockchain with the given transactions.

        Parameters:
            - transactions: The transactions to include in the new block.
        """
        last_block = self.get_last_block()
        new_block = Block(
            index=last_block.index + 1,
            previous_hash=last_block.hash,
            timestamp=Block.format_timestamp(date.datetime.now()),
            transactions=transactions
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """
        Validates the blockchain.

        Returns:
            - bool: True if the blockchain is valid, False otherwise.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.compute_hash():
                return False

            # Check if the current block's previous hash matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self) -> None:
        """
        Displays the blockchain.
        """
        for block in self.chain:
            print(f"Block {block.index} [{block.timestamp}]")
            print(f"Transactions: {block.transactions}")
            print(f"Current Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print("-" * 30)


# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block("First transaction")
    blockchain.add_block("Second transaction")

    blockchain.display_chain()
