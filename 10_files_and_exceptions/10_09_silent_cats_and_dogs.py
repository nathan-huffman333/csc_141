# Difficulty: 0/10 Not at all hard, just had to write 'pass' instead of an error message.
# This code reads two files of cats and dog names unless the file is not found.


import os
os.system('cls')
from pathlib import Path

path = Path("10_files_and_exceptions/cats.txt")


try:
    print("Cat names:")
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    pass

path = Path("10_files_and_exceptions/dogs.txt")


try:
    print("\nDog names:")
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    pass