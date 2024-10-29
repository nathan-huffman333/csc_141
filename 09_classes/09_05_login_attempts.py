# This code allows for the value of login attempts to be increased and reset.

import os
os.system('cls')

class User:
    def __init__(self, first_name, last_name, age, hair_color, eye_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Eye Color: {self.eye_color}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Nathan", "Huffman", 19, "Dark Brown", "Blue")
user.describe_user()
print("\n")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login Attempts: {user.login_attempts}")
print("\n")
user.greet_user()
print("\n")
print("RESETING LOGIN ATTEMPTS...")
user.reset_login_attempts()
print(f"Login Attempts: {user.login_attempts}")
print("\n")