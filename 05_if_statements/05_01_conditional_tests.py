# The point of this code is to see if one string equals another.

greeting = "hello"

print("\nIs greeting equal to hello? I predict TRUE.")
print(greeting == "hello")

print("\nIs greeting equal to goodbye? I predict FALSE.")
print(greeting == "goodbye")

leaving = "goodbye"

print("\nIs leaving equal to goodbye? I predict TRUE.")
print(leaving == "goodbye")

print("\nIs leaving equal to hello? I predict FALSE.")
print(leaving == "hello")

# AND statements:

print("\nWhen greeting equals hello AND leaving equals goodbye, it will be TRUE.")
print(greeting == "hello" and leaving == "goodbye")

print("\nWhen greeting equals hello AND leaving DOESN'T equal goodbye, it will be FALSE.")
print(greeting == "hello" and leaving == "NO")

print("\nWhen greeting DOESN'T equal hello AND leaving equalS goodbye, it will be FALSE.")
print(greeting == "NO" and leaving == "goodbye")

print("\nWhen greeting DOESN'T equal hello AND leaving DOESN'T equal goodbye, it will be FALSE.")
print(greeting == "NO" and leaving == "NO")

# OR Statements:

print("\nWhen greeting equals hello and leaving equals goodbye, it will be TRUE.")
print(greeting == "hello" or leaving == "goodbye")

print("\nWhen greeting equals hello or leaving equals goodbye, it will be TRUE.")
print(greeting == "hello" or leaving == "NO")

print("\nWhen BOTH greeting DOESN'T equal hello and leaving DOESN'T equal goodbye, it will be FALSE.")
print(greeting == "NO" or leaving == "NO")
