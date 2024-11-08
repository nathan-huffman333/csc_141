def city_country(city, country, population=0):
    if population == 0:
        return f"{city.title()}, {country.title()}"
    else:
        return f"{city.title()}, {country.title()} - Population: {population}"