print("loop asking their age to determine ticket price.") 
while True:
    age_input = input("Please enter your age (or 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $15.")  