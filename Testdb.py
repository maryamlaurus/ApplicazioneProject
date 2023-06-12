import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Arcobaleno1"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE ciao")