## Description
Generate an up-to-date files-tree with short descriptions.

The descriptions are specified in the same files with a specific tag tag:

e.g. [treesource] The main readme

Directories descriptions are specified in the respective `treesource.txt` file

Files and folder which are not specifically described are omitted from the tree by default.

## Example
```
$ python -m treesource -u
.
├── 🗀 example_folder\
│   ├── 🗀 first_subfolder\ (a documented folder)
│   │   ├── 🗀 sub-sub1\
│   │   │   └── 🗋 file3.sh (this is file 3)
│   │   ├── 🗀 sub-sub2\
│   │   │   └── 🗋 file4.cpp (this is file 4)
│   │   └── 🗋 random_file.rdm (a documented file)
│   ├── 🗀 second_subfolder\ (a documented folder with no documented files)
│   ├── 🗋 a_text_file.txt (a text file)
│   ├── 🗋 my_javascript.js (this is file 1)
│   └── 🗋 test.py (a python script)
└── 🗋 README.md (The main readme)
```

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
                        the rendering format [txt|md]
```

## Output formats
At the moment only txt and markdown are supported as output formats.

The data is represented as [anytree](https://anytree.readthedocs.io/en/2.8.0/index.html), therefore implementing other renderings is easy.

**How to implement new rendering formats:**

Rendering formats are specified in `treesource/render/formats.py`
1. Write a new rendering function starting from one of the existing
2. update the command line argument parsing in __main__.py