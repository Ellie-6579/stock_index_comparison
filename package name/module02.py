##module02: Takes the log returns calculated in module01 and computes two risk metrics using historical simulation

import numpy as np

#daily var and cvar
#Calculate Value-at-Risk (VaR):
def calculate_var(log_returns, confidence_level=0.95):
    returns_array=np.array(log_returns)
    alpha=(1-confidence_level)*100 #convert confidence level to the tail percentile.  alpha=5 represents the worst 5% of trading days
    var=np.percentile(returns_array, alpha) #NumPy lines up all your historical log returns from worst to best and picks the exact number sitting at that 5th percentile mark. That number is your VaR cutoff
    
    return var

#On a typical day, our returns fluctuate. But looking at our historical worst-case scenarios, 5% of our days were worse than this specific percentage."

#Everything sitting worse than that cutoff line in your sorted data is what Module 2 then grabs to calculate your CVaR (average crash depth)!

#Calculate Conditional Value-at-Risk (CVaR) - expected shortfall
def calculate_cvar(log_returns, confidence_level=0.95):
    returns_array=np.array(log_returns)
    var = calculate_var(returns_array, confidence_level) #find the var threshold
    tail_losses = returns_array[returns_array <= var] #filter all returns that are worse or equal to the var threshold
    
    if len(tail_losses) == 0: #take avg of those extreme tail losses
        return var # Fallback safety check
        
    cvar = np.mean(tail_losses)
    
    return cvar

#some notes: The finance industry used to be reliant only to VaR as a measurement to measure the risk of a portfolio,asset,liability..
#VaR poorly measures tail risk
#VaR is a statistical measure that quantifies the potential loss for a given confidence level and time horizon
#Expected Shortfall: Is the avg of losses beyonf the VaR threshold for a given confidence level: addresses Vars limitations by capturing the severity of losses in the tail of the distribution and satisfying the propertirs if a coherent risk measure


def calculate_correlation(stock_returns, index_returns):
    #Calculate Correlation Coefficient [-1,1]
    correlation_matrix = np.corrcoef(stock_returns, index_returns)
    correlation = correlation_matrix[0, 1]
    return correlation

def calculate_beta(stock_returns, index_returns):
    #Calculate Beta: Covariance(Stock, Index) / Variance(Index)
    covariance_matrix = np.cov(stock_returns, index_returns)
    covariance = covariance_matrix[0, 1]
    market_variance = covariance_matrix[1, 1] # Variance of the benchmark index
    beta = covariance / market_variance
    return beta
