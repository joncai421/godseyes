# window.App.main.context.dispatcher.stores.QuoteSummaryStore
#  --> "cashflowStatementHistory"
#  --> "cashflowStatementHistoryQuarterly"
#  --> "balanceSheetHistoryQuarterly"
#  --> "balanceSheetHistory"
#  --> "incomeStatementHistoryQuarterly"
#  --> "incomeStatementHistory"
#  --> "earnings"
#  --> "price"
#  --> "quoteType"
#  --> "summaryDetail"
#  --> "symbol"
#  --> "pageViews"
import lib.dbU
import lib.tools
import config.sheet_default_value
import time
import urllib.request
import re
import random
import copy
import json
sheets_tables={'cashflowStatementHistory':{'table':'cash_flow_data','type':'a','index':'cashflowStatements'},
               'cashflowStatementHistoryQuarterly':{'table':'cash_flow_data','type':'q','index':'cashflowStatements'},
               'balanceSheetHistoryQuarterly':{'table':'balance_sheet_data','type':'q','index':'balanceSheetStatements'},
               'balanceSheetHistory':{'table':'balance_sheet_data','type':'a','index':'balanceSheetStatements'},
               'incomeStatementHistoryQuarterly':{'table':'income_statement_data','type':'q','index':'incomeStatementHistory'},
               'incomeStatementHistory':{'table':'income_statement_data','type':'a','index':'incomeStatementHistory'},
               }

def get_symbols (condition):
    res = lib.dbU.select('stock_basic_info',['stock_symbol'],condition)
    return res

def getPage(symbol):
    url = 'https://finance.yahoo.com/quote/AAPL/financials?p='+symbol
    response = urllib.request.urlopen(url)
    result = response.read().decode('utf-8')
    # print(result)
    match = re.search(r'(root\.App\.main).*', result)
    if match:
        try:
            match = match.group(0)
            match= match.replace('root.App.main =', '')
            match= match.replace('root.App.main=', '')
            mlen = len(match)
            if match[mlen-1]==";":
                match = match[0:mlen-1]
            match = json.loads(match)
        except:
            print ('json convert failed')
            match={}
        return match
    else:
        return {}

def update_iterate(symbol_list):
    global sheets_tables
    hasReport = -1
    for index in range(len(symbol_list)):
        insert_obj = {'cash_flow_data':[],'balance_sheet_data':[],'income_statement_data':[]}
        symbol = symbol_list[index][0]
        print ('update_iterate :' + symbol + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        reportObj = getPage(symbol)
        if 'context' in reportObj and 'dispatcher' in reportObj['context'] and 'stores' in reportObj['context'][
            'dispatcher'] and 'QuoteSummaryStore' in reportObj['context']['dispatcher']['stores']:
            reportObj = reportObj['context']['dispatcher']['stores']['QuoteSummaryStore']
            for sheets in reportObj:
                if sheets in sheets_tables:
                    table_name = sheets_tables[sheets]['table']
                    report_type = sheets_tables[sheets]['type']
                    index = sheets_tables[sheets]['index']
                    if index in reportObj[sheets]:
                        for report in reportObj[sheets][index]:
                            sheet_obj = copy.deepcopy(config.sheet_default_value.get_sheet_default_value(index))
                            sheet_obj['stock_symbol'] = symbol
                            # print ('--------'+sheets+'_'+index+'--------')
                            # print (report)
                            for field in report:
                                if field != 'maxAge':
                                    sheet_obj[field] = report[field]['raw'] if 'raw' in report[field] else 0
                            sheet_obj['report_type'] = report_type
                            # sheet_obj['Finsert_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                            # sheet_obj['Fmodify_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                            # sheet_obj['Flastest_modify_time']=time.strftime('%Y-%m-%d %H:%M:%S')
                            timeObj = lib.tools.timestamp_to_datetime(report['endDate']['raw'])
                            sheet_obj['year'] = timeObj['year']
                            sheet_obj['month'] = timeObj['month']
                            sheet_obj['date'] = timeObj['date']
                            # if len(sheet_obj.keys())==34:
                            #     print (888)
                            #     print (table_name)
                            #     print (sheet_obj.keys())

                            insert_obj[table_name].append(sheet_obj)
                            hasReport = 1

            for table in insert_obj:
                if len(insert_obj[table])>0:
                    lib.dbU.insert(table, insert_obj[table])
            lib.dbU.update('stock_basic_info', {'hasReport': hasReport}, {'stock_symbol': symbol})
        else:
            print ('reportObj invalid')
        # time.sleep(random.randint(2, 5))

def getReport():
    condition = [['hasReport', '=', '0'],['has_month_price', '=', '1']]
    # condition = [['hasReport', '=', '0'],['up2015to2019', '=', '1']]
    symbol_list = get_symbols(condition)
    print (str(len(symbol_list)) + ' stock to fill data')
    if int(len(symbol_list)) > 0:
        # update_iterate([['ATO']])
        update_iterate(symbol_list)
    else:
        print ('---task completed---')


