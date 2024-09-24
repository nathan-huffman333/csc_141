# This code displays a person's name and what some of their favorite places are.

favorite_places = {
    'Nathan' : ["Home", "Albright", "New York"],
    'Tara' : ["Vermont","Albright"],
    'Andrea' : ["France","Garden"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for places in favorite_places[name]:
        print(f"\t{places}")
