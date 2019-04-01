import utilities.update_shock_table as ust
import utilities.update_month_price_data as umpd
import utilities.update_daily_price_data as udpd
import utilities.update_latest_daily_price_data as uldpd
import utilities.find_reverse as find_rev
import utilities.find_predict as find_pred
import utilities.find_go_up as fgu
import utilities.getReport as gr
import utilities.analyze_report as ar
import utilities.count_avg_volume as cag
import utilities.update_amplitude as ua
import utilities.update_latest_month_price_data as ulm
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
elif sys.argv[1] == '10':
    print ('---find_reverse---')
    find_rev.get_reverse_for_symbol(sys.argv[2],sys.argv[3])
elif sys.argv[1] == '11':
    print ('---find_predict_reverse---')
    find_pred.get_predict_for_symbol(sys.argv[2],sys.argv[3], 'rev')
elif sys.argv[1] == '12':
    print ('---find_predict---')
    find_pred.get_predict_for_symbol(sys.argv[2],sys.argv[3], 'not rev')
elif sys.argv[1] == '13':
    print ('---find_go_up---')
    fgu.find_go_up(sys.argv[2])
elif sys.argv[1] == '14':
    print ('---count_avg_volume---')
    cag.get_avg_volume(sys.argv[2])
elif sys.argv[1] == '15':
    print ('---count_avg_volume---')
    cag.volume_to_avg_rate(sys.argv[2])
elif sys.argv[1] == '16':
    print ('---uaupdate_amplitude_for_symbol---')
    ua.update_amplitude_for_symbol(sys.argv[2],sys.argv[3])
elif sys.argv[1] == '17':
    print ('---update_latest_month_price_data---')
    ulm.fill_month_price_data()