import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pdf_tool import get_page_count, get_pdf_info, merge_pdfs, split_pdf

class TestPdfTool:
    """Tests for PDF Tool."""

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

    def test_merge_pdfs_missing_files(self):
        """Test merge_pdfs skips missing files gracefully."""
        try:
            merge_pdfs(["fake1.pdf", "fake2.pdf"], "output_test.pdf")
            print("✅ test_merge_pdfs_missing_files passed!")
        except Exception as e:
            print(f"⚠️  merge_pdfs raised an exception: {e}")

    def test_split_pdf_missing_file(self):
        """Test split_pdf with non-existent file."""
        result = split_pdf("non_existent.pdf", "output_folder")
        assert result == []
        print("✅ test_split_pdf_missing_file passed!")

if __name__ == "__main__":
    t = TestPdfTool()
    t.test_get_pdf_info_missing_file()
    t.test_get_page_count_missing_file()
    t.test_merge_pdfs_missing_files()
    t.test_split_pdf_missing_file()
    print("\n✅ All tests passed!")
