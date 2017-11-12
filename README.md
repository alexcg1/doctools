# Doctools

These are some very rough and ready tools to create Markdown documents and convert them into other formats.

## The Tools

* **newdoc** creates a new document based on a template directory. It creates a new directory and new Markdown file named after whatever argument it is given.
* **md2pdf** converts Markdown to PDF. There are other tools that do this (like pandoc) but the results seem ugly to me. md2pdf converts Markdown to HTML, and then HTML to PDF.
* **revup** is just a simple wrapper script for reveal-md. I'll add more options in the future
* **remote2doc** creates a Markdown file to be processed by reveal-md. You specify a file with a list of image URLs, and it creates a slide for each image.

## Compatibility

They've been tested on Xubuntu Linux 17.10. They should mostly work on Windows, with some tweaking. Haven't tested on Macos