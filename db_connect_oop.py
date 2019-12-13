import pyodbc

class MSDBConnnection():
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Airport'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                          + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.docker_Northwind.cursor()

    def __sql_query(self, sql_query):       #Encapsulated: this is private
        return self.cursor.execute('SELECT', sql_query)