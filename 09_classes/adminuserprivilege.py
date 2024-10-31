class User:
    def __init__(self, first_name, last_name, age, hair_color, eye_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.login_attempts = 0

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Hair Color: {self.hair_color}")
        print(f"Eye Color: {self.eye_color}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age, hair_color, eye_color):
        super().__init__(first_name, last_name, age, hair_color, eye_color)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["Adding Posts", "Deleting Posts", "Banning Users"]

    def show_privileges(self):
        print("ADMIN PRIVILEGES:")
        for x in self.privileges:
            print(f"\t{x.upper()}")