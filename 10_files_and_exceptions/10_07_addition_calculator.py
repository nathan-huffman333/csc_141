# Difficulty: 6/10 This code was moderately difficult to format correctly into a while loop to allow for the ability to continuously add and decide when to stop.  
# This code repeatedly takes numbers inputed by the user to add together and ensures that they are an int variable. 

import os
os.system('cls')

answer = 0
print("Input numbers you'd like to add together and type 'q' or 'Q' to quit and reveal the sum.\n")

while True:
    num = (input("Number: " ))
    if num == "q" or num == "Q":
        print(f"\nAnswer: {answer}\n")
        break
    try:
        num = int(num)
        answer += num
    except ValueError:
        print("Error: You input a word or letter and not a number.")