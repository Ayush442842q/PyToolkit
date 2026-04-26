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
        print("❌ gTTS is not installed!")
        print("   Run: pip install gtts")
        return False
