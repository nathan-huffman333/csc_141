import os
os.system('cls')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Customers Served: {self.number_served}")
        
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    
    def set_number_served(self):
        customers = input("Customers served: ")
        number_served = customers
        return(number_served)
    
    def increment_number_served(self):
        print()

restaurant = Restaurant("La Bella Italia", "Italian", 25)
restaurant.describe_restaurant()
print("\n")
restaurant = Restaurant("La Bella Italia", "Italian", 17)
restaurant.describe_restaurant()
print("\n")
restaurant.set_number_served()