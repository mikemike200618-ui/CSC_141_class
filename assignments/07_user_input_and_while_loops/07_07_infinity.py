print("loop that never ends unless the user decides to quit.") 
while True:
    response = input("Type 'exit' to quit the loop: ")
    if response.lower() == 'exit':
        print("Exiting the loop. Goodbye!") 
        print("to exit the loop,press Ctrl+C") 
        break
    else:
        print("You entered:", response)
        print("the loop will continue until you type 'exit'.") 
