favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

new_names = ["nathan", "sarah", "greg", "bob","phil"]

print("\n")
for name in new_names:
    if name == name in favorite_languages.keys():
        print(f"Hello {name.title()}, thank you for responding to our poll.")
    else:
        print(f"Hello {name.title()}, please respond to our poll.")
print("\n")