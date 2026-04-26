import os
import sys

OUTPUT_FOLDER = "qr_codes"
DEFAULT_FILENAME = "qrcode.png"
DEFAULT_SIZE = 10
DEFAULT_BORDER = 4

def check_dependencies():
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
    return True

def ensure_output_folder(folder=OUTPUT_FOLDER):
    os.makedirs(folder, exist_ok=True)
    return folder

def generate_qr(data, filename=DEFAULT_FILENAME, folder=OUTPUT_FOLDER,
                size=DEFAULT_SIZE, border=DEFAULT_BORDER):
    """Generates a QR code from given data and saves it as an image."""
    import qrcode

    if not data.strip():
        print("❌ Data cannot be empty!")
        return None

    ensure_output_folder(folder)
    output_path = os.path.join(folder, filename)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    print(f"✅ QR code saved to: {output_path}")
    return output_path
