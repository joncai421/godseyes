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

cookieProcessor = urllib.request.HTTPCookieProcessor()
opener = urllib.request.build_opener(cookieProcessor)
#sulotion for error: urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed---
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#------

#premium cookie:
#thamba=2; thamba=2; APID=UP4cb49ffa-44d5-11ea-b845-06c47f77dfdf; APIDTS=1580713302; PH=fn=eEYl6vvsppBziRMc&l=en-US; Y=v=1&n=1m1ns3a5a7thr&l=1s59pggo59iuf365tc8d8u8fah7cv9xlel4pm5fj/o&p=02qvvvv00000000&r=16f&intl=us; AO=u=1; GUCS=Af5TjKua; A1S=d=AQABBBwMKF4CEKqtb8cnQJlGfNR38HUuqjUFEgEAAQIaOV4KX9x0rXYB_SMAAAcIHAwoXnUuqjUID6hgelzVIAivH4_v7DCBbgkBBwoBlQ&S=AQAAAr1ESoGMh2gx5_704d2QRew; B=3baheelf2g30s&b=4&d=hi7gp8BtYFlFcjdDFTYl&s=pu&i=qGB6XNUgCK8fj._sMIFu; GUC=AQEAAQJeORpfCkIfhgRq; cmp=t=1580715317&j=0; PRF=t%3DV%252B%255EIXIC%252B%255EGSPC%252BFB%252BKO%252BGM%252BJPM%252BHSY%252BCIB%252BADC%252BGS%252BTME%252BAXP%252BAAON%252BBRKB%26qsp-fnncls-cue%3D1"

#premium data:(vaild premium user login cookie required)
#annual banlance:
#https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=annualTotalAssets%2CtrailingTotalAssets%2CannualStockholdersEquity%2CtrailingStockholdersEquity%2CannualGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CannualRetainedEarnings%2CtrailingRetainedEarnings%2CannualCapitalStock%2CtrailingCapitalStock%2CannualTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CannualTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CannualOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CannualNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CannualNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CannualLongTermDebt%2CtrailingLongTermDebt%2CannualCurrentLiabilities%2CtrailingCurrentLiabilities%2CannualOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CannualCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CannualCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CannualIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CannualAccountsPayable%2CtrailingAccountsPayable%2CannualCurrentDebt%2CtrailingCurrentDebt%2CannualTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CannualOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CannualOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CannualGoodwill%2CtrailingGoodwill%2CannualInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CannualNetPPE%2CtrailingNetPPE%2CannualAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CannualGrossPPE%2CtrailingGrossPPE%2CannualCurrentAssets%2CtrailingCurrentAssets%2CannualOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CannualInventory%2CtrailingInventory%2CannualAccountsReceivable%2CtrailingAccountsReceivable%2CannualCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CannualOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CannualCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1580725608&corsDomain=finance.yahoo.com
#quarterly banlance:
#https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=quarterlyTotalAssets%2CtrailingTotalAssets%2CquarterlyStockholdersEquity%2CtrailingStockholdersEquity%2CquarterlyGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CquarterlyRetainedEarnings%2CtrailingRetainedEarnings%2CquarterlyCapitalStock%2CtrailingCapitalStock%2CquarterlyTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CquarterlyTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CquarterlyOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CquarterlyNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CquarterlyNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CquarterlyLongTermDebt%2CtrailingLongTermDebt%2CquarterlyCurrentLiabilities%2CtrailingCurrentLiabilities%2CquarterlyOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CquarterlyCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CquarterlyCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CquarterlyIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CquarterlyAccountsPayable%2CtrailingAccountsPayable%2CquarterlyCurrentDebt%2CtrailingCurrentDebt%2CquarterlyTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CquarterlyOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CquarterlyOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CquarterlyGoodwill%2CtrailingGoodwill%2CquarterlyInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CquarterlyNetPPE%2CtrailingNetPPE%2CquarterlyAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CquarterlyGrossPPE%2CtrailingGrossPPE%2CquarterlyCurrentAssets%2CtrailingCurrentAssets%2CquarterlyOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CquarterlyInventory%2CtrailingInventory%2CquarterlyAccountsReceivable%2CtrailingAccountsReceivable%2CquarterlyCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CquarterlyOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CquarterlyCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1580726454&corsDomain=finance.yahoo.com

