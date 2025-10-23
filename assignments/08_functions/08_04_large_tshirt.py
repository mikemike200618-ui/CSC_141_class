print("modify the make_shirt() function to include a default size and message.") 
def make_shirt(size='L', message='I love Python'):
    """Display a message about the shirt size and the printed message."""
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")
# Call the function with default arguments
make_shirt()
# Call the function with a custom size
make_shirt(size='M')
# Call the function with a custom message
make_shirt(message='Code is fun!')
# Call the function with both custom size and message
make_shirt(size='S', message='Hello, World!')
# This modified function now has default values for size and message.
# It can be called with no arguments to use the defaults, or with one or both arguments
# to customize the shirt details.