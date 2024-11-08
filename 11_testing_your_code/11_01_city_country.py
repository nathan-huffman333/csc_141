# Difficulty: 2/10 Not that hard, just had to format things correctly.
# This code takes a function from another file and using another function, runs it to create a formated location of a city and country.

import os
os.system('cls')
from city_functions import city_country


def test_city_country():
    print("\nType 'quit' at any time to quit.")
    while True:
        city = input("\nInput city: ")
        if city == 'quit':
            break
        country = input("Input country: ")
        if country == 'quit':
            break
        formatted = city_country(city, country)
        print(f"\tNeatly formatted location: {formatted}")

test_city_country()