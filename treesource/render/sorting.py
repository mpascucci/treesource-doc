def select_by_type(node_type, nodes):
    return filter(lambda node: node.node_type==node_type, nodes)

def sort_by_name(nodes):
    return sorted(nodes, key=lambda node: node.name)

def directory_first_alphabetical(nodes):
    """sort in alphabetical order, first directories then files"""
    dirs = select_by_type('dir', nodes)
    files = select_by_type('file', nodes)
    return sort_by_name(dirs) + sort_by_name(files)