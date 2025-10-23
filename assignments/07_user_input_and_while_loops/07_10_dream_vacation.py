print("a program to plan your dream vacation.") 
responses = {}
polling_active = True
while polling_active:
    name = input("What is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")
    responses[name] = destination
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False 
print("\n--- Poll Results ---")
for name, destination in responses.items():
    print(f"{name} would like to visit {destination}.") 