#!/usr/bin/env python

import sys
import os
import argparse
import subprocess
import markdown
# import pdfkit
# import pymdownx.emoji
import codecs
from weasyprint import HTML, CSS
from os.path import expanduser
# import json

parser = argparse.ArgumentParser(description="Converts Markdown to pretty PDF documents")
parser.add_argument("file", help="The file you want to convert")
parser.add_argument("--output", "-o", help="Name of the output file", required=False)
parser.add_argument("-s", "--show", help="Open PDF file after conversion", required=False, action="store_true")
parser.add_argument("--keep", help="Keep the intermediate HTML file", required=False, action="store_true")
# parser.add_argument("--output", "-o", help="Define the output filename", required=False)
# parser.add_argument("--css", help="Define the stylesheet to use", required=False)
args = parser.parse_args()

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

home = expanduser("~")
null = open(os.devnull, 'w')

# Read file
# input = sys.argv[1]
input = args.file
if os.path.exists(input):

    # Define filenames
    base_filename = os.path.splitext(input)[0]
    html_filename = base_filename+".html"

    if args.output:
        pdf_filename = args.output
    else:    
        pdf_filename = base_filename+".pdf"

    input_text = open(input).read()
    input_text = unicode(input_text, "utf-8")

    # md = markdown.Markdown(extensions=['markdown.extensions.tables', 'markdown.extensions.meta', 'markdown.extensions.smarty', 'markdown.extensions.toc', 'pymdownx.emoji'], extension_configs={})
    md = markdown.Markdown(extensions=['markdown.extensions.tables', 'markdown.extensions.meta', 'markdown.extensions.smarty', 'markdown.extensions.toc'], extension_configs={})

    html = md.convert(input_text)

    input_dir = os.path.dirname(os.path.abspath(input))
    template_dir = os.path.join(home, "code", "doctools", "template")
    css_dir = os.path.join(template_dir,"css")
    css_file = os.path.join(css_dir, "tufte-print-full-width.css")

    css_file_abs_path = os.path.realpath(css_file)  
    print("CSS file at "+css_file)
    
    html_header = u'<html>\n<head>\n<meta charset="utf-8"/>\n<title></title>\n<link rel="stylesheet" href="'+css_file+'">\n</head>\n  <body>'
    # html_header = u'<html>\n<head>\n<meta charset="utf-8"/>\n<title></title>\n</head>\n  <body>'

    html_footer = u'</body>\n</html>'

    # Markdown to HTML
    print("Converting HTML to MarkDown")
    html = md.convert(input_text)
    all_html = html_header+html+html_footer
    all_html = all_html.encode('utf-8')
    print("Writing HTML to "+html_filename)
    html_file = open(html_filename, "w")
    html_file.write(all_html)
    print("Finished HTML conversion")

    # HTML to PDF

    # Write YAML to PDF
    # pdf_options_allowed = ['page-size', 'orientation', 'title', 'margin-top', 'margin-bottom', 'margin-left', 'margin-right']

    # pdf_options = {  
    #     'margin-top': '2cm',
    #     'margin-left': '1cm',
    #     'margin-right': '1cm',
    #     'margin-bottom': '2cm',
    #     'footer-right': '[page]',
    # }

    # print("Writing YAML metadata to PDF")

    # for i in md.Meta:
    #     if i in pdf_options_allowed:
    #         pdf_options[i] = md.Meta[i]

    # weasyprint.document.DocumentMetadata(title=None, authors=None, description=None, keywords=None, generator=None, created=None, modified=None, attachments=None)
    # print("Finished writing YAML metadata")

    if os.path.exists(pdf_filename):
        print("Overwriting existing version of "+pdf_filename)
    else:
        print("Creating new PDF file: "+pdf_filename)

    print ("Writing "+html_filename+" to "+pdf_filename)

    subprocess.Popen(["weasyprint", html_filename, pdf_filename])

    html_file.close()

    # HTML(html_filename).write_pdf(pdf_filename, stylesheets=[CSS(css_file_abs_path)])

    if args.show:
        open_file(pdf_filename)

    # if not args.keep:
    #     print("Removing temporary HTML file")
    #     os.remove(html_filename)

    sys.exit()
else:
    print(input+": No such file or directory")