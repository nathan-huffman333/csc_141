import os
os.system('cls')

sandwich_orders = ["grilled cheese", "PB and J", "pastrami", "bacon", "tuna", "pastrami", "ham and cheese", "grilled cheese", "pastrami", "bacon", "PB and J",]
finished_sandwiches = []

print("The deli is out of pastrami.\n")

while len(sandwich_orders) > 0:
    if sandwich_orders[0] == "pastrami":
        print("I'm sorry the deli is out of pastrami.")
        sandwich_orders.pop(0)
    else:
        print("I made your", sandwich_orders[0],"sandwich.")
        if sandwich_orders[0] in finished_sandwiches:
            sandwich_orders.pop(0)
        else: 
            finished_sandwiches.append(sandwich_orders[0])
            sandwich_orders.pop(0)    


print("\n")
for x in range(len(finished_sandwiches)):
    print("I made at least one",finished_sandwiches[x],"sandwich")