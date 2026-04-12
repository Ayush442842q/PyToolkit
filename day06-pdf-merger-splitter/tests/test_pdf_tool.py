import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pdf_tool import get_page_count, get_pdf_info

class TestPdfTool:
    """Basic test structure for PDF Tool."""

    def test_get_pdf_info_missing_file(self):
        """Test get_pdf_info with non-existent file."""
        result = get_pdf_info("non_existent.pdf")
        assert result is None
        print("✅ test_get_pdf_info_missing_file passed!")

    def test_get_page_count_missing_file(self):
        """Test get_page_count with non-existent file."""
        result = get_page_count("non_existent.pdf")
        assert result == 0
        print("✅ test_get_page_count_missing_file passed!")

if __name__ == "__main__":
    t = TestPdfTool()
    t.test_get_pdf_info_missing_file()
    t.test_get_page_count_missing_file()
    print("\n✅ All tests passed!")
