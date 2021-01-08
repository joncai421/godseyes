import glob
import copy
import json
import lib.dbU
import lib.tools
import config.report_field_definition as r_field_definition
import time
import random

def remove_dot_from_symbol():
    error_symbols = {}
    checked_symbols = []
    duplicated_symbols = []
    valid = 0
    res = lib.dbU.select('stock_basic_info', ['fid','stock_symbol'], [['stock_symbol',' like ',"'%.%'"]], [])
    print(len(res))
    for r in res:
        fid = r[0]
        symbol = r[1]
        fixed_symbol = symbol.replace('.NASDAQ','')
        fixed_symbol = fixed_symbol.replace('.NYSE','')
        fixed_symbol = fixed_symbol.replace('.','')
        lib.dbU.update('stock_basic_info', {'hasReport': -4, 'stock_symbol': fixed_symbol}, {'fid': fid})

def get_symbols():
    a = []
    # res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [], [], db='hk')
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['hasReport', '=', '33']], [])
    for r in res:
        a.append(r[0])
    print(len(a))
    print(a)

def check_valid2():
    file_list_symbols = []
    report_files = glob.glob("asset/premium_report_txt/report_*.txt")
    for f in report_files:
        symbol = f.split('/')[2].replace('.txt', '').split('_')[1]
        if symbol not in file_list_symbols:
            file_list_symbols.append(symbol)

    symbol_in_db = []
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['hasReport', '=', '-3']], [])
    for r in res:
        symbol_in_db.append(r[0])

    print(len(file_list_symbols))
    print(len(symbol_in_db))
    print(list(set(file_list_symbols) - set(symbol_in_db)))
    s = set(file_list_symbols)
    temp3 = [x for x in symbol_in_db if x not in s]
    print(temp3)


def check_valid():
    error_symbols = {}
    checked_symbols = []
    duplicated_symbols = []
    valid = 0
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['hasReport', '=', '-3']], [])
    print(len(res))
    for r in res:
        symbol = r[0]
        report_files = glob.glob("asset/premium_report_txt/report_"+symbol+"_*.txt")
        if len(report_files)!=6:
            error_symbols[symbol] = len(report_files)
            print(symbol)
        else:
            valid = valid+1

        if symbol in checked_symbols:
            duplicated_symbols.append(symbol)
        else:
            checked_symbols.append(symbol)

    print(error_symbols)
    print(len(checked_symbols))
    print(duplicated_symbols)
    print(valid)

def getFieldNameAndValue (obj):
    if 'type' in obj:
        return {'name':obj['type'], 'value':[]}
    elif 'type' in obj['meta'] and len(obj['meta']['type']) and obj['meta']['type'][0] in obj:
        field_name = obj['meta']['type'][0]
        isTTM = 'trailing' in field_name
        field_value = obj[field_name] if field_name in obj else []
        if isTTM:
            return {'name': field_name, 'value': field_value, 'timestamp': obj['timestamp'][0]}
        else:
            return {'name':field_name,'value':field_value}
    else:
        return {'name': obj['meta']['type'][0], 'value': []}

def getFieldtype(field_list):
    for f in field_list:
        if f is not None:
            origin_value = f['reportedValue']['raw']
            fixed_value = int(origin_value) if int(origin_value) == float(origin_value) else origin_value
            vtype = type(fixed_value)
            return {'data_type':str(vtype).replace("<class '",'').replace("'>",""), 'default_value': '' if vtype == 'string' else 0}
    return None

def genFieldKeyFromReport():
    table_map = {'balance_annual':{}, 'banlance_quaterly':{}, 'income_quaterly':{}, 'income_annual':{}, 'cash_quaterly':{}, 'cash_annual':{}}
    types = ['balance_annual', 'banlance_quaterly', 'income_quaterly', 'income_annual', 'cash_quaterly', 'cash_annual']
    for t in types:
        # map[t] = {}
        report_file = "asset/premium_report_txt/report_V_" + t + ".txt"
        file = open(report_file, "r")
        report_json = json.loads(file.read())
        file.close()
        for field in report_json['timeseries']['result']:
            field_data = getFieldNameAndValue(field)
            table_map[t][field_data['name']] = getFieldtype(field_data['value'])
    print(table_map)

