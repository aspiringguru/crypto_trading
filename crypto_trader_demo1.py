#https://kucoinapidocs.docs.apiary.io/#
#https://medium.com/building-an-arbitrage-bot-for-crypto-currencies-on/building-an-arbitrage-bot-for-crypto-currencies-on-binance-and-kucoin-9f6d480507ec
#https://bitcointalk.org/index.php
#


import time
from binance.client import Client as BinanceClient
from kucoin.client import Client as kuClient

from keys import keys
#keep keys in separate file, keys.py
#set .gitignore to keep keys.py file out of git repo
"""
example content for keys.py, obtain keys from kucoin.com &
keys = dict(
    kuClient_key         =  'blah',
    kuClient_secret      =  'blah',
    BinanceClient_key    =  'blah',
    BinanceClient_secret =  'blah',
)
"""

KUCLIENT_KEY = keys['kuClient_key']
KUCLIENT_SECRET = keys['kuClient_secret']
BINANCECLIENT_KEY = keys['BinanceClient_key']
BINANCECLIENT_SECRET = keys['BinanceClient_secret']

client = kuClient(KUCLIENT_KEY, KUCLIENT_SECRET)
bclient = BinanceClient(BINANCECLIENT_KEY, BINANCECLIENT_SECRET)
##kucoin
orders = client.get_buy_orders('KCS-BTC', limit=50)#KCS-BTC error
sellorders = client.get_sell_orders('KCS-BTC', limit=50)
##binance
depth = bclient.get_order_book(symbol='BNBBTC')#BTCETH

print(orders)
print ("\n\n")
print(sellorders)
print ("\n\n")
print(depth)


lang_url = "https://api.kucoin.com/v1/open/lang-list"
