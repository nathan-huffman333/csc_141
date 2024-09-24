# This code is used to build of the previous one, but now it displays when there is no more users.

usernames = ["nathan", "james", "admin", "user", "coder"]

for x in usernames:
    if x != "admin":
        print("Hello "+x+", thank you for logging in again.")
    else:
        print("Hello "+x+", would you like to see a status report?")

for x in range(len(usernames)-1):
    usernames.pop(0)
print("\n")

if usernames:
    print("We need to find some users!")