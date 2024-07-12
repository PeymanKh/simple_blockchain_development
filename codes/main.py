"""
main.py

This module initializes a blockchain and adds five blocks to it.

Author: Peyman Kh
Date: 2024-07-12
"""

from blockchain import Blockchain


def main():
    # Initialize the blockchain
    blockchain = Blockchain()

    # Add 5 blocks with dummy transactions
    transactions = [
        "First transaction",
        "Second transaction",
        "Third transaction",
        "Fourth transaction",
        "Fifth transaction"
    ]

    for transaction in transactions:
        blockchain.add_block(transaction)

    # Display the blockchain
    blockchain.display_chain()

    # Validate the blockchain
    is_valid = blockchain.is_chain_valid()
    print(f"Blockchain valid? {is_valid}")


if __name__ == "__main__":
    main()
