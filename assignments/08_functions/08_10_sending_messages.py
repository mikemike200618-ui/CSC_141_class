print("write a function called send_messages().") 
def send_messages(messages, sent_messages):
    """Simulate sending each message by moving it to sent_messages list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
# List of messages to be sent
messages = ["Hello!", "How are you?", "Goodbye!"]
sent_messages = []
# Call the function to send messages
send_messages(messages, sent_messages)
print("\nThe following messages have been sent:")
for message in sent_messages:
    print(message)
# This function takes a list of messages and simulates sending each one by
# removing it from the original list and adding it to a new list of sent messages.
# It demonstrates how to manipulate lists within a function in Python. 