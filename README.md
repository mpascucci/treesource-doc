### Description
Generate an up-to-date files-tree with short descriptions.

The descriptions are specified in the same files with a specific tag tag:

e.g. [treesource] The main readme

Directories descriptions are specified in the respective `treesource.txt` file

Files and folder which are not specifically described are omitted from the tree by default.

### Usage
execute the python module from the root folder `python -m treesource`

### Example
```
.
├── 🗀 example_folder\
│   ├── 🗀 subfolder\  (a documented folder)
│   │   ├── 🗀 sub-sub\
│   │   │   └── 🗎  file3  (this is file 3)
│   │   ├── 🗀 sub-sub2\
│   │   │   └── 🗎  file4  (this is file 4)
│   │   └── 🗎  file  (a documented file)
│   ├── 🗀 subfolder 2\  (a documented folder with no documented files)
│   ├── 🗎  a.txt  (a text file)
│   ├── 🗎  file1.txt  (this is file 1)
│   └── 🗎  test.py  (a python script)
└── 🗎  README.md  (The main readme)
```

### Output formats
At the moment only txt and markdown are supported as output formats.

The data is represented as [anytree](https://anytree.readthedocs.io/en/2.8.0/index.html), therefore implementing other renderings is relatively easy.
