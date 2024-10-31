# This code generates winning tickets and your ticket continuously until you have won, and then tells you how many attempts it took.

import os
os.system('cls')
from random import choice

def winning_ticket(lottery):
    winner = []
    while len(winner) < 4:
        pulled_item = choice(lottery)
        if pulled_item not in winner:
            winner.append(pulled_item)
    return(winner)


def generate_ticket(lottery):
    my_ticket = []
    while len(my_ticket) < 4:
        pulled_item = choice(lottery)
        if pulled_item not in my_ticket:
            my_ticket.append(pulled_item)
    return(my_ticket)


def check_ticket(winner, my_ticket):
    if all(item in winner for item in my_ticket):
        print(f"Your ticket is: {ticket}")
        print(f"The winning ticket was: {win_ticket}")
        print("\nYou win a prize! Congratulations!")
        print(f"It only took: {attempts} attempts")
        return(True)
    else:
        return(False)


lottery = (42, 55, "J", 33, "H", 25, 96, "O", 14, 76, "W", 8, 82, 66, "N")
attempts = 1

win_ticket = winning_ticket(lottery)
ticket = generate_ticket(lottery)

while not check_ticket(win_ticket, ticket):
    attempts += 1
    win_ticket = winning_ticket(lottery)
    ticket = generate_ticket(lottery)
print("\n")