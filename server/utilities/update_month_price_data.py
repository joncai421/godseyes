import lib.dbU
import requests

def insert_month_price_table(raw_data):
    timestamp = raw_data['chart']['result'][0]['timestamp']
    dividends_events = raw_data['chart']['result'][0]['events']['dividends'] if 'events' in raw_data['chart']['result'][0] else {}
    splits_events = raw_data['chart']['result'][0]['events']['splits'] if 'events' in raw_data['chart']['result'][0] else {}
    open_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['open']
    close_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['close']
    high_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['high']
    low_price = raw_data['chart']['result'][0]['indicators']['quote'][0]['low']
    volume = raw_data['chart']['result'][0]['indicators']['quote'][0]['volume']
    length = len(timestamp)

    # lib.dbU.insert('stock_basic_info', insert_list)

def get_m_price_data(symbol):
    print (symbol)
    url = 'https://query2.finance.yahoo.com/v8/finance/chart/'+symbol+'?formatted=true&crumb=qzKRwVIK1az&lang=en-US&region=US&period1=951580800&period2=1553616000&interval=1mo&events=div%7Csplit&corsDomain=finance.yahoo.com'
    print ('request url:' + url)
    result = requests.get(url).json()
    return result

def get_symbols (condition):
    res = lib.dbU.select('stock_basic_info',['stock_symbol'],condition)
    return res

def update_from_symbol_list(symbol_list):
    print (1)

# type: #1:all,2:active
def fill_month_price_data(type):
    print (111)
    condition = [['has_month_price','=','0']]
    if type==2:
        condition.append(['stock_status', '=', "'c'"])
    symbol_list = get_symbols(condition)
    print (str(len(symbol_list))+' stock to fill data')

    r = get_m_price_data(symbol_list[0][0])
    insert_month_price_table(r)
    # for x in symbol_list:
    #     r = get_m_price_data(x[0])
    #     insert_month_price_table(r)