#quarterly cash flow:
#https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=quarterlyFreeCashFlow%2CtrailingFreeCashFlow%2CquarterlyCapitalExpenditure%2CtrailingCapitalExpenditure%2CquarterlyOperatingCashFlow%2CtrailingOperatingCashFlow%2CquarterlyEndCashPosition%2CtrailingEndCashPosition%2CquarterlyBeginningCashPosition%2CtrailingBeginningCashPosition%2CquarterlyChangeInCashSupplementalAsReported%2CtrailingChangeInCashSupplementalAsReported%2CquarterlyCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CquarterlyNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CquarterlyCashDividendsPaid%2CtrailingCashDividendsPaid%2CquarterlyRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CquarterlyCommonStockIssuance%2CtrailingCommonStockIssuance%2CquarterlyRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CquarterlyInvestingCashFlow%2CtrailingInvestingCashFlow%2CquarterlyNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CquarterlySaleOfInvestment%2CtrailingSaleOfInvestment%2CquarterlyPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CquarterlyPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CquarterlyOtherNonCashItems%2CtrailingOtherNonCashItems%2CquarterlyChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CquarterlyChangeInInventory%2CtrailingChangeInInventory%2CquarterlyChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CquarterlyChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CquarterlyStockBasedCompensation%2CtrailingStockBasedCompensation%2CquarterlyDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CquarterlyDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CquarterlyNetIncome%2CtrailingNetIncome&merge=false&period1=493590046&period2=1580726233&corsDomain=finance.yahoo.com
#annual cash flow:
#https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=annualFreeCashFlow%2CtrailingFreeCashFlow%2CannualCapitalExpenditure%2CtrailingCapitalExpenditure%2CannualOperatingCashFlow%2CtrailingOperatingCashFlow%2CannualEndCashPosition%2CtrailingEndCashPosition%2CannualBeginningCashPosition%2CtrailingBeginningCashPosition%2CannualChangeInCashSupplementalAsReported%2CtrailingChangeInCashSupplementalAsReported%2CannualCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CannualNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CannualCashDividendsPaid%2CtrailingCashDividendsPaid%2CannualRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CannualCommonStockIssuance%2CtrailingCommonStockIssuance%2CannualRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CannualInvestingCashFlow%2CtrailingInvestingCashFlow%2CannualNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CannualSaleOfInvestment%2CtrailingSaleOfInvestment%2CannualPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CannualPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CannualOtherNonCashItems%2CtrailingOtherNonCashItems%2CannualChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CannualChangeInInventory%2CtrailingChangeInInventory%2CannualChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CannualChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CannualStockBasedCompensation%2CtrailingStockBasedCompensation%2CannualDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CannualDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CannualNetIncome%2CtrailingNetIncome&merge=false&period1=493590046&period2=1580726340&corsDomain=finance.yahoo.com

#annual income:
#https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=annualEbitda%2CtrailingEbitda%2CannualWeighteAverageShare%2CtrailingWeighteAverageShare%2CannualDilutedAverageShares%2CtrailingDilutedAverageShares%2CannualBasicAverageShares%2CtrailingBasicAverageShares%2CannualearningsPerShare%2CtrailingearningsPerShare%2CannualDilutedEPS%2CtrailingDilutedEPS%2CannualBasicEPS%2CtrailingBasicEPS%2CannualNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CannualNetIncome%2CtrailingNetIncome%2CannualNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CannualTaxProvision%2CtrailingTaxProvision%2CannualPretaxIncome%2CtrailingPretaxIncome%2CannualOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CannualInterestExpense%2CtrailingInterestExpense%2CannualOperatingIncome%2CtrailingOperatingIncome%2CannualOperatingExpense%2CtrailingOperatingExpense%2CannualSellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CannualResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CannualGrossProfit%2CtrailingGrossProfit%2CannualCostOfRevenue%2CtrailingCostOfRevenue%2CannualTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580726527&corsDomain=finance.yahoo.com
#quarterly income:
#https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=quarterlyEbitda%2CtrailingEbitda%2CquarterlyWeighteAverageShare%2CtrailingWeighteAverageShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyearningsPerShare%2CtrailingearningsPerShare%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580726564&corsDomain=finance.yahoo.com

#fixed quarterly income sheet report:(non-premuim)
#https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=quarterlyEbitda%2CtrailingEbitda%2CquarterlyWeighteAverageShare%2CtrailingWeighteAverageShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyearningsPerShare%2CtrailingearningsPerShare%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580745554&corsDomain=finance.yahoo.com

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
def getDivided (a,b):
    a = a if isinstance(a, float) else float(a)
    b = b if isinstance(b, float) else float(b)
    if a == 0 or b == 0:
        return 0
    else:
        return a / b

def getRate (a,b):
    return round(getDivided(a,b)*100, 4)

