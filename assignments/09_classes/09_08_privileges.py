print("write a class called Privileges") 
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
print("modify the Admin class to use the Privileges class") 
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = Privileges([
            "can add post",
            "can delete post",
            "can ban user",
            "can modify settings"
        ]) 
print("create an instance of the Admin class")
admin_user = Admin("Bob", "Johnson") 
print("call the describe_user method")
admin_user.describe_user()
print("call the show_privileges method from the Privileges class")
admin_user.privileges.show_privileges()
# This code defines a Privileges class to manage admin privileges separately.
# The Admin class is modified to include an instance of the Privileges class,
# demonstrating composition in object-oriented programming. 