print("the first three items in the list:") 
players = ['mr smith', 'newton', 'harry', 'florence', 'eli'] 
print(players[0:3])
print("three items from the middle of the list:")
print(players[0:3])
print("the last three items in the list:")
print(players[-3:])     
# Slicing a list to get specific parts of it
# The first print statement outputs a message indicating that the first three items in the list will be displayed
# The players list contains five string elements representing player names
# The slice players[0:3] retrieves the first three elements from the list (indexes 0, 1, and 2)
# The second print statement outputs a message indicating that three items from the middle of the list will be displayed
# The slice players[0:3] is repeated here, which again retrieves the first three elements from the list
# The third print statement outputs a message indicating that the last three items in the list will be displayed
# The slice players[-3:] retrieves the last three elements from the list using negative indexing
# Each print statement outputs the corresponding sliced list. 