def read_value_analyse():
    # p=['MU','LX', 'ALXN']
    report_file = glob.glob("asset/value_analyse/value_analyse_*.txt")
    map = {}
    result = {}
    outlook = []
    list = []
    i = 0
    for f in report_file:
        file = open(f, "r")
        report_json = json.loads(file.read())
        file.close()
        symbol = f.split('/')[2].replace('.txt', '').split('_')[2]
        # print(symbol)
        if 'finance' in report_json and 'result' in report_json['finance'] and 'valuationDescription' in report_json['finance']['result'] and 'outlook' in report_json['finance']['result'] and 'priceBookRatio' in report_json['finance']['result']:
            ol = report_json['finance']['result']['outlook'].replace('%','')
            priceBookRatio = report_json['finance']['result']['priceBookRatio']#市净率
            peRatio = report_json['finance']['result']['peRatio']#市盈率
            if report_json['finance']['result']['valuationDescription'] == "Undervalued" and 0 < peRatio < 25 and int(ol)>30:
            # if report_json['finance']['result']['valuationDescription'] == "Undervalued" and int(ol)>70 and priceBookRatio <3 and peRatio < 17 and peRatio > 0:
                if ol not in map:
                    map[ol] = []
                # if symbol in p:
                map[ol].append(symbol)
                outlook.append(int(ol))
                list.append(symbol)
                i = i + 1
    outlook.sort()
    outlook = {}.fromkeys(outlook).keys()
    for o in outlook:
        result[str(o)] = map[str(o)]
    print(i)
    print(result)
    print(' \r\n \r\n')
    print(list)

def get_active_symbols():
    report_file = glob.glob("asset/premium_report_txt_HK/report_*_income_annual.txt")
    valid_symbols = []
    invalid_symbols = []
    outdated_symbols = []
    for f in report_file:
        file = open(f, "r")
        report_json = json.loads(file.read())
        file.close()
        valid = 0
        symbol = f.split('/')[2].replace('.txt', '').split('_')[1]
        if 'timeseries' in report_json and 'result' in report_json['timeseries'] and len(report_json['timeseries']['result']):
            # print(11)
            for field in report_json['timeseries']['result']:
                # print(22)
                if 'annualTotalRevenue' in field:
                    # print(33)
                    if field['timestamp'] and len(field['timestamp']) > 0:
                        # print(44)
                        latest_report_time = field['timestamp'][len(field['timestamp']) - 1]  # e.g.1569801600
                        report_year = lib.tools.timestamp_to_datetime(latest_report_time)['year']
                        if int(report_year) >= 2018:
                            # print(66)
                            valid = 1
                            break
                        else:
                            # print(77)
                            valid = 2
                            break
                    else:
                        # print(55)
                        break
        if valid == 0:
            # print(symbol)
            invalid_symbols.append(symbol)
        elif valid ==1:
            valid_symbols.append(symbol)
        else:
            outdated_symbols.append(symbol)
    print('----------------invalid_symbols------------------------')
    print(len(invalid_symbols))
    print(invalid_symbols)
    print(' \r\n \r\n')
    print('----------------outdated_symbols------------------------')
    print(len(outdated_symbols))
    print(outdated_symbols)
    print(' \r\n \r\n')
    print('----------------valid_symbols------------------------')
    print(len(valid_symbols))
    print(valid_symbols)

def get_default_obj (symbol, type):
    fr = r_field_definition.get_report_definition(type)
    o = {'stock_symbol': symbol}
    for r in fr:
        o[r] = fr[r]['default_value']
    return o

