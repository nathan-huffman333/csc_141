import os
os.system('cls')
import TextAdventureFunctions
from TextAdventureFunctions import commands
from TextAdventureFunctions import cabin
from TextAdventureFunctions import username

items = ["axe", "lantern", "pickaxe", "amulet"]
currentlocation = ""
print("THE ADVENTURE")
print()
print()
print("Type 'start' to start the game! ")
start = input("\n\n")
start = start.lower()
if start == "start":
    os.system('cls')
    print("INSTRUCTIONS:")
    print()
    print()
    print("On your quest you will have several options to choose from at each location, including moving onwards or backtracking. Charging in with reckless abandon is unwise, and you'll be bound to meet a quick fate. Here are some of your")
    print("commands that you will use on your journey: ")
    print()
    commands()
while start != "start":
  start = input("Try again: ")
  if start == "start":
    os.system('cls')
    print("INSTRUCTIONS:")
    print()
    print()
    print("On your quest you will have several options to choose from at each location, including moving onwards or backtracking. Charging in with reckless abandon is unwise, and you'll be bound to meet a quick fate. Here are some of your")
    print("commands that you will use on your journey: ")
    print()
    commands()
    break
print() 
username()
cabin()