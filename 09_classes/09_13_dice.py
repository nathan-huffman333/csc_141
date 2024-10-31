# This code has the class 'Die' which allows for the rolling of multiple sided die, with a default value of 6.

import os
os.system('cls')
from random import randint

class Die:
    """This class includes possible methods callable for the 'Die' class and it's number of sides"""
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        """This command rolls the die 10 times and prints the value"""
        for x in range(10):
            print(f"\t{randint(1, self.sides)}")
        print("\n")

roll = Die()
print(f"Roll a {roll.sides} sided die 10 times:")
roll.roll_die()

roll.sides = 10
print(f"Roll a {roll.sides} sided die 10 times:")
roll.roll_die()