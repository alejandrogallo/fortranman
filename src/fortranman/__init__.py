__version__ = '0.1.0'

import argparse
import pkg_resources
import sys
import os
import glob


def get_resource(keyword):
    resource_folder = pkg_resources.resource_filename(__name__, '')
    wildcard = os.path.join(resource_folder, "{0}*".format(keyword))
    return glob.iglob(wildcard)


def main():
    parser = argparse.ArgumentParser(description="Fortran man pages")
    parser.add_argument(
        "-k", "--keyword",
        default="", help="keyword (wildcard)", action="store")
    parser.add_argument(
        "-l", "--list", help="List available man pages", action="store_true")
    args = parser.parse_args()

    if args.list:
        for r in get_resource(args.keyword):
            print(r)
        sys.exit(0)

    files = get_resource(args.keyword)
    try:
        cmd = " ".join(["man", next(files)])
        print(cmd)
        os.system(cmd)
    except StopIteration:
        print("This keyword '{0}' is not in the database".format(args.keyword))
        sys.exit(1)
