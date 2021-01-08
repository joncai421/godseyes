import lib.dbU
import lib.tools
def get_all_symbol(result_year):
    up_map = {}
    res = lib.dbU.select('daily_price_'+result_year, ['stock_symbol'], [['diff_rate','>','0']], [])
    for r in res:
        stock_symbol = r[0]
        if stock_symbol in up_map:
            up_map[stock_symbol]+=1
        else :
            up_map[stock_symbol] = 1
    return up_map

def get_trend_days(result_year):
    res = lib.dbU.select('daily_price_' + result_year, ['stock_symbol'], [['stock_symbol', '=', "'DJI'"]], [])
    return len(res)

def find_go_up(result_year):
    res = get_all_symbol(result_year)
    trend_days = int(get_trend_days(result_year))
    print ('trend_days:'+str(trend_days))
    result_map={}
    for r in res:
        if res[r] >trend_days*0.8:
            if str(res[r]) in result_map:
                result_map[str(res[r])].append(r)
            else:
                result_map[str(res[r])] = [r]

    print (result_map)


