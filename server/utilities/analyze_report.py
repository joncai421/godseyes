import lib.dbU
import time
import requests
import random

def getDivided (a,b):
    a = a if isinstance(a, float) else float(a)
    b = b if isinstance(b, float) else float(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 4)

def update_analyze_cash_sheet():
    res = lib.dbU.select('cash_flow_data',[
        'cash_flow_data.stock_symbol',
        'cash_flow_data.cid',
        'cash_flow_data.depreciation',
        'cash_flow_data.capitalExpenditures',
        'balance_sheet_data.totalAssets',
        'income_statement_data.netIncome',
        'cash_flow_data.repurchaseOfStock',
    ],[
        ['cash_flow_data.report_year','=','balance_sheet_data.report_year'],
        ['cash_flow_data.report_year','=','income_statement_data.report_year'],
        ['cash_flow_data.report_month','=','income_statement_data.report_month'],
        ['cash_flow_data.report_month','=','balance_sheet_data.report_month'],
        ['cash_flow_data.report_type','=','balance_sheet_data.report_type'],
        ['cash_flow_data.report_type','=','income_statement_data.report_type'],
        ['cash_flow_data.capitalExpenditures_rate2','=','0'],
        # ['cash_flow_data.Fstatus','=','0'],
       ],[
        ['balance_sheet_data', 'cash_flow_data.stock_symbol', '=', 'balance_sheet_data.stock_symbol'],
        ['income_statement_data','cash_flow_data.stock_symbol', '=', 'income_statement_data.stock_symbol'],
    ], db='hk')

    for index in range(len(res)):
        symbol = res[index][0]
        cid = res[index][1]
        depreciation = int(res[index][2])
        capitalExpenditures = abs(int(res[index][3]))
        totalAssets = int(res[index][4])
        netIncome = int(res[index][5])
        repurchaseOfStock = int(res[index][6])
        depreciation_rate = getRate(depreciation,totalAssets)
        capitalExpenditures_rate = getRate(capitalExpenditures,netIncome)
        capitalExpenditures_rate2 = getRate(capitalExpenditures-abs(repurchaseOfStock),netIncome)
        repurchaseOfStock_rate = getRate(abs(repurchaseOfStock),netIncome)
        print ('update_iterate :' + symbol + ',index:' + str(index + 1) + ' of ' + str(len(res)))
        lib.dbU.update('cash_flow_data', {'repurchaseOfStock_rate':repurchaseOfStock_rate,'capitalExpenditures_rate2':capitalExpenditures_rate2,'depreciation_rate': str(depreciation_rate),'capitalExpenditures_rate':str(capitalExpenditures_rate),'Fstatus':'1'}, {'cid': cid}, db='hk')

def update_analyze_balance_sheet():
    res = lib.dbU.select('balance_sheet_data',[
        'balance_sheet_data.stock_symbol',
        'balance_sheet_data.bid',
        'balance_sheet_data.totalLiab',
        'balance_sheet_data.totalAssets',
        'balance_sheet_data.netReceivables',
        'balance_sheet_data.totalCurrentAssets',
        'balance_sheet_data.totalStockholderEquity',
        'balance_sheet_data.totalCurrentLiabilities',
        'balance_sheet_data.retainedEarnings',
        'income_statement_data.netIncome',
    ],[
        ['balance_sheet_data.report_year', '=', 'income_statement_data.report_year'],
        ['balance_sheet_data.report_month', '=', 'income_statement_data.report_month'],
        ['balance_sheet_data.report_type', '=', 'income_statement_data.report_type'],
        ['balance_sheet_data.Fstatus', '=', '0'],
    ],[
        ['income_statement_data', 'income_statement_data.stock_symbol', '=', 'balance_sheet_data.stock_symbol'],
    ], db='hk')

    for index in range(len(res)):
        symbol = res[index][0]
        bid = res[index][1]
        totalLiab = int(res[index][2])
        totalAssets = abs(int(res[index][3]))
        netReceivables = int(res[index][4])
        totalCurrentAssets = int(res[index][5])
        totalStockholderEquity = int(res[index][6])
        totalCurrentLiabilities = int(res[index][7])
        retainedEarnings = int(res[index][8])
        netIncome = int(res[index][9])
        debtRatio = getRate(totalLiab,totalAssets)
        receivables_rate = getRate(netReceivables,totalAssets)
        current_ratio = getRate(totalCurrentAssets,totalCurrentLiabilities)
        total_debt_to_equity_ratio = getRate(totalLiab,totalStockholderEquity)
        retainedEarnings_rate = getRate(retainedEarnings,netIncome)

        print ('update_iterate :' + symbol + ',index:' + str(index + 1) + ' of ' + str(len(res)))
        lib.dbU.update('balance_sheet_data', {'debtRatio': str(debtRatio),'receivables_rate':str(receivables_rate),'current_ratio':str(current_ratio),'total_debt_to_equity_ratio':str(total_debt_to_equity_ratio),'retainedEarnings_rate':retainedEarnings_rate,'Fstatus':'1'}, {'bid': bid}, db='hk')

def update_analyze_income_sheet():
    res = lib.dbU.select('income_statement_data',[
        'income_statement_data.stock_symbol',
        'income_statement_data.ic_id',
        'income_statement_data.grossProfit',
        'income_statement_data.totalRevenue',
        'income_statement_data.researchDevelopment',
        'income_statement_data.netIncome',
        'income_statement_data.sellingGeneralAdministrative',
        'income_statement_data.costOfRevenue',
        'income_statement_data.interestExpense',
        'stock_basic_info.share_capital'
    ],[
        ['income_statement_data.Fstatus','=','0'],
       ],[
        ['stock_basic_info', 'income_statement_data.stock_symbol', '=', 'stock_basic_info.stock_symbol'],
    ], db='hk')

    for index in range(len(res)):
        symbol = res[index][0]
        ic_id = res[index][1]
        grossProfit = int(res[index][2])
        totalRevenue = abs(int(res[index][3]))
        researchDevelopment = int(res[index][4])
        netIncome = int(res[index][5])
        sellingGeneralAdministrative = int(res[index][6])
        costOfRevenue = int(res[index][7])
        interestExpense = int(res[index][8])
        share_capital = int(res[index][9])
        GrossProfitMargin = getRate(grossProfit,totalRevenue)
        research_cost_rate = getRate(researchDevelopment,totalRevenue)
        NetInterestRate = getRate(netIncome,totalRevenue)
        SGA_Rate = getRate(sellingGeneralAdministrative,totalRevenue)
        costOfRevenue_Rate = getRate(costOfRevenue,totalRevenue)
        interest_Rate = getRate(interestExpense,totalRevenue)
        Earnings_per_share = getDivided(netIncome,share_capital)
        print ('update_iterate :' + symbol + ',index:' + str(index + 1) + ' of ' + str(len(res)))
        lib.dbU.update('income_statement_data', {'GrossProfitMargin': str(GrossProfitMargin),'research_cost_rate':str(research_cost_rate),
                                                 'NetInterestRate': str(NetInterestRate),'SGA_Rate':str(SGA_Rate),
                                                 'costOfRevenue_Rate': str(costOfRevenue_Rate),'interest_Rate':str(interest_Rate),
                                                 'Earnings_per_share':str(Earnings_per_share),'Fstatus':'1'}, {'ic_id': ic_id}, db='hk')
