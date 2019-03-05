import lib.dbU
import time
import requests
import random

def get_stock_info(symbol):
    url = 'https://query2.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&symbols='+symbol
    print ('request url:' + url)
    result = requests.get(url).json()
    return result

def update_iterate(symbol_list):
    for index in range(len(symbol_list)):
        print ('update_iterate :' + symbol_list[index][0] + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        r = get_stock_info(symbol_list[index][0])
        if len(r['quoteResponse']['result'])>0:
            stock_status = 'c' if r['quoteResponse']['result'][0]['tradeable'] == True else 'f'
            stock_name = r['quoteResponse']['result'][0]['longName'] if 'longName' in r['quoteResponse']['result'][0] else ''
            quoteType = r['quoteResponse']['result'][0]['quoteType'] if 'quoteType' in r['quoteResponse']['result'][0] else ''
            exchange = r['quoteResponse']['result'][0]['exchange'] if 'exchange' in r['quoteResponse']['result'][0] else ''
            lib.dbU.update('stock_basic_info', {'stock_status': 'c','stock_name':stock_name, 'exchange':exchange}, {'stock_symbol': symbol_list[index][0]})
            time.sleep(random.randint(1,3))
        else:
            lib.dbU.update('stock_basic_info', {'stock_status': 'not found'}, {'stock_symbol': symbol_list[index][0]})
            time.sleep(random.randint(1,3))
    print ('---task completed---')

# res=lib.dbU.select('stock_basic_info',['stock_symbol','stock_name'],[['stock_status','=',"'c'"],['stock_name','=',"''"]])
res=lib.dbU.select('stock_basic_info',['stock_symbol'],[['stock_name','=',"''"],['up2015to2019','=','1']])
print (len(res))
update_iterate(res)