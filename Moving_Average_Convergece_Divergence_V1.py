#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
import datapane as dp

#MACD Crossover - Uses the difference between Exponential Averages to determine the momentum and direction of the market 
ticker_input = input("Enter ticker without the $ symbol: ")
#Caterpillar Graph for 
cat = yf.Ticker(ticker_input)
print(cat.history(period="36mo"))

#Graph CAT Closing price for the past 36 months
cat = yf.download(ticker_input, period='36mo', Interval='1d') #print everyday on the graph 
cat_price_chart = px.line(cat['Close'],title= 'Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
cat_price_chart.show()


# Buy -  When MACD line crosses above the Signal Line
# Sell - When MACD line crosses below the Signal Line
# MACD Line - Short Term Exponential Average - Long Term Exponential Average 
# Signal Line - 9 period Smooth Exponential Moving Average 
# Short: 12 Period Long: 26 Periods 

#Short exponential moving average
cat['Short12'] = cat['Close'].ewm(span=12).mean()
#Long exponential moving average
cat['Long26'] = cat['Close'].ewm(span=26).mean()

#MACD 12 day EMA - 26 day EMA  
#https://www.investopedia.com/terms/m/macd.asp#:~:text=The%20MACD%20line%20is%20calculated,for%20buy%20or%20sell%20signals.
cat['MACD'] = cat['Short12'] -cat['ong26']  

#Signal Line - 9 day MACD EMA Average
#https://www.investopedia.com/terms/m/macd.asp#:~:text=The%20MACD%20line%20is%20calculated,for%20buy%20or%20sell%20signals.
cat['Signal Line'] = cat['MACD'].ewm(span=9).mean()
print (cat)


buy_list = []
sell_list = []
bought = False
#https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/macd#:~:text=When%20the%20MACD%20line%20crosses,line%20the%20stronger%20the%20signal.
# Buy -  When MACD line crosses above the Signal Line
# Sell - When MACD line crosses below the Signal Line
for dates in range (len(cat)):
    if bought == False and cat['MACD'][dates] > cat['Signal Line'][dates]:
        if bought == False:
            buy_list.append(dates)
            bought = True
    elif bought == True and cat['MACD'][dates] < cat['Signal Line'][dates]:
        if bought == True:
            sell_list.append(dates)
            bought = False

buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(cat.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(cat.iloc[sell_list[close_values_two]].Close)
print ("sell_close", sell_list_close_value)

buy_total = 0
for i in range(len(buy_list_close_value)):
    buy_total = buy_total + buy_list_close_value[i]
print ("Total $ Used to Buy: ", buy_total)

sell_total = 0
for i in range(len(sell_list_close_value)):
    sell_total = sell_total + sell_list_close_value[i]
print ("Total $ Gained: ", sell_total)

total_value = sell_total - buy_total
rounded_total_value = round(total_value,2)
print ("Net gain: $", rounded_total_value)


#Show on matplotlib graph
cat[['MACD','Signal Line']].plot(label = ticker_input, figsize=(20,10))
plt.show()
