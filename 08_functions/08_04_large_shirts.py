# This code has default values for shirts, but a new shirt could deviate from these values.

import os
os.system('cls')

def make_shirt(size = 'large', words = 'i love python'):
    print(f"The shirt is size {size.title()}, and says {words.title()}.\n")

make_shirt()
make_shirt(size = 'medium', words = 'i love coding')