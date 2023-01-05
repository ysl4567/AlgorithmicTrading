#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
#import datapane as dp

#MACD Crossover - Uses the difference between Exponential Averages to determine the momentum and direction of the market 
ticker_input = input("Enter ticker without the $ symbol: ")
#Caterpillar Graph for 
cat = yf.Ticker(ticker_input)
print(cat.history(period="36mo"))

#Graph CAT Closing price for the past 36 months
cat = yf.download(ticker_input, period='36mo', interval='1d') #print everyday on the graph 
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
cat['MACD'] = cat['Short12'] -cat['Long26']  

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
print ("Buy", buy_list) #days since 
print ("Sell", sell_list) #days since

buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(cat.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(cat.iloc[sell_list[close_values_two]].Close)
print ("sell_close", sell_list_close_value)

print ("BUYBUY", buy_list)
buy_list_date_value = buy_list 
print ("buy_date", buy_list_date_value)

print ("SELLSELL", sell_list)
sell_list_date_value = sell_list
print ("sell_date", sell_list_date_value)


length_buy_date_list = len(buy_list_date_value)
length_sell_date_list = len (sell_list_date_value)
length_buy_date_new = []
length_sell_date_new = []


if length_buy_date_list < length_sell_date_list:
    for o in range (length_buy_date_list):
        length_buy_date_new.append(buy_list_date_value[o])
        length_sell_date_new.append(sell_list_date_value[o])

elif length_buy_date_list > length_sell_date_list:
    for i in range (length_sell_date_list):
        length_buy_date_new.append(buy_list_date_value[i])
        length_sell_date_new.append(sell_list_date_value[i])

elif length_buy_date_list == length_sell_date_list:
    for z in range (length_sell_date_list):
        length_buy_date_new.append(buy_list_date_value[z])
        length_sell_date_new.append(sell_list_date_value[z])


length_buy_list = len(buy_list_close_value)
length_sell_list = len(sell_list_close_value)
length_sell_lits = len(sell_list_close_value)
length_buy_list_new = []
length_sell_list_new = []

if length_buy_list > length_sell_list:
    for l in range (length_sell_list):
        length_buy_list_new.append(buy_list_close_value[l])
        length_sell_list_new.append(sell_list_close_value[l])
elif length_buy_list < length_sell_list:
    for a in range (length_buy_list):
        length_buy_list_new.append(buy_list_close_value[a])
        length_sell_list_new.append(sell_list_close_value[a])
elif length_buy_list == length_sell_list:
    for z in range (length_sell_list):
        length_buy_list_new.append(buy_list_close_value[z])
        length_sell_list_new.append(sell_list_close_value[z])



print ("sell_same_length",length_sell_list_new) #same length - 1
print ("buy_same_length",length_buy_list_new) #same length - 1
print ("buy_date_same_length", length_buy_date_new) #same length - 2 Dates
print ("sell_date_same_length", length_sell_date_new) #same length - 2 Dates
print (len(length_sell_list_new))
print (len(length_buy_list_new))

y = len(length_buy_list_new)
x = 0

while True:
    print("x is", x)
    if x >= len(length_buy_list_new):
        break

    if length_buy_list_new[x] > length_sell_list_new[x]:
        length_buy_list_new.pop(x)
        length_sell_list_new.pop(x)
        length_sell_date_new.pop(x)
        length_buy_date_new.pop(x)
        
    else:
        x = x + 1 # when you keep 
        
print("Done!")
print("sell",length_sell_list_new) #$ value
print("buy",length_buy_list_new) #$value
print ("sell date",length_sell_date_new)
print ("buy date", length_buy_date_new)
print ("=",cat.iloc[length_buy_date_new].index)
print ("=",cat.iloc[length_sell_date_new].index)
print ("=",cat.iloc[length_buy_list_new].index)
print ("=",cat.iloc[length_sell_list_new].index)
print ("=",cat.iloc[length_buy_date_new])
print ("=",cat.iloc[length_sell_list_new].Close)

sell_amount = 0
for i in range(len(length_sell_list_new)):
    sell_amount = sell_amount + length_sell_list_new[i]
print ("Total Money earned from selling: ", sell_amount)

buy_amount = 0
for i in range(len(length_buy_list_new)):
    buy_amount = buy_amount + length_buy_list_new[i]
print ("Total Money spent on buying: ", buy_amount)

net_profit = sell_amount - buy_amount
rounded_net_profit = round(net_profit, 2)
print ("Net Profit: $", rounded_net_profit)


#Show on matplotlib graph
#cat[['MACD','Signal Line']].plot(label = ticker_input, figsize=(20,10))
# need to get list equal to each other #----------------------------------------------------------------
cat[['Close']].plot(label = ticker_input, figsize=(20,10))
plt.scatter(cat.iloc[length_buy_date_new].index, cat.iloc[length_buy_date_new].Close, marker = '^', color = 'green') #buy - select
plt.scatter(cat.iloc[length_sell_date_new].index, cat.iloc[length_sell_date_new].Close, marker = '^', color = 'red') #sell - select
plt.show()







 
