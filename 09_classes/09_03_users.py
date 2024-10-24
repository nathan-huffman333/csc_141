# This code describes users's characteristics and greets them.

import os
os.system('cls')

class User:
    def __init__(self, first_name, last_name, age, hair_color, eye_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Eye Color: {self.eye_color}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")


user = User("Nathan", "Huffman", 19, "Dark Brown", "Blue")
user.describe_user()
print("\n")
user.greet_user()
print("\n")

user = User("Anthony", "Frederick", 18, "Brown", "Blue")
user.describe_user()
print("\n")
user.greet_user()
print("\n")
