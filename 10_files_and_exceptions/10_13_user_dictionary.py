# Difficulty: 6/10 A little hard to understand the code of the book as well as remembering dictionaries and how to use them with json files.
# This code asks for the user's name, age, and favorite color if it is not already known, and then when the program is rerun, it recalls the previous information from a json file.

from pathlib import Path
import json
import os
os.system('cls')


def does_information_exist(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        data = json.loads(contents)
        return data
    else:
        return None


def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = int(input("How old are you? "))
    color = input("What is your favorite color? ")
    user_info = {
        'username' : username,
        'age' : age,
        'fav_color' : color
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    data = does_information_exist(path)
    if data:
        print(f"Welcome back, {info['username']}!")
        print(f"You are {info['age']} years old.")
        print(f"Your favorite color is {info['fav_color']}.\n")
    else:
        info = get_new_username(path)
        print(f"We'll remember you when you come back, {info['username']}!\n")
        

greet_user()
print("\n")