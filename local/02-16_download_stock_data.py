
# download link from yahoo finance
#https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1655683200&interval=1d&events=history&includeAdjustedClose=true

# to download files with python, use the requests library

import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")
print("Ticker: ", ticker)

from_date = input('Enter start from date in format YYYY/MM/DD: ')
to_date = input('Enter end date in YYYY/MM/DD format: ' )
print("From: ", from_date, "To: ", to_date)

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')
print("From: ", from_datetime, "To: ", to_datetime)

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))
print("From: ", from_epoch, "To: ", to_epoch)


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

content = requests.get(url, headers=headers).content     #this is a method that expects a url 

print(content)

filename = ticker + ".csv"
with open(filename, 'wb') as file:
    file.write(content)
