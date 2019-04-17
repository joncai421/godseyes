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
    res = lib.dbU.select('stock_basic_info',['stock_symbol'],condition,[], db='hk')
    return res

def getPage(symbol):
    url = 'https://hk.finance.yahoo.com/quote/'+symbol+'.HK/financials?p='+symbol+'.HK'
    try:
        response = urllib.request.urlopen(url, timeout=5)
        result = response.read().decode('utf-8')
        # print(result)
        match = re.search(r'(root\.App\.main).*', result)
        if match:
            try:
                match = match.group(0)
                match = match.replace('root.App.main =', '')
                match = match.replace('root.App.main=', '')
                mlen = len(match)
                if match[mlen - 1] == ";":
                    match = match[0:mlen - 1]
                match = json.loads(match)
            except:
                print ('json convert failed')
                match = {}
            return match
        else:
            return {}
    except:
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
                                    if field not in sheet_obj:
                                        print ('1--------------------------')
                                        print (symbol)
                                        print (table_name)
                                        print (field)
                                        print ('2--------------------------')
                                    sheet_obj[field] = report[field]['raw'] if 'raw' in report[field] else 0
                            sheet_obj['report_type'] = report_type
                            # sheet_obj['Finsert_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                            # sheet_obj['Fmodify_time'] = time.strftime('%Y-%m-%d %H:%M:%S')
                            # sheet_obj['Flastest_modify_time']=time.strftime('%Y-%m-%d %H:%M:%S')
                            timeObj = lib.tools.timestamp_to_datetime(report['endDate']['raw'])
                            sheet_obj['report_year'] = timeObj['year']
                            sheet_obj['report_month'] = timeObj['month']
                            sheet_obj['report_date'] = timeObj['date']
                            # if len(sheet_obj.keys())==34:
                            #     print (888)
                            #     print (table_name)
                            #     print (sheet_obj.keys())

                            insert_obj[table_name].append(sheet_obj)
                            hasReport = 1

            for table in insert_obj:
                if len(insert_obj[table])>0:
                    lib.dbU.insert(table, insert_obj[table], db='hk')
            lib.dbU.update('stock_basic_info', {'hasReport': hasReport}, {'stock_symbol': symbol}, db='hk')
        else:
            print ('reportObj invalid')
            lib.dbU.update('stock_basic_info', {'hasReport': '-1'}, {'stock_symbol': symbol}, db='hk')
        # time.sleep(random.randint(2, 5))

def getReport():
    condition = [['hasReport', '=', '0'],['stock_status', '=', '"c"']]
    # condition = [['hasReport', '=', '0'],['up2015to2018', '=', '1'],['fid%2','!=','0']]
    # condition = [['hasReport', '=', '0'],['up2015to2018', '=', '1']]
    # condition = [['hasReport', '=', '0'],['up2015to2019', '=', '1']]
    symbol_list = get_symbols(condition)
    print (str(len(symbol_list)) + ' stock to fill data')
    if int(len(symbol_list)) > 0:
        # update_iterate([['ATO']])
        update_iterate(symbol_list)
    else:
        print ('---task completed---')


