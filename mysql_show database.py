#import mysql
import mysql.connector as conn

#establishing the connection
mydb = conn.connect(
    host="localhost",
    user="root",
    passwd="password123", #enter your own password
)

mycursor = mydb.cursor()
#creating a cursor

#command to show databases
mycursor.execute("SHOW DATABASES ")

#loop through all databases to print them one by one. python will print them as tuple
for database in mycursor:
    print(database)





