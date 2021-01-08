import threading
from datetime import date

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def partial(func, *part_args):
    def wrapper(*extra_args):
        args = list(part_args)
        args.extend(extra_args)
        return func(*args)

    return wrapper

def timestamp_to_datetime(time):
    return {
        'datetime':date.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S'),
        'fulldate':date.fromtimestamp(int(time)).strftime('%Y-%m-%d'),
        'year':date.fromtimestamp(int(time)).strftime('%Y'),
        'month':str(int(date.fromtimestamp(int(time)).strftime('%m'))),
        'date':str(int(date.fromtimestamp(int(time)).strftime('%d'))),
        'hour':date.fromtimestamp(int(time)).strftime('%H'),
        'mins':date.fromtimestamp(int(time)).strftime('%M'),
        'sec':date.fromtimestamp(int(time)).strftime('%S'),
    }

def trans_type(i):
    if isinstance(i, float):
        return i
    else:
        try:
            return float(i)
        except:
            return 0

def getDivided (a,b):
    a = trans_type(a)
    b = trans_type(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 2)