def initial_timestamp(symbol, robj, field_value, report_type, time_type):
    timestamps = []
    for f in field_value:
        if 'timestamp' in f:
            field_name = f['meta']['type'][0]
            isTTM = 'trailing' in field_name
            timestamp = f['timestamp']
            if not isTTM:
                timestamps.append(len(timestamp))
            for t in timestamp:
                d = lib.tools.timestamp_to_datetime(t)
                fulldate = d['fulldate']
                if isTTM:
                    robj[report_type]['ttm']['report_timestamp'] = t
                    robj[report_type]['ttm']['report_datetime'] = fulldate
                    robj[report_type]['ttm']['report_year'] = d['year']
                    robj[report_type]['ttm']['report_month'] = d['month']
                    robj[report_type]['ttm']['report_date'] = d['date']
                    robj[report_type]['ttm']['report_type'] = 'ttm'
                else:
                    if fulldate not in robj[report_type][time_type]:
                        robj[report_type][time_type][fulldate] = get_default_obj(symbol, report_type)
                        robj[report_type][time_type][fulldate]['report_timestamp'] = t
                        robj[report_type][time_type][fulldate]['report_datetime'] = fulldate
                        robj[report_type][time_type][fulldate]['report_year'] = d['year']
                        robj[report_type][time_type][fulldate]['report_month'] = d['month']
                        robj[report_type][time_type][fulldate]['report_date'] = d['date']
                        robj[report_type][time_type][fulldate]['report_type'] = time_type
    l = {}.fromkeys(timestamps).keys()
    if len(l) >1:
        print('------------'+symbol+'--'+report_type+'---'+time_type+'---timestamp error-----------')
        print(timestamps)

