Code written in Visual Studio Code Python

Install:
numpy
pandas
matplotlib
yfinance 
seaborn
plotly
datapane


Type commands below in python to install necessary software (one by one)
pip install numpy
pip install pandas
pip install matplotlib
pip intstall yfinance
pip install seaborn
pip install plotly
pip install datapane

File Descriptions

1. Bollinger Bands

(Occidental Group) OXY and (Bank of America) BAC used as examples. Screenshots uploaded.

Bollinger_Bands_V1.py
 - Goal: All possible buy and sell points based on Bollinger Band Definition
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol. 
 - Output represents all the possible sell and buy points based on the Bollinger Band method

Bollinger_Bands_V2.py
 - Goal: Alternating buy and sell points with no guarantee that all are profitable
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol.
 - Output represents the possible sell and buy points assuming user is alternating buying and selling.

Bollinger_Bands_V3.py
 - Goal: Non-alternating buy and sell points with all being profitable
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol
 - This code eliminates the loss seen when there is a sharp decrease in the value of the stock as shown in V2

Bollinger_Bands_V4.py
 - Goal: Alternating buy and sell points with all being profitable
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol 
 - Still a work in progress
 - Won't work for all stocks
 
 
 2. Simple Moving Average (SMA)
 
 Simple_Moving_Average_V1.py
  - Goal: Alternating buy and sell points with no guarantee that all are profitable
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  - Outputs for BAC and OXY are not net profitable and similar when compared to SMA
  - Outputs are widely inaccurate.
  - BAC, 36 month period: Net Gain: $-36.20
  - OXY, 36 month period: Net Gain: $-71.09
  
 Simple_Moving_average_V2.py
  -
  
 3. Exponential Moving Average (EMA)
 
 Exponential_Moving_Average_V1.py
  - Goal: Alternating buy and sell points with no guarantee that all are profitable
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  - Outputs for BAC and OXY are not net profitable and similar when compared to SMA
  - BAC, 36 month period: Net Gain: $-35.70
  - OXY, 36 month period: Net Gain: $-70.50
 
 Exponential_Moving_Average_V2.py
  - 
 
 4. Moving Average Convergence Divergence (MACD)
 
 Moving_Average_Convergence_Divergence_V1.py
  - Goal: Alternating buy and sell points with no guarantee that all are profitable
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  
 
 Moving_Average_Convergence_Divergence_V2.py
  -
 
 
 Currently working on: 
 
Combining all technical analyses explored to produce a more accurate and optimal alternating buy trade signal graph. 

Next step:
Create a stock price predictor using neural networks and machine learning.


