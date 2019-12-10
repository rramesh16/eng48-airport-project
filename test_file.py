# Run tests here

from passengers_class import *
from plane_class import *
from flight_class import *

def test_passenger():
    new_passenger = Passenger('Joana Thomson', 'B343123')
    assert new_passenger.passport_no == 'B343123', 'New passenger not created. Make sure you have defined both the name and passport number.'
    new_passenger = Passenger('Brit Kuman', 'B13927')
    assert new_passenger.passport_no == 'B13927', 'New passenger not created. Make sure you have defined both the name and passport number.'

def test_plane():
    new_plane = Plane('BA005')
    assert new_plane.plane_number == 'BA005', 'Plane number not defined'

def test_flight_missing_info():
    new_flight = Flight()
    assert  isinstance(new_flight, Flight)

def test_flight_origin():
    origin = Flight.add_origin(Flight,'Chicago')
    assert origin == 'Chicago', 'Origin not defined'

def test_flight_destination():
    destination = Flight.add_destination(Flight,'New York')
    assert destination == 'New York', 'Destination not defined'

def test_flight_plane():
    flight_number = Flight.add_plane(Flight,'BA343123')
    assert flight_number == 'BA343123', 'Flight number not defined'

def test_flight_add_passenger():
    passenger_name = 'Joana Thomson'
    passport_no = 'BA343123'
    list_of_passengers.append(Flight(passenger_name, passport_no))
    assert list_of_passengers[-1].passengers == 'Joana Thomson', 'Passenger not added'



