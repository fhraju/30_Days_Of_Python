import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

files_dir = os.path.join(BASE_DIR, "images")

if not os.path.exists(files_dir):
    print("This is not a valid path")