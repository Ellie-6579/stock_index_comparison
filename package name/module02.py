##module02: Takes the log returns calculated in module01 and computew two risk metrics using historical simulation

import numpy as np

#Calculate Value-at-Risk (VaR):
def calculate_var(log_returns, confidence_level=0.95):
    returns_array=np.array(log_returns)
    alpha=(1-confidence_level)*100 #convert confidence level to the tail percentile.  alpha=5 represents the worst 5% of trading days
    var=np.percentile(returns_array, alpha) #NumPy lines up all your historical log returns from worst to best and picks the exact number sitting at that 5th percentile mark. That number is your VaR cutoff
    return var

#Calculate Conditional Value-at-Risk (CVaR)
def calculate_cvar(log_returns, confidence_level=0.95):
    returns_array=np.array(log_returns)
    var = calculate_var(returns_array, confidence_level) #find the var threshold
    tail_losses = returns_array[returns_array <= var] #filter all returns that are worse or equal to the var threshold
    
    if len(tail_losses) == 0: #take avg of those extreme tail losses
        return var # Fallback safety check
        
    cvar = np.mean(tail_losses)
    
    return cvar



