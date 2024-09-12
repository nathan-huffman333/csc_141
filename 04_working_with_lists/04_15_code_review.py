# Changes to 4_11_my pizzas_your_pizzas:
pizzas = ["pepperoni",
          "cheese",
          "stuffed crust"
          ]
friends_pizzas = pizzas [:]

pizzas.append("meatlovers")
friends_pizzas.append("hawaiian")
print("\nMy favorite pizzas are: ")
for x in pizzas:
    print(x)
print("\nMy friend's favorite pizzas are: ")
for x in friends_pizzas:
    print(x)
print("\n")

# Change to 04_12_more_loops:
my_foods = ['pizza',
            'falafel',
            'carrot cake'
            ]
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for x in my_foods:
    print(x)
print("\nMy friend's favorite foods are:")
for x in friend_foods:
    print(x)

# Changes to 04_02_animals
animals = ["dog",
           "cat",
           "hamster"
           ]

print("\n")
for x in animals:
    print(x)
print("\nI have 2 "+animals[0]+"s.")
print("I have 1 "+animals[1]+".")
print("My sister has had 4 "+animals[2]+"s.\n")
print("All of these animals make great pets, have four legs, and me or a family"
" member has or has owned.\n")