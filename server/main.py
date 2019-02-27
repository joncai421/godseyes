import utilities.update_shock_table as ust
import utilities.update_month_price_data as umpd
import sys
if sys.argv[1] == '1':
    print ('---fill_shock_basic_info---')
    ust.fill_shock_basic_info()
elif sys.argv[1] == '2':
    print ('---fill_month_price_data:for all stock---')
    umpd.fill_month_price_data(1)#update for all stock
elif sys.argv[1] == '3':
    print ('---fill_month_price_data:for active stock---')
    umpd.fill_month_price_data(2)#update for active stock