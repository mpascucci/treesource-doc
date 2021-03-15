from . import engine


def as_text(tree, use_unicode=False):
    """render the doctree as text"""
    # The rendering FORMATS
    # pre: the ASCII chars that represent the tree
    # icon: an icon displayed is use_unicode is true
    # name: the file/directory name
    # doc: the documentation string

    # folder that has a documentation
    doc_folder_format = "{pre}{icon}{name}/ ({doc})"
    # folder without documentation
    no_doc_folder_format = "{pre}{icon}{name}/"
    # file that has a documentation
    doc_file_format = "{pre}{icon}{name} ({doc})"
    # file without documentation
    no_doc_file_format = "{pre}{icon}{name}"

    rendered = ""

    # unicode icons
    if use_unicode:
        folder_icon = "🗀 "
        file_icon = "🗋 "
    else:
        folder_icon = ""
        file_icon = ""

    rendered = engine.render_tree(
        tree,
        folder_icon, file_icon,
        doc_folder_format, no_doc_folder_format,
        doc_file_format, no_doc_file_format
    )

    return rendered


def as_markdown(tree, use_unicode=True):
    """render the doctree as markdown"""

    # The rendering FORMATS
    # pre: the ASCII chars that represent the tree
    # icon: an icon displayed is use_unicode is true
    # name: the file/directory name
    # doc: the documentation string

    # folder that has a documentation
    doc_folder_format = "`{pre}{icon}`**`{name}\\`** _{doc}_\\"
    # folder without documentation
    no_doc_folder_format = "`{pre}{icon}`**`{name}\\`**\\"
    # file that has a documentation
    doc_file_format = "`{pre}{icon}{name}` _{doc}_\\"
    # file without documentation
    no_doc_file_format = "`{pre}{icon}{name}`\\"

    rendered = ""

    # unicode icons
    if use_unicode:
        folder_icon = "🗀 "
        file_icon = "🗋 "
    else:
        folder_icon = ""
        file_icon = ""

    rendered = engine.render_tree(
        tree,
        folder_icon, file_icon,
        doc_folder_format, no_doc_folder_format,
        doc_file_format, no_doc_file_format
    )

    return rendered
