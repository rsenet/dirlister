#!/usr/bin/env python3
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import warnings
import argparse
import requests
import sys
import re
import os

ALL_LINKS = []
FORBIDDEN = ["?C=N;O=D", "?C=M;O=A", "?C=S;O=A", "?C=D;O=A"]
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def parse_web_page(url, dirlister_ext=None, dirlister_log=None):
    page  = requests.get(url)
    soup  = BeautifulSoup(page.text, "lxml")

    try:
        for link in soup.findAll('a'):
            link_name = link.get('href')
            full_url  = "%s%s" % (url, link_name)

            if link_name not in FORBIDDEN:
                if full_url not in ALL_LINKS:
                    if "wp-content" not in link_name:
                        if dirlister_ext:
                            path = urlparse.urlparse(full_url).path
                            ext  = os.path.splitext(path)[1][1:]

                            if ext in dirlister_ext:
                                print(full_url)

                                if dirlister_log:
                                    dirlister_log.write("%s\n" % full_url)

                        else:
                            if dirlister_log:
                                dirlister_log.write("%s\n" % full_url)

                            print(full_url)

                        ALL_LINKS.append(full_url)
                        parse_web_page(full_url, dirlister_ext, dirlister_log)

    except TypeError:
        pass

    return ALL_LINKS
