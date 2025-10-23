print("function called city_country().") 
def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city.title()}, {country.title()}"
# Call the function with different city-country pairs and print the results
print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('tokyo', 'japan'))
# This function takes a city name and a country name as arguments,
# formats them properly, and returns the formatted string.
# The function is then called with different city-country pairs to demonstrate its usage.