print("an ice cream stand is a specific kind of restaurant") 
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type="Ice Cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []  # Initialize an empty list for flavors

    def add_flavor(self, flavor):
        """Add a new flavor to the ice cream stand."""
        self.flavors.append(flavor)

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"Available flavors at {self.name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")
print("create an instance of the IceCreamStand class") 
my_ice_cream_stand = IceCreamStand("Sweet Treats")
print("add some flavors to the ice cream stand") 
my_ice_cream_stand.add_flavor("Vanilla")
my_ice_cream_stand.add_flavor("Chocolate")
my_ice_cream_stand.add_flavor("Strawberry")
print("display the available flavors") 
my_ice_cream_stand.display_flavors()
# This code defines an IceCreamStand class that inherits from the Restaurant class.
# It adds functionality to manage and display ice cream flavors.