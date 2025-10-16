friend_pizzas = ['pepperoni', 'cheese', 'veggie', 'sausage']   
my_pizzas = friend_pizzas[:]
friend_pizzas.append('pepperoni')
my_pizzas.append('cheese') 
print("My favorite pizzas are:")
for pizza in my_pizzas:
	print(pizza) 
print("\nMy friend's favorite pizzas are:") 
for pizza in friend_pizzas:
	print(pizza)
# This code demonstrates how to copy a list and modify both the original and the copied list independently
# The friend_pizzas list contains four types of pizzas as strings
# The my_pizzas list is created as a copy of friend_pizzas using slicing
# The append method is used to add 'pepperoni' to the friend_pizzas
# and 'cheese' to the my_pizzas list
# Two for loops are used to iterate through each list and print the favorite pizzas
# The first print statement outputs a message indicating that the following pizzas are the user's favorites
# The second print statement outputs a message indicating that the following pizzas are the friend's favorites
# Each pizza type is printed on a new line due to the for loop iterating through the lists
# The \n in the second print statement adds a blank line for better readability between the two lists