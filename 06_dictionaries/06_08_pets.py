# This code is for displaying what animal a pet is and who own it. 

pet1 = {
    'Type' : "Dog",
    'Owner' : "Nathan"
}

pet2 = {
    'Type' : "Hamster",
    'Owner' : "Tara"
}

pet3 = {
    'Type' : "Cat",
    'Owner' : "Andrea"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\n")
    print(f"\tAnimal: {pet["Type"].title()}")
    print(f"\tOwner: {pet['Owner'].title()}")