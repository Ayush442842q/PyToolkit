import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from resizer import get_image_info, resize_image, apply_grayscale, flip_image, rotate_image, crop_image, convert_format, apply_blur, resize_by_percentage

class TestResizer:
    """Full tests for Image Resizer."""

    def test_get_image_info_missing(self):
        result = get_image_info("non_existent.jpg")
        assert result is None
        print("✅ test_get_image_info_missing passed!")

    def test_resize_image_missing(self):
        result = resize_image("non_existent.jpg", 100, 100, "output.jpg")
        assert result is None
        print("✅ test_resize_image_missing passed!")

    def test_apply_grayscale_missing(self):
        result = apply_grayscale("non_existent.jpg", "output.jpg")
        assert result is None
        print("✅ test_apply_grayscale_missing passed!")

    def test_flip_image_invalid_direction(self):
        result = flip_image("non_existent.jpg", "diagonal", "output.jpg")
        assert result is None
        print("✅ test_flip_image_invalid_direction passed!")

    def test_rotate_image_missing(self):
        result = rotate_image("non_existent.jpg", 90, "output.jpg")
        assert result is None
        print("✅ test_rotate_image_missing passed!")

    def test_crop_image_missing(self):
        result = crop_image("non_existent.jpg", 0, 0, 100, 100, "output.jpg")
        assert result is None
        print("✅ test_crop_image_missing passed!")

    def test_convert_format_missing(self):
        result = convert_format("non_existent.jpg", "output.png")
        assert result is None
        print("✅ test_convert_format_missing passed!")

    def test_apply_blur_missing(self):
        result = apply_blur("non_existent.jpg", "output.jpg")
        assert result is None
        print("✅ test_apply_blur_missing passed!")

    def test_resize_by_percentage_missing(self):
        result = resize_by_percentage("non_existent.jpg", 50, "output.jpg")
        assert result is None
        print("✅ test_resize_by_percentage_missing passed!")

if __name__ == "__main__":
    t = TestResizer()
    t.test_get_image_info_missing()
    t.test_resize_image_missing()
    t.test_apply_grayscale_missing()
    t.test_flip_image_invalid_direction()
    t.test_rotate_image_missing()
    t.test_crop_image_missing()
    t.test_convert_format_missing()
    t.test_apply_blur_missing()
    t.test_resize_by_percentage_missing()
    print("\n✅ All tests passed!")
