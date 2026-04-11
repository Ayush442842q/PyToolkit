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

def test_get_by_category():
    expenses = [
        {"Amount": "100", "Category": "Food", "Date": "2026-04-01", "Description": "Lunch"},
        {"Amount": "200", "Category": "Transport", "Date": "2026-04-01", "Description": "Uber"},
    ]
    result = get_by_category(expenses, "Food")
    assert len(result) == 1
    assert result[0]["Category"] == "Food"
    print("✅ test_get_by_category passed!")

test_get_by_category()

def test_get_summary():
    expenses = [
        {"Amount": "100", "Category": "Food", "Date": "2026-04-01", "Description": "Lunch"},
        {"Amount": "200", "Category": "Food", "Date": "2026-04-01", "Description": "Dinner"},
        {"Amount": "150", "Category": "Transport", "Date": "2026-04-01", "Description": "Uber"},
    ]
    summary = get_summary(expenses)
    assert summary["Food"] == 300.0
    assert summary["Transport"] == 150.0
    print("✅ test_get_summary passed!")

test_get_summary()
