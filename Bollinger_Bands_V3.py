#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
import datapane as dp

#Bollinger(R) Bands developd by John Bollinger
#https://www.iforex.in/education-center/bollinger-bands#:~:text=To%20calculate%20the%20upper%20Bollinger,is%20the%20lower%20Bollinger%20Band.
#Middle Band = 20 Day SMA - Simple Moving Average
#Upper Band = Middle Band + (2 * 20 standard deviation of close price)
#Lower Band = Middle Band - (2 * 20 standard deviation of close price)

#ticker input
#for input, change 'VOO' to ticker_input
ticker_input = input("Please enter ticker value (w/o $ symbol): ")

#VOO Graph for 
voo = yf.Ticker(ticker_input)
print(voo.history(period="18mo"))

#Graph VOO Closing price for the past 18 months
voo = yf.download(ticker_input, period='18mo', Interval='1d') #print everyday on the graph - plotly.express
voo_price_chart = px.line(voo['Close'],title= 'VOO' + ' Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
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


#When to buy and sell - https://www.fidelity.com/viewpoints/active-investor/understanding-bollinger-bands#:~:text=Buy%20and%20sell%20signals,-In%20addition%20to&text=When%20it%20breaks%20below%20the,but%20rather%20a%20continuation%20pattern.
#Buy - When the closing prices goes above the upper band
#Sell - When the closing price goes below the lower band 
#where function - where inequality is true print value, else false don't print value
sell_value_dates = []
buy_value_dates = []
buy_value_close = []
sell_value_close = []
for i in range (len(voo)): #all possible sell dates counting from start date
    if voo['UPPER'][i] < voo['Close'][i]:
        sell_value_dates.append(i)
print (sell_value_dates)

for j in range (len(voo)): #all possible buy dates counting from start date
    if voo['LOWER'][j] > voo['Close'][j]:
        buy_value_dates.append(j)
print (buy_value_dates)

for k in range (len(voo)): #all the UPPER close values
    if voo['UPPER'][k] < voo['Close'][k]:
        sell_value_close.append(voo['UPPER'][k])
print (sell_value_close)

for l in range (len(voo)): #all the LOWER close values
    if voo['LOWER'][l] > voo['Close'][l]:
        buy_value_close.append(voo['LOWER'][l])
print (buy_value_close)
#------------------------------------------------------------------------------------------------------------------------------------------------------
sell_point = []
buy_point = []
buy_point_2 = []
sell_point_2 = []
minimum_length = min(len(sell_value_dates),len(buy_value_dates),len(sell_value_close), len(buy_value_close))
x = 0
y = x
bought = False
for x in range(minimum_length):
    for y in range (y,y+2):
        if sell_value_dates[x] > buy_value_dates[x] and sell_value_close[x] > buy_value_close[x]:
            if bought == False:
                buy_point_2.append(buy_value_dates[x])
                sell_point_2.append(sell_value_dates[x])
                sell_point.append(sell_value_close[x])
                buy_point.append(buy_value_close[x])
                bought == True

#Graph with Matplotlib - select
#plt.plot(voo[['Close', 'MID', 'UPPER', 'LOWER']])
voo[['Close', 'MID', 'UPPER', 'LOWER']].plot(label = ticker_input, figsize=(20,10))
plt.fill_between(voo.index, voo.UPPER, voo.LOWER, color = 'grey', alpha=0.3)
plt.scatter(voo.iloc[buy_point_2].index, voo.iloc[buy_point_2].Close, marker = '^', color = 'green') #buy     -- Date Since start, Close Value 
#INDEX OF BUY_POINT_2 AND BUY_POINT MUST BE THE SAME
plt.scatter(voo.iloc[sell_point_2].index, voo.iloc[sell_point_2].Close, marker = '^', color = 'red') #sell
#plt.scatter(voo.index[voo.BUY], voo[voo.BUY].Close, marker = '^', color = 'green') #buy
#plt.scatter(voo.index[voo.SELL], voo[voo.SELL].Close, marker = '^', color = 'red') #sell
plt.show()


























