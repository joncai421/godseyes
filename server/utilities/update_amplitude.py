import lib.dbU

def getDivided (a,b):
    a = a if isinstance(a, float) else float(a)
    b = b if isinstance(b, float) else float(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 8)

def update_amplitude_for_symbol(symbol, year):
    res = lib.dbU.select('daily_price_' + year, ['dp_id','Pri_last_close', 'Pri_high', 'Pri_low','Pri_open'],[['stock_symbol', '=', "'" + symbol + "'"],['Pri_amplitude_total','=','0']], [])
    for r in range(len(res)):
        print ('update_iterate :' + symbol + ',index:' + str(r + 1) + ' of ' + str(len(res)))
        dp_id = res[r][0]
        Pri_last_close = float(res[r][1])
        Pri_high = float(res[r][2])
        Pri_low = float(res[r][3])
        Pri_open = float(res[r][4])
        Pri_amplitude_high = getRate(Pri_high-Pri_open,Pri_open)
        Pri_amplitude_low = getRate(Pri_open-Pri_low,Pri_open)
        Pri_amplitude_total = Pri_amplitude_high+Pri_amplitude_low
        lib.dbU.update('daily_price_' + year, {'Pri_amplitude_high': Pri_amplitude_high,'Pri_amplitude_low': Pri_amplitude_low,'Pri_amplitude_total': Pri_amplitude_total,},{'dp_id': dp_id})
    print ('-----completed-----')