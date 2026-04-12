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
