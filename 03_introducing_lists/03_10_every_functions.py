games = ["Demon's Souls","Dark Souls","Dark Souls 2","Dark Souls 3","Bloodborne","Sekiro","Elden Ring"]

print("\n")
print(games)
print("\n")

print(sorted(games))
print("\n")

print(sorted(games, reverse = True))
print("\n")

print("My favorite games in the series are " + games[1] + " and " + games[4] + ".\n")

print("My least favorite game in the series is "+ games[2] + ".\n")
games.pop(2)

print("The games that I have not gotten all achievements for, or not finished are: " + games[0] + ", " + games[4] + ", and " + games[5] + ".\n")
del games[0]
games.remove("Sekiro")
games.remove("Elden Ring")

games.sort()
print(games)

games.insert(3, "Elden Ring")
print("\nThe most popular game in the series is " + games[len(games)-1]+". \n")