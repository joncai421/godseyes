import xlsxwriter
import lib.dbU
import config.fields_defenition
import config.report_field_definition as r_field_definition

def trans_type(i):
    if isinstance(i, float):
        return i
    elif isinstance(i, str):
        return 0
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

def export (symbol,data):
    workbook = xlsxwriter.Workbook('asset/report_excel/'+symbol+'.xlsx')
    skip_fields = ['bid','cf_id','ic_id','stock_symbol','Flastest_modify_time','Fstatus']
    bold = workbook.add_format({'bold': True})
    red = workbook.add_format({'color': 'red'})
    green = workbook.add_format({'color': 'green'})
    for sheet_data in data:
        for t in sheet_data['data']:
            sheet_name = sheet_data['name'] + '_' + t
            skip_amount = 0
            sheet = workbook.add_worksheet(sheet_name)
            sheet.set_column(0,len(sheet_data['field']), 21)
            for col_index in range(len(sheet_data['field'])):
                field_name = sheet_data['field'][col_index][0]
                if field_name not in skip_fields:
                    name_on_page = r_field_definition.get_report_definition(sheet_data['name'])[field_name]['name_on_page'] if 'name_on_page' in r_field_definition.get_report_definition(sheet_data['name'])[field_name] else ''
                    cn_name = r_field_definition.get_report_definition(sheet_data['name'])[field_name]['cn_name'] if 'cn_name' in r_field_definition.get_report_definition(sheet_data['name'])[field_name] else ''
                    sheet.write(0, col_index-skip_amount, field_name, bold) #title
                    sheet.write(1, col_index-skip_amount, name_on_page, bold) #cn_title
                    sheet.write(2, col_index-skip_amount, cn_name, bold) #cn_title
                    for row_index in range(len(sheet_data['data'][t])):
                        fixed_row_index = 3 if row_index ==0 else row_index*2+3
                        cur_cell_data = sheet_data['data'][t][row_index][col_index]
                        sheet.write(fixed_row_index, col_index-skip_amount, cur_cell_data)
                        if row_index < len(sheet_data['data'][t])-1:
                            prev_cell_data = sheet_data['data'][t][row_index+1][col_index]
                            diff = getRate(trans_type(cur_cell_data) - trans_type(prev_cell_data), abs(trans_type(prev_cell_data)))
                            color = red if diff >0 else green
                            sheet.write(fixed_row_index+1, col_index - skip_amount, str(diff)+'%', color)
                else:
                    skip_amount+=1


    # Write a total using a formula.
    # income_statement.write(row, 0, 'Total')
    # income_statement.write(row, 1, '=SUM(B1:B4)')

    workbook.close();

def export_excel_with_symbol(symbol, isHK):
    if isHK == 'hk':
        database = 'hk'
    else:
        database = 'wallstreet'
    balance_sheet_data_annual = lib.dbU.select('balance_table', ['*'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type',' IN ', "('annual','ttm')"]], [], orderby='report_timestamp desc', db=database)
    balance_sheet_data_quarterly = lib.dbU.select('balance_table', ['*'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type',' IN ', "('quarterly','ttm')"]], [], orderby='report_timestamp desc', db=database)
    balance_sheet_field = lib.dbU.getTableFields('balance_table', db=database)
    cash_flow_data_annual = lib.dbU.select('cash_flow_table', ['*'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type',' IN ', "('annual','ttm')"]], [], orderby='report_timestamp desc', db=database)
    cash_flow_data_quarterly = lib.dbU.select('cash_flow_table', ['*'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type',' IN ', "('quarterly','ttm')"]], [], orderby='report_timestamp desc', db=database)
    cash_flow_field = lib.dbU.getTableFields('cash_flow_table', db=database)
    income_statement_data_annual = lib.dbU.select('income_sheet_table', ['*'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type',' IN ', "('annual','ttm')"]], [], orderby='report_timestamp desc', db=database)
    income_statement_data_quarterly = lib.dbU.select('income_sheet_table', ['*'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type',' IN ', "('quarterly','ttm')"]], [], orderby='report_timestamp desc', db=database)
    income_statement_field = lib.dbU.getTableFields('income_sheet_table', db=database)
    rdata = [
        {'name':'balance','field':balance_sheet_field,'data':{'annual': balance_sheet_data_annual,'quarterly': balance_sheet_data_quarterly}},
        {'name':'cash','field':cash_flow_field,'data':{'annual':cash_flow_data_annual,'quarterly':cash_flow_data_quarterly}},
        {'name':'income','field':income_statement_field,'data':{'annual':income_statement_data_annual,'quarterly':income_statement_data_quarterly}},
    ]
    export(symbol, rdata)