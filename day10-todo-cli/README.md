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

## Storage
Todos are saved in `todos.json` in the same directory.

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
