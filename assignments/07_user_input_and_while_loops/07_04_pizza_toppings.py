print("looping pizza toppings. enter 'quit' when you are done.") 
while True:
    topping = input("Enter a pizza topping: ")
    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza.")
print("Your pizza is being prepared with the selected toppings.")
print("i'll add that topping to your pizza.") 