
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # New attribute with default value

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served by a given amount."""
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Additional customers cannot be negative.") 
print("create an instance of the Restaurant class") 
my_restaurant = Restaurant("Pasta Palace", "Italian")
print("set the number of customers served to 5") 
my_restaurant.set_number_served(5)
print("display the number of customers served") 
print(f"Number of customers served: {my_restaurant.number_served}")
print("increment the number of customers served by 3") 
my_restaurant.increment_number_served(3)
print("display the updated number of customers served") 
print(f"Number of customers served: {my_restaurant.number_served}")
# This code adds an attribute to track the number of customers served by the restaurant.
# It includes methods to set and increment this number, demonstrating how to manage state within a class in Python.
