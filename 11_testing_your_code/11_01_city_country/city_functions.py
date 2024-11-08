# Difficulty: 9/10 I could not for the life of me figure out how to set up pytest correctly, the code itself was incredibly easy, but for some reason pytest just wasn't working for a long time.
# This code takes a function from another file and using another function, runs it to create a formated location of a city and country.

def city_country(city, country):
    return f"{city.title()}, {country.title()}"