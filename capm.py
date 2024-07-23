import yfinance as yf
import pandas as pd
import datetime
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Define the stock ticker and the index ticker
stock_ticker = "BARC.L"  # Example: Barclays PLC
index_ticker = "^FTSE"   # FTSE 100

# Define the time period
start_date = "2010-01-01"
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Fetch stock data
stock_data = yf.download(stock_ticker, start=start_date, end=end_date)
index_data = yf.download(index_ticker, start=start_date, end=end_date)

# Display the data
print(stock_data.head())
print(index_data.head())

# Calculate monthly returns
stock_data['Monthly Return'] = stock_data['Adj Close'].resample('M').ffill().pct_change()
index_data['Monthly Return'] = index_data['Adj Close'].resample('M').ffill().pct_change()

# Drop NA values
stock_data.dropna(subset=['Monthly Return'], inplace=True)
index_data.dropna(subset=['Monthly Return'], inplace=True)

# Display the processed data
print(stock_data[['Monthly Return']].head())
print(index_data[['Monthly Return']].head())



# Align the data
data = pd.concat([stock_data['Monthly Return'], index_data['Monthly Return']], axis=1)
data.columns = ['Stock Return', 'Market Return']
data.dropna(inplace=True)

# Add a constant to the independent variable
X = sm.add_constant(data['Market Return'])
y = data['Stock Return']

# Perform linear regression
model = sm.OLS(y, X).fit()
beta = model.params['Market Return']
print(f"The beta of the stock is: {beta}")

# Define the risk-free rate and market return
risk_free_rate = 0.01  # Example: 1%
market_return = index_data['Monthly Return'].mean() * 12  # Annualize the monthly return

# Calculate the expected return using CAPM
expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
print(f"The expected return of the stock is: {expected_return}")


# Plot stock's historical returns against market returns
plt.figure(figsize=(10, 6))
sns.regplot(x='Market Return', y='Stock Return', data=data)
plt.title(f'{stock_ticker} Returns vs. {index_ticker} Returns')
plt.xlabel('Market Return')
plt.ylabel('Stock Return')
plt.show()

# Plot risk-return scatter plot for the portfolio
portfolio_data = pd.DataFrame({
    'Stock': [stock_ticker],
    'Beta': [beta],
    'Expected Return': [expected_return]
})

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Beta', y='Expected Return', data=portfolio_data, s=100)
plt.title('Risk-Return Scatter Plot')
plt.xlabel('Beta')
plt.ylabel('Expected Return')
plt.axhline(y=risk_free_rate, color='r', linestyle='--')
plt.show()

# Display the Security Market Line (SML)
betas = [0, 1.0, 2.0]
sml_returns = [risk_free_rate + b * (market_return - risk_free_rate) for b in betas]

plt.figure(figsize=(10, 6))
sns.lineplot(x=betas, y=sml_returns, marker='o')
plt.scatter(portfolio_data['Beta'], portfolio_data['Expected Return'], color='red', s=100)
plt.title('Security Market Line (SML)')
plt.xlabel('Beta')
plt.ylabel('Expected Return')
plt.axhline(y=risk_free_rate, color='r', linestyle='--')
plt.show()

# Sensitivity analysis by varying the risk-free rate and market return
varying_rf_rates = [0.005, 0.01, 0.015]  # Example: 0.5%, 1%, 1.5%
varying_market_returns = [0.06, 0.08, 0.10]  # Example: 6%, 8%, 10%

sensitivity_results = []

for rf in varying_rf_rates:
    for mr in varying_market_returns:
        exp_return = rf + beta * (mr - rf)
        sensitivity_results.append({
            'Risk-Free Rate': rf,
            'Market Return': mr,
            'Expected Return': exp_return
        })

sensitivity_df = pd.DataFrame(sensitivity_results)
print(sensitivity_df)

# Generate a detailed report (example)
report = f"""
CAPM Analysis Report
=====================
Stock Ticker: {stock_ticker}
Market Index: {index_ticker}
Analysis Period: {start_date} to {end_date}

Beta Calculation
----------------
The beta of the stock is: {beta}

Expected Return Calculation
---------------------------
Risk-Free Rate: {risk_free_rate}
Market Return: {market_return}
Expected Return: {expected_return}

Sensitivity Analysis
--------------------
{tabulate(sensitivity_df, headers='keys', tablefmt='psql')}
"""

print(report)
