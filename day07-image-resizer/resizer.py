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

def display_info(info):
    """Displays image info in a formatted way."""
    if not info:
        print("❌ No info to display.")
        return
    print("\n🖼️  Image Information")
    print("-" * 35)
    print(f"📁 Filename : {info['filename']}")
    print(f"🎨 Format   : {info['format']}")
    print(f"🌈 Mode     : {info['mode']}")
    print(f"📐 Size     : {info['width']} x {info['height']} px")
    print(f"💾 Filesize : {info['size_kb']} KB")
    print("-" * 35)
