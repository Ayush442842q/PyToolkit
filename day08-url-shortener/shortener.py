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

def save_history(history):
    """Saves URL history to JSON file."""
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def add_to_history(original_url, short_url):
    """Adds a new entry to URL history."""
    history = load_history()
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "original": original_url,
        "shortened": short_url
    }
    history.append(entry)
    save_history(history)
    print(f"📝 Saved to history!")

def display_history():
    """Displays all shortened URLs from history."""
    history = load_history()
    if not history:
        print("❌ No history found!")
        return
    print(f"\n📋 URL Shortener History ({len(history)} entries)")
    print("-" * 60)
    for i, entry in enumerate(history, 1):
        print(f"\n{i}. [{entry['date']}]")
        print(f"   🔗 Original : {entry['original'][:50]}...")
        print(f"   ✂️  Shortened: {entry['shortened']}")
    print("-" * 60)

def clear_history():
    """Clears all URL history."""
    save_history([])
    print("✅ History cleared!")

def get_history_count():
    """Returns the number of URLs in history."""
    return len(load_history())

def shorten_bulk(urls):
    """Shortens multiple URLs at once."""
    results = []
    for url in urls:
        short = shorten_url(url)
        if short:
            add_to_history(url, short)
            results.append({"original": url, "shortened": short})
    return results

def main():
    """Main function to run the URL shortener."""
    print("✂️  URL Shortener")
    print("-" * 30)
    print("1. Shorten a URL")
    print("2. Shorten multiple URLs")
    print("3. View history")
    print("4. Clear history")
    print("5. Exit")

    choice = input("\nChoose option (1-5): ")

    if choice == "1":
        url = input("Enter URL: ").strip()
        short = shorten_url(url)
        if short:
            add_to_history(url, short)

    elif choice == "2":
        print("Enter URLs one per line. Empty line to finish:")
        urls = []
        while True:
            url = input().strip()
            if not url:
                break
            urls.append(url)
        results = shorten_bulk(urls)
        print(f"\n✅ Shortened {len(results)} URLs!")

    elif choice == "3":
        display_history()

    elif choice == "4":
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == "y":
            clear_history()

    elif choice == "5":
        print("👋 Goodbye!")

    else:
        print("❌ Invalid option!")

if __name__ == "__main__":
    main()
