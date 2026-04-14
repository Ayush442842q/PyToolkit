import os
from PIL import Image, ImageFilter

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

def resize_image(image_path, width, height, output_path):
    """Resizes an image to given dimensions."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    resized = img.resize((width, height), Image.LANCZOS)
    resized.save(output_path)
    print(f"✅ Resized to {width}x{height} and saved to: {output_path}")
    img.close()
    return output_path

def resize_by_percentage(image_path, percent, output_path):
    """Resizes an image by a percentage of its original size."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    new_width = int(img.width * percent / 100)
    new_height = int(img.height * percent / 100)
    resized = img.resize((new_width, new_height), Image.LANCZOS)
    resized.save(output_path)
    print(f"✅ Resized to {percent}% ({new_width}x{new_height}) and saved to: {output_path}")
    img.close()
    return output_path

def crop_image(image_path, left, top, right, bottom, output_path):
    """Crops an image to given coordinates."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    cropped = img.crop((left, top, right, bottom))
    cropped.save(output_path)
    print(f"✅ Cropped image saved to: {output_path}")
    img.close()
    return output_path

def convert_format(image_path, output_path):
    """Converts an image to a different format based on output extension."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    if img.mode == "RGBA" and not output_path.endswith(".png"):
        img = img.convert("RGB")
    img.save(output_path)
    print(f"✅ Converted and saved to: {output_path}")
    img.close()
    return output_path
