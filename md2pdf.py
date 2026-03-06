import sys
import os
from markdown import markdown
from xhtml2pdf import pisa

CSS = """
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #24292e;
    margin: 40px;
}
h1 {
    font-size: 24pt;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 6px;
    margin-top: 24px;
    margin-bottom: 16px;
}
h2 {
    font-size: 20pt;
    border-bottom: 1px solid #eaecef;
    padding-bottom: 6px;
    margin-top: 24px;
    margin-bottom: 16px;
}
h3 {
    font-size: 16pt;
    margin-top: 24px;
    margin-bottom: 16px;
}
h4 {
    font-size: 14pt;
    margin-top: 24px;
    margin-bottom: 16px;
}
h5 {
    font-size: 12pt;
    margin-top: 24px;
    margin-bottom: 16px;
}
h6 {
    font-size: 11pt;
    color: #6a737d;
    margin-top: 24px;
    margin-bottom: 16px;
}
p {
    margin-top: 0;
    margin-bottom: 16px;
}
code {
    font-family: Courier, monospace;
    font-size: 10pt;
    background-color: #f6f8fa;
    padding: 2px 4px;
}
pre {
    background-color: #f6f8fa;
    padding: 16px;
    font-family: Courier, monospace;
    font-size: 10pt;
    line-height: 1.45;
    overflow: auto;
}
blockquote {
    padding: 0 16px;
    color: #6a737d;
    border-left: 4px solid #dfe2e5;
    margin: 0 0 16px 0;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 16px;
}
th, td {
    padding: 6px 13px;
    border: 1px solid #dfe2e5;
}
th {
    font-weight: bold;
    background-color: #f6f8fa;
}
hr {
    border: 0;
    border-top: 1px solid #eaecef;
    margin: 24px 0;
}
a {
    color: #0366d6;
}
ul, ol {
    padding-left: 2em;
    margin-bottom: 16px;
}
li {
    margin-bottom: 4px;
}
img {
    max-width: 100%;
}
"""

EXTENSIONS = [
    "tables",
    "fenced_code",
    "sane_lists",
    "smarty",
    "nl2br",
]


def convert(md_path):
    md_path = os.path.abspath(md_path)
    pdf_path = os.path.splitext(md_path)[0] + ".pdf"

    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown(md_text, extensions=EXTENSIONS)

    full_html = (
        "<!DOCTYPE html><html><head>"
        '<meta charset="utf-8">'
        f"<style>{CSS}</style>"
        f"</head><body>{html_body}</body></html>"
    )

    with open(pdf_path, "wb") as f:
        result = pisa.CreatePDF(full_html, dest=f)

    if result.err:
        print(f"Error: conversion failed for {md_path}")
        input("Press Enter to close...")
        sys.exit(1)

    print(f"Saved: {pdf_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: md2pdf <file.md>")
        input("Press Enter to close...")
        sys.exit(1)

    md_path = sys.argv[1]

    if not os.path.isfile(md_path):
        print(f"Error: file not found: {md_path}")
        input("Press Enter to close...")
        sys.exit(1)

    try:
        convert(md_path)
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to close...")
        sys.exit(1)


if __name__ == "__main__":
    main()
