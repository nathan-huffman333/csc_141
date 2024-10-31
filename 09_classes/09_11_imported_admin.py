# This imports multiple classes from another file to describe admins and users.

import os
os.system('cls')

from admin import User
from admin import Admin
from admin import Privileges

nathan = Admin("Nathan", "Huffman", 19, "Dark Brown", "Blue")
nathan.describe_user()
print("\n")
nathan.privileges.show_privileges()
print("\n")

user = User("Anthony", "Frederick", 18, "Brown", "Blue")
user.describe_user()
print("\n")