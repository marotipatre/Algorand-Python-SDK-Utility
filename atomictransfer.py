from algosdk.v2client.algod import AlgodClient

import algokit_utils
from algosdk.transaction import (
    PaymentTxn,
    AssetOptInTxn,
    AssetTransferTxn,
    calculate_group_id,
)

# Algorand node API parameters
ALGOD_API_ADDR = "https://testnet-api.algonode.cloud"
ALGOD_API_TOKEN = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# Create an instance of the Algod client
algod_client = AlgodClient(ALGOD_API_TOKEN, ALGOD_API_ADDR)

# wallet creation
src_account = algokit_utils.get_account_from_mnemonic(
    "cricket accuse punch auction border soccer enter weird magic engine possible brown auction enter brave robust dutch daughter energy deer brand kind science above forum"
)
receiver_wallet = algokit_utils.get_account_from_mnemonic(
    "mule shock blur finish drive unveil yard citizen phrase advice saddle mirror laptop huge object seed pizza inch inmate open legend effort laugh able purse"
)

trans_params = algod_client.suggested_params()


# Create a transaction group

# First Transaction

payment_tx = PaymentTxn(
    sender=src_account.address,
    receiver=receiver_wallet.address,
    amt=1,
    note=b"pay message",
    sp=trans_params,
)

# second Transaction

asset_opt_in_tx = AssetOptInTxn(
    sender=receiver_wallet.address, index=6653571999, sp=trans_params
)

# third transaction

asset_transfer_tx = AssetTransferTxn(
    sender=src_account.address,
    receiver=receiver_wallet.address,
    index=665357197,
    amt=1,
    sp=trans_params,
)

# Compute the group ID and assign it to each transaction
group_id = calculate_group_id([payment_tx, asset_opt_in_tx, asset_transfer_tx])

payment_tx.group = group_id
asset_opt_in_tx.group = group_id
asset_transfer_tx.group = group_id

# Sign each transaction with the appropriate account
signed_tx1 = payment_tx.sign(src_account.private_key)
signed_tx2 = asset_opt_in_tx.sign(receiver_wallet.private_key)
signed_tx3 = asset_transfer_tx.sign(src_account.private_key)

# Submit the group of signed transactions
try:
    txid = algod_client.send_transactions([signed_tx1, signed_tx2, signed_tx3])
    print(f"Transaction ID: {txid}")

except Exception as e:
    print(f"Error: {e}")
