- All recorded profits and losses based on data as of November 3, 2022 @ 9 pm

- (Occidental Group) OXY and (Bank of America) BAC used as examples. Screenshots uploaded for each technical analysis

- 36 month time period is an arbitrary period. Period can be changed accordingly.

- Run all codeson VSCode on 'DeBug Python File' mode

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


Bollinger_Bands_V1.py
 - Goal: All possible buy and sell points based on Bollinger Band Definition
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol. 
 - Output represents all the possible sell and buy points based on the Bollinger Band method

Bollinger_Bands_V2.py
 - Goal: Alternating buy and sell points with no guarantee that all are profitable
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol.
 - Output represents the possible sell and buy points assuming user is alternating buying and selling

Bollinger_Bands_V3.py
 - Goal: Non-alternating buy and sell points with all being profitable
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol
 - This code eliminates the loss seen when there is a sharp decrease in the value of the stock as shown in V2

Bollinger_Bands_V4.py
 - Goal: Alternating buy and sell points with all being profitable
 - Input any ticker symbol (ex. TQQQ, CAT) without the $ symbol 
 - Eliminates all non-profitable transactions
 
 2. Simple Moving Average (SMA)
 
 Simple_Moving_Average_V1.py
  - Goal: Alternating buy and sell points with no guarantee that all are profitable
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  
 Simple_Moving_average_V2.py
  - Goal: Show only profitable buy and sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol

  
 3. Exponential Moving Average (EMA)
 
 Exponential_Moving_Average_V1.py
  - Goal: Alternating buy and sell points with no guarantee that all are profitable
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol

 Exponential_Moving_Average_V2.py
  - Goal: Show only profitable buy and sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol


 4. Moving Average Convergence Divergence (MACD)
 
 Moving_Average_Convergence_Divergence_V1.py
  - Goal: Show MACD and Signal Line without any buy or sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  
 Moving_Average_Convergence_Divergence_V2.py
  - 
 Moving_Average_Convergence_Divergence_V3.py
  -
  
 5. Money Flow Index (MFI)
 
 Money_Flow_Index_V1.py
  - 
 Money_Flow_Index_V2.py
  - 
 Money_Flow_Index_V3.py
  -
   
 6. Stochastic Oscillator 
 
 Stochastic_Oscillator_V1.py
  -
 Stochastic_Oscillator_V2.py
  -
 Stochastic_Oscillator_V3.py
  -
  
 7. Relative Strength Index (RSI)
 
 Relative_Strength_Index_V1.py
  - Work in progress...
 
 
 
Currently working on: 

The way the current algorithm works to weed out non-profitable trades also weeds out profitable trades. Need to create a more efficient way to just weed out the non-profitable trades.
Combining all technical analyses explored to produce a more accurate and optimal alternating buy-trade signal graph. 
Fix Relative Strength Index.

Next step:
Create a stock price predictor using neural networks and machine learning to understand what technical analysis is most effective in a given situation.


