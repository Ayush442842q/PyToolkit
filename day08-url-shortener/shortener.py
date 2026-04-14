import requests
import json
import os
from datetime import datetime

# PyToolkit - Day 08
# Tool: URL Shortener
# Author: Ayush442842q
# Description: Shorten URLs using TinyURL API and track history

TINYURL_API = "https://tinyurl.com/api-create.php"
HISTORY_FILE = "url_history.json"

def is_valid_url(url):
    """Checks if a URL is valid."""
    return url.startswith("http://") or url.startswith("https://")

def shorten_url(url):
    """Shortens a URL using TinyURL API."""
    if not is_valid_url(url):
        print("❌ Invalid URL! Must start with http:// or https://")
        return None
    try:
        response = requests.get(TINYURL_API, params={"url": url})
        response.raise_for_status()
        short_url = response.text.strip()
        print(f"✅ Shortened: {short_url}")
        return short_url
    except requests.exceptions.RequestException as e:
        print(f"❌ Error shortening URL: {e}")
        return None

def load_history():
    """Loads URL history from JSON file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
