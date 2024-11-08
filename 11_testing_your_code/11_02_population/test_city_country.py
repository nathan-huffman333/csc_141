# For comments, see new_city_functions.py

from new_city_functions import city_country
import os
os.system('cls')

def test_city_country():
    formatted = city_country("new york city", "the united states of america")
    print(f"Neatly formatted location: {formatted}\n")

def test_city_county_population():
    formatted = city_country("santiago", "chile", 5000000)
    print(f"Neatly formatted location: {formatted}\n")