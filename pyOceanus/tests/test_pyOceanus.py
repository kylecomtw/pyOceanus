from unittest import TestCase
import pyOceanus

class pyOceanusTest(TestCase):
    def test_init(self):
        oc = pyOceanus.Oceanus()
        self.assertTrue(True)
    
    def test_parse(self):
        oc = pyOceanus.Oceanus()
        pp = oc.parse("這是一個測試的句子。")
        self.assertTrue(True)

