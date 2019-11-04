#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:54:51 2019
This file contains all code to parse the closing prices of the DAX 30
constituents from yahoo.finance

@author: julianwossner
"""
# Code found on 
#https://pythonprogramming.net/sp500-company-price-data-python-programming-for-finance/?completed=/sp500-company-list-python-programming-for-finance/


# Import packages
import bs4 as bs
import datetime as dt
import os
import pandas_datareader as data
import pickle
import requests
import yfinance as yf


# Define Function to parse tickers of SP500 companies
def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)
        
    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
        
    return tickers

# tickers = str(save_sp500_tickers()).replace("\\n","") # Get tickers
tickers = save_sp500_tickers()
tickers = [s.replace("\n","") for s in tickers]
# Define start and end data
start_date = '2015-01-01'
end_date =  '2019-09-30'

SP500_data = data.DataReader(tickers, 'yahoo', start_date, end_date)
SP500_close = SP500_data["Close"]   
# Save as .csv file
SP500_close.to_csv("SP500_price_data_15.csv")

tickers = save_sp500_tickers()
tickers = [s.replace("\n","") for s in tickers]

# Define start and end data
start_date = '2000-01-01'
end_date =  '2019-09-30'

SP500_data = data.DataReader(tickers, 'yahoo', start_date, end_date)
SP500_close = SP500_data["Close"]   
# Save as .csv file
SP500_close.to_csv("SP500_price_data_00.csv")