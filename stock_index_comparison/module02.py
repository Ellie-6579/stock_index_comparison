#module02

import numpy as np

#Calculate Value-at-Risk (VaR):
def calculate_var(log_returns, confidence_level=0.95): #set the default value of confidence interval to be 0.95
    returns_array = np.array(log_returns)
    alpha = (1-confidence_level)*100 #convert confidence level to the tail percentile.  alpha=5 represents the worst 5% of trading days
    var = np.percentile(returns_array, alpha) #numpy lines up all historical log returns from worst to best and picks the exact number sitting at that 5th percentile mark. That number is the VaR cutoff
    
    return var

#Calculate Conditional Value-at-Risk (CVaR) - expected shortfall:
def calculate_cvar(log_returns, confidence_level=0.95):
    returns_array=np.array(log_returns)
    var = calculate_var(returns_array, confidence_level) #finds the var threshold: Any return worse than this threshold is considered part of the extreme tail
    tail_losses = returns_array[returns_array <= var] #filter all returns that are worse or equal to the var threshold
    
    if len(tail_losses) == 0: #safety check
        return var
        
    cvar = np.mean(tail_losses) #take avg of those extreme tail losses
    
    return cvar

#Ignore:

#Calculate correlation of the Apple Stock and the S&P500 Index:
#def calculate_correlation(stock_returns, index_returns):
##Calculate Correlation Coefficient [-1,1]
#correlation_matrix = np.corrcoef(stock_returns, index_returns)
#correlation = correlation_matrix[0, 1]
#return correlation

#Calculate Beta:
#def calculate_beta(stock_returns, index_returns):
##Calculate Beta: Covariance(Stock, Index) / Variance(Index)
#covariance_matrix = np.cov(stock_returns, index_returns)
#covariance = covariance_matrix[0, 1]
#market_variance = covariance_matrix[1, 1] # Variance of the benchmark index
# beta = covariance / market_variance
# return beta
