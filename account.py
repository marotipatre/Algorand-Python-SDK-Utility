from algosdk import account, mnemonic

# Generate an Algorand account
private_key, address = account.generate_account()

print("Private Key:", private_key)
print("Address:", address)

# Convert private key to mnemonic
mnemonic_phrase = mnemonic.from_private_key(private_key)
print("Mnemonic Phrase:", mnemonic_phrase)

# Derive private key from mnemonic
derived_private_key = mnemonic.to_private_key(mnemonic_phrase)
print("Private Key Derived from Mnemonic:", derived_private_key)

# Compare the original private key with the derived private key
print("Comparison Between Original and Derived Private Keys:", private_key == derived_private_key)
