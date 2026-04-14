import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from resizer import get_image_info, resize_image, apply_grayscale

class TestResizer:
    """Basic tests for Image Resizer."""

    def test_get_image_info_missing(self):
        result = get_image_info("non_existent.jpg")
        assert result is None
        print("✅ test_get_image_info_missing passed!")

    def test_resize_image_missing(self):
        result = resize_image("non_existent.jpg", 100, 100, "output.jpg")
        assert result is None
        print("✅ test_resize_image_missing passed!")

if __name__ == "__main__":
    t = TestResizer()
    t.test_get_image_info_missing()
    t.test_resize_image_missing()
    print("\n✅ All tests passed!")
