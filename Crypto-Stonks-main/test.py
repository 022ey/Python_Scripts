import requests
import json

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

#data=cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page='10',price_change_percentage='1h,24h,7d' )

#reqdata=cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', per_page='100',price_change_percentage='1h,24h,7d' )

#with open('data.json', 'w') as f:
    #json.dump(reqdata, f)

with open('data.json') as json_file:
    data = json.load(json_file)

rank=1
index= rank-1
dic= data[index]

ticker= dic["symbol"]+'usd'
print(ticker)
