import sys
import os
import shutil
sys.path.insert(0, os.path.abspath(".."))

from tts import get_supported_languages, ensure_output_folder

def test_supported_languages_not_empty():
    langs = get_supported_languages()
    assert len(langs) > 0
    print("✅ test_supported_languages_not_empty passed!")

test_supported_languages_not_empty()

def test_english_in_languages():
    langs = get_supported_languages()
    assert "en" in langs
    assert langs["en"] == "English"
    print("✅ test_english_in_languages passed!")

test_english_in_languages()

def test_ensure_output_folder():
    test_folder = "test_audio_temp"
    ensure_output_folder(test_folder)
    assert os.path.exists(test_folder)
    shutil.rmtree(test_folder)
    print("✅ test_ensure_output_folder passed!")

test_ensure_output_folder()

def test_hindi_in_languages():
    langs = get_supported_languages()
    assert "hi" in langs
    assert langs["hi"] == "Hindi"
    print("✅ test_hindi_in_languages passed!")

test_hindi_in_languages()