def get_symbols (isUpdate):
    if isUpdate:
        # condition = [['stock_basic_info.stock_symbol', ' IN ', " ('V', 'MA','AXP','BRKB','BRKA','TRV','HSY') "]]
        # condition = [['stock_basic_info.stock_symbol', ' IN ', " ('V') "]]
        condition = [['stock_basic_info.hasReport', '=', '1']]
        res = lib.dbU.select('stock_basic_info',
                             ['stock_basic_info.stock_symbol',
                              'income_statement_data.report_year',
                              'income_statement_data.report_month',
                              'income_statement_data.report_type',
                              ],
                             condition, [
                                 ['income_statement_data', 'stock_basic_info.stock_symbol', '=',
                                  'income_statement_data.stock_symbol']
                             ])
        stock_map = {}
        for r in res:
            stock_symbol = r[0]
            report_year = r[1]
            report_month = r[2]
            report_type = r[3]
            if stock_symbol not in stock_map:
                stock_map[stock_symbol] = {'a':{'y':0,'m':0},'q':{'y':0,'m':0}}
                stock_map[stock_symbol][report_type] = {'y':report_year,'m':report_month}
            elif is_valid_time(report_year, report_month, stock_map[stock_symbol][report_type]['y'], stock_map[stock_symbol][report_type]['m']):
                stock_map[stock_symbol][report_type] = {'y': report_year, 'm': report_month}

        stock_list = []
        for s in stock_map:
            stock_list.append([s, stock_map[s]['a']['y'], stock_map[s]['a']['m'], stock_map[s]['q']['y'], stock_map[s]['q']['m']])
        return stock_list
    else:
        condition = [['stock_basic_info.has_daily_price', '=', '1']]
        res = lib.dbU.select('stock_basic_info', ['stock_symbol'],condition)
        return res

def getPage(symbol):
    url = 'https://finance.yahoo.com/quote/'+symbol+'/financials?p='+symbol
    try:
        response = urllib.request.urlopen(url)
        # response = urllib.request.urlopen(url, timeout=5)
        # response = opener.open(url)
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

def formatingData (table_name, sheet_obj):
    # ------------------------balance_sheet_data----------------------------
    if table_name == 'balance_sheet_data':
        # fix bug in yahoo's data
        if int(sheet_obj['totalAssets']) - int(sheet_obj['totalLiab']) != int(sheet_obj['totalStockholderEquity']):
            fixed_totalStockholderEquity = int(sheet_obj['totalAssets']) - int(sheet_obj['totalLiab'])
            if sheet_obj['commonStock'] == 0:
                sheet_obj['commonStock'] = fixed_totalStockholderEquity - sheet_obj['totalStockholderEquity']
            sheet_obj['totalStockholderEquity'] = fixed_totalStockholderEquity

        sheet_obj['totalNonCurrentLiabilities'] = sheet_obj['totalLiab'] - sheet_obj['totalCurrentLiabilities']
        sheet_obj['total_cash'] = sheet_obj['cash'] - sheet_obj['shortTermInvestments']
        sheet_obj['debtRatio'] = getRate(sheet_obj['totalLiab'], sheet_obj['totalAssets'])
        sheet_obj['receivables_rate'] = getRate(sheet_obj['netReceivables'], sheet_obj['totalAssets'])
        sheet_obj['current_ratio'] = getRate(sheet_obj['totalCurrentAssets'], sheet_obj['totalCurrentLiabilities'])
        sheet_obj['total_debt_to_equity_ratio'] = getRate(sheet_obj['totalLiab'], sheet_obj['totalStockholderEquity'])
        # sheet_obj['retainedEarnings_rate'] = getRate(sheet_obj['retainedEarnings'], assit_table_obj['netIncome'])

    # ------------------------ cash_flow_data ----------------------------
    if table_name == 'cash_flow_data':
        sheet_obj['FreeCashFlow'] = sheet_obj['totalCashFromOperatingActivities'] + sheet_obj['capitalExpenditures']
        # sheet_obj['depreciation_rate'] = getRate(sheet_obj['depreciation'], assit_table_obj['totalAssets'])
        sheet_obj['capitalExpenditures_rate'] = getRate(sheet_obj['capitalExpenditures'], sheet_obj['netIncome'])
        sheet_obj['capitalExpenditures_rate2'] = getRate(sheet_obj['capitalExpenditures'] - abs(sheet_obj['repurchaseOfStock']), sheet_obj['netIncome'])
        sheet_obj['repurchaseOfStock_rate'] = getRate(abs(sheet_obj['repurchaseOfStock']), sheet_obj['netIncome'])

    # ------------------------income_statement_data----------------------------
    if table_name == 'income_statement_data':
        sheet_obj['GrossProfitMargin'] = getRate(sheet_obj['grossProfit'], sheet_obj['totalRevenue'])
        sheet_obj['research_cost_rate'] = getRate(sheet_obj['researchDevelopment'], sheet_obj['totalRevenue'])
        sheet_obj['NetInterestRate'] = getRate(sheet_obj['netIncome'], sheet_obj['totalRevenue'])
        sheet_obj['SGA_Rate'] = getRate(sheet_obj['sellingGeneralAdministrative'], sheet_obj['totalRevenue'])
        sheet_obj['costOfRevenue_Rate'] = getRate(sheet_obj['costOfRevenue'], sheet_obj['totalRevenue'])
        sheet_obj['interest_Rate'] = getRate(sheet_obj['interestExpense'], sheet_obj['totalRevenue'])
        sheet_obj['share_capital'] = getRate(sheet_obj['netIncome'], sheet_obj['Earnings_per_share'])

    return sheet_obj

