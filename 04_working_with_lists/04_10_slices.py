# I used the list of the previous assignment, then display the first three, last three, and three items from the middle of the list.

cubes = [value**3 for value in range(1, 11)]

print("The first three items in the list are: ")
for x in cubes[:3]:
    print(x)

print("\nThree items from the middle of the list are: ")
for x in cubes[4 : -3]:
    print(x)

print("\nThe last three items in the list are: ")
for x in cubes[-3:]:
    print(x)
