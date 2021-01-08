import copy
import json
import lib.dbU
import lib.tools
import config.report_field_definition as r_field_definition
import time
import requests
import random

requests.adapters.DEFAULT_RETRIES = 5
session = requests.session()
session.keep_alive = False

def get_request_url(symbol, type, isPremuim):
    if type=='balance_annual':
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'.HK?lang=en-US&region=US&symbol='+symbol+'.HK&padTimeSeries=true&type=annualTotalAssets%2CtrailingTotalAssets%2CannualStockholdersEquity%2CtrailingStockholdersEquity%2CannualGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CannualRetainedEarnings%2CtrailingRetainedEarnings%2CannualCapitalStock%2CtrailingCapitalStock%2CannualTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CannualTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CannualOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CannualNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CannualNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CannualLongTermDebt%2CtrailingLongTermDebt%2CannualCurrentLiabilities%2CtrailingCurrentLiabilities%2CannualOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CannualCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CannualCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CannualIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CannualAccountsPayable%2CtrailingAccountsPayable%2CannualCurrentDebt%2CtrailingCurrentDebt%2CannualTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CannualOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CannualOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CannualGoodwill%2CtrailingGoodwill%2CannualInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CannualNetPPE%2CtrailingNetPPE%2CannualAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CannualGrossPPE%2CtrailingGrossPPE%2CannualCurrentAssets%2CtrailingCurrentAssets%2CannualOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CannualInventory%2CtrailingInventory%2CannualAccountsReceivable%2CtrailingAccountsReceivable%2CannualCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CannualOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CannualCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=2880725608&corsDomain=finance.yahoo.com'
    elif type == 'balance_quarterly':
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'.HK?lang=en-US&region=US&symbol='+symbol+'.HK&padTimeSeries=true&type=quarterlyTotalAssets%2CtrailingTotalAssets%2CquarterlyStockholdersEquity%2CtrailingStockholdersEquity%2CquarterlyGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CquarterlyRetainedEarnings%2CtrailingRetainedEarnings%2CquarterlyCapitalStock%2CtrailingCapitalStock%2CquarterlyTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CquarterlyTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CquarterlyOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CquarterlyNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CquarterlyNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CquarterlyLongTermDebt%2CtrailingLongTermDebt%2CquarterlyCurrentLiabilities%2CtrailingCurrentLiabilities%2CquarterlyOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CquarterlyCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CquarterlyCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CquarterlyIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CquarterlyAccountsPayable%2CtrailingAccountsPayable%2CquarterlyCurrentDebt%2CtrailingCurrentDebt%2CquarterlyTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CquarterlyOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CquarterlyOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CquarterlyGoodwill%2CtrailingGoodwill%2CquarterlyInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CquarterlyNetPPE%2CtrailingNetPPE%2CquarterlyAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CquarterlyGrossPPE%2CtrailingGrossPPE%2CquarterlyCurrentAssets%2CtrailingCurrentAssets%2CquarterlyOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CquarterlyInventory%2CtrailingInventory%2CquarterlyAccountsReceivable%2CtrailingAccountsReceivable%2CquarterlyCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CquarterlyOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CquarterlyCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=2880726454&corsDomain=finance.yahoo.com'
    elif type == 'income_quarterly':
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'.HK?lang=en-US&region=US&symbol='+symbol+'.HK&padTimeSeries=true&type=quarterlyEbitda%2CtrailingEbitda%2CquarterlyWeighteAverageShare%2CtrailingWeighteAverageShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyearningsPerShare%2CtrailingearningsPerShare%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=2880726564&corsDomain=finance.yahoo.com'
    elif type == 'income_annual':
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'.HK?lang=en-US&region=US&symbol='+symbol+'.HK&padTimeSeries=true&type=annualEbitda%2CtrailingEbitda%2CannualWeighteAverageShare%2CtrailingWeighteAverageShare%2CannualDilutedAverageShares%2CtrailingDilutedAverageShares%2CannualBasicAverageShares%2CtrailingBasicAverageShares%2CannualearningsPerShare%2CtrailingearningsPerShare%2CannualDilutedEPS%2CtrailingDilutedEPS%2CannualBasicEPS%2CtrailingBasicEPS%2CannualNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CannualNetIncome%2CtrailingNetIncome%2CannualNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CannualTaxProvision%2CtrailingTaxProvision%2CannualPretaxIncome%2CtrailingPretaxIncome%2CannualOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CannualInterestExpense%2CtrailingInterestExpense%2CannualOperatingIncome%2CtrailingOperatingIncome%2CannualOperatingExpense%2CtrailingOperatingExpense%2CannualSellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CannualResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CannualGrossProfit%2CtrailingGrossProfit%2CannualCostOfRevenue%2CtrailingCostOfRevenue%2CannualTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=2880726527&corsDomain=finance.yahoo.com'
    elif type == 'cash_quarterly':
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'.HK?lang=en-US&region=US&symbol='+symbol+'.HK&padTimeSeries=true&type=quarterlyFreeCashFlow%2CtrailingFreeCashFlow%2CquarterlyCapitalExpenditure%2CtrailingCapitalExpenditure%2CquarterlyOperatingCashFlow%2CtrailingOperatingCashFlow%2CquarterlyEndCashPosition%2CtrailingEndCashPosition%2CquarterlyBeginningCashPosition%2CtrailingBeginningCashPosition%2CquarterlyChangeInCashSupplementalAsReported%2CtrailingChangeInCashSupplementalAsReported%2CquarterlyCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CquarterlyNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CquarterlyCashDividendsPaid%2CtrailingCashDividendsPaid%2CquarterlyRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CquarterlyCommonStockIssuance%2CtrailingCommonStockIssuance%2CquarterlyRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CquarterlyInvestingCashFlow%2CtrailingInvestingCashFlow%2CquarterlyNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CquarterlySaleOfInvestment%2CtrailingSaleOfInvestment%2CquarterlyPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CquarterlyPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CquarterlyOtherNonCashItems%2CtrailingOtherNonCashItems%2CquarterlyChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CquarterlyChangeInInventory%2CtrailingChangeInInventory%2CquarterlyChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CquarterlyChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CquarterlyStockBasedCompensation%2CtrailingStockBasedCompensation%2CquarterlyDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CquarterlyDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CquarterlyNetIncome%2CtrailingNetIncome&merge=false&period1=493590046&period2=2880726233&corsDomain=finance.yahoo.com'
    elif type == 'cash_annual':
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'.HK?lang=en-US&region=US&symbol='+symbol+'.HK&padTimeSeries=true&type=annualFreeCashFlow%2CtrailingFreeCashFlow%2CannualCapitalExpenditure%2CtrailingCapitalExpenditure%2CannualOperatingCashFlow%2CtrailingOperatingCashFlow%2CannualEndCashPosition%2CtrailingEndCashPosition%2CannualBeginningCashPosition%2CtrailingBeginningCashPosition%2CannualChangeInCashSupplementalAsReported%2CtrailingChangeInCashSupplementalAsReported%2CannualCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CannualNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CannualCashDividendsPaid%2CtrailingCashDividendsPaid%2CannualRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CannualCommonStockIssuance%2CtrailingCommonStockIssuance%2CannualRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CannualInvestingCashFlow%2CtrailingInvestingCashFlow%2CannualNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CannualSaleOfInvestment%2CtrailingSaleOfInvestment%2CannualPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CannualPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CannualOtherNonCashItems%2CtrailingOtherNonCashItems%2CannualChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CannualChangeInInventory%2CtrailingChangeInInventory%2CannualChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CannualChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CannualStockBasedCompensation%2CtrailingStockBasedCompensation%2CannualDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CannualDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CannualNetIncome%2CtrailingNetIncome&merge=false&period1=493590046&period2=2880726340&corsDomain=finance.yahoo.com'
    else:
        print('--------get_request_url type error!---------')

    if isPremuim:
        return url
    else:
        return url.replace('premium/', '')


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
                if int(s['report_timestamp'])>0:
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
                if int(s['report_timestamp'])>0:
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
                if int(s['report_timestamp'])>0:
                    insert_list['income_sheet_table'].append(s)

    return insert_list


