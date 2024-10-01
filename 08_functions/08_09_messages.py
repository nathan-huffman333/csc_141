# This code displays some short simple messages from a list with a function.

import os
os.system('cls')

def show_messages(joke):
    for message in joke:
        print(message)

joke = ["knock knock.", "who's there?", "Kenya", "Kenya who?", "Kenya lend me some money?"]
show_messages(joke)