import unittest
import shutil
from blockstore import BlockStore

shutil.rmtree("./testblockdir")

class TestBlockStore(unittest.TestCase):
    bstore = BlockStore("./testblockdir")

    def test_hash(self):
        self.assertEqual("6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090",
                         self.bstore.get_hash("abc123"))
        self.assertEqual("7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
                         self.bstore.get_hash("Hello World!"))

    def test_block_storage(self):
        hash = self.bstore.put_block("Hello, World!")
        self.assertEqual("dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f", hash)
        contents = self.bstore.get_block_contents(hash)
        self.assertEqual("Hello, World!", contents)


if __name__ == '__main__':
    unittest.main()
