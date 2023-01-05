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
so = yf.download(ticker_input, period='36mo',interval='1d') #print everyday on the graph 
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


so[['LOWER','UPPER','STOOSCI']].plot(label = ticker_input, figsize=(20,10))
#plt.scatter(so.iloc[buy_list].index, so.iloc[buy_list].Close, marker = '^', color = 'green') #buy - select
#plt.scatter(so.iloc[sell_list].index, so.iloc[sell_list].Close, marker = '^', color = 'red') #sell - select
plt.show()
