# Comprehensive-CAPM-Analysis-Tool-for-UK-Stocks-in-Python
I developed a Python-based tool for comprehensive analysis using the CAPM, tailored for UK stocks. It calculates the expected return, determines stock beta, analyses market trends, and visualizes the risk-return relationship for a portfolio of UK stocks. 
I have developed a Python-based tool designed to perform a comprehensive analysis using the Capital Asset Pricing Model (CAPM) specifically tailored for UK stocks. This tool calculates the expected return on a given UK stock, determines the stock's beta, analyzes market trends, and visualizes the risk-return relationship for a portfolio of UK stocks. The project encompasses data collection, processing, analysis, and visualization to provide a thorough financial analysis.

Project Features:
Data Collection:

Utilizes the yfinance library to fetch historical stock price data and FTSE 100 index data from Yahoo Finance.
Collects UK government bond yield data from reliable sources such as the Office for National Statistics (ONS) or the Bank of England for the risk-free rate.
Data Processing:

Cleans and preprocesses the collected data.
Calculates monthly returns for individual stocks and the FTSE 100 index.
Beta Calculation:

Computes the beta of stocks using linear regression.
Analyzes the sensitivity of stock returns to market returns.
Expected Return Calculation:

Applies the CAPM formula to calculate the expected return of stocks.
Visualization:

Plots historical stock returns against market returns to visualize beta.
Creates a risk-return scatter plot for a selected portfolio of UK stocks.
Displays the Security Market Line (SML) to illustrate the relationship between expected return and beta.
Analysis and Reporting:

Performs sensitivity analysis by varying the risk-free rate and market return.
Generates a detailed report summarizing the findings, including graphs and insights.
This tool provides investors and financial analysts with a robust means of evaluating the risk and return profile of UK stocks, aiding in informed investment decision-making.
