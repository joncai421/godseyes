import lib.dbU
import lib.tools
import datetime

def find_top_three (index_list, map):
    sort_list = list(dict.fromkeys(index_list))
    sort_list.sort(reverse = True)
    result = {}
    result[str(sort_list[0])] = map[str(sort_list[0])]
    result[str(sort_list[1])] = map[str(sort_list[1])]
    result[str(sort_list[2])] = map[str(sort_list[2])]
    return result

def get_trend_from_symbol(result_year, reverse_to_symbol, type):
    trend = []
    res = lib.dbU.select('daily_price_'+result_year, ['diff_rate','Pmonth','Pdate'], [['stock_symbol','=',"'"+reverse_to_symbol+"'"]], [])
    for r in res:
        diff_rate = float(r[0])
        Pmonth = int(r[1])
        Pdate = int(r[2])
        d = datetime.datetime(int(result_year), Pmonth, Pdate)
        # prev_date = datetime.date.strftime(date - datetime.timedelta(1), '%Y-%m-%d')
        prev_date = str((d - datetime.timedelta(1)).day)
        prev_month = str((d - datetime.timedelta(1)).month)
        trend1 = '<=' if type =='rev' else '>='
        trend2 = '>=' if type =='rev' else '<='
        if diff_rate>=0.1:
            trend.append({'t':trend1,'m':prev_month,'d':prev_date,'p':'-0.1'})
        elif diff_rate<=-0.1:
            trend.append({'t':trend2,'m':prev_month,'d':prev_date,'p':'0.1'})
    return trend

def get_predict_for_symbol(result_year, reverse_to_symbol, type):
    reverse_map = {}
    result_map = {}
    trend = get_trend_from_symbol(result_year, reverse_to_symbol, type)
    trend_number = int(len(trend))
    for tr in trend:
        res = lib.dbU.select('daily_price_' + result_year, ['stock_symbol'],[['diff_rate', tr['t'], tr['p']],['Pmonth','=',tr['m']],['Pdate','=',tr['d']]], [])
        for r in res:
            symbol = r[0]
            if symbol not in reverse_map:
                reverse_map[symbol] =1
            else:
                reverse_map[symbol]+=1
    index_list = []
    for r in reverse_map:
        # if reverse_map[r] >=trend_number/2:
        index_list.append(reverse_map[r])
        if str(reverse_map[r]) in result_map:
            result_map[str(reverse_map[r])].append(r)
        else:
            result_map[str(reverse_map[r])] = [r]
    top3 = find_top_three(index_list,result_map)

    print (result_map)
    print ('---------')
    print (top3)
    print ('trend_number:'+str(trend_number))
    print ('type:'+type)
    print ('result_year:'+result_year)
    print ('reverse_to_symbol:'+reverse_to_symbol)


