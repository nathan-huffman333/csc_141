# Difficulty: 2/10 Pretty easy now that pytest is working, the coding was relatively simple.
# This code does the same as the last one except now there is an optional parameter of 'population'.

from new_city_functions import city_country
import os
os.system('cls')

def test_city_country():
    formatted = city_country("new york city", "the united states of america")
    print(f"Neatly formatted location: {formatted}\n")

def test_city_county_population():
    formatted = city_country("santiago", "chile", 5000000)
    print(f"Neatly formatted location: {formatted}\n")