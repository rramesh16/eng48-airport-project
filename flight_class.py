from passengers_class import *
from plane_class import *
class Flight():
    def __init__(self, passenger =[], passport_number = ''):
        self.origin = ''
        self.destination = ''
        self.plane = ''
        self.passengers = passenger

    def add_plane(self, plane):
        self.plane = plane
        return self.plane

    def add_origin(self, origin):
        self.origin = origin
        return self.origin

    def add_destination(self, destination):
        self.destination = destination
        return self.destination

    def add_passengers(self, passenger):
        self.passengers.append(list_of_passengers)
        return self.passengers



# Creating flights

flight1 = Flight()
flight1.add_destination('Chicago')
flight1.add_origin('London')
flight1.add_plane('BA006')

flight2 = Flight()
flight2.add_destination('Dubai')
flight2.add_origin('Sydney')
flight2.add_plane('EK551')

list_flights = []
list_flights.append(flight1)
list_flights.append(flight2)