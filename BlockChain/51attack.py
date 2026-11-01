import hashlib
from collections import Counter

# Creating a block
class Block:
    def __init__(self,data,previous_hash,miner):
        self.data=data
        self.previous_hash=previous_hash
        self.miner=miner
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data=(
            str(self.data)+
            str(self.previous_hash)+str(self.miner)
        )
        return hashlib.sha256(block_data.encode()).hexdigest()

# Creating Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [Block("Genesis Block","0"*64,"systeam")]

    def add_block(self,data):
        self.chain.append(Block(data,self.chain[-1].hash))

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash for block",i)
                return False
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash for block",i)
                return False

            print("Blockchain is valid")

        return True



    def check_for_51_percent_attack(self):
          counted_array=Counter(self.miner for block in self.chain)
          for miner,count in counted_array.items():
              percent=(count/len(self.chain))*100
              print(f"miner name:{miner:} percentage:{percent:}")
              if percent>51:
                  print("invalid")
                  return False
          return True
 

blockchain = Blockchain()
blockchain.add_block(
    Block("Alice pays Bob 5 BTC", "","minerA")
)

blockchain.add_block(
    Block("Bob pays Charlie 3 BTC", "","minerB")
)

blockchain.add_block(
    Block("Charlie pays David 2 BTC", "","minerc")
)

print("Chain Length:",blockchain.get_chain_length()) 

print("\nChecking Blockchain:")
blockchain.validate_chain()   

print("\nChecking 51% Attack:")
bool = blockchain.check_for_51_percent_attack()