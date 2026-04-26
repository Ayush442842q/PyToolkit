# Dev Notes - Text to Speech

## What I learned
- `gtts.gTTS(text, lang, slow)` — creates TTS object
- `.save(filepath)` — saves audio as mp3 file
- `slow=True` — speaks at reduced speed (great for language learning)
- Language codes — 2 letter codes like 'en', 'hi', 'fr', 'ja'
- `os.path.splitext()` — splits filename from extension
- `os.path.basename()` — gets filename from full path

## How gTTS works
1. Sends your text to Google Translate's TTS engine
2. Google returns an mp3 audio stream
3. gTTS saves that stream to a file
Requires internet connection to work!

## Challenges
- gTTS needs internet — won't work offline
- For offline TTS, pyttsx3 is an alternative (no quality guarantee)
- Some languages need the correct unicode text input

## Fun ideas to extend this
- Combine with file_organizer — read folder names aloud
- Combine with web_scraper — read headlines aloud
- Build a study tool — paste notes and listen while commuting
