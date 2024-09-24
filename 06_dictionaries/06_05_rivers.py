# This code is for describing what rivers run through what country.

rivers = {
    'Egypt': "the nile",
    'The USA': "the mississippi",
    'Brazil and Peru': "the amazon"
}

# prints the (river) runs through (country)
for country, river in rivers.items():
    print(f"\n{river.title()} river runs through {country}")
# prints the countries
for country in rivers.keys():
    print(f"\n{country}")
# prints the rivers
for country, river in rivers.items():
    print(f"\n{river.title()}")
print("\n")