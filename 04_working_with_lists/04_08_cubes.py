# I designed the code to print the numbers 1 to 10 all to the 3rd power.

cubes = []

for x in range(1, 11):
    cubes.append(x**3)

for x in cubes:
    print(x)