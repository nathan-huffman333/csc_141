# This code describes the size and words on a t-shirt

import os
os.system('cls')

def make_shirt(size, words):
    print(f"The shirt is size {size.title()}, and says {words.title()}.\n")

make_shirt("xl", "Property of Nathan")


size = input("Your shirt size: ")
words = input("Sentence on shirt: ")
print("\n")
make_shirt(size, words)
