import os
import sys

OUTPUT_FOLDER = "audio_output"
DEFAULT_LANGUAGE = "en"
DEFAULT_FILENAME = "output.mp3"

SUPPORTED_LANGUAGES = {
    "en": "English", "hi": "Hindi", "fr": "French",
    "de": "German", "es": "Spanish", "it": "Italian",
    "ja": "Japanese", "ko": "Korean", "pt": "Portuguese",
    "ru": "Russian", "zh": "Chinese", "ar": "Arabic",
}

def check_gtts():
    try:
        import gtts
        return True
    except ImportError:
        print("❌ gTTS is not installed! Run: pip install gtts")
        return False

def ensure_output_folder(folder=OUTPUT_FOLDER):
    os.makedirs(folder, exist_ok=True)
    return folder

def get_supported_languages():
    return SUPPORTED_LANGUAGES

def display_languages():
    print("\n🌍 Supported Languages")
    print("-" * 30)
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"  {code:<6} → {name}")
    print("-" * 30)

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
    return text_to_speech(text, filename=filename, lang=lang, folder=folder)

def main():
    """Main interactive menu for Text to Speech tool."""
    if not check_gtts():
        sys.exit(1)

    print("\n🔊 Text to Speech Converter")
    print("-" * 40)
    print("1. Convert text to speech")
    print("2. Convert text to speech (slow)")
    print("3. Convert text file to speech")
    print("4. Show supported languages")
    print("5. Exit")
    print("-" * 40)

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        text = input("Enter text: ")
        lang = input(f"Language code (default: {DEFAULT_LANGUAGE}): ").strip() or DEFAULT_LANGUAGE
        filename = input("Output filename (default: output.mp3): ").strip() or DEFAULT_FILENAME
        text_to_speech(text, filename=filename, lang=lang)
    elif choice == "2":
        text = input("Enter text: ")
        lang = input(f"Language code (default: {DEFAULT_LANGUAGE}): ").strip() or DEFAULT_LANGUAGE
        text_to_speech_slow(text, lang=lang)
    elif choice == "3":
        file_path = input("Enter text file path: ").strip()
        lang = input(f"Language code (default: {DEFAULT_LANGUAGE}): ").strip() or DEFAULT_LANGUAGE
        file_to_speech(file_path, lang=lang)
    elif choice == "4":
        display_languages()
    elif choice == "5":
        print("👋 Bye!")
    else:
        print("❌ Invalid option!")

if __name__ == "__main__":
    main()
