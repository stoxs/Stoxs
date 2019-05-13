import mysql.connector
import csv


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="data1000",
  database= "NASDAQ_CAPITAL"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE COMPANY (name VARCHAR(100), symbol VARCHAR(6) PRIMARY KEY)")

filepath = '/Users/user1/Desktop/WSJ/\\17_4_2019\\SCAP.csv'

with open(filepath, 'r') as csvFile:
  r = csv.reader(csvFile)
  ir = iter(r)
  next(ir)
  for row in ir:
    symbol = row[1]
    if '%' in symbol:
      continue
    if '.' in symbol:
      continue
    sql = "INSERT INTO COMPANY (name, symbol) VALUES (%s, %s)"
    name = row[0]
    val = (name, symbol);
    cursor.execute(sql, val)
    db.commit()


csvFile.close()
