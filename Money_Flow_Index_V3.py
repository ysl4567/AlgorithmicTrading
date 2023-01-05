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
#Caterpillar Graph for 
mfi = yf.Ticker(ticker_input)
print(mfi.history(period="36mo"))

#Graph mfi Closing price for the past 36 months
mfi = yf.download(ticker_input, period='36mo', Interval='1d') #print everyday on the graph 
mfi_price_chart = px.line(mfi['Close'],title= 'Daily Close Price',color_discrete_map={'Close':'gray'},width=1000, height=1000)
mfi_price_chart.show()

#https://corporatefinanceinstitute.com/resources/wealth-management/money-flow-index/
#1. Typical Price
mfi['Typical Price'] = (mfi['Low'] + mfi['High'] + mfi['Close']) /3
typical_price = (mfi['Low'] + mfi['High'] + mfi['Close']) /3
#2 Raw Money Flow
mfi['Raw Money Flow'] = (mfi['Volume'] * mfi['Typical Price'])
raw_money_flow = (mfi['Volume'] * mfi['Typical Price'])
#3 Compute The Money Ratio
positive_money_flow = []
negative_money_flow = []
for i in range(1, len(mfi['Typical Price'])):
    if typical_price[i] > typical_price[i-1]:
        negative_money_flow.append(typical_price[i-1])
        positive_money_flow.append(0)
    elif typical_price[i] < typical_price[i-1]:
        positive_money_flow.append(typical_price[i-1])
        negative_money_flow.append(0)
    else:
        negative_money_flow.append(0)
        positive_money_flow.append(0)
#mfi['Positive Money Flow'] = positive_money_flow #
#mfi['Negative Money Flow'] = negative_money_flow #
#print (negative_money_flow)
#print (positive_money_flow)
#3b Positive and Negative Money Flow in the 14 Day Period
positive_money_flow_period = []
negative_money_flow_period = []
period_positive = 14
period_negative = 14
for e in range(len(positive_money_flow) - period_positive + 1):
    positive_money_flow_period.append((positive_money_flow[e:period_positive]))
    period_positive = period_positive + 1
#print (len(positive_money_flow_period))

for j in range(len(negative_money_flow) - period_negative + 1):
    negative_money_flow_period.append((negative_money_flow[j:period_negative]))
    period_negative = period_negative + 1
#print (len(negative_money_flow_period))

added_positive_money_flow_period = []
added_negative_money_flow_period = []
row = len(positive_money_flow_period)
column = len(positive_money_flow_period[0])
row2 = len(negative_money_flow_period)
column2 = len(negative_money_flow_period[0])
#print (negative_money_flow_period)
#print (positive_money_flow_period)


for a in range(row):
    sum = 0
    for b in range(column):
        sum = sum + positive_money_flow_period[a][b]
    added_positive_money_flow_period.append(sum)
#mfi['PositiveMoneyFlow'] = added_positive_money_flow_period
    
for c in range(row2):
    sum2 = 0
    for d in range(column2):
        sum2 = sum2 + negative_money_flow_period[c][d]
    added_negative_money_flow_period.append(sum2)
#mfi['NegativeMoneyFlow'] = added_negative_money_flow_period

len(added_positive_money_flow_period)
len(added_negative_money_flow_period)
#print("+",added_positive_money_flow_period)
#print("-",added_negative_money_flow_period)
#print (len(mfi))

#4 Money Ratio
money_ratio = []
for i in range(len(added_negative_money_flow_period)):
    c = added_positive_money_flow_period[i] / added_negative_money_flow_period[i]
    money_ratio.append(c)
#print (len(money_ratio)) 743 BAC
#print ("Money Ratio", money_ratio)

#5 Money Flow Index
#data = {'set_of_numbers': [1,2,3,4,5,np.nan,6,7,np.nan,np.nan,8,9,10,np.nan]}
MFI = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
#print (MFI)
for i in range(len(money_ratio)):
    e = money_ratio[i]
    d = 100-(100/ (1+e))
    MFI.append(d)
#print ("MFI", MFI)
#print (len(MFI)) 757 BAC

mfi['UPPER'] = 80
mfi['LOWER'] = 20
mfi['MFI'] = MFI

#https://www.avatrade.com/education/technical-analysis-indicators-strategies/mfi-indicator-trading-strategies
#Buy and Sell Condition
#Buy: Reading of 20 or below as defined by the LOWER line means stock is oversold. Should seek to buy. 
#Sell: Reading of 80 or above as defined by the UPPER line means stock is overbought. Should seek to sell.

buy_list = []
sell_list = []
bought = False

for dates in range(len(mfi)):
    if bought == False and mfi['LOWER'][dates] > mfi['MFI'][dates]: #buy
        if bought == False:
            buy_list.append(dates)
            bought = True
    elif bought == True and mfi['MFI'][dates] > mfi['UPPER'][dates]: #sell
        if bought == True:
            sell_list.append(dates)
            bought = False
print ("Buy", buy_list) #days since 
print ("Sell", sell_list) #days since

buy_list_close_value = []
for close_values in range (len(buy_list)):
    buy_list_close_value.append(mfi.iloc[buy_list[close_values]].Close)
print ("buy_close", buy_list_close_value)

sell_list_close_value = []
for close_values_two in range (len(sell_list)):
    sell_list_close_value.append(mfi.iloc[sell_list[close_values_two]].Close)
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
print ("=",mfi.iloc[length_buy_date_new].index)
print ("=",mfi.iloc[length_sell_date_new].index)
print ("=",mfi.iloc[length_buy_list_new].index)
print ("=",mfi.iloc[length_sell_list_new].index)
print ("=",mfi.iloc[length_buy_date_new])
print ("=",mfi.iloc[length_sell_list_new].Close)

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
mfi[['Close']].plot(label = ticker_input, figsize=(20,10))
plt.scatter(mfi.iloc[length_buy_date_new].index, mfi.iloc[length_buy_date_new].Close, marker = '^', color = 'green') #buy - select
plt.scatter(mfi.iloc[length_sell_date_new].index, mfi.iloc[length_sell_date_new].Close, marker = '^', color = 'red') #sell - select
plt.show()
