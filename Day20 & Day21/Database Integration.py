import mysql.connector
import getpass

dbdetails = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = getpass.getpass() #input("Enter the DB password:")
)

cursorpoint = dbdetails.cursor()
#cursorpoint.execute("SHOW DATABASES")
cursorpoint.execute("CREATE DATABASE PythonApp")
#cursorpoint.execute("DROP DATABASE PythonApp")

#for x in cursorpoint:
#  print(x)

print("**************************************")

dbdetails = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = getpass.getpass(),
  database = "PythonApp"
)

try:
    cursorpoint = dbdetails.cursor()
    cursorpoint.execute("CREATE TABLE SERVICE_DETAILS (name VARCHAR(50), description VARCHAR(50), status VARCHAR(50))")
    #cursorpoint.execute("SELECT * FROM SERVICE_DETAILS")
    #myresult = cursorpoint.fetchall()
#    print(myresult)
    #for x in myresult:
    #    print(x)
except:
    print("Error Occured!")
finally:
    cursorpoint.close()
