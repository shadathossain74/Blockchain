import hashlib
import time

class Block:
    def __init__(self,transaction,previous_hash):
        self.timestamp=time.time()
        self.transaction=transaction
        self.previous =previous_hash
        self.nonce=0
        self.hash=self.chash()
    def chash(self):
        data=str(self.timestamp)+str(self.transaction)+str(self.previous)+str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()   
    def mining_block(self,difficulty):
        while self.hash[:difficulty]!="0"*difficulty:
            self.nonce+=1
            self.hash=self.chash()
        print('Block mined:', self.hash) 
       
difficulty =2
transaction=["transaction1","transaction2","transaction3"]
previous_block="000000000000000000000000000000000000000000000000000000000000000000000000000000"
block=Block(transaction,previous_block)
block.mining_block(difficulty)

print("block1:")
previous_block=block.chash()
transaction=["transaction2","transaction6","transaction7"]
block=Block(transaction,previous_block)
block.mining_block(difficulty)
print("block2:")
previous_block=block.chash()
transaction=["transaction10","transaction20","transaction25"]
block=Block(transaction,previous_block)
block.mining_block(difficulty)
previous_block=block.chash()
print("block1:")


