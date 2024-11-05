# Difficulty: 4/10 Wasn't too bad, just had a little trouble with the while loop and making sure everything was added.
# This code asks for a guests name and adds it to the guest book before printing it. 

import os
os.system('cls')
from pathlib import Path

path = Path("10_files_and_exceptions/guest_book.txt")

contents = ""

while True:
    contents += input("What is your name: ")
    contents += ("\n")
    if "quit" in contents:
        contents = contents.replace("quit", "")
        break

path.write_text(contents)
print("\n")
contents = path.read_text()
print(contents)