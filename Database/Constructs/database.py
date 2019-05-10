import mysql.connector


db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "data1000"
)

cursor = db.cursor()

cursor.execute("SHOW DATABASE")


for x in cursor:
  print(x)