from anytree import RenderTree
from .sorting import directory_first_alphabetical


def render_tree(
        tree, folder_icon, file_icon,
        doc_folder_format, no_doc_folder_format,
        doc_file_format, no_doc_file_format):
    """Render the doctree as text

    tree: the file-tree
    folder and file_icon : chars to use before file/folder names
    formats: format templates for the file/folder names

    # The rendering FORMATS use special tokens:
    pre: the ASCII chars that represent the tree
    icon: an icon displayed is use_unicode is true
    name: the file/directory name
    doc: the documentation string

    # EXAMPLE:
    # folder that has a documentation
    #    doc_folder_format = "{pre}{icon}{name}\\ ({doc})"
    # folder without documentation
    #    no_doc_folder_format = "{pre}{icon}{name}\\"   
    # file that has a documentation
    #    doc_file_format = "{pre}{icon}{name} ({doc})"
    # file without documentation
    #    no_doc_file_format = "{pre}{icon}{name}"
    """

    rendered = ""

    for pre, _, node in RenderTree(tree, childiter=directory_first_alphabetical):
        # directories
        if node.node_type == 'dir':
            if node.doc is None:  # no doc
                rendered += no_doc_folder_format.format(
                    pre=pre, icon=folder_icon, name=node.name, doc=''
                ) + "\n"
            else:
                rendered += doc_folder_format.format(
                    pre=pre, icon=folder_icon, name=node.name, doc=node.doc
                ) + "\n"
        # files
        elif node.node_type == 'file':
            if node.doc is None:  # no doc
                rendered += no_doc_file_format.format(
                    pre=pre, icon='', name=node.name, doc=''
                ) + "\n"
            else:
                rendered += doc_file_format.format(
                    pre=pre, icon=file_icon, name=node.name, doc=node.doc
                ) + "\n"
        else:
            rendered += "{pre}{name}".format(pre=pre, name=node.name) + "\n"

    return rendered
