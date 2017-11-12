# Doctools

These are some very rough and ready tools to create Markdown documents and convert them into other formats.

## The Tools

* **newdoc** creates a new document based on a template directory. It creates a new directory and new Markdown file named after whatever argument it is given.
* **md2pdf** converts Markdown to PDF. There are other tools that do this (like pandoc) but the results seem ugly to me. md2pdf converts Markdown to HTML, and then HTML to PDF.
* **revup** is just a simple wrapper script for reveal-md. I'll add more options in the future
* **remote2doc** creates a Markdown file to be processed by reveal-md. You specify a file with a list of image URLs, and it creates a slide for each image.

## Template

The template folder holds the files which create the document:

* **index.md** contains the basic structure and metadata of the document.
* **css** contains styling information for use with md2pdf
* **plugin** contains plugins for use with reveal-md
* **preproc.js** and **reveal.json** are used with reveal-js, via reveal-md

## Todo

* Clean up code and CSS
* Move commonly used settings to another file
* Test on other platforms
* New tool: autodoc - based on keywords in input file, create Markdown document with images and Wikipedia summaries of those subjects.

## Dependencies

For PDF conversion (md2pdf):

* Weasyprint

For Reveal-js presentations (revup):

* Reveal.js
* Reveal-md

For creating presentations of images:

* Python module: urllib
* Python module: rfc3987

## Compatibility

They've been tested on Xubuntu Linux 17.10. They should mostly work on Windows, with some tweaking. Haven't tested on Macos