# This code asks how many people wants tickets, how old each person is and displays how much the ticket will cost for each person. 

import os
os.system('cls')

users = int(input("How many people want to buy tickets?: "))
while users < 1:
    users = int(input("No seriously, how many people want to buy tickets?: "))

x = 0
asking = True
while asking:
    age = input("How old are you?: ")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age >= 3 and age < 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
        x += 1
    if x == users:
        asking = False