print("use the final version of electric_car.py from 9_07 as a starting point") 
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
print("make a class called Battery") 
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")
        else:
            print("Battery is already at maximum capacity.")
print("make a class called ElectricCar that inherits from Car") 
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
print("create an instance of ElectricCar") 
my_electric_car = ElectricCar("Tesla", "Model S", 2020) 
print("display the car's range before upgrading the battery") 
my_electric_car.battery.get_range()
print("upgrade the battery") 
my_electric_car.battery.upgrade_battery()
print("display the car's range after upgrading the battery") 
my_electric_car.battery.get_range()
# This code defines a Battery class with an upgrade_battery method that increases the battery size to 100 kWh if it is not already at that capacity.
# The ElectricCar class contains an instance of the Battery class.
# An instance of ElectricCar is created, and the battery's range is displayed before and after upgrading the battery. 
