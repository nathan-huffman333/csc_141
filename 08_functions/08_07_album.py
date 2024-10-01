# This code displays information about different albums

import os
os.system('cls')

def make_album(artist, album_title, none = ''):
    if none:
        album = {'Artist' : artist.title(),
                'Album Name' : album_title.title(),
                'Number of Songs' : none}
    else: 
        album = {'Artist' : artist.title(),
                'Album Name' : album_title.title()}
    return(album)

print(make_album("metallica", "ride the lightning"))
print(make_album("rammstein", "mutter"))
print(make_album("megadeth", "rust in peace"))
print(make_album("metallica", "master of puppets", 8))