# This code is able to print and update the number of customers a restaurant serves by using different methods.  

import os
os.system('cls')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Customers Served: {self.number_served}")
        
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    
    def set_number_served(self, number_served):
        self.number_served = number_served

    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurant = Restaurant("La Bella Italia", "Italian")
restaurant.describe_restaurant()
print("\n")

restaurant.set_number_served(50)
restaurant.describe_restaurant()
print("\n")

restaurant.set_number_served(250)
restaurant.describe_restaurant()
print("\n")

restaurant.increment_number_served(50)
restaurant.describe_restaurant()
print("\n")