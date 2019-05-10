from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import datetime

path = input("Enter folder path: ")

url_page = ['http://www.wsj.com/mdc/public/page/2_3024-AMEX.html?mod=topnav_2_3002',
            'http://www.wsj.com/mdc/public/page/2_3024-NYSE.html?mod=topnav_2_3024',
            'http://www.wsj.com/mdc/public/page/2_3024-Nasdaq.html',
            'http://www.wsj.com/mdc/public/page/2_3024-SCAP.html?mod=topnav_2_3002']

big_data = []

for element in url_page:
    page = urlopen(element)

    soup = BeautifulSoup(page, 'html.parser')

    div = soup.find('div', attrs={'id': 'column0'})
    tables = div.find_all('table', attrs={'bgcolor': '#cccccc'})

    name = []
    symbol = []
    opn = []
    high = []
    low = []
    close = []
    netchg = []
    perchg = []
    volume = []
    weekhgh = []
    weeklow = []
    div = []
    yld = []
    pe = []
    ytd = []

    for table in tables:
        rows = table.find_all('tr', attrs={'class': 'p12'})
        for row in rows:
            data = row.find_all('td')
            name.append(data[0].getText().strip('\xa0'))
            symbol.append(data[1].getText().strip('\xa0'))
            opn.append(data[2].getText().strip('\xa0'))
            high.append(data[3].getText().strip('\xa0'))
            low.append(data[4].getText().strip('\xa0'))
            close.append(data[5].getText().strip('\xa0'))
            netchg.append(data[6].getText().strip('\xa0'))
            perchg.append(data[7].getText().strip('\xa0'))
            volume.append(data[8].getText().strip('\xa0'))
            weekhgh.append(data[9].getText().strip('\xa0'))
            weeklow.append(data[10].getText().strip('\xa0'))
            div.append(data[11].getText().strip('\xa0'))
            yld.append(data[12].getText().strip('\xa0'))
            pe.append(data[13].getText().strip('\xa0'))
            ytd.append(data[14].getText().strip('\xa0'))

    dictionary = {'Name': name, 'Symbol': symbol, 'Open': opn, 'High': high, 'Low': low, 'Close': close,
                  'Net Change': netchg, '% Change': perchg, 'Volume': volume, '52 Week High': weekhgh,
                  '52 Week Low': weeklow, 'Div': div, 'Yield': yld, 'PE': pe, "YTD % Change": ytd}
    dataframe = pd.DataFrame(dictionary)

    big_data.append(dataframe)


now = datetime.datetime.now()
date = (str(now.day) + '_' + str(now.month) + '_' + str(now.year))

filename = [date + 'AMEX' + '.csv', date + 'NYSE' + '.csv', date + 'NASDAQ' + '.csv', date + 'SCAP' + '.csv']

for i in range(4):
    big_data[i].to_csv(path+'\\'+filename[i], index=False)
