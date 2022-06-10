#!/usr/bin/env python3
from lib import parser
import argparse
import sys
import re

__author__  = 'Regis SENET'
__email__   = 'regis.senet@orhus.fr'
__git__     = 'https://github.com/rsenet/dirlister'
__version__ = '0.1'
__license__ = 'GPLv3'
__pyver__   = '%d.%d.%d' % sys.version_info[0:3]
short_desc  = "Script to quickly scrap WordPress directory listing"

arg_parser = argparse.ArgumentParser(description=short_desc)
arg_parser.add_argument('--url', help="Specify the URL to parse")
arg_parser.add_argument('--ext', help="Specify extension(s) to search (pdf,png,css,etc.)")
arg_parser.add_argument('--log', help="Specify output log file")
u_args = arg_parser.parse_args()

# Get variable
dirlister_url = u_args.url
dirlister_ext = u_args.ext.split(",") if u_args.ext else None
dirlister_log = u_args.log

try:
    if dirlister_url:
        if dirlister_log:
            out_file = open(dirlister_log, "a")
            parser.parse_web_page(dirlister_url, dirlister_ext, out_file)

        else:
            parser.parse_web_page(dirlister_url, dirlister_ext)

    else:
        print("[x] Error! URL attribute is mandatory)")

except KeyboardInterrupt:
    print("\n[x] Leaving ...")
