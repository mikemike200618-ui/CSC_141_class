print("make a class called Restaurant") 
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")
print("create an instance of the Restaurant class") 
my_restaurant = Restaurant("Pasta Palace", "Italian")
print("call the describe_restaurant method") 
my_restaurant.describe_restaurant()
print("call the open_restaurant method") 
my_restaurant.open_restaurant() 
# This code defines a Restaurant class with methods to describe the restaurant and indicate when it's open.
