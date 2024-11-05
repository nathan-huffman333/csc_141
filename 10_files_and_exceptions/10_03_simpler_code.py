# Difficulty: 3/10 Not to hard, just had to create the pi text file.
# This code uses another file to print the digits of pi without using a temporary variable like the book did.

import os
os.system('cls')

from pathlib import Path
path = Path('10_files_and_exceptions/pi_digits.txt')

contents = path.read_text()

for line in contents.splitlines():
    print(line)