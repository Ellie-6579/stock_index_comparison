## Stock vs. Index Comparison project: 
The main goal of this project is to compare an individual stock (Apple) with a market index (S&P 500) to see how their prices grow and how much risk or volatility they carry.
Data Source: Downloaded from Investing.com chistorical daily data covering the dates from 01/01/2023 untill 17/10/2026.
Data Cleaning: Because the stock market is closed on weekends and holidays, some dates were missing. The CSV files were cleaned so both datasets match up and can be compared properly.
Columns Used: Only the Date and Price columns were used for this analysis.

## Module 1: Returns & Volatility##

-Log returns help track daily price changes smoothly. It makes it easier to calculate how much money goes up or down day-by-day.
We use log returns instead of normal percentage returns because they can be easily added together over time and handle compounding much more smoothly than normal percentages.

-Volatility measures how shaky the price swings are.
Daily volatility measures how much a price bounces around on a single day - that number is a small fraction. It is hard to judge how risky an investment is over the long term.So it is most useful if we annualize the volatility

## Module 2: Tail Risk (VaR & CVaR - nonparametric/historical) 

Value-at-Risk: A risk metric that answers the question: "What is the maximum expected loss under normal market conditions at a specific confidence level (95% or 99%)?". 

VaR poorly measures tail risk - this is why we need CVaR

Conditional Value-at-Risk: A more advanced and conservative downside risk metric. While VaR tells you the cutoff threshold for bad days, CVaR tells you the average severity of the losses on the absolute worst days that cross that threshold.

Note:
Before 2008, the financial industry relied heavily only on VaR. However, the 2008 crisis exposed the blind spot of VaR and so after 2008, regulators and risk managers turned to CVaR

## Demo
The script generates a visual report with three stacked charts: 
1. Growth Trajectory: Both assets start at 100 on Trading Day zero so you can easily see percentage growth or loss over time side-by-side.
Result: Apple experiences wider price swings and sharper drawdowns than the index, demonstrating the higher ups and downs of a single stock compared to a broad index.

2. Asset Volatility: Compares the overall price shakiness of Apple versus the S&P 500.
Result: Apple’s annualized volatility sits around 25%, whereas the S&P 500 sits around 15%. This shows that holding a single stock exposes an investor to significantly more year-round price swings than holding the market.

3. Tail Risk (VaR & CVaR): Uses positive loss percentages (using absolute values) to clearly show how much more downside risk Apple carries compared to the whole market.

Comparison of different confidence levels:
95% Confidence Level: Focuses on ordinary bad days. It means that 95 out of 100 trading days, your loss will not go past this number (or you have a 5% chance of exceeding it).
99% Confidence Level: Focuses on extreme crash days. It looks deeper into the tail, meaning 99 out of 100 trading days your loss stays within this boundary (or you have only a 1% chance of hitting a loss this severe).
=>Moving from 95% to 99% confidence increases loss severity for both assets as we move deeper into crash territory.

Apple's downside losses are roughly double those of the S&P 500, showing that individual stocks suffer far heavier tail-risk losses during market sell-offs.

## Result
The question: Am I getting compensated with enough growth to justify taking on higher volatility, deeper tail-risk, and amplified market sensitivity compared to just buying the whole index?
Answer: No, for this specific timeframe, Apple (AAPL) did not adequately compensate investors for the extra risk it carried compared to just buying the S&P 500 (SPY).




