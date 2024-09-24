# This program is used to see if a string is equal to another string, or if a number is equal to another number.

string_one = "Thing"
string_two = "Other"

print(string_one == string_two)
print(string_one != string_two)
print("\n")

print(string_one.lower() == "thing")
print(string_two.lower() == "OTHER")
print("\n")

num1 = 5
num2 = 10

print(num1*2 == num2)
print(num1 == num2)
print(num1 < num2)
print(num1 > num2)
print(num2 > num1)
print(num2 < num1)
print(num1*2 <= num2)
print(num1*3 <= num2)
print(num1 >= num2)
print(num1*3 >= num2)
print("\n")

print(string_one == "Thing" and num1 == 5)
print(string_two == "Thing" and num1 == 5)
print(string_one == "Other" or num1 == 5)
print(string_one == "Other" or num1 == 10)
print("\n")

list1 = ["one","two","three","four"]

print("four" in list1)
print("five" in list1)