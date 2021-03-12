from anytree import RenderTree
from .sorting import directory_first_alphabetical

def as_text(tree):
    """render the doctree as text"""
    for pre, _, node in RenderTree(tree, childiter=directory_first_alphabetical):
        if node.node_type == 'dir':
            if node.doc is None:
                print("%s%s\\" % (pre, node.name))
            else:
                print("%s%s\\  (%s)" % (pre, node.name, node.doc))
        elif node.node_type == 'file':
            print("%s%s  (%s)" % (pre, node.name, node.doc))
        else:
            print("%s%s" % (pre, node.name))
         