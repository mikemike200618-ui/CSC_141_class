 
import random
class Die:
    def __init__(self):
        pass

    def roll_die(self):
        result = random.randint(1, 6)
        print(f"You rolled a {result}")
print("create an instance of the Die class") 
die = Die() 
print("roll the die 10 times") 
for _ in range(10):
    die.roll_die()
# This code defines a Die class with a method roll_die() that generates and prints a random number between 1 and 6.
# An instance of the Die class is created, and the die is rolled 10 times to demonstrate the functionality.