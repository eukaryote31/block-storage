import os.path
import hashlib

# Maximum block size
MAX_BLOCK_SIZE = 128 * 1024;


class BlockStore:
    def __init__(self, blockdir):
        assert isinstance(blockdir, str)
        self.blockdir = blockdir
        os.makedirs(blockdir, exist_ok=True)

    def collect_file(self, hash, output):
        fileparts = self.get_block_contents(hash).split(b'\n')

        outputfile = open(output, "wb")

        for hash in fileparts:
            part = self.get_block_contents(hash)
            outputfile.write(part)

        outputfile.close()

    def put_file(self, file):
        """Puts a file into storage. Returns a hash identifying it. """
        partHashes = []

        inputfile = open(file, "rb")
        while True:
            block = inputfile.read(MAX_BLOCK_SIZE)

            # empty block means we have read the whole file
            if block == b'':
                break

            # put the block into the block store
            partHashes.append(self.put_block(block))

        inputfile.close()

        descriptor = "\n".join(partHashes)

        return self.put_block(descriptor)

    def has_block(self, blockhash):
        """Checks if the BlockStore has a block"""
        return os.path.exists(self.get_block_file(blockhash))

    def put_block(self, blockdata):
        """Puts a string as a block"""

        hash = self.get_hash(blockdata)

        # dont put block if it already exists
        if self.has_block(hash):
            return hash

        file_output = open(self.get_block_file(hash), "wb")

        file_output.write(blockdata)

        file_output.close()

        return hash

    def get_hash(self, data):
        """Get a hash for the given data"""
        if isinstance(data, str):
            data = data.encode("UTF-8")

        sha256 = hashlib.sha256()
        sha256.update(data)
        return sha256.hexdigest()

    def get_block_file(self, hash):
        if isinstance(hash, bytes):
            hash = hash.decode()
            
        return os.path.join(self.blockdir, hash)

    def get_block_contents(self, hash):
        block_file = open(self.get_block_file(hash), "rb")


        data = block_file.read()
        block_file.close()
        return data
