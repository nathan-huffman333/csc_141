# This code asks the user for their age to see how much a movie ticket will cost them.

import os
os.system('cls')

while True:
    age = int(input("How old are you?: "))
    if age < 3:
        print("The ticket is free.")
    elif age >= 3 and age < 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")