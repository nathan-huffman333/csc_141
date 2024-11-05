# Difficulty: 2/10 this was pretty easy but for some reason I had to specify the chapter name folder and not just the name of the text file.
# This code prints information from a separate file about things I learned how to do in python.

import os
os.system('cls')
from pathlib import Path

path = Path('10_files_and_exceptions\learning_python.txt')

contents = path.read_text()


print(contents)
print("\n")

lines = contents.splitlines()
for line in lines:
    print(line)