# This is first program, which assigns a sentence to a variable which is then printed.
# After that the same variable is assigned a different sentence and printed, showing how it can be used as a placeholder.  

message = "Hello, this is the first message."

print()
print(message)
print()

message = "Goodbye, this is the last message."

print(message)
print()

# This is the second program, which assigns my name to a variable in all lower case. It's then inserted into a sentence in all caps by using the upper command.
# After that is inserted into a sentence with the lower command, which in this case, doesn't have any visible change.
# Finally, the variable is inserted with the title command, which capitalizes the first and second word like you would a proper name or title.

name = "nathan huffman"

print()
print("Hello, "+name.upper()+", how are you today?")
print()

print()
print("Hello, "+name.lower()+", how are you today?")
print()

print()
print("Hello, "+name.title()+", how are you today?")
print()