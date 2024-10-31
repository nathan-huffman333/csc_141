from user import User

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