from db_connect_oop import *

class AirportFlights(MSDBConnnection):
    def __init__(self):
        super().__init__()
        self.table = 'Flight'

    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all(self):
        query = "SELECT * FROM Flight"
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f" ID: {record.ID} , Plane ID: {record.PlaneID} , Origin: {record. Origin}, Destination: {record.Destination}")

    def add_passenger_to_flight(self):
        query1 = "SELECT * FROM Flight"
        data = self.__sql_query(query1)
        while True:
            record1 = data.fetchone()
            if record1 is None:
                break
            print(
                f" ID: {record1.ID} , Plane ID: {record1.PlaneID} , Origin: {record1.Origin}, Destination: {record1.Destination}")
        choose_flight = input('Please enter the id number of the flight you want to modify:')

        query2 = "SELECT * FROM Passengers"
        data = self.__sql_query(query2)
        while True:
            record2 = data.fetchone()
            if record2 is None:
                break
            print(
                f" ID: {record2.ID} , First Name: {record2.FirstName} , Last Name: {record2.LastName}, Passport Number: {record2.PassportNo}")
        choose_passenger = input('Please enter the id number of the passenger you want to add:')

        if choose_flight == '1':
            query = f"INSERT INTO Flight(PlaneID, Origin, Destination, PassengerID) VALUES ('1', 'London', 'Chicago', '{choose_passenger}'})"
            result = self.cursor.execute(query)
            self.cursor.commit()
            print('All done. Thank you!')

        elif choose_flight == '2':
            query = f"INSERT INTO Flight(PlaneID, Origin, Destination, PassengerID) VALUES ('2', 'Sydney', 'Dubai', '{choose_passenger}'})"
            result = self.cursor.execute(query)
            self.cursor.commit()
            print('All done. Thank you!')



