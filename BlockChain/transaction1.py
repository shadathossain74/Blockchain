from  bitcoinlib.transactions  import Transaction
from bitcoinlib.keys import Key


private_key= Key()
reciver_key=Key()

print("this is private")
print(private_key.wif())
print("this address:",private_key.address())

tx=Transaction()
previous_txid="11"*32
tx.add_input(
prev_txid=previous_txid,
output_n=0,
keys=private_key,
value=1000,
address=private_key.address(),
)
tx.add_output(
address=reciver_key.address(),
value=20,
)
tx.sign(
    keys=private_key,
    index_n=0
)


print(tx.raw().hex())