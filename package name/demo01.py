

#Import libraries needed
import matplotlib.pyplot as plt
import numpy as np

#Import custom modules 
from module01 import load_data, calculate_log_returns, calculate_annualized_volatility
from module02 import calculate_var, calculate_cvar, calculate_beta, calculate_correlation

#Load Data
apple_dates, apple_prices = load_data("Apple_Data.csv")
sp_dates, sp_prices = load_data("S&P500_Data.csv")
    
#Compute returns & risk metrics for Apple Stock:
apple_returns = calculate_log_returns(apple_prices)
apple_vol = calculate_annualized_volatility(apple_returns)
apple_var95 = calculate_var(apple_returns, 0.95) #the default 95%
apple_cvar95 = calculate_cvar(apple_returns, 0.95)
apple_var99 = calculate_var(apple_returns, 0.99)
apple_cvar99 = calculate_cvar(apple_returns, 0.99)
    
#Compute returns & risk metrics for S&P 500
sp_returns = calculate_log_returns(sp_prices)
sp_vol = calculate_annualized_volatility(sp_returns)
sp_var95 = calculate_var(sp_returns, 0.95)
sp_cvar95 = calculate_cvar(sp_returns, 0.95)
sp_var99 = calculate_var(sp_returns, 0.99)
sp_cvar99 = calculate_cvar(sp_returns, 0.99)
    
#Compute relative metrics (Beta & Correlation)
correlation = calculate_correlation(apple_returns, sp_returns)
beta = calculate_beta(apple_returns, sp_returns)
#Calculates Beta and Correlation between an individual stock and a market index.

#After calculating all the necessary metrics we will start building our report - Stock to Index comparison:
#I will use Matplotlib's OO approach
fig, axes = plt.subplots(1,3,figsize(10,13)) #matplotlib creates a figure with subplot areas, handing them back inside a list called axes
ax_metrics, ax_price, ax_dist = axes #array unpacking

#Bar Chart: Comparative Risk Metrics Bar Chart We group the percentage-based risk metrics together for a direct visual comparison
metric_labels = ['Ann. Volatility', '95% Daily VaR', '99% Daily VaR', '95% CVaR', '99% CVaR']
#Convert the results into percentages
apple_metrics = [apple_vol * 100, abs(apple_var95 * 100), abs(apple_var99 * 100), abs(apple_cvar95 * 100), abs(apple_cvar99 * 100)]
sp_metrics = [sp_vol * 100, abs(sp_var95 * 100), abs(sp_var99 * 100), abs(sp_cvar95 * 100), abs(sp_cvar99 * 100)]
# VaR and CVaR represent losses, so they are mathematically negative: use abs()

x = np.arange(len(metric_labels)) 

# Plot side-by-side bars
rects1 = ax_metrics.bar(x - width/2, apple_metrics, width=0.35, label='Apple (AAPL)', color='blue')
rects2 = ax_metrics.bar(x + width/2, sp_metrics, width=0.35, label='S&P 500 (SPY)', color='red')
    
ax_metrics.set_title("Risk Metrics Comparison (Beta: {beta:.2f} | Correlation: {correlation:.2f})")
ax_metrics.set_ylabel("Percentage (%) / Magnitude")
ax_metrics.set_xticks(x)
ax_metrics.set_xticklabels(metric_labels)
ax_metrics.grid()
ax_metrics.legend()

plt.show()



    

