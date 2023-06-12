import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Arcobaleno1",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM zalando")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)