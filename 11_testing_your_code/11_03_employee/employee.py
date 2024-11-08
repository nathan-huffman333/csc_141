# Difficulty: 5/10 Not that bad, I just needed a refresher on classes and how to implement them into other functions.
# This code has the class for a employee, and then in a another file has the functions that can be called to increase the employee's salary either by a default amount or custom amount.

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, default_raise = 5000):
        self.salary += default_raise