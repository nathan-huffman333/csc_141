# Difficulty: 2/10 Really easy, just had to make the two files and two try except blocks.
# This code reads and prints cats and dogs names from two files.

import os
os.system('cls')
from pathlib import Path

path = Path("10_files_and_exceptions/cats.txt")

print("Cat names:")
try:
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    print("File: 'cats.txt' not found.")

path = Path("10_files_and_exceptions/dogs.txt")

print("\nDog names:")
try:
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    print("File: 'cats.txt' not found.")