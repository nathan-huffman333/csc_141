# This code displays the name of a city and the country it resides in one string.

import os
os.system('cls')

def city_country(city, country):
    return((f"{city.title()}, {country.title()}"))

print(city_country("philadelphia", "USA"))
print(city_country("london", "england"))
print(city_country("tokyo", "japan"))