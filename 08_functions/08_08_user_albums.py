# This code displays information about albums that the user provides.

import os
os.system('cls')

def make_album(artist, album_title):
    album = {'Artist' : artist.title(),
            'Album Name' : album_title.title()}
    return(album)

again = True
while again:
    artist = input("Album's artist: ")
    album_title = input("Album title: ")
    print(make_album(artist, album_title))
    print("\n")
    again = input("Contine? (Y/N): ")
    again = again.lower()
    if again == "n" or again == "no":
        again = False
    else:
        print("\n")
