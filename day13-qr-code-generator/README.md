# Day 13 - QR Code Generator

A Python CLI tool that generates QR codes for URLs, text, emails, WiFi and more.

## Features
- Generate standard black & white QR codes
- Generate colored QR codes with custom colors
- Bulk generate multiple QR codes at once
- Auto-detects data type (URL, Email, Phone, WiFi, Text)
- Saves as PNG images

## Requirements
```bash
pip install qrcode[pil] Pillow
```

## Usage
```bash
python qr_generator.py
```

## Example
```
📱 QR Code Generator
----------------------------------------
1. Generate QR code (black & white)
2. Generate QR code (colored)
3. Generate QR codes in bulk
4. Show QR code info
5. Exit
----------------------------------------
Choose an option (1-5): 1
Enter data (URL, text, email...): https://github.com/Ayush442842q
Output filename (default: qrcode.png): github.png
✅ QR code saved to: qr_codes/github.png
```

## Supported Data Types
| Type | Example |
|------|---------|
| URL | https://example.com |
| Email | mailto:user@example.com |
| Phone | tel:+1234567890 |
| WiFi | WIFI:S:MyNetwork;T:WPA;P:password;; |
| Text | Any plain text |

## Libraries Used
- `qrcode` — generates QR code data matrix
- `Pillow` — renders and saves QR code as image
