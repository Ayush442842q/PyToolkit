import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from todo import add_todo, load_todos, save_todos, mark_done, delete_todo

# Use a test file so we don't mess with real todos
import todo
todo.TODO_FILE = "test_todos.json"

class TestTodo:
    """Tests for Todo CLI App."""

    def setup(self):
        """Reset todo file before each test."""
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

if __name__ == "__main__":
    t = TestTodo()
    t.test_add_todo()
    t.test_load_empty()
    print("\n✅ All tests passed!")
