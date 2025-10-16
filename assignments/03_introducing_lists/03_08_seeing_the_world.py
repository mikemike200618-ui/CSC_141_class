places = ["japan", "italy", "egypt", "france", "germany"]

print(places == sorted(places))  # False
print(places)  # Original list
print(sorted(places))  # Alphabetically sorted list
print(places)  # Original list again to show it hasn't changed
print(sorted(places, reverse=True))  # Reverse alphabetical order
print(places)  # Original list again to show it hasn't changed
places.reverse()  # Reverse the order of the list
print(places)  # List after reversing
places.reverse()  # Reverse it back to the original order
print(places)  # Original list again
places.sort()  # Sort the list in alphabetical order
print(places)  # List after sorting
places.sort(reverse=True)  # Sort the list in reverse alphabetical order
print(places)  # List after reverse sorting
print(len(places))  # Number of items in the list 
print("The first five places in my list are:japan,italy,egypt,france,germany")  
for place in places[:5]:
    print(place)
print("Three places from the middle of my list are:egypt,france,germany ") 
for place in places[2:5]:
    print(place)  
print("The last five places in my list are:japan,italy,egypt,france,germany")
for place in places[-5:]: 
    print(place) 
    