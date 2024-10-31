# This code imports Restaurant from another file and calls some of its methods.

import os
os.system('cls')
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "peanut butter cup", "mint chocolate chip", "cotton candy"]

    def display_flavors(self):
        print("Flavors Available:")
        for x in self.flavors:
            print(f"\t{x.title()}")

restaurant = IceCreamStand("Joe's Ice Cream Shop", "Ice Cream")
restaurant.describe_restaurant()
print("")
restaurant.display_flavors()
print("")
restaurant.open_restaurant()
print("\n")

restaurant = Restaurant("Ramsay's Kitchen", "Fine Dining")
restaurant.describe_restaurant()
print("\n")
restaurant.open_restaurant()
print("\n")