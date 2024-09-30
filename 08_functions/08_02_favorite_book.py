# This code is to display one of my favorite books using a parameter in a function.

import os
os.system('cls')

def favorite_book(title):
    print("One of my favorite books is: " + title.title() + ".")

title = "calvin and hobbes"
favorite_book(title)