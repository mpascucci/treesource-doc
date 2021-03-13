from __future__ import print_function
from os import getcwd
import argparse
from treesource import generate_tree, render


if __name__ == "__main__":

    # argument parses
    parser = argparse.ArgumentParser(
        prog='python -m treesource',
        description='Source file-trees generator.')
    parser.add_argument('-u', dest='use_unicode', action='store_const',
                        const=True, default=False,
                        help='use special unicode symbols as icons')
    parser.add_argument('-a', dest='show_all', action='store_const',
                        const=True, default=False,
                        help='show all files and folder, not only documented ones')
    parser.add_argument('-r', '--root', metavar='PATH', type=str,
                        default=getcwd(), help='the root directory of the tree')

    parser.add_argument('-f', '--format', metavar='FORMAT', type=str,
                        default='txt', help='the rendering format [txt|md]')
    args = parser.parse_args()

    # generate the tree
    tree = generate_tree(args.root, keep_undocumented=args.show_all)

    # render the tree
    if args.format.upper() in ['MD', 'MARKDOWN']:
        rendered = render.as_markdown(tree, use_unicode=args.use_unicode)
    elif args.format.upper() in ['TXT', 'TEXT', 'ASCII']:
        rendered = render.as_text(tree, use_unicode=args.use_unicode)
    else:
        print("ERROR: Unrecognised format option: {}".format(args.format))
        rendered = render.as_text(tree, use_unicode=args.use_unicode)

    print(rendered)
