print("a function called describe_city().")   
def describe_city(city, country='USA'):
    """Display a message describing the city and its country."""
    print(f"{city} is in {country}.")
# Call the function with different cities
describe_city('New York')
describe_city('Los Angeles')
describe_city('Tokyo', 'Japan')
# This function takes a city name and an optional country name (defaulting to 'USA').
# It prints a message indicating where the city is located.
# The function is called with different cities to demonstrate its usage. 