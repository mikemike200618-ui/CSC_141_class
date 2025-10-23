print("using a program that has one function in it, store that function in a separate file, and import that function into your main program file.") 
from printing_functions import print_models, show_completed_models # type: ignore 
# List of designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# List to hold completed models
completed_models = []
# Call the function to print models
print_models(unprinted_designs, completed_models)
# Call the function to show completed models
show_completed_models(completed_models)
# This code imports two functions from a separate file called printing_functions.py.
# It then uses these functions to simulate printing 3D models and displaying the completed models.
# The functions handle the logic for printing and displaying, while the main program
# manages the lists of designs and completed models. 
# This demonstrates how to organize code into separate files and reuse functions across different programs. 


