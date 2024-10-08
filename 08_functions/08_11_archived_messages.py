# This code prints messages and moves them to another list using a copy to show how the original list is unmodified.

import os
os.system('cls')

def show_messages(joke):
    for message in joke:
        print(message)


def send_messages(x):
    for x in joke:
        print(x)
        sent_messages.append(x)

sent_messages = []
joke = ["Knock knock.", "Who's there?", "Kenya", "Kenya who?", "Kenya lend me some money?"]

send_messages(joke[:])
print(f"\nFirst list: {joke}")
print(f"Second list: {sent_messages}")