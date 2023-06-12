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

lista = []

for x in myresult:
  lista.append(x)
  print(x)

for y in lista:
  print(y)