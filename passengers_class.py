from Human_class import *

class Passenger(Human):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_no = passport_number

    def add_passport_number(self, passport_no):
        new_passenger_passport = self
        new_passenger_passport.passport_no.append(passport_no)

list_of_passengers = []

# Create Passengers
passenger1 = Passenger('Joana Thomson', 'B343123')
passenger2 = Passenger('Vanessa Williams', 'B578998')
passenger3 = Passenger('Andrew Smith', 'B789876')
passenger4 = Passenger('Blake McDonald', 'B732244')
passenger5 = Passenger('Alex Walton', 'B465745')

#Append list_of_passengers
list_of_passengers.append(passenger1)
list_of_passengers.append(passenger2)
list_of_passengers.append(passenger3)
list_of_passengers.append(passenger4)
list_of_passengers.append(passenger5)




