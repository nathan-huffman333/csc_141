guests = ["Julius Caesar", "Hidetaka Miyazaki", "Albert Einstein"]

print("\n")
for x in range (len(guests)):
    print("Hello, "+guests[x]+", I would like to invite you to dinner tonight to learn more about your life.")
print("\n")

print("Unfortunately, Julius Caesar could not make it to the dinner tonight.")
print("\n")

guests.pop(0)
guests.insert(0, "Mark Fischbach")

for x in range (len(guests)):
    print("Hello, "+guests[x]+", I would like to invite you to dinner tonight to learn more about your life.")
print("\n")

print("Good news everyone! I now have bigger table and can accomodate for more guests, so I will be inviting three new guests.")
print("\n")

guests.insert(0, "Keanu Reeves")
guests.insert(2, "James Hetfield")
guests.insert(len(guests), "Isaac Newton")

for x in range (len(guests)):
    print("Hello, "+guests[x]+", I would like to invite you to dinner tonight to learn more about your life.")
print("\n")