current_users = ['alice', 'bob', 'charlie', 'dave', 'eve'] 
new_users = ['Frank', 'Grace', 'Heidi', 'alice', 'bob']   
for user in new_users:
	if user.lower() in [u.lower() for u in current_users]:
		print(f"Username '{user}' is already taken. Please enter a new username.")
	else:
		print(f"Username '{user}' is available.") 
# This program checks the availability of new usernames against a list of current usernames.
# It performs a case-insensitive comparison to ensure that usernames are unique regardless of letter casing.
# The program uses a for loop to iterate through the list of new usernames.
# For each new username, it checks if it exists in the current usernames list (converted to lowercase).
# If the username is already taken, it prompts the user to enter a new one; otherwise, it confirms that the username is available.
# You can modify the lists of current and new usernames to test different scenarios.
# Example: If 'alice' is in current_users, the output will indicate that 'alice' is already taken, even if the new username is 'Alice'.
# The program is straightforward and easy to modify for different username lists or comparison criteria if needed. 