def get_default_obj (symbol, type):
    fr = r_field_definition.get_report_definition(type)
    o = {'stock_symbol': symbol}
    for r in fr:
        o[r] = fr[r]['default_value']
    return o

# def send_request(symbol,type, isPremuim):
#     url = get_request_url(symbol,type, isPremuim)
#     result = requests.get(url)
#     return result.json()

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

def get_symbol():
    condition = [['stock_basic_info.hasReport', '=', '33']]
    # condition = [['stock_basic_info.stock_symbol', ' IN ', "('0122', '0281', '2196', '2388', '8070', '8401')"]]
    res = lib.dbU.select('stock_basic_info',['stock_symbol'],condition, [], db='hk')
    return res

def isNewReport(latestReportsYear, latestReportsMonth, ryear, rmonth):
    if ryear>latestReportsYear:
        return True
    elif ryear==latestReportsYear:
        if rmonth>latestReportsMonth:
            return True
        else:
            return False
    else:
        return False

def getLatestReportTime(symbol, report_type, time_type):
    tableMap = {'income':'income_sheet_table','balance':'balance_table','cash':'cash_flow_table'}
    # sheet_data = lib.dbU.select(tableMap[report_type], ['report_year','report_month'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type','=',"'"+time_type+"'"],['Fstatus','>','-1']], [], orderby='(report_year*10+report_month) desc', nolog=True, db='hk')
    sheet_data = lib.dbU.select(tableMap[report_type], ['report_year','report_month'],[['stock_symbol', '=', "'"+symbol+"'"],['report_type','=',"'"+time_type+"'"]], [], orderby='(report_year*10+report_month) desc', nolog=True, db='hk')
    if len(sheet_data):
        latestReportsYear = int(sheet_data[0][0])
        latestReportsMonth = int(sheet_data[0][1])
        return {'year':latestReportsYear, 'month':latestReportsMonth}
    else:
        return {'year':0, 'month':0}

