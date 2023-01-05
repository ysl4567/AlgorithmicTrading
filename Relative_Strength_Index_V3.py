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
rsi = yf.Ticker(ticker_input)
print(rsi.history(period="36mo"))

#Graph rsi Closing price for the past 36 months
rsi = yf.download(ticker_input, period='36mo', interval='1d') #print everyday on the graph 
rsi_price_chart = px.line(rsi['Close'],title= 'Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
rsi_price_chart.show()

#https://www.fidelity.com/viewpoints/active-investor/how-to-use-RSI#:~:text=The%20relative%20strength%20index%20(RSI,be%20approaching%20a%20cautionary%20signal.
rsi['UPPER'] = 70
rsi['LOWER'] = 30

#https://www.macroption.com/rsi-calculation/
#14 Day Simple Moving Average is most commonly used
rsi['RSI14'] = rsi['Close'].rolling(14).mean()
fourteen_day_average_values = []
for values in range(len(rsi['RSI14'])):
    fourteen_day_average_values.append(rsi['RSI14'][values])
#print (fourteen_day_average_values)
#print (len(fourteen_day_average_values)) 757
#print (len(rsi['ALB14'])) 757
#get rid of nan values
intermediate = fourteen_day_average_values[14:]
#print (intermediate)

#calculate differences between each value in intermediate
up_and_down = []
n = 1
for i in range(len(intermediate) -1):
    up_and_down.append(intermediate[n] - intermediate[n-1])
    n = n + 1 
#print(up_and_down)
#print (len(up_and_down))
#calculate the gains and losses in each 14 day period
total = len(up_and_down) - 14 + 1 #total number of set of fourteen numbers
multid = []
positive = []
negative = []
for b in range(total):
    multid.append(up_and_down[b:b+14])
print ("\n")
#print ("multid", multid)

for i in range(len(multid)):
    pos_addition = 0
    neg_addition = 0
    for j in range(len(multid[0])):
        if multid[i][j] > 0:
            pos_addition = pos_addition + multid[i][j]
        elif multid[i][j] < 0:
            neg_addition = neg_addition + multid[i][j]
        elif multid[i][j] == 0:
            neg_addition = neg_addition = multid[i][j]
    positive.append(pos_addition)
    negative.append(neg_addition)
#print ("\n")
print ("POS",positive)
#print ("\n")
print ("NEG",negative)
#print (len(positive))
#print (len(negative))

#calculate relative strength
relative_strength = []
for i in range(len(negative)):
    if positive[i] == 0:
        relative_strength.append(negative[i])
    elif negative[i] == 0:
        relative_strength.append(positive[i])
    else:
        relative_strength.append(positive[i] / negative[i])
#print (relative_strength)
#print (len(relative_strength))

#calculate RSI
RSI = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
for i in range(len(relative_strength)):
    RSI.append((100)-((100)/(1+(relative_strength[i]))))
#print (RSI)
#print (len(RSI))
#print (len(rsi))
rsi['RSI'] = RSI

buy_list = []
sell_list = []
bought = False

for dates in range(len(rsi)):
    if bought == False and rsi['LOWER'][dates] > rsi['RSI'][dates]: #buy
        if bought == False:
            buy_list.append(dates)
            bought = True
    elif bought == True and rsi['RSI'][dates] > rsi['UPPER'][dates]: #sell
        if bought == True:
            sell_list.append(dates)
            bought = False
print ("Buy", buy_list) #days since 
print ("Sell", sell_list) #days since

buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(rsi.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(rsi.iloc[sell_list[close_values_two]].Close)
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
print ("=",rsi.iloc[length_buy_date_new].index)
print ("=",rsi.iloc[length_sell_date_new].index)
print ("=",rsi.iloc[length_buy_list_new].index)
print ("=",rsi.iloc[length_sell_list_new].index)
print ("=",rsi.iloc[length_buy_date_new])
print ("=",rsi.iloc[length_sell_list_new].Close)

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


#Print on graph
rsi[['Close']].plot(label = ticker_input, figsize=(20,10))
plt.scatter(rsi.iloc[length_buy_date_new].index, rsi.iloc[length_buy_date_new].Close, marker = '^', color = 'green') #buy - select
plt.scatter(rsi.iloc[length_sell_date_new].index, rsi.iloc[length_sell_date_new].Close, marker = '^', color = 'red') #sell - select
plt.show()
