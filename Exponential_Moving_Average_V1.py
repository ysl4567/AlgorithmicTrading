#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sbn
import plotly.express as pltex
import datapane as dp

ticker_input = input("Enter ticker without the $ symbol: ")


#Albemarle Graph for 
alb = yf.Ticker(ticker_input)
print(alb.history(period="36mo"))

#Graph ALB Closing price for the past36 months
alb = yf.download(ticker_input, period='36mo', Interval='1d') #print everyday on the graph 
alb_price_chart = pltex.line(alb['Close'],title='Albemarle Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
alb_price_chart.show()

#alb = alb['Close'].to_frame()
#In project 1, we want to explore Moving Averages Algorithmic Trading
#Short Moving Average. Set this equal to 5 days. Using close value.
alb['ALB20'] = alb['Close'].ewm(span=20).mean()
#Long Moving Average. Set this equal to 100 days. Uinsg close value
alb['ALB50'] = alb['Close'].ewm(span=50).mean()
print (alb)

buy_list = []
sell_list = []
bought = False

#When should I buy and sell?
#https://blog.quantinsti.com/moving-average-trading-strategies/
#Buy: faster moving averages cross above the slower moving averages 
#Sell: faster moving averages cross below the slower moving averages.
for dates in range(len(alb)):
    if bought == False and alb['ALB20'][dates] > alb['ALB50'][dates]:
        if bought == False:
            buy_list.append(dates)
            bought = True
    elif bought == True and alb['ALB20'][dates] < alb['ALB50'][dates]:
        if bought == True:
            sell_list.append(dates)
            bought = False

buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(alb.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(alb.iloc[sell_list[close_values_two]].Close)
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

#Print on graph - matplotlib
#Short Moving Average - better for day trading. Accounts for abnormalities. Long Moving Average - Better for long term. Does not account for abnormalities
alb[['Close','ALB20',  'ALB50']].plot(label = ticker_input, figsize=(20,10))
plt.scatter(alb.iloc[buy_list].index, alb.iloc[buy_list].Close, marker = '^', color = 'green') #buy - select
plt.scatter(alb.iloc[sell_list].index, alb.iloc[sell_list].Close, marker = '^', color = 'red') #sell - select
plt.show()
