current_users = ["james", "nathan", "tara", "jeffrey", "andrea"]
new_users = ["NATHAN", "matthew", "josh", "peter", "TARA"]

for x in current_users:
    x = x.lower()

for x in new_users:
    x = x.lower()
    if x in current_users:
        print("That username has already been chosen.")
    else:
        print("That username is available")