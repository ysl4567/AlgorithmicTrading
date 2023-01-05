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

#Graph mfi Closing price for the past 36 months
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

rsi[['UPPER', 'LOWER','RSI']].plot(label = ticker_input, figsize=(20,10))
plt.show()

