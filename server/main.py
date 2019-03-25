import utilities.update_shock_table as ust
import utilities.update_month_price_data as umpd
import utilities.update_daily_price_data as udpd
import utilities.update_latest_daily_price_data as uldpd
import utilities.getReport as gr
import utilities.analyze_report as ar
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
elif sys.argv[1] == '4':
    print ('---get report:for active stock---')
    gr.getReport()
elif sys.argv[1] == '5':
    print ('---cash flow data analyze update---')
    ar.update_analyze_cash_sheet()
elif sys.argv[1] == '6':
    print ('---balance sheet data analyze update---')
    ar.update_analyze_balance_sheet()
elif sys.argv[1] == '7':
    print ('---income sheet data analyze update---')
    ar.update_analyze_income_sheet()
elif sys.argv[1] == '8':
    print ('---update_daily_price_data:for all stock---')#insert all daily historical data
    udpd.fill_daily_price_data()
elif sys.argv[1] == '9':
    print ('---update_daily_price_data:for all stock---')#update all daily historical data
    uldpd.fill_daily_price_data()