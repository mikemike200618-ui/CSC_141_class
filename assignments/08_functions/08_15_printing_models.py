print("put the functions for the example printing_models.py file in a separate file called printing_functions.py") 
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
# This code defines two functions: print_models() and show_completed_models().
# The first function simulates printing 3D models by moving them from an unprinted list
# to a completed list, while the second function displays all the completed models.
# These functions can be imported and used in other Python files to manage 3D printing tasks.