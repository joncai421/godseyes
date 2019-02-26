import requests
import lib.dbU

def get_index_data(index):
    url = 'http://rankandfiled.com/data/identifiers?start='+index
    print ('request url:'+url)
    result = requests.get(url).json()['list']
    return result

def get_existed_symbol():
    res = lib.dbU.select('stock_basic_info',['stock_symbol','cik'],[])
    stock_symbol_list = []
    for x in res:
        stock_symbol_list.append(x[0])
    return stock_symbol_list

def update_shock_basic_info():
    insert_list = []
    # existed_symbols = get_existed_symbol()
    index_Data = get_index_data('0')
    print (index_Data[0])