numbers = list(range(1, 9)) 
for number in numbers:
	if number == 1:
		print("1st")
	elif number == 2:
		print("2nd")
	elif number == 3:
		print("3rd")
	else:
		print(f"{number}th")  
# This program converts numbers from 1 to 8 into their corresponding ordinal representations.
# It uses a for loop to iterate through a list of numbers from 1 to 8
# and an if-elif-else statement to determine the correct ordinal suffix for each number.
# The program checks if the number is 1, 2, or 3 to assign
# the special suffixes "st", "nd", and "rd" respectively.
# For all other numbers, it appends "th" to the number.
# The output is printed in the format of "number + suffix".