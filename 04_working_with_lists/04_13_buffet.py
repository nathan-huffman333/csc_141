buffet = ("Mac and Cheese","Hot Dogs", "Pizza", "French Fries", "Mashed Potatoes")

print("\nOriginal Menu:")
for item in buffet:
    print(item)
print("\n")

buffet = ("Mac and Cheese","Hot Dogs", "Pizza", "Salad", "Shrimp")
print("Modified Menu:")
for item in buffet:
    print(item)
print("\n")

# This doesn't work on purpose to show that tuples can't be changed:

buffet[3] = "Salad"

