# Difficulty: 2/10  This code was preety easy, I just had to play around with the replace command a bit to learn it.
# This code replaces the word "python" with "C" from the previously imported file and prints the information.

import os
os.system('cls')
from pathlib import Path

path = Path('10_files_and_exceptions\learning_python.txt')
contents = path.read_text()


lines = contents.splitlines()
for line in lines:
    line = line.replace('python', 'C')
    print(line)

