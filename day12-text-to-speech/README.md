# Day 12 - Text to Speech

A Python CLI tool that converts text and text files into spoken audio using Google TTS.

## Features
- Convert any text to mp3 audio
- Slow mode for language learning
- Convert entire text files to audio
- Supports 12 languages including Hindi, French, Japanese and more
- Interactive menu

## Requirements
```bash
pip install gtts
```

## Usage
```bash
python tts.py
```

## Example
```
🔊 Text to Speech Converter
----------------------------------------
1. Convert text to speech
2. Convert text to speech (slow)
3. Convert text file to speech
4. Show supported languages
5. Exit
----------------------------------------
Choose an option (1-5): 1
Enter text: Hello, this is a test!
Language code (default: en): en
Output filename (default: output.mp3): hello.mp3
✅ Audio saved to: audio_output/hello.mp3
```

## Supported Languages
| Code | Language |
|------|----------|
| en | English |
| hi | Hindi |
| fr | French |
| de | German |
| es | Spanish |
| ja | Japanese |
| zh | Chinese |
| ar | Arabic |

## Libraries Used
- `gtts` — Google Text-to-Speech, converts text to mp3
