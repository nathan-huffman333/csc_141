# This code is for displaying the information of several people in neat and efficient way.

Nathan = {
    'first_name': "Nathan",
    'last_name': "Huffman",
    'age': 19,
    'city': "Doylestown"
}

Tara = {
    'first_name': "Tara",
    'last_name': "Huffman",
    'age': 22,
    'city': "Doylestown"
}

Andrea = {
    'first_name': "Andrea",
    'last_name': "Huffman",
    'age': 45,
    'city': "Doylestown"
}

people = [Nathan, Tara, Andrea]

for person in people:
    print("\n")
    print(f"\tFirst name: {person['first_name'].title()}")
    print(f"\tLast name: {person['last_name'].title()}")
    print(f"\tFull name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person["age"]}")
    print(f"\tCity: {person["city"].title()}")


