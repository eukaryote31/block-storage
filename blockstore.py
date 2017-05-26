import os.path
import hashlib


class BlockStore:
    def __init__(self, blockdir):
        assert isinstance(blockdir, str)
        self.blockdir = blockdir
        os.makedirs(blockdir, exist_ok=True)

    def has_block(self, blockhash):
        """Checks if the BlockStore has a block"""
        return os.path.exists(self.get_block_file(blockhash))

    def put_block(self, blockdata):
        """Puts a string as a block"""
        assert isinstance(blockdata, str)

        hash = self.get_hash(blockdata)

        # dont put block if it already exists
        if self.has_block(hash):
            return hash

        file_output = open(self.get_block_file(hash), "w")

        file_output.write(blockdata)

        file_output.close()

        return hash

    def get_hash(self, data):
        """Get a hash for the given data"""
        assert isinstance(data, str)
        sha256 = hashlib.sha256()
        sha256.update(data.encode("UTF-8"))
        return sha256.hexdigest()

    def get_block_file(self, hash):
        return os.path.join(self.blockdir, hash)

    def get_block_contents(self, hash):
        block_file = open(self.get_block_file(hash), "r")

        return block_file.read()
