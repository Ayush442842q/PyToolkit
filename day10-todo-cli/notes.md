# Dev Notes - Todo CLI App

## What I learned
- `json.load()` — reads JSON from file into Python dict/list
- `json.dump(data, f, indent=4)` — writes Python data to JSON with formatting
- List comprehensions for filtering: `[t for t in todos if not t["done"]]`
- `datetime.now().strftime()` — formats current date and time as string
- Using a separate test JSON file to avoid polluting real data during tests
- ID management: using `len(todos) + 1` for auto-incrementing IDs

## Data structure
Each todo is stored as:
```json
{
    "id": 1,
    "title": "Buy groceries",
    "priority": "high",
    "done": false,
    "created_at": "2024-01-15 10:30",
    "completed_at": "2024-01-15 11:00"
}
```

## Challenges
- IDs can get out of sync if todos are deleted — consider UUID in future
- JSON file gets recreated if deleted — handled with os.path.exists() check
- Test isolation: must reset todo file before each test
