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

## Examples

### Resize Image
```python
from resizer import resize_image
resize_image("photo.jpg", 800, 600, "resized.jpg")
# ✅ Resized to 800x600 and saved to: resized.jpg
```

### Resize by Percentage
```python
from resizer import resize_by_percentage
resize_by_percentage("photo.jpg", 50, "half.jpg")
# ✅ Resized to 50% (400x300) and saved to: half.jpg
```

### Convert Format
```python
from resizer import convert_format
convert_format("photo.jpg", "photo.png")
# ✅ Converted and saved to: photo.png
```

### Apply Grayscale
```python
from resizer import apply_grayscale
apply_grayscale("photo.jpg", "gray.jpg")
# ✅ Grayscale image saved to: gray.jpg
```

### Get Image Info
```python
from resizer import get_image_info, display_info
info = get_image_info("photo.jpg")
display_info(info)
# 🖼️  Image Information
# -----------------------------------
# 📁 Filename : photo.jpg
# 🎨 Format   : JPEG
# 🌈 Mode     : RGB
# 📐 Size     : 1920 x 1080 px
# 💾 Filesize : 512.4 KB
# -----------------------------------
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
