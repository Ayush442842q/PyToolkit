# Day 07 - Image Resizer 🖼️

A command-line image processing tool built with Pillow.

## Features
- 📐 Resize to exact dimensions
- 📊 Resize by percentage
- ✂️ Crop images
- 🔄 Rotate images
- ↔️ Flip horizontally or vertically
- 🎨 Convert between formats (jpg, png, bmp, webp)
- ⬛ Apply grayscale filter
- 🌫️ Apply blur filter
- ℹ️ View image info

## Requirements
- Python 3.6+
- Pillow

## Installation
```bash
pip install Pillow
```

## Usage
```bash
python resizer.py
```

## Functions
| Function | Description |
|----------|-------------|
| `resize_image(path, w, h, out)` | Resize to exact dimensions |
| `resize_by_percentage(path, %, out)` | Resize by percentage |
| `crop_image(path, l, t, r, b, out)` | Crop to coordinates |
| `convert_format(path, out)` | Convert image format |
| `apply_grayscale(path, out)` | Make image grayscale |
| `apply_blur(path, out, radius)` | Apply Gaussian blur |
| `rotate_image(path, degrees, out)` | Rotate by degrees |
| `flip_image(path, direction, out)` | Flip horizontal/vertical |
| `get_image_info(path)` | Get image metadata |
| `display_info(info)` | Print formatted image info |

## Author
Ayush442842q
