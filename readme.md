# Algorand Python SDK Project

This project demonstrates how to interact with the Algorand blockchain using Python. It includes scripts for account creation, payments, and atomic transfers.

## Prerequisites

- Python 3.7 or higher
- `pip` or `pipx` for package management
- An Algorand node or access to a public Algorand API (e.g., TestNet)

## Installation

### Step 1: Install the Algorand Python SDK

You can install the Algorand Python SDK using `pip` or `pipx`.

#### Using `pip`:
```bash
pip install py-algorand-sdk
```

#### Using `pipx`:
```bash
pipx install py-algorand-sdk
```
### Step 2: Clone the Repository
```bash
git clone https://github.com/marotipatre/Algorand-Python-SDK-Utility.git
cd algorand-python-sdk
```

If you encounter issues during installation, you can use the --break-system-packages attribute (useful for Linux systems):
```bash
pip install py-algorand-sdk --break-system-packages
```
### Step 3: Install Additional Dependencies
This project also uses the python-dotenv package to manage environment variables. Install it using:
```bash
pip install python-dotenv
```

Setup
Step 1: Create an Account
Run the account.py script to generate a new Algorand account:

```bash
python [account.py](http://_vscodecontentref_/1)
```

This will output:

A private key
An Algorand address
A mnemonic phrase
Step 2: Configure Environment Variables
Copy the .env.template file to .env:
```bash
cp .env.template .env
```
Open the .env file and paste your private key into the PRIVATE_KEY field:
```bash
PRIVATE_KEY=your_private_key_here
```

Ensure the Algorand node configuration matches your setup (e.g., TestNet or LocalNet).

Step 3: Run the Scripts
Payment Script
Run the payment.py script to send a payment transaction:
```bash
python payment.py
```
This will output the transaction ID and the status of the transaction.

Atomic Transfer Script
Run the atomictransfer.py script to execute a group of transactions atomically:
```bash
python atomictransfer.py
```


This will output the transaction ID and the status of the atomic transfer.

Troubleshooting
Dependency Issues: If you encounter dependency conflicts, use the --break-system-packages attribute with pip.
Environment Variables: Ensure the .env file is correctly configured and matches your Algorand node setup.
Transaction Errors: Verify that your account has sufficient funds and that the Algorand node is accessible.
Notes
Always keep your private key and mnemonic phrase secure.
Use the TestNet for development and testing before deploying to MainNet.
Resources
Algorand Developer Documentation
Algorand Python SDK GitHub

