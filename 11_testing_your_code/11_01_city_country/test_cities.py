# For comments, see city_functions.py

from city_functions import city_country
import os
os.system('cls')

def test_city_country():
    formatted = city_country("new york city", "the united states of america")
    print(f"Neatly formatted location: {formatted}\n")