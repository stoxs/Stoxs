import pandas as pd
import mysql.connector
import datetime

# returns the table dataframe for the given company from startDate to endDate
def getcompanytable (companySymbol, marketSymbol, startDate, endDate):
  # check for date bounds
  db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="data1000",
      database=marketSymbol
  )

  cursor = db.cursor()
  now = datetime.datetime.now()
  now.date()

  sqll = "SELECT date, openp, high, low, closep, netchg, perchg, volume FROM "+companySymbol+"0 WHERE date >= \'" + startDate + "\' AND date <= \'" + endDate + "\'"

  cursor.execute(sqll)
  result = cursor.fetchall()
  p = pd.DataFrame(data = result)
  p.columns = ["Date", "Open", "High", "Low", "Close", "Net_chg", "Per_chg", "Volume"]

  return p

# exports the company table as a csv file to a local path
def export_csv(companySymbol, marketSymbol, startDate, endDate):
    path = input("Enter folder path: ")
    df = getcompanytable(companySymbol, marketSymbol, startDate, endDate)
    df.to_csv(path + marketSymbol + '-' + companySymbol + '.csv', index=False)


