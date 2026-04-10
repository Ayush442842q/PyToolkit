import requests
from bs4 import BeautifulSoup

# Configuration
BASE_URL = "https://news.ycombinator.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def get_page(url):
    """Fetches the HTML content of a page."""
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching page: {e}")
        return None

def parse_headlines(html):
    """Parses headlines from Hacker News."""
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    headlines = []

    for item in soup.select(".titleline > a"):
        headlines.append({
            "title": item.text,
            "link": item.get("href")
        })

    return headlines