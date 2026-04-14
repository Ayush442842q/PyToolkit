# Day 08 - URL Shortener ✂️

A command-line URL shortener using TinyURL API with history tracking.

## Features
- 🔗 Shorten any URL instantly using TinyURL
- 📋 View full history of shortened URLs
- 🗂️ Bulk shorten multiple URLs at once
- 💾 History saved to JSON file
- 🗑️ Clear history anytime
- ✅ URL validation before shortening

## Requirements
- Python 3.6+
- requests

## Installation
```bash
pip install requests
```

## Usage
```bash
python shortener.py
```

## Examples

### Shorten a URL
```python
from shortener import shorten_url, add_to_history
short = shorten_url("https://www.google.com")
# ✅ Shortened: https://tinyurl.com/xyz123
add_to_history("https://www.google.com", short)
# 📝 Saved to history!
```

### Bulk Shorten
```python
from shortener import shorten_bulk
urls = ["https://google.com", "https://github.com"]
results = shorten_bulk(urls)
# ✅ Shortened 2 URLs!
```

### View History
```python
from shortener import display_history
display_history()
# 📋 URL Shortener History (2 entries)
```

## Functions
| Function | Description |
|----------|-------------|
| `is_valid_url(url)` | Validates URL format |
| `shorten_url(url)` | Shortens a single URL |
| `shorten_bulk(urls)` | Shortens multiple URLs |
| `add_to_history(original, short)` | Saves entry to history |
| `display_history()` | Prints all history |
| `clear_history()` | Clears all history |
| `get_history_count()` | Returns history count |

## Author
Ayush442842q
