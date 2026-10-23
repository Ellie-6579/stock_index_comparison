
#Import libraries needed
import matplotlib.pyplot as plt
import numpy as np

#Import custom modules 
from stock_index_comparison.module01 import load_data, calculate_log_returns, calculate_annualized_volatility
from stock_index_comparison.module02 import calculate_var, calculate_cvar

#Load Data
apple_dates, apple_prices = load_data("data/Apple_Data.csv")
sp_dates, sp_prices = load_data("data/S&P500_Data.csv")
#Convert into arrays
apple_prices = np.array(apple_prices)
sp_prices = np.array(sp_prices)

#Calculate returns and risk metrics for Apple Stock:
apple_returns = calculate_log_returns(apple_prices)
apple_vol = calculate_annualized_volatility(apple_returns)
apple_var95 = calculate_var(apple_returns,0.95) 
apple_cvar95 = calculate_cvar(apple_returns,0.95) 
apple_var99 = calculate_var(apple_returns,0.99)
apple_cvar99 = calculate_cvar(apple_returns,0.99)
    
#Calculate returns and risk metrics for S&P 500 Index:
sp_returns = calculate_log_returns(sp_prices)
sp_vol = calculate_annualized_volatility(sp_returns)
sp_var95 = calculate_var(sp_returns,0.95)
sp_cvar95 = calculate_cvar(sp_returns,0.95)
sp_var99 = calculate_var(sp_returns,0.99)
sp_cvar99 = calculate_cvar(sp_returns,0.99)

#After calculating all the necessary metrics we will start building our report
# Stock to Index comparison
#I will use Matplotlib's OO approach to visualize the results
fig, axes = plt.subplots(3,1,figsize=(10,14)) #matplotlib creates a figure with subplot areas, handing them back inside a list called axes
ax_growth, ax_vol, ax_dist = axes #array unpacking

#Graph 1: Growth Trajectory (Rebased to 100)
#Normalize the starting price of both assets to 100 so they can be easily compared on the same scale from day zero. This way we can instantly see the percentage growth or loss over time.
apple_norm = (apple_prices / apple_prices[0]) * 100
sp_norm = (sp_prices / sp_prices[0]) * 100

ax_growth.plot(apple_norm, label='Apple Stock (AAPL)', color='blue')
ax_growth.plot(sp_norm, label='S&P 500 Index (SPY)', color='red')
ax_growth.set_title("Growth Trajectory Comparison (Rebased to 100)", fontweight='bold')
ax_growth.set_ylabel("Normalized Value")
ax_growth.set_xlabel("Trading Days")
ax_growth.grid()
ax_growth.legend()

#Graph 2: Annualized Volatility comparison
vol_labels = ['Annualized Volatility']
x_vol = np.arange(len(vol_labels))
ax_vol.bar(x_vol - 0.35/2, [apple_vol * 100], width=0.35, label='Apple (AAPL)', color='blue')
ax_vol.bar(x_vol + 0.35/2, [sp_vol * 100], width=0.35, label='S&P 500 (SPY)', color='red')
ax_vol.set_title("Asset Volatility Comparison", fontweight='bold')
ax_vol.set_ylabel("Volatility (%)")
ax_vol.set_xticks(x_vol)
ax_vol.set_xticklabels(vol_labels)
ax_vol.grid()
ax_vol.legend()

# Graph 3: Tail Risk - VaR and CVaR Comparison 
risk_labels = ['95% VaR', '99% VaR', '95% CVaR', '99% CVaR'] 
x_risk = np.arange(len(risk_labels)) #generate numeric positions for the four risk categories on the X-axis

apple_risks = [abs(apple_var95) * 100, abs(apple_var99) * 100, abs(apple_cvar95) * 100, abs(apple_cvar99) * 100] # VaR and CVaR represent losses, so they are mathematically negative: use abs()
sp_risks = [abs(sp_var95) * 100, abs(sp_var99) * 100, abs(sp_cvar95) * 100, abs(sp_cvar99) * 100]
width=0.35 #width of bars
#Plots the grouped side-by-side bars. Apple's bars are shifted slightly to the left, and the S&P 500's bars are shifted slightly to the right:
ax_dist.bar(x_risk - width/2, apple_risks, width=width, label='Apple (AAPL)', color='blue') 
ax_dist.bar(x_risk + width/2, sp_risks, width=width, label='S&P 500 (SPY)', color='red')
ax_dist.set_title("Tail Risk Comparison (VaR & CVaR)", fontweight='bold')
ax_dist.set_ylabel("Loss Magnitude (%)")
#Maps the numeric X positions (0, 1, 2, 3) directly to your text labels "risk_labels":
ax_dist.set_xticks(x_risk)
ax_dist.set_xticklabels(risk_labels)
ax_dist.grid()
ax_dist.legend()

plt.subplots_adjust(hspace=0.4, top=0.95, bottom=0.03)
plt.show()


