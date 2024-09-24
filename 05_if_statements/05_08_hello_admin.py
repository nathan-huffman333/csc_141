# This code is used to see if the username is "admin", and if so, display a different message than it does for other users.

usernames = ["nathan", "james", "admin", "user", "coder"]

for x in usernames:
    if x != "admin":
        print("Hello "+x+", thank you for logging in again.")
    else:
        print("Hello "+x+", would you like to see a status report?")