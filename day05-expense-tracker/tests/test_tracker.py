import sys
import os
sys.path.insert(0, os.path.abspath(".."))

from tracker import get_total, get_by_category, get_summary

def test_get_total():
    expenses = [
        {"Amount": "100", "Category": "Food", "Date": "2026-04-01", "Description": "Lunch"},
        {"Amount": "200", "Category": "Transport", "Date": "2026-04-01", "Description": "Uber"},
    ]
    assert get_total(expenses) == 300.0
    print("✅ test_get_total passed!")

test_get_total()
