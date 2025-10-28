
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
print("create an instance of the User class") 
user1 = User("John", "Doe")  
user2 = User("Jane", "Smith") 
print("call the describe_user method for each user") 
user1.describe_user()
user2.describe_user()
print("call the greet_user method for each user") 
user1.greet_user()
user2.greet_user()
# This code defines a User class with methods to describe the user and greet them.
# It then creates two instances of the User class and calls the methods for each instance., "