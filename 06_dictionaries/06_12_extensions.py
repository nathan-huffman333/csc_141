# This code adds more to an example in the book, where a username and info about the user is displayed.

people = {
'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
},

'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
 },

'nhuffman' : {
    'first': 'nathan',
    'last': 'huffman',
    'location': 'reading'
 },

'thuffman' : {
    'first': "tara",
    'last': "huffman",
    'location': "doylestown"
}
}

for username, info in people.items():
    print(f"\nUsername: {username}")
    print(f"\tFirst name: {info['first'].title()}")
    print(f"\tLast name: {info['last'].title()}")
    print(f"\tFull name: {(f"{info['first']} {info['last']}").title()}")
    print(f"\tLocation: {info['location'].title()}")