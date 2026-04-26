# Day 11 - YouTube Downloader

A Python CLI tool to download YouTube videos and audio using yt-dlp.

## Features
- Download videos in mp4 format (best quality)
- Download audio only in mp3 format
- Fetch video info without downloading
- Download entire playlists
- Interactive menu

## Requirements
```bash
pip install yt-dlp
```

## Usage
```bash
python downloader.py
```

## Example
```
🎬 YouTube Downloader
----------------------------------------
1. Download Video (mp4)
2. Download Audio (mp3)
3. Get Video Info
4. Download Playlist
5. Exit
----------------------------------------
Choose an option (1-5): 3
Enter URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

🎬 Video Information
----------------------------------------
📌 Title    : Rick Astley - Never Gonna Give You Up
⏱️  Duration : 3:33
👤 Uploader : Rick Astley
👀 Views    : 1,500,000,000
----------------------------------------
```

## Libraries Used
- `yt-dlp` — powerful YouTube downloader (updated fork of youtube-dl)
- `subprocess` — runs yt-dlp commands from Python
- `json` — parses video metadata
