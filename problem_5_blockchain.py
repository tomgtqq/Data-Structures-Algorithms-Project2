import hashlib
import time


class Block:
    def __init__(self, data, previous_hash=None):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return str(self.__dict__)


class Blockchain:
    def __init__(self):
        self.head = Block(data="Genesis block")

    def add_block(self, data):
        if not data:
            print("please check the data")
            return

        block = self.head
        while block.next:
            block = block.next
        block.next = Block(data, block.hash)

    def get_block(self, hash_value=None):
        if not hash_value:
            print("Please input block hash")
            return

        block = self.head
        while block:
            if block.hash == str(hash_value):
                return (block.hash, block.data, block.timestamp)
            block = block.next
        return "Block Not Found"

    def __repr__(self):
        block = self.head
        blockchain_info = []
        while block:
            blockchain_info.append((block.hash, block.data, block.timestamp))
            block = block.next
        return '=>'.join(map(str, blockchain_info))


# Create a private blockchain, there is a genesis block when inital
blockchain = Blockchain()
print(blockchain)

print("----------------------Test 1 add 2 blocks-------------------------------------------")
blockchain.add_block(data="First Block")
blockchain.add_block(data="Second Block")

print(blockchain)

print("----------Test 2 should not create new block for storing empty data-----------------")
blockchain.add_block(data="")

print("----------------------Test 3 get block by hash----------------------------------------")
blockchain.get_block("")
