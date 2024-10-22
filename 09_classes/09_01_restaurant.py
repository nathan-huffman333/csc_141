# This code describes the attributes of a restaurant by using a class.

import os
os.system('cls')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        return self
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        return self


restaurant = Restaurant("La Bella Italia", "Italian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\n")
restaurant.describe_restaurant()
print("\n")
restaurant.open_restaurant()
print("\n")
