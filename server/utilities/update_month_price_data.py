import lib.dbU
import lib.tools
import time
import random
import requests
from_year = 1999
to_year = 2019

def insert_month_price_table(symbol,raw_data):
    global from_year
    global to_year
    timestamp = raw_data['chart']['result'][0]['timestamp']
    dividends_events = raw_data['chart']['result'][0]['events']['dividends'] if 'events' in raw_data['chart']['result'][0] else {}
    splits_events = raw_data['chart']['result'][0]['events']['splits'] if 'events' in raw_data['chart']['result'][0] else {}
    # open_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['open']
    # close_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['close']
    # high_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['high']
    # low_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['low']
    # volume = raw_data['chart']['result'][0]['indicators']['quote'][0]['volume']
    adjclose = raw_data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    length = len(timestamp)
    insert_map = {}
    for index in range(length):
        timeObj = lib.tools.timestamp_to_datetime(timestamp[index])
        year = timeObj.year
        month = timeObj.month
        if from_year <= year and year <=to_year:
            table_name = 'month_price_' + year
            if table_name not in insert_map:
                insert_map[table_name] = {
                    'open': {'stock_symbol': symbol, 'price_type': 'open',
                             'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'close': {'stock_symbol': symbol, 'price_type': 'close',
                              'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'high': {'stock_symbol': symbol, 'price_type': 'high',
                             'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'low': {'stock_symbol': symbol, 'price_type': 'low',
                            'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'adjclose': {'stock_symbol': symbol, 'price_type': 'adjclose',
                                 'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'volume': {'stock_symbol': symbol, 'price_type': 'volume',
                               'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'dividends_events': {'stock_symbol': symbol, 'price_type': 'volume',
                                         'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                    'splits_events': {'stock_symbol': symbol, 'price_type': 'volume',
                                      'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S')},
                }
            for p_type in raw_data['chart']['result'][0]['indicators']['quote'][0]:
                insert_map[table_name][p_type]['m' + month] = raw_data['chart']['result'][0]['indicators']['quote'][0][p_type][index] or 0
            insert_map[table_name]['adjclose']['m' + month] = adjclose[index] or 0
            if timestamp[index] in dividends_events:
                insert_map[table_name]['dividends_events']['m' + month] = dividends_events[timestamp[index]]['amount'] or 0
            if timestamp[index] in splits_events:
                insert_map[table_name]['splits_events']['m' + month] = dividends_events[timestamp[index]]['amount'] or 0

    for year_tables in insert_map:
        i_list = []
        for prc_type in insert_list[year_tables]:
            i_list.append(insert_list[year_tables][prc_type])
        lib.dbU.insert(tables, i_list)
    print ('insert completed for symbol:' + symbol+',updating has_month_price status..')
    lib.dbU.update(tables, {'has_month_price',1},{'stock_symbol':symbol})


def get_m_price_data(symbol):
    print ('filling starting for symbol:'+symbol)
    url = 'https://query2.finance.yahoo.com/v8/finance/chart/'+symbol+'?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&period1=951580800&period2=1553616000&interval=1mo&events=div%7Csplit&corsDomain=finance.yahoo.com'
    print ('request url:' + url)
    result = requests.get(url).json()
    return result

def get_symbols (condition):
    res = lib.dbU.select('stock_basic_info',['stock_symbol'],condition)
    return res

def update_iterate(symbol_list, index):
    if index<len(symbol_list):
        r = get_m_price_data(symbol_list[index][0])
        if r['chart']['result'] is not None:
            insert_month_price_table(symbol_list[index][0],r)
            index += 1
            print (symbol_list[index][0]+' has completed filling, wait for next one...')
            time.sleep(random.randint(30,45))
            update_iterate(symbol_list, index)
        else:
            print (r)
            index += 1
            update_iterate(symbol_list, index)
    else:
        print ('---task completed---')

# type: #1:all,2:active
def fill_month_price_data(type):
    condition = [['has_month_price','=','0']]
    if type==2:
        condition.append(['stock_status', '=', "'c'"])
    symbol_list = get_symbols(condition)
    print (str(len(symbol_list))+' stock to fill data')

    update_iterate([['AAPL']],0)
    # update_iterate(symbol_list,0)


