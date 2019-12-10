from passengers_class import *
from plane_class import *
class Flight():
    def __init__(self, passenger = None, passport_number = None):
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
