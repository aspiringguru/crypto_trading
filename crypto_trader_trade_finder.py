#https://medium.com/building-an-arbitrage-bot-for-crypto-currencies-on/building-an-arbitrage-bot-for-crypto-currencies-on-binance-and-kucoin-9f6d480507ec


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


def watch():
    try:
        orders = client.get_buy_orders('DASH-ETH', limit=5)
        sellorders = client.get_sell_orders('DASH-ETH', limit=5)
        depth = bclient.get_order_book(symbol='DASHETH')
        bsell = depth['asks'][0][0]
        bbuy = depth['bids'][0][0]
        ksell = sellorders[0][0]
        kbuy = orders[0][0]
        kbuyAdd = kbuy + 0.01
    except:
        print('problem grabbing order books')
        kbuyAdd = 2
        bbuy = 1

    #if an ask is larger than a sell order arbitrage
    if kbuyAdd < float(bbuy):
        print('buy kucoin sell binance')
        print(sellorders[0])
        print(depth['bids'][0])
        dashbalance = client.get_coin_balance('ETH')
        print(dashbalance['balance'])
        kucoinBalance = dashbalance['balance'] #get balance
        buyPrice = kbuy + 0.000001 #place buy order at top
        print(kucoinBalance/buyPrice)
        amount = kucoinBalance/buyPrice #find the amount you can buy
        print('buying %s dash coin on kucoin' % amount)
        try:
            transaction = client.create_buy_order('DASH-ETH', buyPrice, amount)
            print(transaction)
            print ("call maketrade(transaction['orderOid']), orderOid:", orderOid)
            #maketrade(transaction['orderOid'])

        except:
            client.cancel_all_orders()
            print('problem making trade')
    time.sleep(7)


def maketrade(oid):
    for x in range(0,9):
        time.sleep(1)
        orders = client.get_active_orders('DASH-ETH')
        time.sleep(1)
        print(orders)
        if orders['BUY']:
            print('order has not been filled')
        else:
            print('the order has been filled')
            dashbalance = client.get_coin_balance('DASH')
            address = bclient.get_deposit_address(asset='DASH')
            client.create_withdrawal('DASH', float(dashbalance['balance']), str(address['address']))
            makeTradeBinance()
        print(x)
        if x == 8:
            client.cancel_all_orders()
        time.sleep(1)

def makeTradeBinance():
    print('madeit')

while True:
    watch();
