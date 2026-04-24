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

def add_todo(title, priority="medium"):
    """Adds a new todo item."""
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "priority": priority.lower(),
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Added: [{todo['id']}] {title} (Priority: {priority})")
    return todo

def list_todos(show_done=True):
    """Lists all todos, optionally filtering out completed ones."""
    todos = load_todos()
    if not todos:
        print("📭 No todos found! Add one with add_todo().")
        return []
    print("\n📋 Your Todo List")
    print("=" * 55)
    for todo in todos:
        if not show_done and todo["done"]:
            continue
        status = "✅" if todo["done"] else "⬜"
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(todo["priority"], "🟡")
        print(f"{status} [{todo['id']}] {priority_icon} {todo['title']}")
        print(f"      Created: {todo['created_at']}")
    print("=" * 55)
    return todos

def mark_done(todo_id):
    """Marks a todo as completed by ID."""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = True
            todo["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            save_todos(todos)
            print(f"✅ Marked as done: [{todo_id}] {todo['title']}")
            return True
    print(f"❌ Todo with ID {todo_id} not found.")
    return False

def delete_todo(todo_id):
    """Deletes a todo by ID."""
    todos = load_todos()
    new_todos = [t for t in todos if t["id"] != todo_id]
    if len(new_todos) == len(todos):
        print(f"❌ Todo with ID {todo_id} not found.")
        return False
    save_todos(new_todos)
    print(f"🗑️  Deleted todo with ID: {todo_id}")
    return True
