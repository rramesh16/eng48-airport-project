from db_passenger import *
from db_flight import *
from db_connect_oop import *

passenger_table = AirportPassenger()
flight_table = AirportFlights()

print("///Welcome to the Gathrow Aiport portal!///")

while True:
    print('Please choose an option from below:')
    print("1: Create a new passenger")
    print("2: List all flights")
    print("3: Add passenger to a flight")
    user_input = input("Please enter the option number...")

    if user_input == '1':
        print('creating a passenger')
        passenger_table.insert_passenger()

    elif user_input == '2':
        print('List all flights')
        flight_table.print_all()
        print('///End of flight list///')

    elif user_input == '3'
        