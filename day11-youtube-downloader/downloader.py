import os
import subprocess
import sys

# Configuration
DOWNLOAD_FOLDER = "downloads"
DEFAULT_FORMAT = "mp4"

def check_ytdlp():
    """Checks if yt-dlp is installed."""
    result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ yt-dlp is not installed!")
        print("   Run: pip install yt-dlp")
        return False
    print(f"✅ yt-dlp version: {result.stdout.strip()}")
    return True
