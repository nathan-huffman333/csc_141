# Difficulty: 1/10 Really easy, just had to merge the two files into one if statement.
# This program asks the user for their favorite number and stores it into a json file, then when run again, prints this number from the separate file.

from pathlib import Path
import json

path = Path('favorite_number.json')

if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number, it is: {fav_num}")
else:
    fav_num = int(input("What is your favorite number? "))
    contents = json.dumps(fav_num)
    path.write_text(contents)
    path = Path('favorite_number.json')