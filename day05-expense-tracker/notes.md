# Dev Notes - Expense Tracker

## What I learned
- `csv.writer` — writes rows to CSV file
- `csv.DictReader` — reads CSV as list of dictionaries
- `newline=""` — prevents extra blank lines in CSV on Windows
- `datetime.now().strftime()` — formats current date as string
- Dictionary `.get(key, 0)` — gets value or default
- f-string formatting with `:<12` — left align with padding
- `sorted()` with `key=lambda` — sort by specific field

## Data structure used
Each expense is a dictionary:
{Date, Category, Amount, Description}

## Challenges
- CSV needs headers on first run only — solved with initialize_file()
- Float precision in totals — solved with :.2f formatting
