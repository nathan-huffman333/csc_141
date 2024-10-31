# This code decides what the winning ticket will be randomly based off of a collection of letters and numbers.

import os
os.system('cls')
from random import choice

lottery = (42, 55, "J", 33, "H", 25, 96, "O", 14, 76, "W", 8, 82, 66, "N")
winner = []


print("Let's see what will be the winning ticket...")
while len(winner) < 4:
    pulled_item = choice(lottery)
    if pulled_item not in winner:
        winner.append(pulled_item)
        print(f"\tWe pulled a: {pulled_item}")

print("\n\nSo, if you have the winning ticket of:")
print(f"\t{winner}\n")
print("You win a prize! Congratulations!\n")
                 
