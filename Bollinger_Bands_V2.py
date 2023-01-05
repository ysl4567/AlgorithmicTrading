#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
#import datapane as dp

#Bollinger(R) Bands developd by John Bollinger
#https://www.iforex.in/education-center/bollinger-bands#:~:text=To%20calculate%20the%20upper%20Bollinger,is%20the%20lower%20Bollinger%20Band.
#Middle Band = 20 Day SMA - Simple Moving Average
#Upper Band = Middle Band + (2 * 20 standard deviation of close price)
#Lower Band = Middle Band - (2 * 20 standard deviation of close price)

#ticker input
#for input, change 'VOO' to ticker_input and vice versa
ticker_input = input("Please enter ticker value (w/o $ symbol): ")

#VOO Graph for 
voo = yf.Ticker(ticker_input)
print(voo.history(period="18mo"))

#Graph VOO Closing price for the past 18 months
voo = yf.download(ticker_input, period='18mo', interval='1d') #print everyday on the graph - plotly.express
voo_price_chart = px.line(voo['Close'],title= ticker_input + ' Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
voo_price_chart.show()

#Middle Band - 20 Day Simple Moving Average
voo['MID'] = voo['Close'].rolling(20).mean()

#Standard Deviation - Std Dev of 20 Day Simple Moving Average
#https://www.javatpoint.com/pandas-standard-deviation#:~:text=The%20Pandas%20std()%20is,for%20the%20calculation%20of%20median.
voo['STDDEV'] = voo['Close'].rolling(20).std()

#Upper Band - Middle Band + (2 * 20 standard deviation of close price)
voo['UPPER'] = voo['MID'] + (2*(voo['STDDEV']))

#Lower Band - Middle Band - (2 * 20 standard deviation of close price)
voo['LOWER'] = voo['MID'] - (2*(voo['STDDEV']))

#where function, where inequality is true print true, else print false 
voo['SELL'] = np.where(voo['UPPER'] < voo['Close'], True, False)
voo['BUY'] = np.where(voo['LOWER'] > voo['Close'], True, False)
print (voo)

#graph when to buy and sell
sell_point = []
buy_point = []
minimum_length = min(len(sell_point),len(buy_point))
x = -1
bought = False
#set up for loop to check for all avlues in voo range.
for dates in range(len(voo)):
    if voo['LOWER'][dates] > voo['Close'][dates]: #buy
        if bought == False:
            buy_point.append(dates)
            bought = True
    elif voo['UPPER'][dates] < voo['Close'][dates] and bought == True: #sell
        if bought == True:
            sell_point.append(dates)
            bought = False
            
#Graph with Matplotlib 
#plt.plot(voo[['Close', 'MID', 'UPPER', 'LOWER']])
voo[['Close', 'MID', 'UPPER', 'LOWER']].plot(label =  ticker_input, figsize=(20,10))
plt.fill_between(voo.index, voo.UPPER, voo.LOWER, color = 'grey', alpha = 0.3)
#plt.scatter(voo.index[voo.BUY], voo[voo.BUY].Close, marker = '^', color = 'green') #buy -all
#plt.scatter(voo.index[voo.SELL], voo[voo.SELL].Close, marker = '^', color = 'red') #buy -all
plt.scatter(voo.iloc[buy_point].index, voo.iloc[buy_point].Close, marker = '^', color = 'green') #buy - select
plt.scatter(voo.iloc[sell_point].index, voo.iloc[sell_point].Close, marker = '^', color = 'red') #sell - select
plt.show()




