import mysql.connector
import csv
from datetime import datetime


# Databases: NYSE, AMEX, NASDAQ_CAPITAL, NASDAQ_GLOBAL
# CSV Filenames: \NYSE, \AMEX, \SCAP, \NASDAQ ending with date (YYYY-MM-DD)


# date is a substring \DD-MM-YYYY

def get_date(s):
    part1 = s.partition('\\')
    part2 = part1[2].partition('\\')
    date_string = part2[0]
    d = datetime.strptime(date_string, '%d_%m_%Y')
    d.date()
    return d


def check(x):
    if '...' in x:
        return 0
    else:
        return float(x)


# 'file_path' and "db-name"

def csv_to_database(file_path, db_name):

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="data1000",
        database=db_name
    )

    cursor = db.cursor()

    with open(file_path, 'r') as csvFile:
        r = csv.reader(csvFile)
        ir = iter(r)
        next(ir)
        for row in ir:
            sym = row[1]
            if '%' in sym:
                continue
            if '.' in sym:
                continue

            # get date
            date = get_date(file_path)

            opn = check(row[2])
            high = check(row[3])
            low = check(row[4])
            close = check(row[5])
            netchg = check(row[6])
            perchg = check(row[7])
            volume = check(row[8].replace(',', ''))
            weekhgh = check(row[9])
            weeklow = check(row[10])
            div = check(row[11])
            yld = check(row[12])
            pe = check(row[13])
            ytd = check(row[14])
            sql = "INSERT INTO " + sym + \
                "0 (date, openp, high, low, closep, netchg, perchg, volume, " \
                "weekhigh, weeklow, divd, yield, pe, ytd) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (date, opn, high, low, close, netchg, perchg, volume, weekhgh, weeklow, div, yld, pe, ytd)

            try:
                cursor.execute(sql, val)
            except:
                continue
            db.commit()

    csvFile.close()

# values (date, openp, high, low, closep, netchg, perchg, volume, weekhigh, weeklow, divd, yield, pe, ytd)"
# company symbol ends with 0 for table names
# table company has the name and symbol
