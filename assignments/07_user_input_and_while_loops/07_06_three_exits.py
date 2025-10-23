print("use a while loop with three exits.") 
while True:
    command = input("Enter 'exit1', 'exit2', or 'exit3' to quit: ")
    if command == 'exit1':
        print("Exiting via exit1.")
        break
    elif command == 'exit2':
        print("Exiting via exit2.")
        break
    elif command == 'exit3':
        print("Exiting via exit3.")
        break
    else:
        print("Invalid input, please try again.")
print("You have exited the loop.")
