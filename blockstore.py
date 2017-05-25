import os.path
import hashlib

class BlockStore:
    def __init__(self, blockdir):
        self.blockdir = blockdir

    def has_block(self, blockhash):
        """Checks if the BlockStore has a block"""
        return os.path.exists(os.path.join(self.blockdir, blockhash))

    def put_block(self, blockdata):
        """Puts a string as a block"""
        pass

    def get_hash(self, data):
        """Get a hash for the given data"""
        sha256 = hashlib.sha256()
        sha256.update(data)
        return sha256.hexdigest()