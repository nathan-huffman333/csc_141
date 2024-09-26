# This code asks how many people are in a dining group to know if a table is available or not.

import os
os.system('cls')

group = int(input("How many people are in your dining group?: "))
if group > 8:
    print("I'm sorry, but you will have to wait for a table.\n")
else:
    print("Your table is ready.\n")