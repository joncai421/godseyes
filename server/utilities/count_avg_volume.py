import time
import lib.dbU
from calendar import monthrange

def getDivided (a,b):
    a = a if isinstance(a, float) else float(a)
    b = b if isinstance(b, float) else float(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 4)

def get_avg_volume(year):
    trand_days_in_month = {}
    for i in range(1,13):
        d = lib.dbU.select('daily_price_' + year, ['dp_id'],[['Pmonth', '=', "'" + str(i) + "'"], ['stock_symbol', '=', "'DJI'"]], [])
        trand_days_in_month[str(i)] = len(d)
    res = lib.dbU.select('month_price_'+year, ['*'], [['price_type','=',"'volume'"]], [])
    for r in range(len(res)):
        print ('update_iterate :' + res[r][1] + ',index:' + str(r + 1) + ' of ' + str(len(res)))
        in_obj = {'stock_symbol':res[r][1],'price_type':'avg_volume','day':0,'total':0,"Finsert_time":time.strftime('%Y-%m-%d %H:%M:%S'),"Fmodify_time":time.strftime('%Y-%m-%d %H:%M:%S'),"Flastest_modify_time":time.strftime('%Y-%m-%d %H:%M:%S'),}
        for i in range(2,14):
            m_volume = int(res[r][i])
            month = i-1
            # days_in_month = monthrange(int(year), month)[1]
            in_obj['m'+str(month)] =getDivided(m_volume,trand_days_in_month[str(month)])
        lib.dbU.insert('month_price_'+year, [in_obj])

def volume_to_avg_rate(year):
    avg_volume_map = {}
    mv = lib.dbU.select('month_price_' + year, ['*'], [['price_type', '=', "'avg_volume'"]], [])
    # mv = lib.dbU.select('month_price_' + year, ['*'], [['price_type', '=', "'avg_volume'"]], [])
    for m in mv:
        avg_volume_map[m[1]] = {}
        for i in range(2, 14):
            month = i - 1
            avg_volume_map[m[1]]['m'+str(month)] = m[i]

    # res = lib.dbU.select('daily_price_' + year, ['dp_id','stock_symbol','Pri_volume','Pmonth'], [['stock_symbol','=',"'FHL'"]], [])
    res = lib.dbU.select('daily_price_' + year, ['dp_id','stock_symbol','Pri_volume','Pmonth'], [], [])
    for r in range(len(res)):
        dp_id = res[r][0]
        symbol = res[r][1]
        Pri_volume = res[r][2]
        Pmonth = res[r][3]
        print ('update_iterate :' + symbol + ',index:' + str(r + 1) + ' of ' + str(len(res)))
        if symbol in avg_volume_map and 'm'+str(Pmonth) in avg_volume_map[symbol] and getRate(Pri_volume,avg_volume_map[symbol]['m'+str(Pmonth)])>0:
            month_avg_vo = avg_volume_map[symbol]['m'+str(Pmonth)]
            lib.dbU.update('daily_price_' + year, {'volume_to_avg_rate':getRate(Pri_volume,month_avg_vo)}, {'dp_id': dp_id})

# SELECT * FROM `month_price_2019` where stock_symbol='FHL';
# SELECT volume_to_avg_rate FROM `daily_price_2019` where stock_symbol='FHL';