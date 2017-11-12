#!/usr/bin/env python

import os
import sys
import argparse
import subprocess
from distutils.dir_util import copy_tree
from os.path import expanduser

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

home = expanduser("~")
template_dir = os.path.join(home, "code", "doctools", template)

# Parse arguments
parser = argparse.ArgumentParser(description="Creates a new document folder based on template folder")
parser.add_argument("doc", help="Document name")
parser.add_argument("--verbose", help="Verbose mode", action="store_true")
args = parser.parse_args()

# Create doc
doc_folder_name = args.doc
doc_base_name = os.path.split(doc_folder_name)
doc_file_name = doc_base_name[1]+".md"
doc_file_path = os.path.join(doc_folder_name, doc_file_name)

if args.verbose:
	print("Using template from "+template_dir)
	print("Creating new document directory in " + doc_folder_name)

os.makedirs(doc_folder_name)
# Copy all files from template folder to output dir
if args.verbose:
	print("Copying template files to "+ doc_folder_name)

copy_tree(template_dir, doc_folder_name)

# Open file in default application (assume it's a text editor)
if args.verbose:
	print("Changing directory to "+doc_folder_name)
os.chdir(doc_folder_name)

if args.verbose:
	print("Renaming index.md to "+doc_file_name)
os.rename("index.md", doc_file_name)

open_file(doc_file_path)