def sheets_formating (rmap):
    types = ['balance_quarterly', 'balance_annual', 'cash_quarterly', 'cash_annual', 'cash_ttm', 'income_quarterly', 'income_annual', 'income_ttm']
    insert_list = {'income_sheet_table':[],'balance_table':[],'cash_flow_table':[]}
    total_asset_list = []
    for sheet_type in types:
        report_type = sheet_type.split('_')[0]
        time_type = sheet_type.split('_')[1]
        if time_type == 'ttm':
            sheet_data={rmap[report_type][time_type]['report_datetime']:rmap[report_type][time_type]}
        else:
            sheet_data = rmap[report_type][time_type]
        if report_type == 'balance':
            retainedEarnings_history_list = []
            count = 0
            for sheetOfYear in sheet_data:
                s = sheet_data[sheetOfYear]
                report_datetime = s['report_datetime']
                s['debtRatio'] = lib.tools.getRate(s['TotalLiabilitiesNetMinorityInterest'], s['TotalAssets'])
                s['LongTermDebt_ratio'] = lib.tools.getRate(s['LongTermDebt'], s['TotalAssets'])
                s['current_ratio'] = lib.tools.getRate(s['CurrentLiabilities'], s['CurrentAssets'])
                s['total_debt_to_equity_ratio'] = lib.tools.getRate(s['TotalLiabilitiesNetMinorityInterest'], s['StockholdersEquity'])
                s['quickRatio'] = lib.tools.getRate(s['CurrentAssets']-s['Inventory'], s['CurrentLiabilities'])
                s['cashRatio'] = lib.tools.getRate(s['CashCashEquivalentsAndMarketableSecurities'], s['CurrentAssets'])
                s['BookValue'] = s['TotalAssets'] - s['TotalLiabilitiesNetMinorityInterest'] - s['OtherIntangibleAssets']
                s['receivables_rate'] = s['TotalAssets'] - s['TotalLiabilitiesNetMinorityInterest'] - s['OtherIntangibleAssets']

                if report_datetime in rmap['income'][time_type]:
                    related_income_sheet = rmap['income'][time_type][report_datetime]
                    s['LongDebtToOprtInc_ratio'] = lib.tools.getRate(s['LongTermDebt'], related_income_sheet['OperatingIncome'])
                    if count -1 >=0 and count<len(retainedEarnings_history_list):
                        s['retainedEarnings_rate'] = lib.tools.getRate(s['RetainedEarnings']-retainedEarnings_history_list[count-1], related_income_sheet['NetIncome'])

                count+=1
                retainedEarnings_history_list.append(s['RetainedEarnings'])
                total_asset_list.append(int(s['TotalAssets']))
                insert_list['balance_table'].append(s)

        elif report_type == 'cash':
            for sheetOfYear in sheet_data:
                s = sheet_data[sheetOfYear]
                report_datetime = s['report_datetime']
                if report_datetime in rmap['income'][time_type]:
                    related_income_sheet = rmap['income'][time_type][report_datetime]
                    s['buybackRatio'] = lib.tools.getRate(s['RepurchaseOfCapitalStock'], related_income_sheet['NetIncome'])
                    s['OpertCashToFCF_ratio'] = lib.tools.getRate(s['OperatingCashFlow'], s['FreeCashFlow'])
                    if report_datetime in rmap['income'][time_type]:
                        s['capitalExpenditures_rate'] = lib.tools.getRate(s['CapitalExpenditure'], related_income_sheet['NetIncome'])
                        s['capitalExpenditures_rate'] = lib.tools.getRate(s['CapitalExpenditure'] - abs(s['RepurchaseOfCapitalStock']), related_income_sheet['NetIncome'])

                insert_list['cash_flow_table'].append(s)
        elif report_type == 'income':
            count = 0
            for sheetOfYear in sheet_data:
                s = sheet_data[sheetOfYear]
                report_datetime = s['report_datetime']
                s['taxRate'] = lib.tools.getRate(s['TaxProvision'], s['PretaxIncome'])
                s['GrossProfitMargin'] = lib.tools.getRate(s['GrossProfit'], s['TotalRevenue'])
                s['NetInterestRate'] = lib.tools.getRate(s['NetIncome'], s['TotalRevenue'])
                s['research_cost_rate'] = lib.tools.getRate(s['ResearchAndDevelopment'], s['TotalRevenue'])
                s['SGA_Rate'] = lib.tools.getRate(s['SellingGeneralAndAdministration'], s['TotalRevenue'])
                s['costOfRevenue_Rate'] = lib.tools.getRate(s['CostOfRevenue'], s['TotalRevenue'])
                s['share_capital'] = lib.tools.getRate(s['NetIncome'], s['BasicEPS'])
                s['NOPAT'] = s['OperatingIncome'] * (1-(s['taxRate']/100))
                s['ebitdaToRevRatio'] = lib.tools.getRate(s['Ebitda'], s['TotalRevenue'])
                s['NOPATtoTotRevRatio'] = lib.tools.getRate(s['NOPAT'], s['TotalRevenue'])
                if report_datetime in rmap['cash'][time_type]:
                    related_cash_sheet = rmap['cash'][time_type][report_datetime]
                    s['Ebit'] = s['Ebitda'] - related_cash_sheet['DepreciationAndAmortization']
                    s['InterestCoverageRatio'] = lib.tools.getRate(s['Ebit'], s['InterestExpense'])
                    s['DaOfEbitda'] = lib.tools.getRate(related_cash_sheet['DepreciationAndAmortization'], s['Ebitda'])

                if time_type != 'ttm' and report_datetime in rmap['balance'][time_type]:
                    related_balance_sheet = rmap['balance'][time_type][report_datetime]
                    current_total_asset = int(related_balance_sheet['TotalAssets'])
                    index = total_asset_list.index(current_total_asset)
                    s['pretaxIncomeAssetsRate'] = lib.tools.getRate(s['PretaxIncome'], current_total_asset)
                    s['ROE'] = lib.tools.getRate(s['NetIncome'], related_balance_sheet['StockholdersEquity'])
                    s['interest_Rate'] = lib.tools.getRate(s['InterestExpense'], related_balance_sheet['TotalLiabilitiesNetMinorityInterest'])
                    if index >0:
                        s['ROA'] = lib.tools.getRate(s['NetIncome'], (current_total_asset + total_asset_list[index - 1]) / 2)

                count+=1
                insert_list['income_sheet_table'].append(s)

    return insert_list

