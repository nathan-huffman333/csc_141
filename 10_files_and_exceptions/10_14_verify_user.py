# Difficulty: 2/10 pretty easy, I essentially just had to add an if statment. 
# This code builds off of the previous one, except now it will confirm whether it is the correct user before either diplaying the information or asking for new data.

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
        confirm = input(f"Are you user: {data['username']}? Y/N: ")
        if confirm == "y" or confirm == "Y":
            print(f"Welcome back, {data['username']}!")
            print(f"You are {data['age']} years old.")
            print(f"Your favorite color is {data['fav_color']}.\n")
        else:
            print("My apologies, please enter your information again:")
            data = get_new_username(path)
            print(f"We'll remember you when you come back, {data['username']}!")
    else:
        data = get_new_username(path)
        print(f"We'll remember you when you come back, {data['username']}!")
        

greet_user()