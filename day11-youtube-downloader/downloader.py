import os
import subprocess
import sys
import json
from urllib.parse import urlparse

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

def is_valid_url(url):
    """Validates that the URL is a proper web URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def ensure_download_folder(folder=DOWNLOAD_FOLDER):
    """Creates the download folder if it doesn't exist."""
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Download folder: {os.path.abspath(folder)}")
    return folder

def download_video(url, folder=DOWNLOAD_FOLDER):
    """Downloads a video in mp4 format."""
    if not is_valid_url(url):
        print("❌ Invalid URL!")
        return False
    ensure_download_folder(folder)
    command = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", os.path.join(folder, "%(title)s.%(ext)s"),
        url
    ]
    print(f"⬇️  Downloading video: {url}")
    result = subprocess.run(command, text=True)
    return result.returncode == 0

def download_audio(url, folder=DOWNLOAD_FOLDER):
    """Downloads only audio in mp3 format."""
    if not is_valid_url(url):
        print("❌ Invalid URL!")
        return False
    ensure_download_folder(folder)
    command = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "-o", os.path.join(folder, "%(title)s.%(ext)s"),
        url
    ]
    print(f"🎵 Downloading audio: {url}")
    result = subprocess.run(command, text=True)
    return result.returncode == 0

def get_video_info(url):
    """Fetches video metadata without downloading."""
    if not is_valid_url(url):
        print("❌ Invalid URL!")
        return None
    command = ["yt-dlp", "--dump-json", "--no-playlist", url]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        data = json.loads(result.stdout)
        return {
            "title": data.get("title", "Unknown"),
            "duration": data.get("duration_string", "Unknown"),
            "uploader": data.get("uploader", "Unknown"),
            "views": data.get("view_count", 0),
        }
    return None
