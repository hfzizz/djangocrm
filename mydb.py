import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")
