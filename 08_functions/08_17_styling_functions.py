# This is three programs from the chapters that I have modified to the correct style

import os
os.system('cls')


# 08_04_large_shirts changes:

def make_shirt(size='large', message='i love python'):
    """Describes the attributes of a T-shirt, including size and text on it.
    If unspecified, it uses default values for the size and text."""
    print(f"The shirt is size {size.title()}, and says {message.title()}.\n")

make_shirt()
make_shirt(size='medium', message='i love coding')
print("\n")



# 08_07_album changes:

def make_album_dictionary(artist, album_title, number_of_songs=''):
    """Receives the artist and album title, and possibly the number of songs.
    Adds arguments to a dictionary and returns it."""
    if number_of_songs:
        album = {'Artist' : artist.title(),
                'Album Name' : album_title.title(),
                'Number of Songs' : number_of_songs}
    else: 
        album = {'Artist' : artist.title(),
                'Album Name' : album_title.title()}
    return(album)

print(make_album_dictionary("metallica", "ride the lightning"))
print(make_album_dictionary("rammstein", "mutter"))
print(make_album_dictionary("megadeth", "rust in peace"))
print(make_album_dictionary("metallica", "master of puppets", 8))
print("\n")



# 08_11_archived_messages changes:

def show_messages(joke):
    """Receives list 'joke' as an argument and prints its contents."""
    for message in joke:
        print(message)


def send_messages(x):
    """Receives list 'joke' as an argument and prints its contents.
    Adds the content from the list 'joke' to the list 'sent_messages'."""
    for x in joke:
        print(x)
        sent_messages.append(x)

sent_messages = []
joke = ["Knock knock.",
        "Who's there?",
        "Kenya",
        "Kenya who?",
        "Kenya lend me some money?"]

send_messages(joke[:])
print(f"\nFirst list: {joke}")
print(f"Second list: {sent_messages}")