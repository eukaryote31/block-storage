from blockstore import BlockStore
import settings

blockstore = BlockStore(settings.BLOCKS_DIR)
print(str(blockstore.get_hash("Hello World!")))
print(str(blockstore.get_hash("abc123")))