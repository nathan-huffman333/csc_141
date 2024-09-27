# This code is for saying what sandwiches were ordered and what were made.

import os
os.system('cls')

sandwich_orders = ["grilled cheese", "PB and J", "bacon", "tuna", "ham and cheese", "grilled cheese", "bacon", "PB and J",]
finished_sandwiches = []

while len(sandwich_orders) > 0:
    print("I made your", sandwich_orders[0],"sandwich.")
    if sandwich_orders[0] in finished_sandwiches:
        sandwich_orders.pop(0)
    else: 
        finished_sandwiches.append(sandwich_orders[0])
        sandwich_orders.pop(0)    


print("\n")
for x in range(len(finished_sandwiches)):
    print("I made at least one",finished_sandwiches[x],"sandwich")
    