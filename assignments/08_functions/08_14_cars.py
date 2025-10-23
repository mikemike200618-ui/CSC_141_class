print("write a function that stores information about a car in a dictionary.") 
def make_car(manufacturer, model, **car_info):
    """Return a dictionary representing a car."""
    car = {
        'manufacturer': manufacturer.title(),
        'model': model.title()
    }
    for key, value in car_info.items():
        car[key] = value
    return car
# Call the function with different car information and print the results
car1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car2 = make_car('tesla', 'model s', color='red', autopilot=True, battery='long range')
print(car1)
print(car2)
# This function builds a dictionary containing information about a car,
# using required manufacturer and model parameters, along with arbitrary keyword arguments for additional car details.
# The function is then called with different car information to demonstrate its usage.