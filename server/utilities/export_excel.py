import xlsxwriter
import lib.dbU
import config.fields_defenition

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
    skip_fields = ['bid','cid','ic_id','stock_symbol','Fstatus','Fmark','Fmodify_time','Finsert_time','Flastest_modify_time']
    bold = workbook.add_format({'bold': True})
    red = workbook.add_format({'color': 'red'})
    green = workbook.add_format({'color': 'green'})
    for sheet_data in data:
        skip_amount = 0
        sheet = workbook.add_worksheet(sheet_data['name'])
        sheet.set_column(0,len(sheet_data['field']), 21)
        for col_index in range(len(sheet_data['field'])):
            field_name = sheet_data['field'][col_index][0]
            if field_name not in skip_fields:
                sheet.write(0, col_index-skip_amount, field_name, bold) #title
                sheet.write(1, col_index-skip_amount, config.fields_defenition.get_dict(sheet_data['name'])[field_name][0] or '', bold) #cn_title
                sheet.write(2, col_index-skip_amount, config.fields_defenition.get_dict(sheet_data['name'])[field_name][1] or '', bold) #cn_title
                for row_index in range(len(sheet_data['data'])):
                    fixed_row_index = 3 if row_index ==0 else row_index*2+3
                    cur_cell_data = sheet_data['data'][row_index][col_index]
                    sheet.write(fixed_row_index, col_index-skip_amount, cur_cell_data)
                    if row_index < len(sheet_data['data'])-1:
                        prev_cell_data = sheet_data['data'][row_index+1][col_index]
                        diff = getRate(trans_type(cur_cell_data) - trans_type(prev_cell_data), abs(trans_type(prev_cell_data)))
                        color = red if diff >0 else green
                        sheet.write(fixed_row_index+1, col_index - skip_amount, str(diff)+'%', color)
            else:
                skip_amount+=1


    # Write a total using a formula.
    # income_statement.write(row, 0, 'Total')
    # income_statement.write(row, 1, '=SUM(B1:B4)')

    workbook.close();

def export_excel_with_symbol(symbol):
    balance_sheet_data = lib.dbU.select('balance_sheet_data', ['*'],[['stock_symbol', '=', "'"+symbol+"'"]], [], orderby='(report_year*10+report_month) desc')
    balance_sheet_field = lib.dbU.getTableFields('balance_sheet_data')
    cash_flow_data = lib.dbU.select('cash_flow_data', ['*'],[['stock_symbol', '=', "'"+symbol+"'"]], [], orderby='(report_year*10+report_month) desc')
    cash_flow_field = lib.dbU.getTableFields('cash_flow_data')
    income_statement_data = lib.dbU.select('income_statement_data', ['*'],[['stock_symbol', '=', "'"+symbol+"'"]], [], orderby='(report_year*10+report_month) desc')
    income_statement_field = lib.dbU.getTableFields('income_statement_data')
    rdata = [
        {'name':'balance_sheet','field':balance_sheet_field,'data':balance_sheet_data},
        {'name':'cash_flow_sheet','field':cash_flow_field,'data':cash_flow_data},
        {'name':'income_statement_sheet','field':income_statement_field,'data':income_statement_data},
    ]
    export(symbol, rdata)