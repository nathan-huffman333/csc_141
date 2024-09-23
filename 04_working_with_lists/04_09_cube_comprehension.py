# I designed the code to print the numbers 1 to 10 all to the 3rd power, but more efficiently than the previous assignment.

cubes = [value**3 for value in range(1, 11)]

for x in cubes:
    print(x)