from bitcoinlib.transactions import Transaction
from bitcoinlib.keys import Key


# Generate a private key
private_key = Key()

print("Private key:", private_key.wif())
print("Bitcoin address:", private_key.address())


# Create transaction
tx = Transaction()


# Fake previous transaction ID for laboratory demonstration
prev_txid = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"


# Add input
tx.add_input(
    prev_txid=prev_txid,
    output_n=0
)


# Add output
tx.add_output(
    value=100000,
    address=private_key.address()
)


# Sign transaction
tx.sign(
    private_key,
    index_n=0,
    hash_type=1
)


# Display signed transaction
print("\nSigned transaction:")
print(tx.raw().hex())