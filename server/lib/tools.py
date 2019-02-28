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
        'year':date.fromtimestamp(int(time)).strftime('%Y'),
        'month':str(int(date.fromtimestamp(int(time)).strftime('%m'))),
        'day':str(int(date.fromtimestamp(int(time)).strftime('%d'))),
        'hour':date.fromtimestamp(int(time)).strftime('%H'),
        'mins':date.fromtimestamp(int(time)).strftime('%M'),
        'sec':date.fromtimestamp(int(time)).strftime('%S'),
    }