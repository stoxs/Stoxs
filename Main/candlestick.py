from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.pyplot import subplots, draw
from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt
from get_df import *


def candlestick(companySymbol, marketSymbol):
    data = getcompanytable(companySymbol, marketSymbol, "2019-04-01", "2019-05-08")

    # drop the date index from the dateframe
    data.reset_index(inplace = True)

    # convert the datetime64 column in the dataframe to 'float days'
    data.Date = mdates.date2num(data.Date)

    # make an array of tuples in the specific order needed
    dataAr = [tuple(x) for x in data[['Date', 'Open', 'Close', 'High', 'Low']].to_records(index=False)]

    # construct and show the plot
    fig = plt.figure()
    ax1 = plt.subplot(1,1,1)
    candlestick_ohlc(ax1, dataAr, colorup = "black", colordown = "red")
    ax1.xaxis_date()
    ax1.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()


