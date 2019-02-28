import lib.dbU
import time
import requests
import random

def get_stock_info(symbol):
    url = 'https://query2.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&symbols='+symbol
    print ('request url:' + url)
    result = requests.get(url).json()
    return result

def update_iterate(symbol_list, index):
    if index<len(symbol_list):
        print ('update_iterate :' + symbol_list[index][0] + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        r = get_stock_info(symbol_list[index][0])
        if len(r['quoteResponse']['result'])>0:
            stock_status = 'c' if r['quoteResponse']['result'][0]['tradeable'] == True else 'f'
            lib.dbU.update('stock_basic_info', {'stock_status': stock_status}, {'stock_symbol': symbol_list[index][0]})
            index += 1
            time.sleep(random.randint(3,6))
            update_iterate(symbol_list, index)
        else:
            lib.dbU.update('stock_basic_info', {'stock_status': 'not found'}, {'stock_symbol': symbol_list[index][0]})
            index += 1
            time.sleep(random.randint(3,6))
            update_iterate(symbol_list, index)
    else:
        print ('---task completed---')

res=lib.dbU.select('stock_basic_info',['stock_symbol','cik'],[['stock_status','=',"'p'"]])
print (len(res))
update_iterate(res,0)