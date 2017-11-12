#!/usr/bin/env python

import argparse
import subprocess

parser = argparse.ArgumentParser(description="Starts reveal-md with some presets")
parser.add_argument("file", help="The file you want to view")
parser.add_argument("--watch", "-w", help="watch update", required=False, action="store_const", const="-w")
args = parser.parse_args()

if args.watch:
	var_watch = args.watch
else:
	var_watch = ""

file = args.file

# If no filename specified, search for Markdown files. If only one, open that
# else:
# 	md_files = []
# 	files = [f for f in os.listdir('.') if os.path.isfile(f)]
# 	for f in files:
# 		filename, file_ext = os.path.splitext(f)
# 		if file_ext == ".md":
# 			md_files.append(f)

# 	if len(md_files) == 1:
# 		file = md_files[0]
# 	else:
# 		print("Please specify a file")
# 		sys.exit()
		
subprocess.Popen(["reveal-md", file, var_watch])