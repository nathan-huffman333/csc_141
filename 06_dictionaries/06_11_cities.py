# This code displays information about different cities.

cities = {
    'New York City:' : {
        'Country' : "USA",
        'Population' : "8 Million",
        'Fact' : "Home to the 'whispering gallery', where people can whisper from across the room and still hear each other.",
    },
    
    'Tokyo:' : {
        'Country' : "Japan",
        'Population' : "37 Million",
        'Fact' : "There are people called “Oshiyas” who's job is to push commuters into crowded trains during rush hour to fit inside.",
    },

    'Paris:' : {
        'Country' : "France",
        'Population' : "11 Million",
        'Fact' : "Originally, the Eiffel Tower was meant to be a temporary monument to demonstrate superior construction skills and technology",
    }
}

for city, info in cities.items():
    print(f"\n{city}")
    print(f"\tCountry: {info['Country']}")
    print(f"\tPopulation: {info['Population']}")
    print(f"\tFact: {info['Fact']}")