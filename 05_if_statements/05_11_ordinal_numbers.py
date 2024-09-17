nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in nums:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")