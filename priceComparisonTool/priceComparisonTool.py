'''
price comparison tool
- track price of a product across different sources
- data source?? (can be in any format from any source, normally will be scraped by another python script)
'''

import json

price_data = None
price = []

# read json file
with open('priceComparisonData.json', encoding='utf8') as im:
    price_data = im.read()

# after reading, convert json to python list of dictionaries
if price_data is not None:
    json_price_data = json.loads(price_data)
    # store relevant information only in price, basically cleaning data to only what you need
    for d in json_price_data:
        price.append({'name': d['name'], 'price': float(d['amazon_price']), 'url': d['amazon_url']})
        price.append({'name': d['name'], 'price': float(d['walmart_price']), 'url': d['walmart_url']})
        price.append({'name': d['name'], 'price': float(d['ebay_price']), 'url': d['ebay_url']})
        minPricedItem = min(price, key=lambda x: float(x['price']))
        # print(minPricedItem['name'],"\n Price:", minPricedItem['price'])
        price = []
    print('=================')
    print('CHEAPEST PRODUCT:\n'+str(minPricedItem["name"])+"\n$" + str(minPricedItem["price"])+"\n"+str(minPricedItem["url"]))

