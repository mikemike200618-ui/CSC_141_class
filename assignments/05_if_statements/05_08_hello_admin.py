usernames = ['alice', 'bob', 'charlie', 'admin', 'eve']
for username in usernames:
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {username}, thank you for logging in.") 
# This program greets users based on their usernames.
# If the username is 'admin', it provides a special greeting. 
# For all other usernames, it provides a standard greeting.
# The program uses a for loop to iterate through a list of usernames.
# It uses an if-else statement to check if the current username is 'admin'.
# Depending on the result of the check, it prints the appropriate greeting.
# You can modify the list of usernames to test different scenarios.
# Example: If the list contains 'admin', the output will include a special message for the admin user.
# The program is straightforward and easy to modify for different usernames or greetings if needed. 
# Example output:
# Hello alice, thank you for logging in.
# Hello bob, thank you for logging in.
# Hello charlie, thank you for logging in.
# Hello admin, would you like to see a status report? 