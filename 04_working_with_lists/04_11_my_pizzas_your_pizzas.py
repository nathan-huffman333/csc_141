pizzas = ["pepperoni", "cheese", "stuffed crust"]
friends_pizzas = pizzas [:]

pizzas.append("meatlovers")
friends_pizzas.append("hawaiian")

print("My favorite pizzas are: ")
for x in pizzas:
    print(x)
print("\n")

print("My friend's favorite pizzas are: ")
for x in friends_pizzas:
    print(x)
print("\n")