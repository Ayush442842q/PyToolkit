import requests
from bs4 import BeautifulSoup

# Configuration
BASE_URL = "https://news.ycombinator.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}