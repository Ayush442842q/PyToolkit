# Dev Notes - Image Resizer

## What I learned
- `Image.open()` — opens an image file
- `Image.LANCZOS` — best resampling filter for downscaling
- `img.resize((w, h))` — resizes keeping exact dimensions
- `img.crop((left, top, right, bottom))` — crops by pixel coords
- `img.rotate(deg, expand=True)` — rotates and expands canvas
- `ImageOps.grayscale()` — converts to grayscale
- `ImageOps.mirror()` — flips horizontally
- `ImageOps.flip()` — flips vertically
- `ImageFilter.GaussianBlur(radius)` — applies blur effect
- RGBA images must be converted to RGB before saving as JPEG

## Supported formats
JPG, JPEG, PNG, BMP, GIF, WEBP

## Challenges
- RGBA to JPEG conversion needs explicit .convert("RGB")
- expand=True in rotate prevents image clipping
- Always close image with img.close() to free memory
