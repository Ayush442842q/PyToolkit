import os
from PIL import Image, ImageFilter, ImageOps

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

def apply_grayscale(image_path, output_path):
    """Converts an image to grayscale."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    gray = ImageOps.grayscale(img)
    gray.save(output_path)
    print(f"✅ Grayscale image saved to: {output_path}")
    img.close()
    return output_path

def apply_blur(image_path, output_path, radius=2):
    """Applies a blur filter to an image."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    blurred = img.filter(ImageFilter.GaussianBlur(radius=radius))
    blurred.save(output_path)
    print(f"✅ Blurred image saved to: {output_path}")
    img.close()
    return output_path

def rotate_image(image_path, degrees, output_path):
    """Rotates an image by given degrees."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    rotated = img.rotate(degrees, expand=True)
    rotated.save(output_path)
    print(f"✅ Rotated {degrees}° and saved to: {output_path}")
    img.close()
    return output_path

def flip_image(image_path, direction, output_path):
    """Flips an image horizontally or vertically."""
    if not os.path.exists(image_path):
        print(f"❌ File not found: {image_path}")
        return None
    img = Image.open(image_path)
    if direction.lower() == "horizontal":
        flipped = ImageOps.mirror(img)
    elif direction.lower() == "vertical":
        flipped = ImageOps.flip(img)
    else:
        print("❌ Direction must be 'horizontal' or 'vertical'.")
        return None
    flipped.save(output_path)
    print(f"✅ Flipped {direction} and saved to: {output_path}")
    img.close()
    return output_path

def main():
    """Main function to run the Image Resizer CLI."""
    print("🖼️  PyToolkit Image Resizer")
    print("=" * 40)
    print("1. Resize to dimensions")
    print("2. Resize by percentage")
    print("3. Crop image")
    print("4. Convert format")
    print("5. Apply grayscale")
    print("6. Apply blur")
    print("7. Rotate image")
    print("8. Flip image")
    print("9. Image info")
    print("0. Exit")
    print("=" * 40)

    choice = input("Choose option (0-9): ").strip()

    if choice == "1":
        path = input("Image path: ").strip()
        w = int(input("Width (px): ").strip())
        h = int(input("Height (px): ").strip())
        out = input("Output path: ").strip()
        resize_image(path, w, h, out)

    elif choice == "2":
        path = input("Image path: ").strip()
        pct = int(input("Percentage (e.g. 50): ").strip())
        out = input("Output path: ").strip()
        resize_by_percentage(path, pct, out)

    elif choice == "3":
        path = input("Image path: ").strip()
        l = int(input("Left: ").strip())
        t = int(input("Top: ").strip())
        r = int(input("Right: ").strip())
        b = int(input("Bottom: ").strip())
        out = input("Output path: ").strip()
        crop_image(path, l, t, r, b, out)

    elif choice == "4":
        path = input("Image path: ").strip()
        out = input("Output path (e.g. image.png): ").strip()
        convert_format(path, out)

    elif choice == "5":
        path = input("Image path: ").strip()
        out = input("Output path: ").strip()
        apply_grayscale(path, out)

    elif choice == "6":
        path = input("Image path: ").strip()
        out = input("Output path: ").strip()
        radius = int(input("Blur radius (default 2): ").strip() or "2")
        apply_blur(path, out, radius)

    elif choice == "7":
        path = input("Image path: ").strip()
        deg = int(input("Degrees to rotate: ").strip())
        out = input("Output path: ").strip()
        rotate_image(path, deg, out)

    elif choice == "8":
        path = input("Image path: ").strip()
        direction = input("Direction (horizontal/vertical): ").strip()
        out = input("Output path: ").strip()
        flip_image(path, direction, out)

    elif choice == "9":
        path = input("Image path: ").strip()
        info = get_image_info(path)
        display_info(info)

    elif choice == "0":
        print("👋 Goodbye!")

    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
