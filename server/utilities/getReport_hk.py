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

def is_valid_time(this_report_year, this_report_month, latest_report_year, latest_report_month):
    if int(this_report_year) > int(latest_report_year):
        return True
    elif int(this_report_year) == int(latest_report_year):
        if int(this_report_month) > int(latest_report_month):
            return True
        else:
            return False
    else:
        return False

def get_symbols (isUpdate):
    if isUpdate:
        # condition = [['stock_basic_info.stock_symbol', ' IN ', " ('0700', '0701') "]]
        condition = [['stock_basic_info.hasReport', '=', '1']]
        res = lib.dbU.select('stock_basic_info',
                             ['stock_basic_info.stock_symbol',
                              'income_statement_data.report_year',
                              'income_statement_data.report_month'],
                             condition, [
                                 ['income_statement_data', 'stock_basic_info.stock_symbol', '=',
                                  'income_statement_data.stock_symbol']
                             ], db='hk')
        stock_map = {}
        for r in res:
            stock_symbol = r[0]
            report_year = r[1]
            report_month = r[2]
            if stock_symbol not in stock_map:
                stock_map[stock_symbol] = {'y':report_year,'m':report_month}
            elif is_valid_time(report_year, report_month, stock_map[stock_symbol]['y'], stock_map[stock_symbol]['m']):
                stock_map[stock_symbol] = {'y': report_year, 'm': report_month}

        stock_list = []
        for s in stock_map:
            stock_list.append([s, stock_map[s]['y'], stock_map[s]['m']])
        return stock_list
    else:
        condition = [['stock_basic_info.has_daily_price', '=', '1']]
        res = lib.dbU.select('stock_basic_info', ['stock_symbol'],condition,[], db='hk')
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


def update_iterate(symbol_list, isUpdate):
    global sheets_tables
    hasReport = -1
    for index in range(len(symbol_list)):
        insert_obj = {'cash_flow_data':[],'balance_sheet_data':[],'income_statement_data':[]}
        symbol = symbol_list[index][0]
        latest_report_year = symbol_list[index][1] or 0
        latest_report_month = symbol_list[index][2] or 0
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
                            for field in report:
                                if field != 'maxAge':
                                    sheet_obj[field] = report[field]['raw'] if 'raw' in report[field] else 0
                            sheet_obj['report_type'] = report_type
                            timeObj = lib.tools.timestamp_to_datetime(report['endDate']['raw'])
                            sheet_obj['report_year'] = timeObj['year']
                            sheet_obj['report_month'] = timeObj['month']
                            sheet_obj['report_date'] = timeObj['date']

                            if isUpdate:
                                if is_valid_time(sheet_obj['report_year'], sheet_obj['report_month'],latest_report_year, latest_report_month):
                                    insert_obj[table_name].append(sheet_obj)
                                # else:
                                #     print ('---no new report to update---')
                            else:
                                insert_obj[table_name].append(sheet_obj)
                                hasReport = 1

            for table in insert_obj:
                if len(insert_obj[table])>0:
                    lib.dbU.insert(table, insert_obj[table], db='hk')
            if not isUpdate:
                lib.dbU.update('stock_basic_info', {'hasReport': hasReport}, {'stock_symbol': symbol}, db='hk')
        else:
            print ('reportObj invalid')
            if not isUpdate:
                lib.dbU.update('stock_basic_info', {'hasReport': '-1'}, {'stock_symbol': symbol}, db='hk')
        # time.sleep(random.randint(2, 5))

def getReport(isUpdate):
    symbol_list = get_symbols(isUpdate)
    print (str(len(symbol_list)) + ' stock to fill data')
    if int(len(symbol_list)) > 0:
        update_iterate(symbol_list, isUpdate)
    else:
        print ('---task completed---')


