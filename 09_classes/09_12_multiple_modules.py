# This takes classes from two separate files to describe users and admins.

import os
os.system('cls')
from user import User
from adminprivilege import Admin
from adminprivilege import Privileges

nathan = Admin("Nathan", "Huffman", 19, "Dark Brown", "Blue")
nathan.describe_user()
print("\n")
nathan.privileges.show_privileges()
print("\n")

user = User("Anthony", "Frederick", 18, "Brown", "Blue")
user.describe_user()
print("\n")