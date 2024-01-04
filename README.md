# Stochastic-Oscilator-for-Cryptocurrencies
This Python project utilizes the Streamlit framework to create an interactive web application for analyzing cryptocurrency data from the Kraken exchange. The application incorporates features such as fetching historical OHLC (Open, High, Low, Close) data, calculating and visualizing technical indicators like the Stochastic Oscillator, candle charts and comparing different cryptocurrencies.

Key Features:
Fetching Kraken Data: Utilizes the Kraken API to retrieve historical OHLC data for selected cryptocurrency pairs.
Candles Graph: Created a candle graph to see the real time price of the criptocurrency and the volume traded. 
Stochastic Oscillator: Calculates the Stochastic Oscillator to analyze price momentum and potential trend reversals.
Streamlit Interface: Employs the Streamlit framework for building a user-friendly web interface, allowing users to interact with and visualize cryptocurrency data.

How to Use:
Input the trading pair and desired parameters via the Streamlit interface.
View historical data, Stochastic Oscillator results, and comparison charts.
Gain insights into cryptocurrency price movements and potential market trends.

Requirements:
Python
Streamlit
Pandas
TA-Lib (Technical Analysis Library)
Kraken API key (for fetching Kraken data)

Installation:
bash
Copy code
pip install streamlit pandas TA-Lib

Usage:
Run the Streamlit application: streamlit run root.py
Input required parameters in the Streamlit sidebar.
Explore cryptocurrency data, candle charts, Stochastic Oscillator results.
