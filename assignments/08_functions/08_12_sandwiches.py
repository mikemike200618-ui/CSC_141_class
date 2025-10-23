print("write a function that accepts a list of items a person wants on a sandwich.") 
def make_sandwich(*items):
    """Display the items requested for the sandwich."""
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}") 
make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'bacon', 'tomato', 'mayonnaise')
make_sandwich('peanut butter', 'jelly')
# This function takes a variable number of arguments representing sandwich items 
# and prints out a list of those items. 
# It demonstrates how to use *args to accept an arbitrary number of arguments in Python.