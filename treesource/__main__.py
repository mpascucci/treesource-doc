from .scan import generate_tree
from os import getcwd
from . import render

if __name__ == "__main__":
    tree = generate_tree(getcwd())
    render.as_text(tree)