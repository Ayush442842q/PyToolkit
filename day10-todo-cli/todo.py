import json
import os
from datetime import datetime

# PyToolkit - Day 10
# Tool: Todo CLI App
# Author: Ayush442842q
# Description: A full-featured command-line Todo app with JSON storage

TODO_FILE = "todos.json"

def load_todos():
    """Loads todos from JSON file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    """Saves todos to JSON file."""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=4)
