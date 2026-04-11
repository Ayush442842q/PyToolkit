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
