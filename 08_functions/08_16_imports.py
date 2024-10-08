# This code uses functions and lists from another file to print messages and move information from one list to another.

import os
os.system('cls')
import imports_functions
from imports_functions import show_messages
from imports_functions import show_messages as show
from imports_functions import send_messages
from imports_functions import send_messages as send
from imports_functions import sent_messages
from imports_functions import joke
from imports_functions import *

print("This is the joke from the orignal list:\n")
show(joke)
print(f"\nFirst list:{joke}")
print(f"Second list: {sent_messages}\n")

print("Here is the joke again but now it has moved to the other list::\n")
send(joke)
print(f"\nFirst list:{joke}")
print(f"Second list: {sent_messages}\n")