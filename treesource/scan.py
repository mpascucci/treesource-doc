import os
import re
from anytree import AnyNode, PostOrderIter


def get_doc_string(path, first_lines=30):
    """look for the doctree docstring in the first lines of the file in path"""

    docstring = None

    try:
        f = open(path, 'r')
    except Exception:
        return None

    try:
        for _ in range(first_lines):
            # read the file line by line and search the docstring
            line = f.readline()
            m = re.match(r"^.*?\[treesource\]\s*(.*)$", line)
            if m:
                docstring = m.groups()[0]
                break
    except UnicodeDecodeError:
        # probably a binary file
        docstring = None
    except Exception:
        docstring = None
    finally:
        f.close()

    return docstring


def walk2tree(walk_lsit, prune_undocumented):
    """transform a filtered folder list into a tree."""
    # create root node
    root = AnyNode(id='root', name='.', doc=None,
                   node_type='root', parent=None)
    # add root node's files
    for f in walk_lsit[0]['files']:
        AnyNode(
            id=f['filename'],
            name=f['filename'],
            parent=root,
            doc=f['docstring'],
            node_type='file'
        )

    nodes = {'root': root}

    # add other nodes
    for entry in walk_lsit[1:]:
        dirname = entry['dirname']
        parent_name = entry['parent']
        parent = nodes[parent_name]
        newnode_name = '/'.join([parent_name, dirname])
        node_type = 'dir'

        newnode = AnyNode(
            id=newnode_name, parent=parent,
            name=dirname, doc=entry['dirdoc'], node_type=node_type
        )
        nodes[newnode_name] = newnode

        for f in entry['files']:
            AnyNode(
                id=f['filename'],
                name=f['filename'],
                parent=newnode,
                doc=f['docstring'],
                node_type='file'
            )

    # prune undocumented nodes
    if prune_undocumented:
        for node in PostOrderIter(root):
            if node.doc == None and len(node.children) == 0:
                node.parent = None

    return root


def generate_tree(startpath, keep_undocumented=False):
    """Generate a file-tree object from the current working directory.

    keep_undocumented: keep undocumented files and directories in the tree

    Returns an anytree object

    """
    walked = []

    # iterate over the os.walk result
    for root, _, files in os.walk(startpath):
        # directory level
        level = root.replace(startpath, '').count(os.sep)

        # directory name
        dirname = os.path.basename(root.replace(startpath, ''))

        documented_files = []
        for filename in files:
            # look for the docstring in the file
            docstring = get_doc_string(os.path.join(root, filename))
            # speed up by not inserting undocumented diles
            if keep_undocumented or (docstring is not None):
                documented_files.append(dict(
                    filename=filename,
                    docstring=docstring)
                )

        # get folder doc
        dirdoc = None
        docfile = os.path.join(root, 'treesource.txt')
        if os.path.exists(docfile):
            with open(docfile, 'r') as f:
                dirdoc = f.readline()

        walked.append(dict(
            parent='root' +
            '/'.join((root.replace(startpath, '').split(os.sep)[:-1])),
            level=level,
            dirname=dirname,
            dirdoc=dirdoc,
            files=documented_files)
        )

    root = walk2tree(walked, prune_undocumented=not keep_undocumented)
    return root
