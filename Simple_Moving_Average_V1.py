#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
import datapane as dp

ticker_input = input("Enter ticker without the $ symbol: ")


#https://www.fidelity.com/viewpoints/active-investor/moving-averages
#Simple Moving Average
#Buy when the short term moving average crosses the long term average
#Sell when the long temr moving average corsses the short term average 

#input any stock ticker
alb = yf.Ticker(ticker_input)
print(alb.history(period="36mo"))

#Graph ALB Closing price for the past 18 months
alb = yf.download(ticker_input, period='36mo', Interval='1d') #print everyday on the graph 
alb_price_chart = px.line(alb['Close'],title='Albemarle Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
alb_price_chart.show()

#In project 1, we want to explore Moving Averages Algorithmic Trading
#Short Moving Average. Set this equal to 5 days. Using close value.
alb['ALB20'] = alb['Close'].rolling(20).mean()

#Long Moving Average. Set this equal to 100 days. Uinsg close value
alb['ALB50'] = alb['Close'].rolling(50).mean()
print (alb)

buy_list = []
sell_list = []
bought = False


for dates in range(len(alb)):
    if bought == False and alb['ALB20'][dates] > alb['ALB50'][dates]:
        if bought == False:
            buy_list.append(dates)
            bought = True
    elif bought == True and alb['ALB20'][dates] < alb['ALB50'][dates]:
        if bought == True:
            sell_list.append(dates)
            bought = False


#Print on graph
#Short Moving Average - better for day trading. Accounts for abnormalities. Long Moving Average - Better for long term. Does not account for abnormalities
alb[['Close','ALB20', 'ALB50']].plot(label = ticker_input, figsize=(20,10))
#alb[['Close','ALB50']].plot(label = 'ALB', figsize=(20,10))
#alb[['Close','ALB100']].plot(label = 'ALB', figsize=(20,10))
plt.scatter(alb.iloc[buy_list].index, alb.iloc[buy_list].Close, marker = '^', color = 'green') #buy - select
plt.scatter(alb.iloc[sell_list].index, alb.iloc[sell_list].Close, marker = '^', color = 'red') #sell - select
plt.show()









