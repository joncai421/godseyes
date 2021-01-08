import glob
import copy
import json
import lib.dbU
import lib.tools
import config.report_field_definition as r_field_definition
import time
import random

def isIncreased (table_data, listOfFields):
    l = len(table_data)
    increase = True
    for d in range(l):
        for f in listOfFields:
            if d +1 <l:
                index = listOfFields.index(f)
                # print(999)
                # print(table_data[d])
                # print(table_data[d+1])
                # print(index)
                # print(f)
                # print(listOfFields)
                # print(table_data[d][index])
                # print(table_data[d+1][index])
                if table_data[d][index] < table_data[d+1][index]:
                    return False
    return increase

def get_grow_sq_fcf():
    list = []
    compare_period = 3
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['up2015to2019', '=', '888'],['hasReport', '=', '33']], [])
    # res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['up2015to2019', '=', '888'],['hasReport', '=', '33']], [])
    # cash_compare_field = ['FreeCashFlow']
    cash_compare_field = ['BeginningCashPosition','EndCashPosition','FreeCashFlow']
    balance_compare_field = ['BookValue','StockholdersEquity','RetainedEarnings']
    # balance_compare_field = ['StockholdersEquity']
    balance_compare_field = ['BookValue','StockholdersEquity']
    # income_compare_field = ['NetIncome']
    income_compare_field = ['NOPAT','pretaxIncomeAssetsRate']
    for r in res:
        symbol = r[0]
        cash_statement = lib.dbU.select('cash_flow_table', cash_compare_field, [['stock_symbol', '=', "'" + symbol + "'"],['report_type',' IN ', "('annual')"]], [], orderby='report_timestamp desc', limit=compare_period, nolog=True)
        balance_sheet = lib.dbU.select('balance_table', balance_compare_field, [['stock_symbol', '=', "'" + symbol + "'"],['report_type',' IN ', "('annual')"]], [], orderby='report_timestamp desc', limit=compare_period, nolog=True)
        income_sheet = lib.dbU.select('income_sheet_table', income_compare_field, [['stock_symbol', '=', "'" + symbol + "'"],['report_type',' IN ', "('annual')"]], [], orderby='report_timestamp desc', limit=compare_period, nolog=True)
        isCashIncreased = isIncreased(cash_statement,cash_compare_field)
        isBalanceIncreased = isIncreased(balance_sheet,balance_compare_field)
        isIncomeIncreased = isIncreased(income_sheet,income_compare_field)
        if isCashIncreased == isBalanceIncreased == isIncomeIncreased ==True:
            list.append(symbol)
    print(list)

def get_grow_sq_fcf():
    list = []
    compare_period = 3
    res = lib.dbU.select('stock_basic_info', ['stock_symbol'], [['up2015to2019', '=', '6666'],['hasReport', '=', '33']], [])
    cash_compare_field = ['BeginningCashPosition','EndCashPosition','FreeCashFlow']
    balance_compare_field = ['BookValue','StockholdersEquity','RetainedEarnings']
    # balance_compare_field = ['StockholdersEquity']
    balance_compare_field = ['BookValue','StockholdersEquity']
    # income_compare_field = ['NetIncome']
    income_compare_field = ['NOPAT','pretaxIncomeAssetsRate']
    for r in res:
        symbol = r[0]
        cash_statement = lib.dbU.select('cash_flow_table', cash_compare_field, [['stock_symbol', '=', "'" + symbol + "'"],['report_type',' IN ', "('annual')"]], [], orderby='report_timestamp desc', limit=compare_period, nolog=True)
        balance_sheet = lib.dbU.select('balance_table', balance_compare_field, [['stock_symbol', '=', "'" + symbol + "'"],['report_type',' IN ', "('annual')"]], [], orderby='report_timestamp desc', limit=compare_period, nolog=True)
        income_sheet = lib.dbU.select('income_sheet_table', income_compare_field, [['stock_symbol', '=', "'" + symbol + "'"],['report_type',' IN ', "('annual')"]], [], orderby='report_timestamp desc', limit=compare_period, nolog=True)
        isCashIncreased = isIncreased(cash_statement,cash_compare_field)
        isBalanceIncreased = isIncreased(balance_sheet,balance_compare_field)
        isIncomeIncreased = isIncreased(income_sheet,income_compare_field)
        if isCashIncreased == isBalanceIncreased == isIncomeIncreased ==True:
            list.append(symbol)
    print(list)