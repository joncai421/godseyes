import lib.dbU
import lib.tools

def get_trend_from_symbol(result_year, reverse_to_symbol):
    trend = []
    res = lib.dbU.select('daily_price_'+result_year, ['diff_rate','Pmonth','Pdate'], [['stock_symbol','=',"'"+reverse_to_symbol+"'"]], [])
    for r in res:
        diff_rate = float(r[0])
        Pmonth = str(r[1])
        Pdate = str(r[2])
        if diff_rate>=0.1:
            trend.append({'t':'<=','m':Pmonth,'d':Pdate,'p':'-0.1'})
        elif diff_rate<=-0.1:
            trend.append({'t':'>=','m':Pmonth,'d':Pdate,'p':'0.1'})
    return trend

def get_reverse_for_symbol(result_year, reverse_to_symbol):
    reverse_map = {}
    result_map = {}
    trend = get_trend_from_symbol(result_year, reverse_to_symbol)
    trend_number = int(len(trend))
    for tr in trend:
        res = lib.dbU.select('daily_price_' + result_year, ['stock_symbol'],[['diff_rate', tr['t'], tr['p']],['Pmonth','=',tr['m']],['Pdate','=',tr['d']]], [])
        for r in res:
            symbol = r[0]
            if symbol not in reverse_map:
                reverse_map[symbol] =1
            else:
                reverse_map[symbol]+=1
    for r in reverse_map:
        if reverse_map[r] >trend_number/3:
            if str(reverse_map[r]) in result_map:
                result_map[str(reverse_map[r])].append(r)
            else:
                result_map[str(reverse_map[r])] = [r]

    print (result_map)


