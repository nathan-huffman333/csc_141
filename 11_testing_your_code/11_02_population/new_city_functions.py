# Difficulty: 2/10 Pretty easy now that pytest is working, the coding was relatively simple.
# This code does the same as the last one except now there is an optional parameter of 'population'.

def city_country(city, country, population=0):
    if population == 0:
        return f"{city.title()}, {country.title()}"
    else:
        return f"{city.title()}, {country.title()} - Population: {population}"