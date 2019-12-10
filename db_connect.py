import pyodbc

# Variables to connect
server = 'localhost,1433'
database = 'Airport'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_Airport = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                  +server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making the cursor
cursor = docker_Airport.cursor()

# Executing some SQL commands
cursor.execute("SELECT * FROM Passengers")

# Fetching data from the executed SQL command and printing
row = cursor.fetchone()
print(row)


