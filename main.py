from blockstore import BlockStore
import settings

blockstore = BlockStore(settings.BLOCKS_DIR)
hash = blockstore.put_file("shakespeare")
blockstore.collect_file(hash, "shakespeare.collected")
