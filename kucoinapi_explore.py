import requests
import time
from binance.client import Client as BinanceClient
from kucoin.client import Client as kuClient

from keys import keys #keep keys in separate file, keys.py
KUCLIENT_KEY = keys['kuClient_key']
KUCLIENT_SECRET = keys['kuClient_secret']

client = kuClient(KUCLIENT_KEY, KUCLIENT_SECRET)

import requests
r = requests.get(url='https://api.kucoin.com/v1/open/lang-list').json()
#print(type(r))
keys = r.keys()
#print ("keys:", keys)
langs = r['data']
for lang in langs:
    print (lang, "\t:", lang[0], "\t:", lang[2])

print ("-----------------------------------------------------------------")
r = requests.get(url='https://api.kucoin.com/v1/open/currencies').json()
#print (r)
print ("\n")
currencies = r['data']['currencies']
for currency in currencies:
    print (currency[0], currency[1])

print ("-----------------------------------------------------------------")
r = requests.get(url='https://api.kucoin.com/v1/user/info').json()
print ("api.kucoin.com/v1/user/info\n", r)

print ("-----------------------------------------------------------------")
r = requests.get(url='https://api.kucoin.com/v1/account//wallet/address').json()
print ("api.kucoin.com/v1/account//wallet/address\n", r)

print ("-----------------------------------------------------------------")
r = requests.get(url='https://api.kucoin.com/v1/order/active').json()
print ("api.kucoin.com/v1/order/active\n", r)

print ("-----------------------------------------------------------------")
r = requests.get(url='https://api.kucoin.com/v1/order/detail').json()
print ("api.kucoin.com/v1/order/detail\n", r)


print ("-----------------------------------------------------------------")
r = requests.get(url='https://api.kucoin.com/v1/open/markets').json()
print ("https://api.kucoin.com/v1/open/markets\n", r)
#print (r['data'])
for coin in r['data']:
    print (coin)

print ("-----------------------------------------------------------------")
url = "https://api.kucoin.com/v1/market/open/symbols"
r = requests.get(url=url).json()
print (url, r)
symbols = []
for coin_info in r['data']:
    print (coin_info)
    symbols.append(coin_info['symbol'])
print (len(r['data']))
print ("symbols:",symbols)
for symbol in symbols:
    orders = client.get_buy_orders(symbol, limit=50)
    print(symbol, "\n", orders)



"""
for method in dir(client):
    print (method)


print ("client.API_KEY:", client.API_KEY)
print ("client.API_SECRET:", client.API_SECRET)
print ("client.API_URL:", client.API_URL)
print ("client.API_VERSION:", client.API_VERSION)
print ("client.RESOLUTION_15MINUTES:", client.RESOLUTION_15MINUTES)
print ("client.RESOLUTION_1DAY:", client.RESOLUTION_1DAY)
print ("client.RESOLUTION_1HOUR:", client.RESOLUTION_1HOUR)
print ("client.RESOLUTION_1MINUTE:", client.RESOLUTION_1MINUTE)
print ("client.RESOLUTION_1WEEK:", client.RESOLUTION_1WEEK)
print ("client.RESOLUTION_30MINUTES:", client.RESOLUTION_30MINUTES)
print ("client.RESOLUTION_5MINUTES:", client.RESOLUTION_5MINUTES)
print ("client.RESOLUTION_8HOURS:", client.RESOLUTION_8HOURS)
print ("client.SIDE_BUY:", client.SIDE_BUY)
print ("client.SIDE_SELL:", client.SIDE_SELL)
print ("client.TRANSFER_DEPOSIT:", client.TRANSFER_DEPOSIT)
print ("client.TRANSFER_STATUS_CANCELLED:", client.TRANSFER_STATUS_CANCELLED)
print ("client.TRANSFER_STATUS_FINISHED:", client.TRANSFER_STATUS_FINISHED)
print ("client.TRANSFER_STATUS_PENDING:", client.TRANSFER_STATUS_PENDING)
print ("client.TRANSFER_WITHDRAWAL:", client.TRANSFER_WITHDRAWAL)

"""
