# Dev Notes - QR Code Generator

## What I learned
- `qrcode.QRCode()` — creates a QR code object with settings
- `version=1` — smallest QR code size (auto-grows with fit=True)
- `error_correction=ERROR_CORRECT_H` — 30% of QR can be damaged and still scan
- `box_size` — pixel size of each black/white square
- `border` — number of white squares around the edge
- `qr.add_data(data)` — adds content to QR code
- `qr.make(fit=True)` — auto-calculates the right version/size
- `qr.make_image(fill_color, back_color)` — renders as image
- `.save(path)` — saves PNG using Pillow

## Error Correction Levels
- ERROR_CORRECT_L — 7% recovery
- ERROR_CORRECT_M — 15% recovery
- ERROR_CORRECT_Q — 25% recovery
- ERROR_CORRECT_H — 30% recovery (best, used here)

## QR Code Data Formats
- URL → just paste the full URL
- WiFi → WIFI:S:NetworkName;T:WPA;P:Password;;
- Phone → tel:+919876543210
- Email → mailto:user@example.com

## Fun ideas to extend
- Add logo/image in center of QR code using Pillow
- Generate vCard QR codes for contact sharing
- Build a web UI using Flask
