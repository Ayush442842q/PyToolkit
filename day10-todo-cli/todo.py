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

def edit_todo(todo_id, new_title):
    """Edits the title of an existing todo."""
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            old_title = todo["title"]
            todo["title"] = new_title
            save_todos(todos)
            print(f"✏️  Updated [{todo_id}]: '{old_title}' → '{new_title}'")
            return True
    print(f"❌ Todo with ID {todo_id} not found.")
    return False

def search_todos(keyword):
    """Searches todos by keyword in title."""
    todos = load_todos()
    results = [t for t in todos if keyword.lower() in t["title"].lower()]
    if not results:
        print(f"🔍 No todos found matching: '{keyword}'")
        return []
    print(f"\n🔍 Search results for '{keyword}':")
    print("=" * 55)
    for todo in results:
        status = "✅" if todo["done"] else "⬜"
        print(f"{status} [{todo['id']}] {todo['title']}")
    print("=" * 55)
    return results

def get_stats():
    """Returns stats about todos."""
    todos = load_todos()
    total = len(todos)
    done = sum(1 for t in todos if t["done"])
    pending = total - done
    high = sum(1 for t in todos if t["priority"] == "high" and not t["done"])
    print("\n📊 Todo Stats")
    print("-" * 30)
    print(f"📋 Total    : {total}")
    print(f"✅ Done     : {done}")
    print(f"⬜ Pending  : {pending}")
    print(f"🔴 High Pri : {high}")
    print("-" * 30)
    return {"total": total, "done": done, "pending": pending, "high_priority": high}

def clear_done():
    """Removes all completed todos."""
    todos = load_todos()
    remaining = [t for t in todos if not t["done"]]
    removed = len(todos) - len(remaining)
    save_todos(remaining)
    print(f"🧹 Cleared {removed} completed todo(s).")
    return removed

def main():
    """Main function to run the Todo CLI."""
    print("📝 PyToolkit Todo CLI")
    print("=" * 40)
    print("1. Add todo")
    print("2. List all todos")
    print("3. List pending todos")
    print("4. Mark as done")
    print("5. Delete todo")
    print("6. Edit todo")
    print("7. Search todos")
    print("8. View stats")
    print("9. Clear completed")
    print("0. Exit")
    print("=" * 40)

    choice = input("Choose option (0-9): ").strip()

    if choice == "1":
        title = input("Todo title: ").strip()
        priority = input("Priority (high/medium/low) [medium]: ").strip() or "medium"
        add_todo(title, priority)
    elif choice == "2":
        list_todos()
    elif choice == "3":
        list_todos(show_done=False)
    elif choice == "4":
        todo_id = int(input("Todo ID to mark done: ").strip())
        mark_done(todo_id)
    elif choice == "5":
        todo_id = int(input("Todo ID to delete: ").strip())
        delete_todo(todo_id)
    elif choice == "6":
        todo_id = int(input("Todo ID to edit: ").strip())
        new_title = input("New title: ").strip()
        edit_todo(todo_id, new_title)
    elif choice == "7":
        keyword = input("Search keyword: ").strip()
        search_todos(keyword)
    elif choice == "8":
        get_stats()
    elif choice == "9":
        clear_done()
    elif choice == "0":
        print("👋 Goodbye!")
    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
