"""
block.py

This module contains the Block class used in the Blockchain implementation.

Author: Peyman Kh
Date: 2024-07-12
"""
# Import libraries
import hashlib


class Block:
    """
    A class used to represent a Block in the Blockchain.

    Attributes:
        - index: The index of the block in the blockchain.
        - previous_hash: The hash of the previous block in the blockchain.
        - timestamp: The timestamp of when the block was created.
        - transactions: The transactions included in the block.
        - hash : The hash of the block.
    """

    def __init__(self, index, previous_hash, timestamp, transactions) -> None:
        """
        Initialize the class instance.

        Parameters
            - index: The index of the block in the blockchain.
            - previous_hash: The hash of the previous block in the blockchain.
            - timestamp: The timestamp of when the block was created.
            - transactions: The transactions included in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Computes the hash of the block.

        Returns:
            - str: The SHA-256 hash of the block.
        """
        hash_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(hash_string.encode()).hexdigest()

    @staticmethod
    def format_timestamp(timestamp) -> str:
        """
        Formats the timestamp to a string without microseconds.

        Parameters:
            - timestamp: The timestamp to format.

        Returns:
            - str:The formatted timestamp.
        """
        return timestamp.strftime('%Y-%m-%d %H:%M:%S')
