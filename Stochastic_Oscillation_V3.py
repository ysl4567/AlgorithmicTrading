#import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns
import plotly.express as px
#import datapane as dp

# Money Flow Index
ticker_input = input("Enter ticker without the $ symbol: ")
so = yf.Ticker(ticker_input)
print(so.history(period="36mo"))

#Graph mfi Closing price for the past 36 months
so = yf.download(ticker_input, period='36mo', interval='1d') #print everyday on the graph 
so_price_chart = px.line(so['Close'],title= 'Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
so_price_chart.show()

#https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/slow-stochastic#:~:text=A%20sell%20signal%20is%20given,can%20be%20adjusted%20as%20needed.
so['LOWER'] = 20
so['UPPER'] = 80

#Calculate the Stochastic Oscillate (%K)
#https://finbold.com/guide/stochastic-oscillator-definition/
L14sets = so.Close.values.tolist()
#print (L14sets)
#print (len(L14sets))
#creat 14 day sets
length1 = len(L14sets) - 14 + 1
L14setssets = []
for b in range(length1):
    L14setssets.append(L14sets[b:b+14])
#print (L14setssets)

#find smallest and biggest value in each 14 day period
biggest_value = np.array(L14setssets)
big = biggest_value.max(axis = 1)
#print (big)
#print (len(big))

smallest_value = np.array(L14setssets)
small = smallest_value.min(axis = 1)
#print (small)
#print (len(small))

#calcuate %K stochastic oscillator

stochastic_oscillator = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]

for i in range(len(small)):
    stochastic_oscillator.append((100*(L14sets[i] - small[i])/ (big[i] - small[i])))
#print (stochastic_oscillator)

so['STOOSCI'] = stochastic_oscillator

buy_list = []
sell_list = []
bought = False
#https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/slow-stochastic#:~:text=A%20sell%20signal%20is%20given,can%20be%20adjusted%20as%20needed.
#Buy when oscillater is below 20 and then crosses back above 20
#Sell when oscillater is above 80 and then crosses back below 80

for dates in range(len(so)):
    if bought == False and so['STOOSCI'][dates] > so['LOWER'][dates] and so['STOOSCI'][dates-1] <20: #Buy
            buy_list.append(dates)
            bought = True
    elif bought == True and so['STOOSCI'][dates] < so['UPPER'][dates] and so['STOOSCI'][dates-1] > 80: #sell
        if bought == True:
            sell_list.append(dates)
            bought = False
print ("Buy", buy_list) #days since 
print ("Sell", sell_list) #days since

buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(so.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(so.iloc[sell_list[close_values_two]].Close)
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
print ("=",so.iloc[length_buy_date_new].index)
print ("=",so.iloc[length_sell_date_new].index)
print ("=",so.iloc[length_buy_list_new].index)
print ("=",so.iloc[length_sell_list_new].index)
print ("=",so.iloc[length_buy_date_new])
print ("=",so.iloc[length_sell_list_new].Close)

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

so[['Close']].plot(label = ticker_input, figsize=(20,10))
plt.scatter(so.iloc[length_buy_date_new].index, so.iloc[length_buy_date_new].Close, marker = '^', color = 'green') #buy - select
plt.scatter(so.iloc[length_sell_date_new].index, so.iloc[length_sell_date_new].Close, marker = '^', color = 'red') #sell - select
plt.show()
