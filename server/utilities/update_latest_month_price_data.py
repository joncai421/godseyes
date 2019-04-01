import lib.dbU
import lib.tools
import time
import random
import requests
from_year = 2019
to_year = 2022
from_month = 2
special_symbol = ['DJI']

trand_days_in_month = {}
def update_trand_days_in_month():
    global from_year
    global to_year
    global trand_days_in_month
    for year in range(from_year,to_year):
        for i in range(1,13):
            d = lib.dbU.select('daily_price_' + str(year), ['dp_id'],[['Pmonth', '=', "'" + str(i) + "'"], ['stock_symbol', '=', "'DJI'"]], [])
            if str(year) not in trand_days_in_month:
                trand_days_in_month[str(year)] = {}
            trand_days_in_month[str(year)][str(i)] = len(d)

def getDivided (a,b):
    a = a if isinstance(a, float) else float(a)
    b = b if isinstance(b, float) else float(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 4)

def insert_month_price_table(symbol,raw_data):
    global from_year
    global to_year
    global from_month
    global trand_days_in_month
    timestamp = raw_data['chart']['result'][0]['timestamp']
    # dividends_events = raw_data['chart']['result'][0]['events']['dividends'] if 'events' in raw_data['chart']['result'][0] and 'dividends' in raw_data['chart']['result'][0]['events'] else {}
    # splits_events = raw_data['chart']['result'][0]['events']['splits'] if 'events' in raw_data['chart']['result'][0] and 'splits' in raw_data['chart']['result'][0]['events'] else {}
    adjclose = raw_data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    length = len(timestamp)

    for index in range(length):
        timeObj = lib.tools.timestamp_to_datetime(timestamp[index])
        year = timeObj['year']
        month = timeObj['month']
        if from_year <= int(year) and int(year) <=to_year and from_month <= int(month):
            table_name = 'month_price_' + year
            update_map = {
                 'open': {},
                 'close': {},
                 'high': {},
                 'low': {},
                 'adjclose': {},
                 'avg_volume': {},
                 'volume': {},
                 'dividends_events': {},
                 'splits_events': {},
            }

            for p_type in raw_data['chart']['result'][0]['indicators']['quote'][0]:
                update_map[p_type]['m' + month] = raw_data['chart']['result'][0]['indicators']['quote'][0][p_type][index] or 0

            adjc = adjclose[index] or 0
            update_map['adjclose']['m' + month] = adjc
            update_map['avg_volume']['m' + month] = getRate(update_map['volume']['m' + month],trand_days_in_month[year][month])
            for ud in update_map:
                # print (111)
                # print ('update:'+table_name)
                # print (update_map[ud])
                # print (ud)
                # print (symbol)
                # print (222)
                lib.dbU.update(table_name, update_map[ud], {'stock_symbol': symbol,'price_type':ud})
                lib.dbU.update('stock_basic_info', {'has_month_price': '1'}, {'stock_symbol': symbol})

    # for d_time in dividends_events:
    #     if from_year <= int(year) and int(year) <= to_year and from_month <= month:
    #         timeObj = lib.tools.timestamp_to_datetime(d_time)
    #         year = timeObj['year']
    #         month = timeObj['month']
    #         update_map['month_price_' + year]['dividends_events']['m'+month] = dividends_events[d_time]['amount']
    #
    # for d_time in splits_events:
    #     if from_year <= int(year) and int(year) <= to_year and from_month <= month:
    #         timeObj = lib.tools.timestamp_to_datetime(d_time)
    #         year = timeObj['year']
    #         month = timeObj['month']
    #         update_map['month_price_' + year]['splits_events']['m'+month] = 0 if splits_events[d_time]['numerator'] ==0 else splits_events[d_time]['denominator']/splits_events[d_time]['numerator']

    # for year_tables in update_map:
    #     i_list = []
    #     for prc_type in update_map[year_tables]:
    #         i_list.append(update_map[year_tables][prc_type])
    #     lib.dbU.insert(year_tables, i_list)
    #     # print (year_tables+':')
    #     # print (i_list)
    # # print ('insert completed for symbol:' + symbol+',updating has_month_price status..')
    # lib.dbU.update('stock_basic_info', {'has_month_price':'1'},{'stock_symbol':symbol})


def get_m_price_data(symbol):
    # print (1111222)
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
    res = lib.dbU.select('stock_basic_info',['stock_symbol'],condition,[])
    return res

def update_iterate(symbol_list):
    for index in range(len(symbol_list)):
        print ('update_iterate :' + symbol_list[index][0] + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        r = get_m_price_data(symbol_list[index][0])
        if r['chart']['result'] is not None and len(r['chart']['result'][0])>0 and 'timestamp' in r['chart']['result'][0]:
            insert_month_price_table(symbol_list[index][0],r)
            print (symbol_list[index][0]+' has completed filling, wait for next one...')
        # else:
        #     print (symbol_list[index][0] + ' is empty, wait for next one...')
            # lib.dbU.update('stock_basic_info', {'has_month_price': '-1'}, {'stock_symbol': symbol_list[index][0]})
            # print (r)
        # time.sleep(random.randint(2, 5))
    print ('---task completed---, check for new data...')
    # fill_month_price_data(2)

def fill_month_price_data():
    condition = [['has_month_price','=','1']]
    update_trand_days_in_month()
    symbol_list = get_symbols(condition)
    print (str(len(symbol_list))+' stock to fill data')

    if int(len(symbol_list))>0:
        # update_iterate([['DJI']])
        update_iterate(symbol_list)
    else:
        print ('---task completed---')


