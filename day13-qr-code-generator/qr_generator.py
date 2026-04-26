import os
import sys

OUTPUT_FOLDER = "qr_codes"
DEFAULT_FILENAME = "qrcode.png"
DEFAULT_SIZE = 10
DEFAULT_BORDER = 4

def check_dependencies():
    """Checks if required libraries are installed."""
    missing = []
    try:
        import qrcode
    except ImportError:
        missing.append("qrcode[pil]")
    try:
        from PIL import Image
    except ImportError:
        missing.append("Pillow")
    if missing:
        print(f"❌ Missing libraries: {', '.join(missing)}")
        print(f"   Run: pip install {' '.join(missing)}")
        return False
    print("✅ All dependencies are available!")
    return True

def ensure_output_folder(folder=OUTPUT_FOLDER):
    """Creates the output folder if it doesn't exist."""
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Output folder: {os.path.abspath(folder)}")
    return folder
