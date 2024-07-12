# Blockchain Implementation with Python

Blockchain technology has been transforming technology and finance with its decentralized, secure, and immutable transaction system. It has the potential to revolutionize various industries, including finance, healthcare, and supply chain management. In this project, we develop a simple blockchain from scratch using Python to understand the concept better.

![AdobeStock_280230556-scaled](https://github.com/user-attachments/assets/2b2ef2f6-bb60-4754-8789-7b76c2d5094e)

# Table of Contents
- [1. Blockchain Components](#blockchain)
- [2. Project Structure](#structure)
- [3. Installation and Setup](#installation)
- [4. Usage](#usage)
- [5. Example Output](#output)


<a name="blockchain"></a>
# 1. Blockchain Components
A blockchain consists of several key components:
1. ***Distributed Ledger***: A decentralized database that records all blockchain transactions or data.
2. ***Blocks***: These are data units containing a set of transactions, linked sequentially to form a chain.
3. ***Cryptographic Hash:***: A digital signature for each block, ensuring the block’s integrity and linking it securely to the previous block.
4. ***Consensus Mechanism:***: The process by which the network agrees on the validity of new transactions and blocks.
5. ***Mining***: The competitive process where participants solve complex puzzles to add new blocks to the blockchain, earning rewards for their effort


<a name="structure"></a>
# 2. Project Structure
The project codes consists of the following files:
- `block.py`: Contains the `Block` class, which represents a single block in the blockchain.
- `blockchain.py`: Contains the `Blockchain` class, which manages the chain of blocks.
- `main.py`: Demonstrates how to use the `Blockchain` class by adding blocks and displaying the blockchain.


<a name="installation"></a>
# 3. Installation and Setup
To run this project, you need to have Python installed. Follow the steps below to set up the project:
1. Clone the repository:
    ```bash
    git clone https://github.com/PeymanKh/simple_blockchain_implementation.git
    cd simple_blockchain_implementation
    ```
2. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

<a name="usage"></a>
# 4. Usage
To run the blockchain implementation and see it in action, execute the `main.py` script:
```bash
python main.py
```

<a name="output"></a>

## 5. Example Output
![Screenshot 2024-07-12 at 23 49 09](https://github.com/user-attachments/assets/307468b3-1347-4857-b49c-1d410dd06b26)
