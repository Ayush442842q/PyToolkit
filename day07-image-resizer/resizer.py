import os
from PIL import Image

# PyToolkit - Day 07
# Tool: Image Resizer
# Author: Ayush442842q
# Description: Resize, crop, convert and apply filters to images

SUPPORTED_FORMATS = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp"]

def get_image_info(image_path):
    """Returns basic info about an image file."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    info = {
        "filename": os.path.basename(image_path),
        "format": img.format,
        "mode": img.mode,
        "width": img.size[0],
        "height": img.size[1],
        "size_kb": round(os.path.getsize(image_path) / 1024, 2)
    }
    img.close()
    return info
