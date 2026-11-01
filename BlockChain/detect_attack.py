import hashlib
import time
from collections import Counter
class Block:
    def __init__(self,transaction,previous,miner):
        self.time=time.time()
        self.transaction=transaction
        self.previous=previous
        self.miner=miner
        self.hash=self.hash1()
    def hash1(self):
        data= str(self.time)+str(self.transaction)+ str(self.previous)+str(self.miner)
        return hashlib.sha256(data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain=[Block("first","0"*32,"system")]
    def add(self,block,miner):
        self.chain.append(Block(block,self.chain[-1].hash,miner))
    def validate(self):

        for i in range(1,len(self.chain)):
            currentblock=self.chain[i]
            previousblock=self.chain[i-1]
            if(currentblock.previous!=previousblock.hash1()):
                print("invalid")
                return False
            if(currentblock.hash1()!=currentblock.hash):
                print("invalid")
                return False 
        print("valid")

    def detect(self):
         count_array=Counter(block.miner for block in self.chain)
         for miner,count in count_array.items():
             percent=count/len(self.chain)
             print(f"{miner:}contibute {percent*100}")
             if percent>.51:
                 print("invalid")
                 return False
         print("valid")
         return True      
    
             



previou_address="0"*32
transaction1=[
    "ertyui",
    "6trewa"
]

blockchain=Blockchain()
blockchain.add("ertyuiop","minerA")



blockchain.add("wertyuidfghjk","minerB")


blockchain.add("wdgdhfgsdjhgds","minerB")
blockchain.add("wdgdhfgsdjfdhcfhgds","minerB")

blockchain.validate()
blockchain.detect()
            
        


