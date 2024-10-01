# This code describes the country that a city resides in.

import os
os.system('cls')

def describe_city(city, country = 'The USA'):
    print(f"{city.title()} is in {country}.")

describe_city("new york city")
describe_city("philadelphia")
describe_city("london", "England")
print("\n")