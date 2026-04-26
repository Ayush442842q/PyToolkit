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
        print(f"❌ Missing: {', '.join(missing)} — Run: pip install {' '.join(missing)}")
        return False
    return True

def ensure_output_folder(folder=OUTPUT_FOLDER):
    os.makedirs(folder, exist_ok=True)
    return folder

def _detect_data_type(data):
    if data.startswith("http://") or data.startswith("https://"):
        return "URL"
    elif data.startswith("mailto:"):
        return "Email"
    elif data.startswith("tel:"):
        return "Phone"
    elif data.startswith("WIFI:"):
        return "WiFi"
    elif "@" in data and "." in data:
        return "Email Address"
    else:
        return "Plain Text"

def get_qr_info(data):
    return {"data": data, "length": len(data), "type": _detect_data_type(data)}

def display_info(info):
    print("\n📋 QR Code Info")
    print("-" * 40)
    print(f"  Type   : {info['type']}")
    print(f"  Length : {info['length']} characters")
    print(f"  Data   : {info['data'][:60]}{'...' if len(info['data']) > 60 else ''}")
    print("-" * 40)

def generate_qr(data, filename=DEFAULT_FILENAME, folder=OUTPUT_FOLDER,
                size=DEFAULT_SIZE, border=DEFAULT_BORDER):
    import qrcode
    if not data.strip():
        print("❌ Data cannot be empty!")
        return None
    ensure_output_folder(folder)
    output_path = os.path.join(folder, filename)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    print(f"✅ QR code saved to: {output_path}")
    return output_path

def generate_qr_colored(data, fill_color="darkblue", back_color="white",
                        filename="qrcode_colored.png", folder=OUTPUT_FOLDER):
    import qrcode
    if not data.strip():
        print("❌ Data cannot be empty!")
        return None
    ensure_output_folder(folder)
    output_path = os.path.join(folder, filename)
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=DEFAULT_SIZE, border=DEFAULT_BORDER)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_path)
    print(f"✅ Colored QR code saved to: {output_path}")
    return output_path

def generate_qr_bulk(data_list, folder=OUTPUT_FOLDER):
    if not data_list:
        print("❌ Data list is empty!")
        return []
    results = []
    for i, data in enumerate(data_list, 1):
        filename = f"qrcode_{i:03d}.png"
        path = generate_qr(data, filename=filename, folder=folder)
        if path:
            results.append(path)
    print(f"\n✅ Generated {len(results)} QR codes in: {folder}")
    return results

def main():
    """Main interactive menu for QR Code Generator."""
    if not check_dependencies():
        sys.exit(1)

    print("\n📱 QR Code Generator")
    print("-" * 40)
    print("1. Generate QR code (black & white)")
    print("2. Generate QR code (colored)")
    print("3. Generate QR codes in bulk")
    print("4. Show QR code info")
    print("5. Exit")
    print("-" * 40)

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        data = input("Enter data (URL, text, email...): ").strip()
        filename = input("Output filename (default: qrcode.png): ").strip() or DEFAULT_FILENAME
        generate_qr(data, filename=filename)
    elif choice == "2":
        data = input("Enter data: ").strip()
        fill = input("Fill color (default: darkblue): ").strip() or "darkblue"
        back = input("Background color (default: white): ").strip() or "white"
        generate_qr_colored(data, fill_color=fill, back_color=back)
    elif choice == "3":
        print("Enter data items (one per line). Type 'done' when finished:")
        items = []
        while True:
            line = input(f"  Item {len(items)+1}: ").strip()
            if line.lower() == "done":
                break
            if line:
                items.append(line)
        generate_qr_bulk(items)
    elif choice == "4":
        data = input("Enter data to analyze: ").strip()
        info = get_qr_info(data)
        display_info(info)
    elif choice == "5":
        print("👋 Bye!")
    else:
        print("❌ Invalid option!")

if __name__ == "__main__":
    main()
