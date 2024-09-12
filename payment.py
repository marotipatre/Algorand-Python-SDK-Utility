from algosdk import transaction, account, util
from algosdk.v2client import algod
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get private key and address from environment variables
private_key = os.getenv("PRIVATE_KEY")
address = account.address_from_private_key(private_key)
print("Address:", address)

# Get Algorand client parameters from environment variables
algod_token = os.getenv("TESTNET_ALGOD_TOKEN")
algod_url = os.getenv("TESTNET_ALGOD_URL")
algod_port = os.getenv("TESTNET_ALGOD_PORT")

# Initialize Algorand client
algod_client = algod.AlgodClient(algod_token, algod_url)

# Get suggested transaction parameters
suggested_params = algod_client.suggested_params()

# Create a payment transaction
payment_txn = transaction.PaymentTxn(
    sender=address,
    sp=suggested_params,
    amt=util.algos_to_microalgos(0.5),
    receiver="XXTICPB6WORBRVTXGBSNTLTUA2ST2EN5XMAVZPRTGY4XFFQXEBLQEPEMZM"
)

# Sign the transaction
signed_txn = payment_txn.sign(private_key)

# Send the transaction
txid = algod_client.send_transaction(signed_txn)
print(f"Txn sent: https://testnet.explorer.perawallet.app/tx/{txid}")

# Wait for transaction confirmation
result = transaction.wait_for_confirmation(algod_client, txid, 4)
print(f"Txn Confirmed in round {result['confirmed-round']}")
