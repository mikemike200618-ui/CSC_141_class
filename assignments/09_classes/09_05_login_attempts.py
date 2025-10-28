
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0  # New attribute to track login attempts

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0
print("create an instance of the User class") 
user1 = User("Alice", "Johnson") 
print("login attempts:", user1.login_attempts) 
print("login attempts to 0") 
user1.reset_login_attempts()
print("display login attempts after reset:", user1.login_attempts)
print("increment login attempts 3 times") 
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("display login attempts after increments:", user1.login_attempts)
# This code adds an attribute to track the number of login attempts for a user.
# It includes methods to increment and reset this number, demonstrating how to manage user state within a