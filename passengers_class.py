from Human_class import *

class Passenger(Human):
    def __init__(self, name, passport_number):
        super().__init__(name)
        self.passport_no = passport_number

    def add_passport_number(self, passport_no):
        new_passenger_passport = self
        new_passenger_passport.passport_no.append(passport_no)

list_of_passengers = []






