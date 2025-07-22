import os
import csv
from datetime import datetime
from app.utils import get_today_date, generate_unique_filename

DATA_DIR = "data"
REPORTS_DIR = os.path.join(DATA_DIR, "reports")

# Ensure the reports directory exists
os.makedirs(REPORTS_DIR, exist_ok=True)

def mark_attendance(name, confidence):
    today_date = get_today_date()
    filename = f"attendance_{today_date}.csv"
    filepath = os.path.join(REPORTS_DIR, filename)

    # Check if the file exists already
    file_exists = os.path.isfile(filepath)

    with open(filepath, mode="a", newline="") as csvfile:
        fieldnames = ["Timestamp", "Name", "Confidence"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write headers if file is new
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Confidence": f"{confidence:.2f}%"
        })

# ✅ Rename this function to match the import in main.py
def get_today_report():
    """Returns today's attendance as a list of dicts"""
    today_date = get_today_date()
    filename = f"attendance_{today_date}.csv"
    filepath = os.path.join(REPORTS_DIR, filename)

    if not os.path.exists(filepath):
        return []

    with open(filepath, mode="r") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

