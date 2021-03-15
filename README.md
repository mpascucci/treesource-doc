## Description
Generate descriptive directory trees dynamically, ready for your project's REAMDE.

The descriptions are specified in the same files with a specific tag tag:

e.g. [treesource] The main readme

Directories descriptions are specified in the respective `treesource.txt` file

Files and folder which are not specifically described are omitted from the tree by default.

## Example
```
$ python -m treesource
.
├── example_folder/
│   ├── first_subfolder/ (a documented folder)
│   │   ├── sub-sub1/
│   │   │   └── file3.sh (this is file 3)
│   │   ├── sub-sub2/
│   │   │   └── file4.cpp (this is file 4)
│   │   └── random_file.rdm (a documented file)
│   ├── second_subfolder/ (a documented folder with no documented files)
│   ├── a_text_file.txt (a text file)
│   ├── my_javascript.js (this is file 1)
│   └── test.py (a python script)
└── README.md (The main readme)
```

## Install
with pip `pip install treesource`.

## Usage
Execute the python module from the root folder: `python -m treesource`
```
usage: python -m treesource [-h] [-u] [-a] [-r PATH] [-f FORMAT]

Source file-trees generator.

optional arguments:
  -h, --help            show this help message and exit
  -u                    use special unicode symbols as icons
  -a                    show all files and folder, not only documented ones
  -r PATH, --root PATH  the root directory of the tree
  -f FORMAT, --format FORMAT
                        the rendering format [txt|md|ascii]
```

## Output formats
At the moment only txt and markdown are supported as output formats.

If you experience encoding-related problems, use the  `-f ascii`.

The data is represented as [anytree](https://anytree.readthedocs.io/en/2.8.0/index.html), therefore implementing other renderings is easy.

**How to implement new rendering formats:**

Rendering formats are specified in `treesource/render/formats.py`
1. Write a new rendering function starting from one of the existing
2. update the command line argument parsing in __main__.py

## Use in a python script
This example shows the use of *treesource* in a python script, and the definition of a custom export format.

```{pyhon}
import treesource as ts

# Generate the tree
root_path='./example_folder'
tree = ts.generate_tree(root_path)


# === Render as pure text
rendered = ts.render.as_text(tree, use_unicode=False)
print(rendered)


# === Render as specific format
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
```

The output is

```
.
├── first_subfolder\ (a documented folder)
│   ├── sub-sub1\
│   │   └── file3.sh (this is file 3)
│   ├── sub-sub2\
│   │   └── file4.cpp (this is file 4)
│   └── random_file.rdm (a documented file)
├── second_subfolder\ (a documented folder with no documented files)
├── a_text_file.txt (a text file)
├── my_javascript.js (this is file 1)
└── test.py (a python script)

.
├── [D]/first_subfolder/ --> a documented folder
│   ├── [D][sub-sub1]
│   │   └── [F][file3.sh] --> this is file 3
│   ├── [D][sub-sub2]
│   │   └── [F][file4.cpp] --> this is file 4
│   └── [F][random_file.rdm] --> a documented file
├── [D]/second_subfolder/ --> a documented folder with no documented files
├── [F][a_text_file.txt] --> a text file
├── [F][my_javascript.js] --> this is file 1
└── [F][test.py] --> a python script
```