import hashlib
import time

class Block:
    def __init__(self,transaction,previous_hash):
        self.time=time.time()
        self.transaction =transaction
        self.previous_hash=previous_hash
        self.nonce=0
        self.hash=self.hash1()

    def hash1(self):
        data=str(self.time)+str(self.transaction)+str(self.previous_hash)+str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()
    def mining(self,difficulty):
        while(self.hash[:difficulty]!="0"*difficulty):
            self.nonce+=1
            self.hash=self.hash1()


difficulty=2

transaction=[
    "fghjkl;",
    "sdfghujik,",
    "ertyuio",
]
previous_hass="0"*32

block=Block(transaction,previous_hass)
block.mining(difficulty)
previous_hass=block.hash1()

