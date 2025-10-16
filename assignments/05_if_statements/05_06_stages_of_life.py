age = 30  # Set age to any integer value

if age < 13:
	print("The person is a child.")
elif age < 20:
	print("The person is a teenager.")
elif age < 65:
	print("The person is an adult.")
else:
	print("The person is an elder.") 
# This program categorizes a person based on their age.
# You can change the value of 'age' to test different categories.
# Categories:
# Child: age < 13
# Teenager: 13 <= age < 20
# Adult: 20 <= age < 65
# Elder: age >= 65
# The program uses if-elif-else statements to determine and print the correct category.
# Each condition is checked in order, and the first true condition's block is executed.
# This ensures that only one category is printed based on the age provided.
# Example: If age is set to 30, the output will be "The person is an adult."
# You can test the program by changing the value of 'age' to see how it categorizes different ages.
# The program is straightforward and easy to modify for different age ranges or categories if needed.