def initial_timestamp(symbol, robj, field_value, report_type, time_type):
    timestamps = []
    latestReportTime = getLatestReportTime(symbol, report_type, time_type)
    if report_type!='balance':
        latesTTMReportTime = getLatestReportTime(symbol, report_type, 'ttm')

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
                    if isNewReport(latesTTMReportTime['year'],latesTTMReportTime['month'], int(d['year']), int(d['month'])):
                        robj[report_type]['ttm']['report_timestamp'] = t
                        robj[report_type]['ttm']['report_datetime'] = fulldate
                        robj[report_type]['ttm']['report_year'] = d['year']
                        robj[report_type]['ttm']['report_month'] = d['month']
                        robj[report_type]['ttm']['report_date'] = d['date']
                        robj[report_type]['ttm']['report_type'] = 'ttm'
                else:
                    if fulldate not in robj[report_type][time_type] and isNewReport(latestReportTime['year'],latestReportTime['month'], int(d['year']), int(d['month'])):
                        robj[report_type][time_type][fulldate] = get_default_obj(symbol, report_type)
                        robj[report_type][time_type][fulldate]['report_timestamp'] = t
                        robj[report_type][time_type][fulldate]['report_datetime'] = fulldate
                        robj[report_type][time_type][fulldate]['report_year'] = d['year']
                        robj[report_type][time_type][fulldate]['report_month'] = d['month']
                        robj[report_type][time_type][fulldate]['report_date'] = d['date']
                        robj[report_type][time_type][fulldate]['report_type'] = time_type
    # print(robj)
    l = {}.fromkeys(timestamps).keys()
    if len(l) >1:
        print('------------'+symbol+'--'+report_type+'---'+time_type+'---timestamp error-----------')
        print(timestamps)

def getReportJson(url, isRetry):
    try:
        # r = requests.get(url, timeout=10)
        r = requests.get(url)
        if(r.status_code==200):
            print('read')
            return r.json()
        else:
            if isRetry:
                print('failed')
                return {}
            else:
                print('failed, retry')
                return getReportJson(url, True)
    except Exception as e:
        if isRetry:
            print('failed')
            return {}
        else:
            print('failed, retry')
            return getReportJson(url, True)
    else:
        if isRetry:
            print('failed')
            return {}
        else:
            print('failed, retry')
            return getReportJson(url, True)

def updateReport():
    print('-------------update start----------------')
    types = ['balance_quarterly', 'balance_annual', 'cash_quarterly', 'cash_annual', 'income_quarterly', 'income_annual']
    error_symbols = []
    res = get_symbol()
    # count = 5700
    count = 0
    l = len(res)
    for i in range(count, l):
    # for r in res:
        r = res[i]
        symbol = r[0]
        print(symbol+',  '+str(count+1)+' of ' +str(l))
        rmap = {'balance':{'annual':{},'quarterly':{}},'cash':{'annual':{},'quarterly':{}, 'ttm':get_default_obj(symbol, 'cash')},'income':{'annual':{},'quarterly':{}, 'ttm':get_default_obj(symbol, 'income')}}
        for sheet_type in types:
            if symbol not in error_symbols:
                url = get_request_url(symbol, sheet_type, False)
                # print(url)
                time.sleep(1)
                report_json = getReportJson(url, False)
                report_type = sheet_type.split('_')[0]
                time_type = sheet_type.split('_')[1]
                if 'timeseries' in report_json and 'result' in report_json['timeseries'] and len(report_json['timeseries']['result'])>0:
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
                                elif 'reportedValue' in f and 'raw' in f['reportedValue'] and f['asOfDate'] in rmap[report_type][fixed_time_type]:
                                    rmap[report_type][fixed_time_type][f['asOfDate']][field_name_to_db] = f['reportedValue']['raw']
                else:
                    if symbol not in error_symbols:
                        error_symbols.append(symbol)
            else:
                break
        if symbol not in error_symbols:
            insert_list = sheets_formating(rmap)
            # print(rmap)
            # print(insert_list)
            for t in insert_list:
                lib.dbU.insert(t, insert_list[t], db='hk')
            count+=1
            time.sleep(1)
        else:
            print('-------error----------')
            print(error_symbols)

    print('completed')
    print(error_symbols)
