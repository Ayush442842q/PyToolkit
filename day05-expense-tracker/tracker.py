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
