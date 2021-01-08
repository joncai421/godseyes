import lib.dbU
import time
import requests
import random

def get_stock_info(symbol):
    try:
        url = 'https://query2.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&symbols='+symbol
        url = 'query1.finance.yahoo.com/v8/finance/chart/0700.HK?formatted=true&crumb=alaFMER.cN8&lang=zh-Hant-HK&region=HK&period1=1460736000&period2=1555344000&interval=1d&events=div%7Csplit&corsDomain=hk.finance.yahoo.com'
        print ('request url:' + url)
        # result = requests.get(url).json()
        result = requests.get(url, timeout=100).json()
        return result
    except:
        return  {'quoteResponse':{'result':[]}}

def update_iterate(symbol_list):
    for index in range(len(symbol_list)):
        print ('update_iterate :' + symbol_list[index][0] + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        r = get_stock_info(symbol_list[index][0])
        if len(r['quoteResponse']['result'])>0:
            stock_status = 'c' if r['quoteResponse']['result'][0]['tradeable'] == True else 'f'
            stock_name = r['quoteResponse']['result'][0]['longName'] if 'longName' in r['quoteResponse']['result'][0] else ''
            quoteType = r['quoteResponse']['result'][0]['quoteType'] if 'quoteType' in r['quoteResponse']['result'][0] else ''
            exchange = r['quoteResponse']['result'][0]['exchange'] if 'exchange' in r['quoteResponse']['result'][0] else ''
            share_capital = r['quoteResponse']['result'][0]['sharesOutstanding']['raw'] if 'sharesOutstanding' in r['quoteResponse']['result'][0] else '0'
            market_capital = r['quoteResponse']['result'][0]['marketCap']['raw'] if 'marketCap' in r['quoteResponse']['result'][0] else '0'
            lib.dbU.update('stock_basic_info', {'market_capital':market_capital, 'share_capital':share_capital}, {'stock_symbol': symbol_list[index][0]})
            # lib.dbU.update('stock_basic_info', {'stock_status': stock_status,'stock_name':stock_name, 'exchange':exchange,'market_capital':market_capital, 'share_capital':share_capital}, {'stock_symbol': symbol_list[index][0]})
            # time.sleep(random.randint(1,3))
        else:
            lib.dbU.update('stock_basic_info', {'market_capital': '-1', 'share_capital': '-1'},
                           {'stock_symbol': symbol_list[index][0]})
            # lib.dbU.update('stock_basic_info', {'stock_status': 'not found'}, {'stock_symbol': symbol_list[index][0]})
            # time.sleep(random.randint(1,3))
    print ('---task completed---')

res=lib.dbU.select('stock_basic_info',['stock_symbol','stock_name'],[['stock_status','=',"'c'"],['stock_name','=',"''"]],[])
# res=lib.dbU.select('stock_basic_info',['stock_symbol'],[['fid','=','21624']],[])
# res=lib.dbU.select('stock_basic_info',['stock_symbol'],[['hasReport','=','1'],['market_capital','=','0'],['fid%3','=','2']],[])
print (len(res))
update_iterate(res)