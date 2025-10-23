print("Call the function send_messages() with a copy of the list of messages. After calling the func-tion, print both of your lists to show that the original list has retained its messages.") 
def send_messages(messages, sent_messages):
    """Simulate sending each message by moving it to sent_messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
# List of messages to be sent
messages = ["Hello!", "How are you?", "Goodbye!"]
sent_messages = []
# Call the function to send messages with a copy of the original list
send_messages(messages[:], sent_messages)
print("\nThe original list of messages:")
for message in messages:
    print(message)
print("\nThe following messages have been sent:")
for message in sent_messages:
    print(message)
# This code defines a function send_messages() that simulates sending messages by moving them from one list to another.
# It then calls the function with a copy of the original list to demonstrate that the original list remains unchanged. 