def get_new_income_data(incomesheetData, fixedIncomeReportObj, insert_obj):
    trailing_data = copy.deepcopy(incomesheetData[0])
    for annual_income in incomesheetData:
        new_income_object = copy.deepcopy(annual_income)
        month = new_income_object['report_month'] if len(new_income_object['report_month'])>1 else '0'+new_income_object['report_month']
        date = new_income_object['report_date'] if len(new_income_object['report_date'])>1 else '0'+new_income_object['report_date']
        report_date = new_income_object['report_year']+'-'+month+'-'+date
        for key in fixedIncomeReportObj:
            if len(fixedIncomeReportObj[key])>0:
                if key[0] == 'a':
                    field = config.sheet_default_value.get_sheet_default_value('income_sheet_trans')[key.replace('annual','')]
                    if field:
                        for i in fixedIncomeReportObj[key]:
                            if 'asOfDate' in i and i['asOfDate'] == report_date:
                                new_income_object[field] = i['reportedValue']['raw']
                elif key[0] == 't' and key!='timestamp':
                    field = config.sheet_default_value.get_sheet_default_value('income_sheet_trans')[key.replace('trailing','')]
                    trailing_data[field] = fixedIncomeReportObj[key][0]['reportedValue']['raw']
        new_income_object = formatingData('income_statement_data', new_income_object)
        insert_obj['income_statement_data_new'].append(new_income_object)
    trailing_data = formatingData('income_statement_data', trailing_data)
    trailing_data['report_type'] = 't'
    insert_obj['income_statement_data_new'].append(trailing_data)

def update_iterate(symbol_list, isUpdate):
    global sheets_tables
    hasReport = -1
    for index in range(len(symbol_list)):
        insert_obj = {'cash_flow_data':[],'balance_sheet_data':[],'income_statement_data':[]}
        symbol = symbol_list[index][0]
        income_table_data = []
        latest_annual_report_year = symbol_list[index][1] or 0
        latest_annual_report_month = symbol_list[index][2] or 0
        latest_quaterly_report_year = symbol_list[index][3] or 0
        latest_quaterly_report_month = symbol_list[index][4] or 0

        print ('update_iterate :' + symbol + ',index:' + str(index + 1) + ' of ' + str(len(symbol_list)))
        page_data = getPage(symbol)
        if 'context' in page_data and 'dispatcher' in page_data['context'] and 'stores' in page_data['context'][
            'dispatcher'] and 'QuoteSummaryStore' in page_data['context']['dispatcher']['stores']:
            reportObj = page_data['context']['dispatcher']['stores']['QuoteSummaryStore']
            fixedIncomeReportObj = page_data['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries']
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
                            timeObj = lib.tools.timestamp_to_datetime(report['endDate']['raw'])
                            sheet_obj['report_year'] = timeObj['year']
                            sheet_obj['report_date'] = timeObj['date']
                            sheet_obj['report_month'] = timeObj['month']

                            sheet_obj = formatingData(table_name, sheet_obj)

                            if table_name == 'income_statement_data' and report_type == 'a':
                                income_table_data.append(sheet_obj)

                            if isUpdate:
                                latest_report_year = latest_annual_report_year if report_type == 'a' else latest_quaterly_report_year
                                latest_report_month = latest_annual_report_month  if report_type == 'a' else latest_quaterly_report_month
                                if is_valid_time(sheet_obj['report_year'], sheet_obj['report_month'], latest_report_year, latest_report_month):
                                    insert_obj[table_name].append(sheet_obj)
                            else:
                                insert_obj[table_name].append(sheet_obj)
                                hasReport = 1

            #fill new_income_statement_data
            # get_new_income_data(income_table_data, fixedIncomeReportObj, insert_obj)

            for table in insert_obj:
                if len(insert_obj[table])>0:
                    lib.dbU.insert(table, insert_obj[table])
            if not isUpdate:
                lib.dbU.update('stock_basic_info', {'hasReport': hasReport}, {'stock_symbol': symbol})
        else:
            print ('reportObj invalid')
            if not isUpdate:
                lib.dbU.update('stock_basic_info', {'hasReport': '-1'}, {'stock_symbol': symbol})
        # time.sleep(random.randint(2, 5))

def getReport(isUpdate):
    symbol_list = get_symbols(isUpdate)
    print (str(len(symbol_list)) + ' stock to fill data')
    if int(len(symbol_list)) > 0:
        update_iterate(symbol_list, isUpdate)
    else:
        print ('---task completed---')


