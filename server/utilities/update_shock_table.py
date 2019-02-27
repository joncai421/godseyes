import requests
import time
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

def fill_shock_basic_info():
    insert_list = []
    existed_symbols = get_existed_symbol()

    for index in range(0,13696, 99):
    # for index in range(0,13762, 50):
        index_data = get_index_data(str(index))
        for d in index_data:
            s = d.split("|")
            row_data = {'stock_symbol':s[0] or '',
                        'exchange':s[1] or '',
                        'industry':s[2] or '',
                        'cik':s[3] or 0,
                        'stock_name':s[4] or '',
                        'irs':s[5] or '0',
                        'business_area':s[6] or '',
                        'incorporated':s[7] or '',
                        'stock_status':s[8] or '',
                        'op_status':0,
                        'Finsert_time':time.strftime('%Y-%m-%d %H:%M:%S'),
                        'Fmodify_time':time.strftime('%Y-%m-%d %H:%M:%S'),
                        'request_index':index or -1,
                        }
            if row_data['stock_symbol'] in existed_symbols:
                # row_data={}
                print ('stock_symbol:'+row_data['stock_symbol']+' has already existed. skip to next.')
            else:
                existed_symbols.append(row_data['stock_symbol'])
                insert_list.append(row_data)

    print ('insert into stock_basic_info with '+str(len(insert_list))+' records')
    lib.dbU.insert('stock_basic_info',insert_list)