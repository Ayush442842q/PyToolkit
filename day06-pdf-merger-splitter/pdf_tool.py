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

def split_pdf(pdf_path, output_folder):
    """Splits a PDF into individual pages."""
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return []
    os.makedirs(output_folder, exist_ok=True)
    reader = PdfReader(pdf_path)
    output_files = []
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = os.path.join(output_folder, f"page_{i + 1}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)
        output_files.append(output_path)
    print(f"✅ Split into {len(output_files)} pages in: {output_folder}")
    return output_files
