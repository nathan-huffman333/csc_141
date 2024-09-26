# This code asks the user for a number and sees whether or not the number is a group of ten.

import os
os.system('cls')

num = int(input("Input a number: "))
if num%10 != 0:
    print("Your number is NOT a multiple of ten.\n")
else:
    print("Your number is a multiple of ten.\n")