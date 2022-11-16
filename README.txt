- (Occidental Group) OXY and (Bank of America) BAC used as examples. Screenshots uploaded for each technical analysis

- Periods can be changed accordingly 

- Run all codes on VSCode on 'DeBug Python File' mode

- Code written in VSCode Python

Install:
numpy
pandas
matplotlib
yfinance 
seaborn
plotly
datapane


Type commands below in python to install necessary software (one by one)
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
pip3 intstall yfinance
pip3 install seaborn
pip3 install plotly
pip3 install datapane

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
  - Goal: Show Close line and all possible alternating buy and sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
 Moving_Average_Convergence_Divergence_V3.py
  - Goal: Show Close line and profitable and alternating buy and sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  
 5. Money Flow Index (MFI)
 
 Money_Flow_Index_V1.py
  - Goal: Show the upper line, lower line, and money flow line
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
 Money_Flow_Index_V2.py
  - Goal: Show close line
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
 Money_Flow_Index_V3.py
  - Goal: Show close line with alternating and profitable buy and sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
   
 6. Stochastic Oscillator 
 
 Stochastic_Oscillator_V1.py
  - Goal: Show the upper line, lower line, and stochastic oscillator line
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
 Stochastic_Oscillator_V2.py
  - Goal: Show the upper line, lower line, stochastic oscillator line, and buy and sell points
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
 Stochastic_Oscillator_V3.py
  - Goal: Show alternating and profitable buy and sell points on close value graph
  - Input any ticker symbol (ex.TQQQ, CAT) without the $ symbol
  
 7. Relative Strength Index (RSI)
 
 Relative_Strength_Index_V1.py
  - Goal: Show the upper line, lower line, and relative strenth index line
  - Work in progress...
 
 
 
Currently working on: 

The way the current algorithm works to weed out non-profitable trades also weeds out profitable trades. Need to create a more efficient way to just weed out the non-profitable trades.
Combining all technical analyses explored to produce a more accurate and optimal alternating buy-trade signal graph. 
Fix Relative Strength Index.

Next step:
Create a stock price predictor using neural networks and machine learning to understand what technical analysis is most effective in a given situation.


