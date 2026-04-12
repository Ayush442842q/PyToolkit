import os
from PyPDF2 import PdfReader, PdfWriter

# PyToolkit - Day 06
# Tool: PDF Merger/Splitter
# Author: Ayush442842q
# Description: Merge, split, rotate and extract pages from PDF files

def merge_pdfs(pdf_list, output_path):
    """Merges multiple PDF files into one."""
    writer = PdfWriter()
    for pdf in pdf_list:
        if not os.path.exists(pdf):
            print(f"❌ File not found: {pdf}")
            continue
        reader = PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"✅ Merged {len(pdf_list)} PDFs into: {output_path}")
    return output_path
