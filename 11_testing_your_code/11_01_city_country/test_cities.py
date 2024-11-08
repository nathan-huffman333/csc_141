# Difficulty: 9/10 I could not for the life of me figure out how to set up pytest correctly, the code itself was incredibly easy, but for some reason pytest just wasn't working for a long time.
# This code takes a function from another file and using another function, runs it to create a formated location of a city and country.

from city_functions import city_country
import os
os.system('cls')

def test_city_country():
    formatted = city_country("new york city", "the united states of america")
    print(f"\tNeatly formatted location: {formatted}")