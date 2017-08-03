from unittest import TestCase
from pyOceanus.tree_parser import parse_tree_repr

tree_str = "(ROOT(IP(NP (PN 這))(VP (VC 是)(NP(QP (CD 一)(CLP (M 個)))(DNP(NP (NN 測試))(DEG 的))(NP (NN 句子))))(PU 。)))"

class TreeParserTest(TestCase):
    def test_parse(self):
        tree = parse_tree_repr(tree_str)
        self.assertTrue(tree != None)
        self.assertTrue(len(tree.children) > 0)
