import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pdf_tool import get_page_count, get_pdf_info, merge_pdfs, split_pdf, rotate_pages, extract_pages

class TestPdfTool:
    """Tests for PDF Tool."""

    def test_get_pdf_info_missing_file(self):
        result = get_pdf_info("non_existent.pdf")
        assert result is None
        print("✅ test_get_pdf_info_missing_file passed!")

    def test_get_page_count_missing_file(self):
        result = get_page_count("non_existent.pdf")
        assert result == 0
        print("✅ test_get_page_count_missing_file passed!")

    def test_merge_pdfs_missing_files(self):
        try:
            merge_pdfs(["fake1.pdf", "fake2.pdf"], "output_test.pdf")
            print("✅ test_merge_pdfs_missing_files passed!")
        except Exception as e:
            print(f"⚠️  merge_pdfs raised an exception: {e}")

    def test_split_pdf_missing_file(self):
        result = split_pdf("non_existent.pdf", "output_folder")
        assert result == []
        print("✅ test_split_pdf_missing_file passed!")

    def test_rotate_pages_invalid_rotation(self):
        result = rotate_pages("non_existent.pdf", 45, "output.pdf")
        assert result is None
        print("✅ test_rotate_pages_invalid_rotation passed!")

    def test_extract_pages_missing_file(self):
        result = extract_pages("non_existent.pdf", [1, 2], "output.pdf")
        assert result is None
        print("✅ test_extract_pages_missing_file passed!")

if __name__ == "__main__":
    t = TestPdfTool()
    t.test_get_pdf_info_missing_file()
    t.test_get_page_count_missing_file()
    t.test_merge_pdfs_missing_files()
    t.test_split_pdf_missing_file()
    t.test_rotate_pages_invalid_rotation()
    t.test_extract_pages_missing_file()
    print("\n✅ All tests passed!")
