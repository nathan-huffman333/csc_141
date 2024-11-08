# Difficulty: 3/10 Not that bad, just had to look over the book a bit and learn some new commands with json files and create another file.
# This program has you input your favorite number, then it creates a json file, and in the other program, it says what is inside that file.

import os
os.system('cls')
from pathlib import Path
import json

fav_num = int(input("What is your favorite number? "))

path = Path('favorite_number.json')
contents = json.dumps(fav_num)
path.write_text(contents)