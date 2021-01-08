import lib.dbU
import lib.tools
import time
import random
import requests
from_year = 1997
to_year = 2019
special_symbol = ['DJI']

def insert_month_price_table(symbol,raw_data):
    global from_year
    global to_year
    timestamp = raw_data['chart']['result'][0]['timestamp']
    dividends_events = raw_data['chart']['result'][0]['events']['dividends'] if 'events' in raw_data['chart']['result'][0] and 'dividends' in raw_data['chart']['result'][0]['events'] else {}
    splits_events = raw_data['chart']['result'][0]['events']['splits'] if 'events' in raw_data['chart']['result'][0] and 'splits' in raw_data['chart']['result'][0]['events'] else {}
    # open_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['open']
    # close_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['close']
    # high_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['high']
    # low_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['low']
    # volume = raw_data['chart']['result'][0]['indicators']['quote'][0]['volume']
    adjclose = raw_data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    length = len(timestamp)
    insert_map = {}
    total_map = {}
    for index in range(length):
        timeObj = lib.tools.timestamp_to_datetime(timestamp[index])
        year = timeObj['year']
        month = timeObj['month']
        if from_year <= int(year) and int(year) <=to_year:
            table_name = 'month_price_' + year
            if table_name not in insert_map:
                insert_map[table_name] = {
                    'open': {'stock_symbol': symbol, 'price_type': 'open','day':0,'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,
                             'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'close': {'stock_symbol': symbol, 'price_type': 'close','day':0,'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,
                              'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'high': {'stock_symbol': symbol, 'price_type': 'high','day':0,'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,
                             'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'low': {'stock_symbol': symbol, 'price_type': 'low','day':0,'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,
                            'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'adjclose': {'stock_symbol': symbol, 'price_type': 'adjclose','day':0,'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,
                                 'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'volume': {'stock_symbol': symbol, 'price_type': 'volume','day':0,'m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,
                               'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'dividends_events': {'stock_symbol': symbol, 'price_type': 'dividends_events','m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,'day':0,
                                         'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                    'splits_events': {'stock_symbol': symbol, 'price_type': 'splits_events','m1':0,'m2':0,'m3':0,'m4':0,'m5':0,'m6':0,'m7':0,'m8':0,'m9':0,'m10':0,'m11':0,'m12':0,'day':0,
                                      'Finsert_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Fmodify_time': time.strftime('%Y-%m-%d %H:%M:%S'),'Flastest_modify_time':time.strftime('%Y-%m-%d %H:%M:%S')},
                }
            if year not in total_map:
                total_map[year] = {'open':0,'close':0,'high':0,'low':0,'adjclose':0,'volume':0,'dividends_events':0,'splits_events':0}
            for p_type in raw_data['chart']['result'][0]['indicators']['quote'][0]:
                insert_map[table_name][p_type]['m' + month] = raw_data['chart']['result'][0]['indicators']['quote'][0][p_type][index] or 0
                total_map[year][p_type]+=raw_data['chart']['result'][0]['indicators']['quote'][0][p_type][index] or 0

            adjc = adjclose[index] or 0
            insert_map[table_name]['adjclose']['m' + month] = adjc
            total_map[year]['adjclose']+= adjc

            # if timestamp[index] in dividends_events:
            #     insert_map[table_name]['dividends_events']['m' + month] = dividends_events[timestamp[index]]['amount']
            #     total_map[year]['dividends_events'] += 1
            # else:
            #     insert_map[table_name]['dividends_events']['m' + month] = 0
            # if timestamp[index] in splits_events:
            #     insert_map[table_name]['splits_events']['m' + month] = dividends_events[timestamp[index]]['amount']
            #     total_map[year]['splits_events'] += 1
            # else:
            #     insert_map[table_name]['splits_events']['m' + month] = 0

    for d_time in dividends_events:
        timeObj = lib.tools.timestamp_to_datetime(d_time)
        year = timeObj['year']
        month = timeObj['month']
        insert_map['month_price_' + year]['dividends_events']['m'+month] = dividends_events[d_time]['amount']
        total_map[year]['dividends_events'] += 1

    for d_time in splits_events:
        timeObj = lib.tools.timestamp_to_datetime(d_time)
        year = timeObj['year']
        month = timeObj['month']
        insert_map['month_price_' + year]['splits_events']['m'+month] = 0 if splits_events[d_time]['numerator'] ==0 else splits_events[d_time]['denominator']/splits_events[d_time]['numerator']
        total_map[year]['splits_events'] += 1

    for y in total_map:
        for p in total_map[y]:
            insert_map['month_price_' + y][p]['total'] = total_map[y][p]

    for year_tables in insert_map:
        i_list = []
        for prc_type in insert_map[year_tables]:
            i_list.append(insert_map[year_tables][prc_type])
        lib.dbU.insert(year_tables, i_list)
        # print (year_tables+':')
        # print (i_list)
    # print ('insert completed for symbol:' + symbol+',updating has_month_price status..')
    lib.dbU.update('stock_basic_info', {'has_month_price':'1'},{'stock_symbol':symbol})


def get_m_price_data(symbol):
    # print (1111222)
    global special_symbol
    print ('filling starting for symbol:'+symbol)
    try:
        if symbol in special_symbol:
            url = 'https://query2.finance.yahoo.com/v8/finance/chart/%5E' + symbol + '?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&period1=883584000&period2=1561564800&interval=1mo&events=div%7Csplit&corsDomain=finance.yahoo.com'
        else:
            url = 'https://query2.finance.yahoo.com/v8/finance/chart/'+symbol+'?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&period1=883584000&period2=1561564800&interval=1mo&events=div%7Csplit&corsDomain=finance.yahoo.com'

        # print ('request url:' + url)
        result = requests.get(url)
        # print (result)
        return result.json()
    except:
       return {'chart':{'result':None}}

def get_symbols (condition):
    res = lib.dbU.select('stock_basic_info',['stock_symbol','cik'],condition,[])
    return res

def update_iterate(symbol_list):
    for index in range(len(symbol_list)):
        print ('update_iterate :' + symbol_list[index][0] + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        r = get_m_price_data(symbol_list[index][0])
        if r['chart']['result'] is not None and len(r['chart']['result'][0])>0 and 'timestamp' in r['chart']['result'][0]:
            insert_month_price_table(symbol_list[index][0],r)
            print (symbol_list[index][0]+' has completed filling, wait for next one...')
        else:
            print (symbol_list[index][0] + ' is empty, wait for next one...')
            lib.dbU.update('stock_basic_info', {'has_month_price': '-1'}, {'stock_symbol': symbol_list[index][0]})
            # print (r)
        # time.sleep(random.randint(2, 5))
    print ('---task completed---, check for new data...')
    # fill_month_price_data(2)

# type: #1:all,2:active
def fill_month_price_data(type):
    condition = [['has_month_price','=','0']]
    if type==2:
        condition.append(['stock_status', '=', "'c'"])
    symbol_list = get_symbols(condition)
    print (str(len(symbol_list))+' stock to fill data')

    if int(len(symbol_list))>0:
        # update_iterate([['DJI']])
        update_iterate(symbol_list)
    else:
        print ('---task completed---')


