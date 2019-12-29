import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2018,12,31)

df = web.DataReader('TSLA', 'yahoo', start, end)
##prints first 5 rows in the data set
#print(df.head())
##prints last 5 rows in the data set
#print(df.tail())
#sends df to a csv file where date is the index
df.to_csv('tsla.csv')

#reading in csv file and keeping index as date
df2 = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)
##printing to double check
#print(df2.head())
#get dataframe to be plot
#df.plot(): this plots all columns
#to plot only price use
df['Adj Close'].plot()
#display that plot
plt.show()
