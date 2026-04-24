import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import todo
todo.TODO_FILE = "test_todos.json"

from todo import add_todo, load_todos, save_todos, mark_done, delete_todo, search_todos, get_stats

class TestTodo:
    """Tests for Todo CLI App."""

    def setup(self):
        save_todos([])

    def test_add_todo(self):
        self.setup()
        result = add_todo("Test task", "high")
        assert result["title"] == "Test task"
        assert result["priority"] == "high"
        assert result["done"] == False
        print("✅ test_add_todo passed!")

    def test_load_empty(self):
        self.setup()
        todos = load_todos()
        assert todos == []
        print("✅ test_load_empty passed!")

    def test_mark_done(self):
        self.setup()
        add_todo("Mark me done")
        result = mark_done(1)
        assert result == True
        todos = load_todos()
        assert todos[0]["done"] == True
        print("✅ test_mark_done passed!")

    def test_mark_done_invalid(self):
        self.setup()
        result = mark_done(999)
        assert result == False
        print("✅ test_mark_done_invalid passed!")

    def test_delete_todo(self):
        self.setup()
        add_todo("Delete me")
        result = delete_todo(1)
        assert result == True
        todos = load_todos()
        assert len(todos) == 0
        print("✅ test_delete_todo passed!")

    def test_search_todos(self):
        self.setup()
        add_todo("Buy groceries")
        add_todo("Read book")
        results = search_todos("groceries")
        assert len(results) == 1
        print("✅ test_search_todos passed!")

    def test_get_stats(self):
        self.setup()
        add_todo("Task 1", "high")
        add_todo("Task 2", "low")
        mark_done(1)
        stats = get_stats()
        assert stats["total"] == 2
        assert stats["done"] == 1
        assert stats["pending"] == 1
        print("✅ test_get_stats passed!")

if __name__ == "__main__":
    t = TestTodo()
    t.test_add_todo()
    t.test_load_empty()
    t.test_mark_done()
    t.test_mark_done_invalid()
    t.test_delete_todo()
    t.test_search_todos()
    t.test_get_stats()
    print("\n✅ All tests passed!")
    # Cleanup
    if os.path.exists("test_todos.json"):
        os.remove("test_todos.json")
