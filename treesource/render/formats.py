# -*- coding: UTF-8 -*-
from . import engine
from sys import version_info


def get_unicode_icons():
    if version_info[0] < 3:
        # python 2.7
        folder_icon = u"\U0001F5C0 ".encode('utf-8')
        file_icon = u"\U0001F5CB ".encode('utf-8')
    else:
        folder_icon = u"\U0001F5C0 "
        file_icon = u"\U0001F5CB "
    return file_icon, folder_icon

def as_text(tree, use_unicode_icons=False):
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
    if use_unicode_icons:
        file_icon, folder_icon = get_unicode_icons()
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

def as_pure_ascii(tree):
    """render as pure ASCII"""
    doc_folder_format = "{pre}{icon}{name}/ ({doc})"
    no_doc_folder_format = "{pre}{icon}{name}/"
    doc_file_format = "{pre}{icon}{name} ({doc})"
    no_doc_file_format = "{pre}{icon}{name}"
    file_icon = ''
    folder_icon = ''
    
    rendered = engine.render_tree(
        tree,
        folder_icon, file_icon,
        doc_folder_format, no_doc_folder_format,
        doc_file_format, no_doc_file_format, pure_ASCII=True
    )
    return rendered


def as_markdown(tree, use_unicode_icons=False):
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
    if use_unicode_icons:
        file_icon, folder_icon = get_unicode_icons()
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
