import lib.dbU
import time
import requests
import random
special_symbol = ['HSI']

def get_stock_info(symbol):
    global special_symbol
    try:
        if symbol in special_symbol:
            url = 'https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=alaFMER.cN8&lang=zh-Hant-HK&region=HK&symbols=%5E'+str(symbol)+'&fields=messageBoardId%2ClongName%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh&corsDomain=hk.finance.yahoo.com'
        else:
            url = 'https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=alaFMER.cN8&lang=zh-Hant-HK&region=HK&symbols='+str(symbol)+'.HK&fields=messageBoardId%2ClongName%2CshortName%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh&corsDomain=hk.finance.yahoo.com'
        print ('request url:' + url)
        # result = requests.get(url).json()
        result = requests.get(url, timeout=100).json()
        return result
    except:
        return  {'quoteResponse':{'result':[]}}
def get_stock_symbol(num):
    num_string = str(num)
    num_string_len =int(len(num_string))
    fill_len = 4-num_string_len
    for i in range(0,fill_len):
        num_string = '0'+num_string
    return num_string

def update_iterate():
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'],[], [], db='hk')
    stock_symbol_list = []
    for r in res:
        stock_symbol_list.append(int(r[0]))

    for index in range(1,3400):
        print ('update_iterate :index:' + str(index) + ' of 3400')
        if index not in stock_symbol_list:
            r = get_stock_info('HSI')
            if len(r['quoteResponse']['result']) > 0:
                stock_status = 'c' if r['quoteResponse']['result'][0]['tradeable'] == True else 'f'
                stock_name = r['quoteResponse']['result'][0]['longName'] if 'longName' in r['quoteResponse']['result'][
                    0] else ''
                # quoteType = r['quoteResponse']['result'][0]['quoteType'] if 'quoteType' in r['quoteResponse']['result'][0] else ''
                exchange = r['quoteResponse']['result'][0]['exchange'] if 'exchange' in r['quoteResponse']['result'][0] else ''
                share_capital = r['quoteResponse']['result'][0]['sharesOutstanding']['raw'] if 'sharesOutstanding' in \
                                                                                               r['quoteResponse']['result'][
                                                                                                   0] else '0'
                market_capital = r['quoteResponse']['result'][0]['marketCap']['raw'] if 'marketCap' in \
                                                                                        r['quoteResponse']['result'][0] else '0'
                lib.dbU.insert('stock_basic_info', [
                    {'fid': get_stock_symbol(index), 'stock_symbol': get_stock_symbol(index), 'stock_status': stock_status,
                     'exchange': exchange, 'stock_name': stock_name, 'market_capital': market_capital,
                     'share_capital': share_capital, 'industry': '', 'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),
                     'has_month_price': 0, 'up2015to2019': 0, 'hasReport': 0, 'up2015to2018': 0, 'has_daily_price': 0}],
                               db='hk')
                # lib.dbU.update('stock_basic_info',
                #                {'stock_status': stock_status, 'stock_name': stock_name, 'exchange': exchange,
                #                 'market_capital': market_capital, 'share_capital': share_capital}, {'stock_symbol': 'HSI'})
                # time.sleep(random.randint(1,3))
            else:
                print ('-----------data error----------------')
            #     lib.dbU.update('stock_basic_info', {'market_capital': '-1', 'share_capital': '-1'},
            #                    {'stock_symbol': symbol_list[index][0]})
                # lib.dbU.update('stock_basic_info', {'stock_status': 'not found'}, {'stock_symbol': symbol_list[index][0]})
            # time.sleep(random.randint(1,3))
    print ('---task completed---')

# res=lib.dbU.select('stock_basic_info',['stock_symbol','stock_name'],[['stock_status','=',"'c'"],['stock_name','=',"''"]],[])
# res=lib.dbU.select('stock_basic_info',['stock_symbol'],[['fid','=','21624']],[])
# res=lib.dbU.select('stock_basic_info',['stock_symbol'],[['hasReport','=','1'],['market_capital','=','0'],['fid%3','=','2']],[])
# print (len(res))
update_iterate()