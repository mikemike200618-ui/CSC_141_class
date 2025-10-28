print("define a Lottery class that can draw a combination of numbers and letters") 
import random 
class Lottery:
    def __init__(self):
        self.numbers = [str(i) for i in range(10)]
        self.letters = [chr(i) for i in range(65, 70)]  # Letters A to E

    def draw(self):
        drawn_numbers = random.sample(self.numbers, 3)
        drawn_letters = random.sample(self.letters, 2)
        return drawn_numbers + drawn_letters
print("create an instance of the Lottery class")
lottery = Lottery() 
print("draw a lottery combination") 
combination = lottery.draw()
print("Lottery combination drawn:", combination)
# This code defines a Lottery class that contains a list of numbers and letters.
# The draw method randomly selects 3 numbers and 2 letters to form a lottery combination.
# An instance of the Lottery class is created, and a lottery combination is drawn and displayed.