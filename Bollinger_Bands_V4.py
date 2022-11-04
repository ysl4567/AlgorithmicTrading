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


#When to buy and sell - https://www.fidelity.com/viewpoints/active-investor/understanding-bollinger-bands#:~:text=Buy%20and%20sell%20signals,-In%20addition%20to&text=When%20it%20breaks%20below%20the,but%20rather%20a%20continuation%20pattern.
#Buy - When the closing prices goes above the upper band
#Sell - When the closing price goes below the lower band 
#where function - where inequality is true print value, else false don't print value
buy_list = []
sell_list = []
bought = False


for dates in range(len(voo)):
    if bought == False and voo['Close'][dates] > voo['UPPER'][dates]:
        if bought == False:
            buy_list.append(dates)
            bought = True
    elif bought == True and voo['Close'][dates] < voo['LOWER'][dates]:
        if bought == True:
            sell_list.append(dates)
            bought = False
print ("Buy", buy_list) #days since 
print ("Sell", sell_list) #days since


buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(voo.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(voo.iloc[sell_list[close_values_two]].Close)
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
print ("=",voo.iloc[length_buy_date_new].index)
print ("=",voo.iloc[length_sell_date_new].index)
print ("=",voo.iloc[length_buy_list_new].index)
print ("=",voo.iloc[length_sell_list_new].index)
print ("=",voo.iloc[length_buy_date_new])
print ("=",voo.iloc[length_sell_list_new].Close)

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



#Graph with Matplotlib - select
#plt.plot(voo[['Close', 'MID', 'UPPER', 'LOWER']])
voo[['Close', 'MID', 'UPPER', 'LOWER']].plot(label = ticker_input, figsize=(20,10))
plt.fill_between(voo.index, voo.UPPER, voo.LOWER, color = 'grey', alpha=0.3)
plt.scatter(voo.iloc[length_buy_date_new].index, voo.iloc[length_buy_date_new].Close, marker = '^', color = 'green') #buy  
plt.scatter(voo.iloc[length_sell_date_new].index, voo.iloc[length_sell_date_new].Close, marker = '^', color = 'red') #sell
plt.show()
