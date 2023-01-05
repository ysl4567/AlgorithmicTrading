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
mfi = yf.download(ticker_input, period='36mo', interval='1d') #print everyday on the graph 
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

#Print on graph
mfi[['UPPER','LOWER', 'MFI']].plot(label = ticker_input, figsize=(20,10))
plt.show()
