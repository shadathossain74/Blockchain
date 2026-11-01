import hashlib
class Block:
    def __init__(self,transaction,pre_add):
        self.data=transaction
        self.pre_add=pre_add
        self.hash=self.chash()
    def chash(self):
        data=str(self.pre_add)+str(self.data)
        return hashlib.sha256(data.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain=[Block("geninseis block","0"*64)]
    def add_block(self,data):
        self.chain.append(Block(data,self.chain[-1].hash))
    def valid_chain(self):
        for i in range(1,len(self.chain)):
            current_block=self.chain[i]
            pre_block=self.chain[i-1]
            if(current_block.hash!=current_block.chash()):
                print("Invalid hash")
                return False
            if(pre_block.pre_add !=pre_block.hash):
                print("invalid hash")
                return False
        return True
    def get_chainlenth(self):
        return len(self.chain)
    def get_hashrate(self):
        total=0
        for block in range (self.chain):
            total+=int(self.chain.hash,16)
        return total
    def check(self):
        total=self.get_hashrate()
        for i in range(self.get_chainlenth):
            blockhash=int(self.chain[i].hash,16)
            if(blockhash/total>.51):
                print("51 detect in :",i)
                return False
blok=Blockchain