def txt2DB():
    print('-------------program start----------------')
    types = ['balance_quarterly', 'balance_annual', 'cash_quarterly', 'cash_annual', 'income_quarterly', 'income_annual']
    # res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['stock_symbol', ' IN ', "('V','HSY')"]], [])
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['hasReport','=','33']], [])
    count = 0
    l = len(res)
    for r in res:
        symbol = r[0]
        print(symbol+',  '+str(count)+' of ' +str(l))
        rmap = {'balance':{'annual':{},'quarterly':{}},'cash':{'annual':{},'quarterly':{}, 'ttm':get_default_obj(symbol, 'cash')},'income':{'annual':{},'quarterly':{}, 'ttm':get_default_obj(symbol, 'income')}}
        for sheet_type in types:
            suffix = 'banlance_quaterly' if sheet_type == 'balance_quarterly' else sheet_type.replace('quarterly','quaterly')
            report_file = "asset/premium_report_txt_HK/report_"+symbol+"_"+suffix+".txt"
            file = open(report_file, "r")
            report_json = json.loads(file.read())
            file.close()
            report_type = sheet_type.split('_')[0]
            time_type = 'quarterly' if 'quaterly' in sheet_type.split('_')[1] else sheet_type.split('_')[1]
            if 'timeseries' in report_json and 'result' in report_json['timeseries'] and len(
                    report_json['timeseries']['result']):
                initial_timestamp(symbol, rmap, report_json['timeseries']['result'], report_type, time_type)
                for field in report_json['timeseries']['result']:
                    field_data = getFieldNameAndValue(field)
                    field_name_in_txt = field_data['name']
                    isTTM = 'trailing' in field_name_in_txt
                    field_name_to_db = field_name_in_txt.replace('trailing', '').replace(time_type, '')
                    fixed_time_type = 'ttm' if isTTM else time_type
                    field_value = field_data['value']
                    for f in field_value:
                        if f is not None:
                            if isTTM:
                                if rmap[report_type][fixed_time_type]['report_timestamp'] == 0:
                                    rmap[report_type][fixed_time_type][field_name_to_db] = f['reportedValue']['raw']
                                else:
                                    timestamp = field_data['timestamp']
                                    if time_type == 'annual' and timestamp > rmap[report_type][fixed_time_type]['report_timestamp'] or time_type == 'quarterly':
                                        rmap[report_type][fixed_time_type][field_name_to_db] = f['reportedValue']['raw']
                            elif 'reportedValue' in f and 'raw' in f['reportedValue']:
                                rmap[report_type][fixed_time_type][f['asOfDate']][field_name_to_db] = f['reportedValue']['raw']
        insert_list = sheets_formating(rmap)
        # print(rmap)
        # print(insert_list)
        for t in insert_list:
            lib.dbU.insert(t, insert_list[t])
        count+=1

def genCreateTable():
    fr = r_field_definition.get_report_definition('cash')
    r = []
    for f in fr:
        type = "bigint(65) NOT NULL DEFAULT '0'" if fr[f]['data_type'] == 'int' else "double(65,11) NOT NULL DEFAULT '0.00000000000'" if fr[f]['data_type'] == 'float' else "varchar(255) NOT NULL DEFAULT ''" if fr[f]['data_type'] == 'string' else "date NOT NULL DEFAULT '0000-00-00'"
        s= '`' + f+ '` '+type
        r.append(s)
    print(',\r\n'.join(r))

def update_report_tables():
    # res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['hasReport', '=', '33']], [])
    res = lib.dbU.select('income_sheet_table', [' DISTINCT stock_symbol'], [['NOPATtoTotRevRatio', '=', '0']], [])
    # res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['stock_symbol', ' IN ', "('V')"]], [])
    count = 0
    l = len(res)
    for r in res:
        symbol = r[0]
        print(symbol + ',  ' + str(count) + ' of ' + str(l))
        balance_table_data = lib.dbU.select('income_sheet_table', ['ic_id','NOPAT','TotalRevenue'], [['stock_symbol', '=', "'" + symbol + "'"]], [])
        for bt in balance_table_data:
            icid = bt[0]
            NOPAT = bt[1]
            TotalRevenue = bt[2]
            update_balance_obj = {'NOPATtoTotRevRatio':lib.tools.getRate(NOPAT, TotalRevenue)}
            lib.dbU.update('income_sheet_table', update_balance_obj, {'ic_id': icid})
        count+=1