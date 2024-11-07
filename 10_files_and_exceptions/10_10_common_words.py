# Difficulty: 1/10 Not hard, but for some reason it didn't work for me when I didn't have the encoding = 'utf-8' which took a long time to figure out.
# This gives an approximation of the amount of 'the's, and counts the amount of 'then's 'there's and actual 'the's that are in the text 'A Yankee Doctor in Paradise".

import os
os.system('cls')

from pathlib import Path

book = Path("10_files_and_exceptions/a_yankee_doctor_in_paradise.txt")

try:
    book = book.read_text(encoding='utf-8').lower()
    print(f"Approximation of amount of 'the's in the book: {book.count('the')}")
    print(f"Amount of 'then's in the book: {book.count('then')}")
    print(f"Amount of 'there's in the book: {book.count('there')}")
    print(f"Actual amount of 'the's in the book: {book.count('the ')}")

except FileNotFoundError:
    pass