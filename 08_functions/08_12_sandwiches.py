# This code prints the ingredients the customer wants in their burger by receiving a list that can contain a number of different arguments.

import os
os.system('cls')

def sandwich(*ingredients):
    print("The customer wants a burger with these ingredients:")
    for ingredient in ingredients:
        print(f"\t{ingredient}")
    print("\n")

sandwich("Patty", "Cheese", "Bacon", "Lettuce", "Tomato", "Onion")
sandwich("Patty", "Cheese", "Bacon")
sandwich("Patty", "Cheese", "Lettuce", "Tomato", "Onion")