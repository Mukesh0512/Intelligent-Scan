# utils.py
import os
import datetime

def get_today_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_unique_filename(prefix='report', ext='csv'):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.{ext}"
