from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector
import datetime
import convert

url_page = ['http://www.barrons.com/mdc/public/page/9_3024-AMEX.html?mod=bol_topnav_9_3024',
            'http://www.barrons.com/mdc/public/page/9_3024-NYSE.html?mod=bol_topnav_9_3024',
            'http://www.barrons.com/mdc/public/page/9_3024-Nasdaq.html?mod=bol_topnav_9_3024',
            'http://www.barrons.com/mdc/public/page/9_3024-SCAP.html?mod=bol_topnav_9_3024']


databases = ["AMEX", "NYSE", "NASDAQ_GLOBAL", "NASDAQ_CAPITAL"]


def scrape_to_database(element, db_name):
    page = urlopen(element)

    soup = BeautifulSoup(page, 'html.parser')

    div = soup.find('div', attrs={'id': 'column0'})
    tables = div.find_all('table', attrs={'bgcolor': '#cccccc'})

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="data1000",
        database=db_name
    )

    cursor = db.cursor()


    for table in tables:
        rows = table.find_all('tr', attrs={'class': 'p12'})
        for row in rows:
            data = row.find_all('td')
            name = data[0].getText().strip('\xa0')
            symbol = data[1].getText().strip('\xa0')

            if '%' in symbol:
                continue
            if '.' in symbol:
                continue

            opn = convert.check(data[2].getText().strip('\xa0'))
            high = convert.check(data[3].getText().strip('\xa0'))
            low = convert.check(data[4].getText().strip('\xa0'))
            close = convert.check(data[5].getText().strip('\xa0'))
            netchg = convert.check(data[6].getText().strip('\xa0'))
            perchg = convert.check(data[7].getText().strip('\xa0'))
            volume = convert.check(data[8].getText().strip('\xa0').replace(',', ''))
            weekhgh = convert.check(data[9].getText().strip('\xa0'))
            weeklow = convert.check(data[10].getText().strip('\xa0'))
            div = convert.check(data[11].getText().strip('\xa0'))
            yld = convert.check(data[12].getText().strip('\xa0'))
            pe = convert.check(data[13].getText().strip('\xa0'))
            ytd = convert.check(data[14].getText().strip('\xa0'))

            now = datetime.datetime.now()
            now.date()

            sql = "INSERT INTO " + symbol + \
                  "0 (date, openp, high, low, closep, netchg, perchg, volume, " \
                  "weekhigh, weeklow, divd, yield, pe, ytd) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (now, opn, high, low, close, netchg, perchg, volume, weekhgh, weeklow, div, yld, pe, ytd)
            try:
                cursor.execute(sql, val)
            except:
                continue
            db.commit()

for i in range(4):
    scrape_to_database(url_page[i], databases[i])