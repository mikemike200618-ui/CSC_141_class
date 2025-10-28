print("a class called Admin that inherits from the User class") 
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
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can modify settings"
        ]

    def show_privileges(self):
        print(f"Admin Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
print("create an instance of the Admin class") 
admin_user = Admin("Alice", "Smith") 
print("call the describe_user method") 
admin_user.describe_user()
print("call the show_privileges method") 
admin_user.show_privileges()
# This code defines an Admin class that inherits from the User class.
# The Admin class has an additional attribute for privileges and a method to display them.
