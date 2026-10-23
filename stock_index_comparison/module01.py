#module01
import csv
import math
import numpy as np
import csv

#Reading the csv dataset containing 'Date' and 'Price' columns and returns lists of dates and prices
def load_data(filepath):
    dates=[] #start with empty lists to hold our data
    prices=[] #represents the closing price of the stock

    with open(filepath, mode='r',encoding='utf-8-sig') as file:
        reader=csv.DictReader(file) #treats the first row of the csv as header names
        for row in reader: #now can call rows by their name
            dates.append(row['Date'])
            prices.append(float(row['Price']))
    return dates, prices

#Calculate Log Returns:
def calculate_log_returns(prices):
    prices_array=np.array(prices) #convert the list of prices into a numpy array 
    log_returns=np.log(prices_array[1:] / prices_array[:-1])  #array slicing for faster results. we get the growth factor Pt/Pt-1 for every single day
    return log_returns

#Calculate annualized volatility:
def calculate_annualized_volatility(log_returns):
    daily_std=np.std(log_returns, ddof=1) #ddof=1:Because the 4 years of stock data is not the entire history of the stock market we will use sample standard deviation instead of population st.dev - ddof means degrees of freedom and when equal to 0 represents the population and when equal to 1 represents the sample.
    annualized_vol=daily_std*math.sqrt(252)
    return annualized_vol
     
