import re
import pdb
from .tree_parser import parse_tree_repr

dep_re = re.compile("([a-z:]*)\(([^\s-]*)-(\d+),\s?([^\s-]*)-(\d+)\)")

class OceanusData:
    def __init__(self, nlp_data):
        self.nlp = nlp_data
        self.deps = self.prepare_dependency()
        self.tokens = self.prepare_tokens()
        self.trees = self.prepare_trees()

    def prepare_tokens(self):
        sentences = self.nlp["data"]["sentences"]
        pos_list = list(map(lambda x: x["pos"], sentences))
        words_list = list(map(lambda x: x["words"], sentences))
        ner_list = list(map(lambda x: x["ner"], sentences))
        toks = []
        for sent_i in range(len(pos_list)):
            tok_iter = zip(words_list[sent_i], \
                           pos_list[sent_i], ner_list[sent_i])
            tok_vec = []
            for w, p, n in tok_iter:
                tok_vec.append((w, p, n))
            toks.append(tok_vec)        
        return toks

    def prepare_dependency(self):
        sentences = self.nlp["data"]["sentences"]
        deps_iter = map(lambda x: x["udep"], sentences)
        deps = []
        for sent_dep in deps_iter:
            dep_vec = []
            for dep_x in sent_dep:
                m_dep = dep_re.match(dep_x)

                if m_dep is None:
                    print("WARNING: cannot parse %s" % dep_x)
                    continue
                rel = m_dep.group(1)
                gov = m_dep.group(2)
                gov_i = int(m_dep.group(3))
                dep = m_dep.group(4)
                dep_i = int(m_dep.group(5))
                dep_vec.append((rel, gov, gov_i, dep, dep_i))
            deps.append(dep_vec)

        return deps
    
    def prepare_trees(self):
        sentences = self.nlp["data"]["sentences"]
        tree_iter = map(lambda x: x["tree"], sentences)
        trees = []
        for tree_str in tree_iter:
            tree_x = parse_tree_repr(tree_str)
            trees.append(tree_x)
        return trees
   
    def get_token(self, sentence_idx, tok_idx):
        if tok_idx == -1: return ("ROOT", "", "")
        return self.tokens[sentence_idx][tok_idx]

    def get_dep_token(self, sent_idx, dep_tuple):
        return (self.get_token(sent_idx, dep_tuple[2]-1), \
                self.get_token(sent_idx, dep_tuple[4]-1))

    def get_dependency(self, sentence_idx, tok_idx):
        sent_dep = self.deps[sentence_idx]
        deps_x = filter(lambda x: x[2] == tok_idx+1 or x[4] == tok_idx+1, \
                        sent_dep)
        return list(deps_x)