import csv
import os
from datetime import datetime

# File to store expenses
DATA_FILE = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Health", "Entertainment", "Others"]

def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])
        print(f"✅ Created {DATA_FILE}")

def add_expense(category, amount, description):
    """Adds a new expense to the CSV file."""
    initialize_file()
    date = datetime.now().strftime("%Y-%m-%d")
    with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])
    print(f"✅ Expense added: {category} - ₹{amount}")

def get_all_expenses():
    """Returns all expenses from the CSV file."""
    initialize_file()
    expenses = []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(row)
    return expenses

def get_total(expenses):
    """Returns total amount of all expenses."""
    return sum(float(e["Amount"]) for e in expenses)

def get_by_category(expenses, category):
    """Filters expenses by category."""
    return [e for e in expenses if e["Category"].lower() == category.lower()]

def display_expenses(expenses):
    """Displays all expenses in a formatted table."""
    if not expenses:
        print("❌ No expenses found!")
        return

    print(f"\n{'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
    print("-" * 55)
    for e in expenses:
        print(f"{e['Date']:<12} {e['Category']:<15} ₹{float(e['Amount']):<9.2f} {e['Description']}")
    print("-" * 55)
    print(f"💰 Total: ₹{get_total(expenses):.2f}")

def get_summary(expenses):
    """Returns a summary of expenses by category."""
    summary = {}
    for e in expenses:
        cat = e["Category"]
        summary[cat] = summary.get(cat, 0) + float(e["Amount"])
    return summary
