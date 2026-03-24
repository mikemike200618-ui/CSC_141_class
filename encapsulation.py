import pygame

def calculateAverage(numbersList):
    total = 0.0
    for number in numbersList:
        total = total + number
    nElements = len(numbersList)
    average = total / nElements
    return average 
class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
    def getSalary(self):
        return self.salary
    def setSalary(self, newSalary):
        self.salary = newSalary
    def displayInfo(self):        print("Name: " + self.name)                                                  

# Example usage
# numbers = [10, 20, 30, 40, 50]
# avg = calculateAverage(numbers)
# print("Average:", avg)
# person = Person("Alice", 50000)
# person.displayInfo()
# person.setSalary(55000)
# print("Updated Salary:", person.getSalary())  

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000) 
oPerson1.displayInfo()
oPerson2.displayInfo() 
oPerson1.setSalary(95000)
print("Updated Salary for " + oPerson1.name + ": " + str(oPerson1.getSalary()))  

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)
# Get the values of the salary variable directly
print(oPerson1.salary)
print(oPerson2.salary)
# Change the salary variable directly
oPerson1.salary = 100000
oPerson2.salary = 111111
# Get the updated salaries and print again
print(oPerson1.salary)
print(oPerson2.salary) 
class Account():
    def __init__(self, interestRate, balance=0):
        self.interestRate = interestRate
        self.balance = balance

    def calculateInterestRate(self):
        # Assuming self.balance has been set in another method
        if self.balance < 1000:
            self.interestRate = 1.0
        elif self.balance < 5000:
            self.interestRate = 1.5
        else:
            self.interestRate = 2.0

oAccount = Account(0.05, 800)
oAccount.calculateInterestRate()
print(oAccount.interestRate) 
class Club():
    def __init__(self, clubName, maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers
        self.membersList = []

    def addMember(self, name):
        # Make sure that there is enough room left
        if len(self.membersList) < self.maxMembers:
            self.membersList.append(name)
            print('OK.', name, 'has been added to the', self.clubName, 'club')
        else:
            print('Sorry, but we cannot add', name, 'to the', self.clubName, 'club.')
            print('This club already has the maximum of', self.maxMembers, 'members.')

    def report(self):
        print()
        print('club:')
        for name in self.membersList:
            print(' ' + name)
        print()
        print('Here are the', len(self.membersList), 'members of the', self.clubName)

# Create a club with at most 5 members
oProgrammingClub = Club('Programming', 5)
oProgrammingClub.addMember('Joe Schmoe')
oProgrammingClub.addMember('Cindy Lou Hoo')
oProgrammingClub.addMember('Dino Richmond')
oProgrammingClub.addMember('Susie Sweetness')
oProgrammingClub.addMember('Fred Farkle')
oProgrammingClub.report()
oProgrammingClub.addMember('Iwanna Join') 
oProgrammingClub.maxMembers = 300 
oProgrammingClub.addMember('Iwanna Join')
oProgrammingClub.memberList.append('Iwanna Join') 
oProgrammingClub.report()
class Person():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Allow the caller to retrieve the salary
    def getSalary(self):
        return self.salary 
    # Allow the caller to change the salary    def setSalary(self, newSalary):
        self.salary = newSalary
    # Display the person's information    def displayInfo(self):    
        print("Name: " + self.name)
        print("Salary: " + str(self.salary)) 
# Example usage 
oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)
oPerson1.displayInfo()
oPerson2.displayInfo()
oPerson1.setSalary(95000)
print("Updated Salary for " + oPerson1.name + ": " + str(oPerson1.getSalary()))
 
oRectangle = pygame.Rect(10, 20, 300, 300) 
class PrivatePerson():
    def __init__(self, name, privateData):
        self.name = name
        self.__privateData = privateData

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name 
# usersPrivateData = oPrivatePerson.__privateData
# AttributeError: 'PrivatePerson' object has no attribute '__privateData'
oPrivatePerson = PrivatePerson('John Doe', 'Sensitive Information')
print(oPrivatePerson.getName())  # Output: John Doe
oPrivatePerson.setName('Jane Doe')
print(oPrivatePerson.getName())  # Output: Jane Doe 
class Example():
    def __init__(self, startingValue):
        self._x = startingValue

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value): # this is the decorated setter method
        self._x = value 
oExample = Example(10)
print(oExample.x)  # Output: 10
oExample.x = 20
print(oExample.x)  # Output: 20
class Student():
    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.__grade = startingGrade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)('New grade: ' + str(newGrade) + ', is an invalid type.')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError('New grade: ' + str(newGrade) + ', must be between 0 and 100.')
        self.__grade = newGrade 

oStudent = Student('Alice')
print(oStudent.grade)  # Output: 0
oStudent.grade = 85
print(oStudent.grade)  # Output: 85
try:
    oStudent.grade = 150  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: New grade: 150, must be between 0 and 100.
try:
    oStudent.grade = 'A+'  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: New grade: A+, is an invalid type.
# Main Student property example
oStudent1= Student('Joe Schmoe')
oStudent2= Student ('Jane Smith')
# Get the students' grades using the 'grade' property and print
print(oStudent1.grade)
print(oStudent2.grade)
print()
# Set new values using the 'grade' property
oStudent1.grade = 85
oStudent2.grade = 92
# Stack class
class Stack():
    ''' Stack class implements a last in first out LIFO algorithm'''
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = [ ]
        else:
            self.dataList = startingStackAsList[:] # make a copy
    def push(self, item):
        self.dataList.append(item)
    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        return self.dataList.pop()

    def peek(self):
        # Retrieve the top item, without removing it
        item = self.dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.dataList)
        return nElements

    def show(self):
        # Show the stack in a vertical orientation
        print('Stack is:')
        for value in reversed(self.dataList):
            print(' ', value)

print(oStudent1.grade)
print(oStudent2.grade) 
oStack = Stack()
oStack.push(5) 
someVariable = oStack.pop() 
print(someVariable)  # Output: 5
