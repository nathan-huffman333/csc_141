games = ["Demon's Souls","Dark Souls","Dark Souls 2","Dark Souls 3","Bloodborne","Sekiro","Elden Ring"]

# This is an error

print("I haven't completed " + games[len(games)] + ".")

# The list index is out of range since the len command counts the amount of items in the list, which is 1 more than the number of indexes since index starts at 0.

# This would be correct:

print("I haven't completed " + games[len(games)-1] + ".")