from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else: 
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

# greet_user()

from collections import defaultdict
import datetime

emails_history = defaultdict(lambda: {"total_count": 0, "history": defaultdict(int)})



emails_history = {"some_email@qq.com": {"total_count": 3, "history": {"2024-05-11": 1, "2024-05-13": 2}}, "some_other@gmail.com": {"total_count": 2, "history": {"2024-05-10": 1, "2024-05-13": 1}}}


