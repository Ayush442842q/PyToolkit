# Dev Notes - URL Shortener

## What I learned
- `requests.get(url, params={})` — sends GET request with query params
- `response.text.strip()` — gets raw text response and removes whitespace
- `json.dump(data, f, indent=4)` — writes JSON with pretty formatting
- `json.load(f)` — reads JSON file into Python dictionary/list
- `datetime.now().strftime("%Y-%m-%d %H:%M")` — formats timestamp
- TinyURL API — free, no API key needed, just pass URL as param
- History tracking pattern — load → append → save

## API used
- TinyURL: https://tinyurl.com/api-create.php?url=YOUR_URL
- No API key required
- Returns shortened URL as plain text

## Challenges
- Always validate URL before sending to API
- JSON history file needs to be initialized as empty list
- Bulk shortening needs individual error handling per URL
