import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Arcobaleno1",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE zalando (Personid int NOT NULL AUTO_INCREMENT PRIMARY KEY, Tipologia VARCHAR(255), Marca VARCHAR(255), Prezzo int)")
