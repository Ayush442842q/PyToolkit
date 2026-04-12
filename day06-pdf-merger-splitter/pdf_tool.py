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

def get_pdf_info(pdf_path):
    """Returns basic info about a PDF file."""
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return None
    reader = PdfReader(pdf_path)
    info = {
        "filename": os.path.basename(pdf_path),
        "pages": len(reader.pages),
        "size_kb": round(os.path.getsize(pdf_path) / 1024, 2),
        "encrypted": reader.is_encrypted
    }
    return info

def extract_pages(pdf_path, page_numbers, output_path):
    """Extracts specific pages from a PDF."""
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return None
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    total_pages = len(reader.pages)
    for num in page_numbers:
        if 1 <= num <= total_pages:
            writer.add_page(reader.pages[num - 1])
        else:
            print(f"⚠️  Skipping invalid page number: {num}")
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"✅ Extracted {len(page_numbers)} pages to: {output_path}")
    return output_path

def display_info(info):
    """Displays PDF info in a formatted way."""
    if not info:
        print("❌ No info to display.")
        return
    print("\n📄 PDF Information")
    print("-" * 35)
    print(f"📁 Filename  : {info['filename']}")
    print(f"📃 Pages     : {info['pages']}")
    print(f"💾 Size      : {info['size_kb']} KB")
    print(f"🔒 Encrypted : {'Yes' if info['encrypted'] else 'No'}")
    print("-" * 35)

def rotate_pages(pdf_path, rotation, output_path):
    """Rotates all pages in a PDF by given degrees (90, 180, 270)."""
    if not os.path.exists(pdf_path):
        print(f"❌ File not found: {pdf_path}")
        return None
    if rotation not in [90, 180, 270]:
        print("❌ Rotation must be 90, 180, or 270 degrees.")
        return None
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"✅ Rotated all pages by {rotation}° and saved to: {output_path}")
    return output_path
