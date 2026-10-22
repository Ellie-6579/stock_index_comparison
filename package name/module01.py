##module01: Calculate Volatility to measure general day-to-day risk
#Historical VaR and CVaR (also known as empirical or non-parametric VaR/CVaR)!

import csv 
import math
import numpy as np

#Reading the csv dataset containing 'Date' and 'Price' columns and returns lists of dates and prices
def load_data(filepath):
    dates=[] #start with empty lists to hold our data
    prices=[] #represents the closing price of the stock

    with open(filepath, mode='r') as file:
        reader=csv.DictReader(file) #treats the first row of the csv as header names
        for row in reader: #now can call rows by their name
            dates.append(row['Date'])
            prices.append(float(row['Price']))
    return dates, prices

#Calculating Log Returns:
def calculate_log_returns(prices):
    prices_array=np.array(prices) #convert the list of prices into a numpy array 
    log_returns=np.log(prices_array[1:] / prices_array[:-1])  #array slicing for faster results. we get the growth factor Pt/Pt-1 for every single day
    return log_returns

#Calculate annualized volatility: why needed ???
def calculate_annualized_volatility(log_returns):
    daily_std=np.std(log_returns, ddof=1) #ddof=1:Because the 4 years of stock data is not the entire history of the stock market we will use sample standard deviation instead of population st.dev. ddof means degrees of freedom and when equal to 0 is the population and when equal to 1 is the sample.
    annualized_vol=daily_std*math.sqrt(252)
    return annualized_vol
     
#Daily volatility numbers are very small.Looking at that raw number doesn't immediately tell you if an asset is risky or stable. That's why you annualize it.
####################################Theory?
## High Volatility Predicts Deep Tails
#While they measure different things, they are deeply connected. An asset with high annualized volatility almost always has wider, deeper VaR and CVaR thresholds.

#"Am I getting compensated with enough growth to justify taking on higher volatility, deeper tail-risk, and amplified market sensitivity compared to just buying the whole index?"