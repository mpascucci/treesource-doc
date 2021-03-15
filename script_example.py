import treesource as ts

# Generate the tree
root_path='./example_folder'
tree = ts.generate_tree(root_path)

# Render as pure text
rendered = ts.render.as_text(tree, use_unicode=False)
print(rendered)

# Render as specific format
# The rendering FORMATS use special tokens which are replaced by the values:
# pre: the ASCII chars that represent the tree
# icon: an icon displayed is use_unicode is true
# name: the file/directory name
# doc: the documentation string

rendered = ts.render.engine.render_tree(
    tree,
    folder_icon='D', file_icon='F',
    doc_folder_format="{pre}[{icon}]/{name}/ --> {doc}",
    no_doc_folder_format="{pre}[{icon}][{name}]",
    doc_file_format="{pre}[{icon}][{name}] --> {doc}",
    no_doc_file_format="{pre}[{icon}][{name}]")

print(rendered)