#!/usr/bin/env python

import sys
import os
import argparse
import subprocess
# import markdown
from os.path import expanduser
from rfc3987 import parse
import urllib
# import json

parser = argparse.ArgumentParser(description="Creates Markdown files containing images from a list in another file")
parser.add_argument("file", help="The file you want to convert. Each file should have an image URL")
parser.add_argument("--output", "-o", help="Name of the output file", required=False)
parser.add_argument("--download", help="Download the remote assets", required=False, action="store_true")
parser.add_argument("--full", help="Make assets fill screen", required=False, action="store_true")
# parser.add_argument("--css", help="Define the stylesheet to use", required=False)
args = parser.parse_args()

# def open_file(filename):
#     if sys.platform == "win32":
#         os.startfile(filename)
#     else:
#         opener ="open" if sys.platform == "darwin" else "xdg-open"
#         subprocess.call([opener, filename])

# home = expanduser("~")
# null = open(os.devnull, 'w')

input = args.file
input_content = open(input).readlines()

output = "output.md"
output_content = open(output, "w")
yaml = open('header.yaml', "r").read()

# <!-- .slide: data-background="./image1.png" -->

if args.full:
	line_before = "<!-- .slide: data-background=\""
	line_after = "\" -->\n\n<!--s-->\n\n"
else:
	line_before = "![]("
	line_after = ")\n\n<!--s-->\n\n"

output_content.write(yaml+"\n\n")

assets_dir = "assets"
img_exts = ["jpg", "jpeg", "gif", "png", "svg"]

if args.download:
	if not os.path.isdir(assets_dir):
		print("Creating directory "+assets_dir)
		os.makedirs(assets_dir)

with open(input) as f:
	mylist = f.read().splitlines()

	for line in mylist:
		if args.download:
			url = line
			url_chunks = parse(line, rule="IRI")
			line = url[url.rfind("/")+1:]
			filename, file_ext = os.path.splitext(line)
			filename_full = filename+file_ext
			img_exts = [".jpg", ".jpeg", ".gif", ".png", ".svg"]
			if file_ext in img_exts:
				print("Downloading image "+filename_full+" to "+assets_dir)
				download = urllib.URLopener()
				download.retrieve(url, assets_dir+"/"+filename_full)
				output_content.write(line_before+assets_dir+"/"+line+line_after)
		else:
			# output_content.write(line_before+line+line_after)
			url_chunks = line.split(".")
			file_ext = "."+url_chunks[-1]
			img_exts = [".jpg", ".jpeg", ".gif", ".png", ".svg"]
			if file_ext in img_exts:
				output_content.write(line_before+line+line_after)

# for line in input_content:
# 	# line.replace("\n\n", "")
# 	print line
# 	url_chunks = parse(line, rule='IRI')
# 	# print url_chunks['path']
# 	# print url_chunks

# 	if not args.download:
# 		output_content.write(line_before+line+line_after)



# for line in mylist:
