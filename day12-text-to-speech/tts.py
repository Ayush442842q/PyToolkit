import os
import sys

OUTPUT_FOLDER = "audio_output"
DEFAULT_LANGUAGE = "en"
DEFAULT_FILENAME = "output.mp3"

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh": "Chinese",
    "ar": "Arabic",
}

def check_gtts():
    try:
        import gtts
        print("✅ gTTS is available!")
        return True
    except ImportError:
        print("❌ gTTS is not installed! Run: pip install gtts")
        return False

def ensure_output_folder(folder=OUTPUT_FOLDER):
    os.makedirs(folder, exist_ok=True)
    return folder

def get_supported_languages():
    """Returns a dict of supported language codes and names."""
    return SUPPORTED_LANGUAGES

def text_to_speech(text, filename=DEFAULT_FILENAME, lang=DEFAULT_LANGUAGE, folder=OUTPUT_FOLDER):
    from gtts import gTTS
    if not text.strip():
        print("❌ Text cannot be empty!")
        return None
    ensure_output_folder(folder)
    output_path = os.path.join(folder, filename)
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_path)
    print(f"✅ Audio saved to: {output_path}")
    return output_path

def text_to_speech_slow(text, filename="output_slow.mp3", lang=DEFAULT_LANGUAGE, folder=OUTPUT_FOLDER):
    from gtts import gTTS
    if not text.strip():
        print("❌ Text cannot be empty!")
        return None
    ensure_output_folder(folder)
    output_path = os.path.join(folder, filename)
    tts = gTTS(text=text, lang=lang, slow=True)
    tts.save(output_path)
    print(f"✅ Slow audio saved to: {output_path}")
    return output_path

def file_to_speech(file_path, lang=DEFAULT_LANGUAGE, folder=OUTPUT_FOLDER):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        print("❌ File is empty!")
        return None
    filename = os.path.splitext(os.path.basename(file_path))[0] + ".mp3"
    print(f"📄 Converting file: {file_path}")
    return text_to_speech(text, filename=filename, lang=lang, folder=folder)
