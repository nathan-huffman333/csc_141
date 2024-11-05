# Difficulty: 3/10 Not too bad, I just had a little trouble at first with the try and except command but I understood it eventually.
# This code asks the user for two numbers then adds them together unless they entered a letter or word, which results in an error message.

import os
os.system('cls')

try:
    num1 = int(input("Number 1: " ))
    num2 = int(input("Number 2: " ))
    print("\n")
    print(num1+num2)
    print("\n")
except ValueError: 
    print("\nError: You input a word or letter and not a number\n")
