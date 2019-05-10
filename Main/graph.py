import matplotlib.pyplot as plt
import pandas as pd
from get_df import *

def plot_price(companySymbol, marketSymbol):
	df = getcompanytable(companySymbol, marketSymbol, '2019-04-01', '2019-05-08')
	df.Open = pd.to_numeric(df.Open)
	df.Close = pd.to_numeric(df.Close)
	ax = plt.gca()

	df.plot(kind='line',x='Date',y='Open',ax=ax)
	df.plot(kind='line',x='Date',y='Close', color='red', ax=ax)

	plt.show()


def plot_netchg(companySymbol, marketSymbol):
	df = getcompanytable(companySymbol, marketSymbol, '2019-04-01', '2019-05-08')
	df.Net_chg = pd.to_numeric(df.Net_chg)
	ax = plt.gca()

	df.plot(kind='line',x='Date',y='Net_chg',ax=ax)

	plt.show()


def plot_perchg(companySymbol, marketSymbol):
	df = getcompanytable(companySymbol, marketSymbol, '2019-04-01', '2019-05-08')
	df.Per_chg = pd.to_numeric(df.Per_chg)
	ax = plt.gca()

	df.plot(kind='line',x='Date',y='Per_chg',ax=ax)

	plt.show()


def plot_volume(companySymbol, marketSymbol):
	df = getcompanytable(companySymbol, marketSymbol, '2019-04-01', '2019-05-08')
	df.Volume = pd.to_numeric(df.Volume)
	ax = plt.gca()

	df.plot(kind='line',x='Date',y='Volume',ax=ax)

	plt.show()


