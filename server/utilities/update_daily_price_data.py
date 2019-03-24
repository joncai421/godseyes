import lib.dbU
import lib.tools
import time
import random
import requests
from_year = 2010
to_year = 2019

def getDivided (a,b):
    a = a if isinstance(a, float) else float(a)
    b = b if isinstance(b, float) else float(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 8)

def insert_daily_price_table(symbol,raw_data):
    global from_year
    global to_year
    last_close = []
    timestamp = raw_data['chart']['result'][0]['timestamp']

    adjclose = raw_data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    length = len(timestamp)
    insert_map = {}
    for index in range(length):
        timeObj = lib.tools.timestamp_to_datetime(timestamp[index])
        year = timeObj['year']
        month = timeObj['month']
        date = timeObj['date']
        if from_year <= int(year) and int(year) <=to_year:
            table_name = 'daily_price_' + year
            if table_name not in insert_map:
                insert_map[table_name] = []
            insert_data = {"stock_symbol": symbol}
            for p_type in raw_data['chart']['result'][0]['indicators']['quote'][0]:
                insert_data['Pri_'+p_type] = raw_data['chart']['result'][0]['indicators']['quote'][0][p_type][index] or 0
            adjc = adjclose[index] or 0
            insert_data['Pmonth'] = month
            insert_data['Pdate'] = date
            insert_data['Pri_adjclose'] = adjc
            insert_data['Pri_amplitude_high'] = getRate(insert_data['Pri_high']-insert_data['Pri_open'],insert_data['Pri_open'])
            insert_data['Pri_amplitude_low'] = getRate(insert_data['Pri_open']-insert_data['Pri_low'],insert_data['Pri_open'])
            insert_data['Pri_amplitude_total'] = insert_data['Pri_amplitude_high']+insert_data['Pri_amplitude_low']
            last_close_last_index = int(len(last_close))-1
            last_close_price = last_close[last_close_last_index] if len(last_close) >0 else 0
            insert_data['Pri_last_close'] = last_close_price
            insert_data['diff'] = insert_data['Pri_close']-last_close_price
            insert_data['adjclose_diff'] = insert_data['Pri_adjclose']-insert_data['Pri_close']
            insert_data['total_diff'] = insert_data['Pri_adjclose']-last_close_price
            insert_data['diff_rate'] = getRate(insert_data['diff'],last_close_price)
            insert_data['adjclose_diff_rate'] = getRate(insert_data['adjclose_diff'],insert_data['Pri_close'])
            insert_data['total_diff_rate'] = getRate(insert_data['total_diff'],last_close_price)
            insert_data['Pmark'] = 0
            insert_data['Finsert_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
            insert_data['Fmodify_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
            insert_data['Flastest_modify_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
            insert_map[table_name].append(insert_data)
            last_close.append(insert_data['Pri_close'])

    for year_tables in insert_map:
       lib.dbU.insert(year_tables, insert_map[year_tables])
        # print (year_tables+':')
    # print ('insert completed for symbol:' + symbol+',updating has_daily_price status..')
    lib.dbU.update('stock_basic_info', {'has_daily_price':'1'},{'stock_symbol':symbol})


def get_d_price_data(symbol):
    print ('filling starting for symbol:'+symbol)
    try:
        url = 'https://query2.finance.yahoo.com/v8/finance/chart/'+symbol+'?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&period1=1262275200&period2=1553616000&interval=1d&events=div%7Csplit&corsDomain=finance.yahoo.com'
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
        r = get_d_price_data(symbol_list[index][0])
        if r['chart']['result'] is not None and len(r['chart']['result'][0])>0 and 'timestamp' in r['chart']['result'][0]:
            insert_daily_price_table(symbol_list[index][0],r)
            print (symbol_list[index][0]+' has completed filling, wait for next one...')
        else:
            print (symbol_list[index][0] + ' is empty, wait for next one...')
            lib.dbU.update('stock_basic_info', {'has_daily_price': '-1'}, {'stock_symbol': symbol_list[index][0]})
            # print (r)
        # time.sleep(random.randint(2, 5))
    print ('---task completed---, check for new data...')
    # fill_daily_price_data()

def fill_daily_price_data():
    condition = [['has_daily_price','=','0'],['stock_status','=',"'c'"]]

    symbol_list = get_symbols(condition)
    print (str(len(symbol_list))+' stock to fill data')

    if int(len(symbol_list))>0:
        # update_iterate([['V'],['FB'],['TME']])
        update_iterate(symbol_list)
    else:
        print ('---task completed---')


