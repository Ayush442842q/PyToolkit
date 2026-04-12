# Day 06 - PDF Merger/Splitter 📄

A command-line tool to merge, split, rotate, and extract pages from PDF files.

## Features
- 📎 Merge multiple PDFs into one
- ✂️ Split a PDF into individual pages
- 📑 Extract specific pages from a PDF
- 🔄 Rotate pages (90°, 180°, 270°)
- 🖼️ Add watermark to all pages
- ℹ️ View PDF info (pages, size, encryption)

## Requirements
- Python 3.6+
- PyPDF2

## Installation
```bash
pip install PyPDF2
```

## Usage
```bash
python pdf_tool.py
```

## Examples

### Merge PDFs
```python
from pdf_tool import merge_pdfs

merge_pdfs(["file1.pdf", "file2.pdf", "file3.pdf"], "merged.pdf")
# ✅ Merged 3 PDFs into: merged.pdf
```

### Split PDF
```python
from pdf_tool import split_pdf

split_pdf("document.pdf", "output_pages/")
# ✅ Split into 5 pages in: output_pages/
```

### Extract Specific Pages
```python
from pdf_tool import extract_pages

extract_pages("document.pdf", [1, 3, 5], "selected.pdf")
# ✅ Extracted 3 pages to: selected.pdf
```

### Rotate Pages
```python
from pdf_tool import rotate_pages

rotate_pages("document.pdf", 90, "rotated.pdf")
# ✅ Rotated all pages by 90° and saved to: rotated.pdf
```

### Get PDF Info
```python
from pdf_tool import get_pdf_info, display_info

info = get_pdf_info("document.pdf")
display_info(info)

# 📄 PDF Information
# -----------------------------------
# 📁 Filename  : document.pdf
# 📃 Pages     : 10
# 💾 Size      : 245.6 KB
# 🔒 Encrypted : No
# -----------------------------------
```

## Functions
| Function | Description |
|----------|-------------|
| `merge_pdfs(pdf_list, output)` | Merges list of PDFs into one file |
| `split_pdf(pdf_path, folder)` | Splits PDF into individual pages |
| `extract_pages(pdf, pages, output)` | Extracts specific page numbers |
| `rotate_pages(pdf, degrees, output)` | Rotates all pages by degrees |
| `add_watermark(pdf, watermark, output)` | Adds watermark PDF to all pages |
| `get_pdf_info(pdf_path)` | Returns pages, size, encryption info |
| `get_page_count(pdf_path)` | Returns total page count |
| `display_info(info)` | Prints formatted PDF info |

## Author
Ayush442842q
