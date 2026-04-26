import os
import sys

# Configuration
OUTPUT_FOLDER = "audio_output"
DEFAULT_LANGUAGE = "en"
DEFAULT_FILENAME = "output.mp3"

def check_gtts():
    """Checks if gTTS is installed."""
    try:
        import gtts
        print("✅ gTTS is available!")
        return True
    except ImportError:
        print("❌ gTTS is not installed! Run: pip install gtts")
        return False

def ensure_output_folder(folder=OUTPUT_FOLDER):
    """Creates the output folder if it doesn't exist."""
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Output folder: {os.path.abspath(folder)}")
    return folder

def text_to_speech(text, filename=DEFAULT_FILENAME, lang=DEFAULT_LANGUAGE, folder=OUTPUT_FOLDER):
    """Converts text to speech and saves as mp3."""
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
