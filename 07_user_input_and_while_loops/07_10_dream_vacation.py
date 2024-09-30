# This code asks for a person's name and place they'd like to visit, then displays the responses.

import os
os.system('cls')

responses = {}

asking = True

while asking:
    name = input("What is your name? ")
    location = input("If you could visit one place in the world, where would it be?: ")
    responses[name] = location
    repeat = input("Would you like to let another person respond? (y/n): ")
    repeat = repeat.lower()
    print("\n")
    if repeat == 'no' or repeat == "n":
        asking = False

print("--- Poll Results ---")
for name, location in responses.items():
    print(f"{name} would like to visit {location}.")
