
from Restaurant import Restaurant # pyright: ignore[reportMissingImports]
print("create an instance of the Restaurant class from the imported module") 
my_restaurant = Restaurant("Global Eats", "International")
print("call the describe_restaurant method on the imported instance") 
my_restaurant.describe_restaurant()
# This code imports the Restaurant class from another file named restaurant.py
# and creates an instance of it, then calls a method to describe the restaurant.
