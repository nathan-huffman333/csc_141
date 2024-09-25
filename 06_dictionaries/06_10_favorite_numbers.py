# This code displays 3 of each person's favorite numbers.

favorite_numbers = {
    'nathan' : [333, 64, 100],
    'anthony' : [100, 500, 1000],
    'jack' : [555, 777, 999],
    'josh' : [80, 56, 10],
    'peter' : [12, 88, 18]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: " + str(numbers)[1:-1])
