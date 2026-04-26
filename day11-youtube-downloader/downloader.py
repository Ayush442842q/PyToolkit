import os
import subprocess
import sys
import json
from urllib.parse import urlparse

DOWNLOAD_FOLDER = "downloads"

def check_ytdlp():
    result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
    if result.returncode != 0:
        print("❌ yt-dlp is not installed! Run: pip install yt-dlp")
        return False
    return True

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def ensure_download_folder(folder=DOWNLOAD_FOLDER):
    os.makedirs(folder, exist_ok=True)
    return folder

def download_video(url, folder=DOWNLOAD_FOLDER):
    if not is_valid_url(url):
        print("❌ Invalid URL!")
        return False
    ensure_download_folder(folder)
    command = ["yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
               "-o", os.path.join(folder, "%(title)s.%(ext)s"), url]
    result = subprocess.run(command, text=True)
    return result.returncode == 0

def download_audio(url, folder=DOWNLOAD_FOLDER):
    if not is_valid_url(url):
        print("❌ Invalid URL!")
        return False
    ensure_download_folder(folder)
    command = ["yt-dlp", "-x", "--audio-format", "mp3",
               "-o", os.path.join(folder, "%(title)s.%(ext)s"), url]
    result = subprocess.run(command, text=True)
    return result.returncode == 0

def get_video_info(url):
    if not is_valid_url(url):
        return None
    command = ["yt-dlp", "--dump-json", "--no-playlist", url]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        data = json.loads(result.stdout)
        return {"title": data.get("title", "Unknown"), "duration": data.get("duration_string", "Unknown"),
                "uploader": data.get("uploader", "Unknown"), "views": data.get("view_count", 0)}
    return None

def display_info(info):
    if not info:
        print("❌ Could not fetch video info!")
        return
    print("\n🎬 Video Information")
    print("-" * 40)
    print(f"📌 Title    : {info['title']}")
    print(f"⏱️  Duration : {info['duration']}")
    print(f"👤 Uploader : {info['uploader']}")
    print(f"👀 Views    : {info['views']:,}")
    print("-" * 40)

def download_playlist(url, folder=DOWNLOAD_FOLDER):
    if not is_valid_url(url):
        print("❌ Invalid URL!")
        return False
    ensure_download_folder(folder)
    command = ["yt-dlp", "-f", "best[ext=mp4]/best",
               "-o", os.path.join(folder, "%(playlist_index)s - %(title)s.%(ext)s"), url]
    result = subprocess.run(command, text=True)
    return result.returncode == 0

def main():
    """Main function — interactive YouTube downloader menu."""
    if not check_ytdlp():
        sys.exit(1)

    print("\n🎬 YouTube Downloader")
    print("-" * 40)
    print("1. Download Video (mp4)")
    print("2. Download Audio (mp3)")
    print("3. Get Video Info")
    print("4. Download Playlist")
    print("5. Exit")
    print("-" * 40)

    choice = input("Choose an option (1-5): ").strip()

    if choice == "5":
        print("👋 Bye!")
        return

    url = input("Enter URL: ").strip()

    if choice == "1":
        download_video(url)
    elif choice == "2":
        download_audio(url)
    elif choice == "3":
        info = get_video_info(url)
        display_info(info)
    elif choice == "4":
        download_playlist(url)
    else:
        print("❌ Invalid option!")

if __name__ == "__main__":
    main()
