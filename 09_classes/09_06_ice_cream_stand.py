# This code uses a subclass for specifically Ice Cream stands in the parent class Restaurant.

import os
os.system('cls')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

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