# Dev Notes - PDF Merger/Splitter

## What I learned
- `PdfReader` — reads PDF files and accesses pages
- `PdfWriter` — creates new PDF files from pages
- `writer.add_page(page)` — adds a page to the output PDF
- `page.rotate(degrees)` — rotates a page in place
- `page.merge_page(watermark)` — overlays a watermark page
- `reader.is_encrypted` — checks if PDF is password protected
- `os.path.getsize()` — gets file size in bytes

## Challenges
- PyPDF2 rotate changed from `rotateClockwise()` to `rotate()` in newer versions
- Watermark merging requires both PDFs to have matching page sizes
- Always open output files in "wb" (write binary) mode

## Data flow
Input PDF → PdfReader → pages list → PdfWriter → Output PDF
