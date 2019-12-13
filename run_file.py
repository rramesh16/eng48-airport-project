from Human_class import *
from passengers_class import *
from flight_class import *
from plane_class import *


print("///Welcome to the Gathrow Aiport portal!///")
while True:
    import time
    print('Please choose an option from below:')
    print("1: Create a new passenger")
    print("2: Add a new plane to the system")
    print("3: List all flights")
    print("4: Add passenger to a flight")
    user_input = input("Please enter the option number...")

    if user_input == '1':
        name = input("Enter passenger's full name:")
        passport_no = input("Enter passenger's passport number:")
        new_passenger = Passenger(name, passport_no)
        print('Passenger:',new_passenger.full_name,',', new_passenger.passport_no, 'is added to the system.')
        # list_of_passengers.append(Passenger(name, passport_no))
        print("Please choose another option or enter 'end' to exit.")
    elif user_input == 'end':
        break

    elif user_input == '2':
        plane_no = input("Please enter the assigned number of the plane:")
        new_plane_number = Plane(plane_no)
        print('Plane:',new_plane_number.plane_number, 'is now added to the system.')
        print("Please choose another option or enter 'end' to exit.")


    elif user_input == '3':
        print('/// List of Flights///')
        for flight in list_flights:
            print('Origin:', flight.origin, ', Destination:', flight.destination, ', Plane:', flight.plane )
        print('///End of list///')
        print("Please choose another option or enter 'end' to exit.")

    elif user_input == '4':
        counter = 1
        for flight in list_flights:
            print(counter, '- Origin:', flight.origin, ', Destination:', flight.destination, ', Plane:', flight.plane)
            counter += 1
        flight_to_add_passenger = input('Choose the flight you want to modify:')
        counter = 1
        for passenger in list_of_passengers:
            print(counter, '- Full Name:', passenger.full_name, ', Passport Number:', passenger.passport_no)
            counter += 1
        passenger_to_be_added = input('Choose a passenger from the list above:')
        if flight_to_add_passenger == '1':
                flight1.add_passengers(list_of_passengers[int(passenger_to_be_added)-1].passport_no)
        elif flight_to_add_passenger == '2':
                flight2.add_passengers(list_of_passengers[int(passenger_to_be_added)-1].passport_no)
        print('Passenger added to the chosen flight')
        print("Please choose another option or enter 'end' to exit.")

    else:
        print("Sorry, I didn't get that. Please try again!")
        time.sleep(2.5)

print('Thanks for using Gathrow Airport portal!')










