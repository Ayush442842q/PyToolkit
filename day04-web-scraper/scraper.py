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

def display_headlines(headlines, scores=None, limit=10):
    """Displays headlines in a numbered list."""
    if not headlines:
        print("❌ No headlines found!")
        return

    print(f"\n🔥 Top {limit} Headlines from Hacker News")
    print("-" * 50)

    for i, item in enumerate(headlines[:limit], 1):
        score = scores[i-1] if scores and i-1 < len(scores) else "N/A"
        print(f"\n{i}. {item['title']}")
        print(f"   🔗 {item['link']}")
        print(f"   ⬆️  {score}")

    print("-" * 50)

def main():
    """Main function to run the web scraper."""
    print("🕷️ Web Scraper - Hacker News Headlines")
    print("-" * 50)

    limit = int(input("How many headlines to show? (1-30): "))
    if limit < 1 or limit > 30:
        print("❌ Please enter a number between 1 and 30!")
        return

    print("\n⏳ Fetching headlines...")
    html = get_page(BASE_URL)
    headlines = parse_headlines(html)
    scores = get_scores(html)
    display_headlines(headlines, scores, limit)

    save = input("\n💾 Save headlines to file? (y/n): ").lower()
    if save == "y":
        save_headlines(headlines[:limit])

if __name__ == "__main__":
    main()

def save_headlines(headlines, filename="headlines.txt"):
    """Saves headlines to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Hacker News Headlines\n")
        f.write("=" * 50 + "\n\n")
        for i, item in enumerate(headlines, 1):
            f.write(f"{i}. {item['title']}\n")
            f.write(f"   {item['link']}\n\n")
    print(f"✅ Headlines saved to {filename}")

def get_scores(html):
    """Fetches upvote scores for each headline."""
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    scores = []

    for score in soup.select(".score"):
        scores.append(score.text)

    return scores



















