from db_connect_oop import *


class AirportPassenger(MSDBConnnection):
    def __init__(self):
        super().__init__()
        self.table = 'Passengers'

    def __sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def insert_passenger(self):
        passenger_firstname = input('Please enter the passenger first name:')
        passenger_lastname = input('Please enter the passenger last name:')
        passenger_passportNo = input('Please enter the passenger passport number:')
        query =f"INSERT INTO Passengers(FirstName, LastName, PassportNo) VALUES ('{passenger_firstname}', '{passenger_lastname}', '{passenger_passportNo}')"
        result = self.cursor.execute(query)
        self.cursor.commit()
        print ('All done. Thank you!')

