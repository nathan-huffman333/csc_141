# This is the functions and lists for 08_16_imports where items from a list are either printed, or printed and moved to another list.

sent_messages = []
joke = ["knock knock.", "who's there?", "Kenya", "Kenya who?", "Kenya lend me some money?"]

def show_messages(joke):
    for message in joke:
        print(message)

def send_messages(joke):
    for x in joke:
        print(x)
        sent_messages.append(x)