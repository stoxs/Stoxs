import mysql.connector
import csv

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="data1000",
  database= "NASDAQ_CAPITAL"
)


cursor = db.cursor()

filepath = '/Users/user1/Desktop/WSJ/\\17_4_2019\\SCAP.csv'

with open(filepath, 'r') as csvFile:
    r = csv.reader(csvFile)
    ir = iter(r)
    next(ir)
    for row in ir:
        sym = row[1]
        if '%' in sym:
            continue
        if '.' in sym:
            continue
        sql = "CREATE TABLE " + sym + "0" + \
        " (date DATE NOT NULL, " + \
        "openp DECIMAL(10, 2), " + \
        "high DECIMAL(10, 2), " + \
        "low DECIMAL(10, 2), " + \
        "closep DECIMAL(10, 2), " + \
        "netchg DECIMAL(10, 2), " + \
        "perchg DECIMAL(10, 2), " + \
        "volume DECIMAL(15, 0), " + \
        "weekhigh DECIMAL(10, 2), " + \
        "weeklow DECIMAL(10, 2), " + \
        "divd DECIMAL(10, 2), " + \
        "yield DECIMAL(10, 2), " + \
        "pe DECIMAL(10, 2), " + \
        "ytd DECIMAL(10, 2), " + \
        "PRIMARY KEY(date))"
        cursor.execute(sql)




csvFile.close()

# values (date, openp, high, low, closep, netchg, perchg, volume, weekhigh, weeklow, divd, yield, pe, ytd)"
# company symbol ends with 0 for table names
# table company has the name and symbol
