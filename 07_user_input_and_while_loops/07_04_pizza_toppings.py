# This asks the user what toppings they want on their pizza until they don't want any more.

import os
os.system('cls')

while True:
    topping = input("What would you like on your pizza?: ")
    if topping != "quit":
        print("\tOkay, I've just added "+topping+" to your pizza.")
    else:
        break