# Dev Notes - YouTube Downloader

## What I learned
- `yt-dlp` — command-line tool to download from YouTube and 1000+ sites
- `subprocess.run()` — run terminal commands from Python
- `capture_output=True` — captures stdout and stderr
- `json.loads()` — converts JSON string to Python dict
- `urlparse()` — breaks URL into components (scheme, netloc, path)
- `-f` flag in yt-dlp — selects video format/quality
- `-x --audio-format mp3` — extracts audio and converts to mp3
- `--dump-json` — gets metadata without downloading

## yt-dlp format string
- `%(title)s.%(ext)s` — saves file as "Video Title.mp4"
- `%(playlist_index)s - %(title)s.%(ext)s` — numbers playlist items

## Challenges
- yt-dlp must be installed separately (pip install yt-dlp)
- ffmpeg needed for audio conversion (can install via choco or winget)
- YouTube changes things often — yt-dlp updates frequently to keep up
