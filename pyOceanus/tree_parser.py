import pdb

class Tree:
    def toJSON(self):
        return {
            "node": self.node, 
            "children":  [x.toJSON() for x in self.children]
        }

    def __init__(self):
        self.node = ""
        self.children = []
    def __repr__(self):
        return "(%s %s)" % (
                self.node, 
                ", ".join([str(x) for x in self.children]))

def popFrames(frames):
    if len(frames) > 1:
        popTree = frames[0]
        frames = frames[1:]
        curTree = frames[0]

        curTree.children.append(popTree)            
    elif len(frames) == 1:
        pass
    else:
        raise Exception("popping an empty frame")
    return frames

def parse_tree_repr(tree_str):
    frames = []
    states = {"openedBySpace": False}
    tree_str = tree_str.replace(" (", "(")
    last_tree = None

    for ch in tree_str:
        if ch == "(":
            frames.insert(0, Tree())
        elif ch == ")":
            if states["openedBySpace"]:
                frames = popFrames(frames)
                states["openedBySpace"] = False

            frames = popFrames(frames)       

        elif ch == " ":            
            frames.insert(0, Tree())
            states["openedBySpace"] = True
        else:
            frames[0].node += ch
    
    return frames[0]

