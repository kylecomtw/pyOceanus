from unittest import TestCase
import pyOceanus

class oceanusUtilsTest(TestCase):
    def test_getNNCompounds(self):        
        oc = pyOceanus.Oceanus()
        pp = oc.parse("這是一位食物銀行的金融經理。")
        nns = pyOceanus.get_NN_compounds(pp)        
        self.assertTrue(len(nns) == 2)

