# Day 10 - Todo CLI App 📝

A full-featured command-line Todo application with JSON storage.

## Features
- ➕ Add todos with priority levels (high/medium/low)
- 📋 List all or only pending todos
- ✅ Mark todos as done
- 🗑️ Delete todos
- ✏️ Edit todo titles
- 🔍 Search by keyword
- 📊 View stats (total, done, pending, high priority)
- 🧹 Clear all completed todos

## Requirements
- Python 3.6+
- No external libraries needed!

## Usage
```bash
python todo.py
```

## Examples

### Add a Todo
```python
from todo import add_todo
add_todo("Buy groceries", "high")
# ✅ Added: [1] Buy groceries (Priority: high)
```

### List Todos
```python
from todo import list_todos
list_todos()
# 📋 Your Todo List
# =======================================================
# ⬜ [1] 🔴 Buy groceries
#       Created: 2024-01-15 10:30
# ✅ [2] 🟡 Read book
#       Created: 2024-01-15 09:00
# =======================================================
```

### Mark as Done
```python
from todo import mark_done
mark_done(1)
# ✅ Marked as done: [1] Buy groceries
```

### Get Stats
```python
from todo import get_stats
get_stats()
# 📊 Todo Stats
# ------------------------------
# 📋 Total    : 5
# ✅ Done     : 2
# ⬜ Pending  : 3
# 🔴 High Pri : 1
# ------------------------------
```

## Functions
| Function | Description |
|----------|-------------|
| `add_todo(title, priority)` | Add a new todo |
| `list_todos(show_done)` | List all or pending todos |
| `mark_done(id)` | Mark todo as completed |
| `delete_todo(id)` | Delete a todo by ID |
| `edit_todo(id, new_title)` | Edit todo title |
| `search_todos(keyword)` | Search by keyword |
| `get_stats()` | Show todo statistics |
| `clear_done()` | Remove all completed todos |

## Author
Ayush442842q
