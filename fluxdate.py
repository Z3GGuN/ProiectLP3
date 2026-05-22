import matplotlib.pyplot as plt
import numpy as np
import requests
import csv



url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&interval=60min&apikey=02VXKSGG85KQ84VT&datatype=csv'
r = requests.get(url)
with open('datacsv.csv', 'wb') as f:
    f.write(r.content)


with open('datacsv.csv') as data:
    reader = csv.DictReader(data)
    timestamps = []
    close_prices = []
    for row in reader:
        timestamps.append(row['timestamp'])
        close_prices.append(row['close'])
timestamps = np.array(timestamps, dtype='datetime64')
close_prices = np.array(close_prices, dtype='float64')


fig, ax = plt.subplots()
ax.plot(timestamps, close_prices, lw=2)


ax.set_ylabel('price')
ax.set_xlabel('date')
ax.set_title('IBM stock evolution')
fig.autofmt_xdate()
plt.show()


