import time
import hashlib


class Block:
    def __init__(self, data):
        self.hash = ""
        self.height = 0
        self.body = data
        self.time = time.time()
        self.previousblockhash = ""

    def __repr__(self):
        return str(self.__dict__)


class Blockchain:
    def __init__(self):
        self.chain = []
        self.add_block(Block("Genesis block"))

    def add_block(self, new_block):
        new_block.height = len(self.chain)

        if(len(self.chain) > 0):
            new_block.previousblockhash = self.chain[len(self.chain) - 1].hash

        new_block.hash = self._calc_hash(new_block)
        self.chain.append(new_block)

    def get_block(self, height):
        return self.chain[height]

    def _calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = repr(data).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return str(self.__dict__)
