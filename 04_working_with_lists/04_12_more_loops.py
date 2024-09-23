# I designed the code to essentially do the same thing as the last code but using lists provided by the book.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for x in my_foods:
    print(x)

print("\nMy friend's favorite foods are:")
for x in friend_foods:
    print(x)
