from unittest import TestCase
from pyOceanus import Oceanus

class OceanusDataTest(TestCase):
    def setUp(self):
        oc = Oceanus()
        self.oc_data = oc.parse("這是一個測試的句子。")

    def test_tokens(self):
        tokens = self.oc_data.tokens        
        self.assertEqual(len(tokens), 1)
        self.assertGreater(len(tokens[0]), 0)
        self.assertGreater(len(tokens[0][0]), 0)

    def test_tree(self):
        trees = self.oc_data.trees
        self.assertGreater(len(trees), 0)
        self.assertGreater(len(trees[0].children), 0)

    def test_dependency(self):
        deps = self.oc_data.deps
        self.assertGreater(len(deps), 0)
        self.assertGreater(len(deps[0]), 0)
        self.assertEqual(len(deps[0][0]), 5)

