
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!") 
restaurant1 = Restaurant("Sushi Central", "Japanese")
restaurant2 = Restaurant("Taco Town", "Mexican")
restaurant3 = Restaurant("Curry Corner", "Indian")
print("call the describe_restaurant method for each instance") 
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
# This code creates three different instances of the Restaurant class,
# each representing a different restaurant with its own name and cuisine type.