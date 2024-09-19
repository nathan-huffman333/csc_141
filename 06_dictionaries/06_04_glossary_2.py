glossary = {
    'comment': "A sentence or group of sentence written to help make code more readable, that does not affect how the code runs.",
    'condition statement': "A command that will check to see if a specification is met, and if so, perform an action.",
    'dictionary': "A collection of key-value pairs, with each key connected to a value and can be used to find the value related to it.",
    'for loop': "A type of loop that uses a string to assign to a variable to repeatedly print different values, often from a list.",
    'integer': "A type of variable that stores information in the form of a number.",
    'key-value pair': "A set of values associated with each other. When you provide a key, it will return the value associated with it.",
    'list': "A type of variable that can store information which can be added to or removed",
    'string': "A type of variable that contains a word or words as information.",
    'tuple': "A type of list in python that cannot have items removed or add to.",
    "variable": "A placeholder that can be assigned or reassigned a value in order to store information."
}

for key, value in glossary.items():
    print(f"\n{key.title()}: {value}")
print("\n")