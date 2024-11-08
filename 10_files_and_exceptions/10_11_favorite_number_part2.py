# See comments on part 1.

from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    fav_num = json.loads(contents)
    print(f"I know your favorite number, it is: {fav_num}")
else:
    print("You have not inputed your favorite number in the other program.")