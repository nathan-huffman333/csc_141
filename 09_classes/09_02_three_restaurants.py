# This code describes the attributes of three different restaurants by using a class.

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
        

restaurant = Restaurant("La Bella Italia", "Italian")
restaurant.describe_restaurant()
print("\n")

restaurant = Restaurant("Wendy's", "Fast Food")
restaurant.describe_restaurant()
print("\n")

restaurant = Restaurant("Ramsay's Kitchen", "Fine Dining")
restaurant.describe_restaurant()
print("\n")