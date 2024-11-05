# Difficulty: 1/10 Super easy, just had to use the new command.
# This code asks the user their name then prints it into the guest.txt file.

import os
os.system('cls')
from pathlib import Path

path = Path("10_files_and_exceptions/guest.txt")

name = input("What is your name: ")
path.write_text(name)

contents = path.read_text()
print(contents)