# import requests
# import http.cookiejar
# import urllib.request
# import ssl
# import re
# import json
# ssl._create_default_https_context = ssl._create_unverified_context
# url = 'https://finance.yahoo.com/quote/V/financials?p=V'
# url2 = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=quarterlyEbitda%2CtrailingEbitda%2CquarterlyWeighteAverageShare%2CtrailingWeighteAverageShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyearningsPerShare%2CtrailingearningsPerShare%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580745554&corsDomain=finance.yahoo.com'
# url3 = 'https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=annualEbitda%2CtrailingEbitda%2CannualWeighteAverageShare%2CtrailingWeighteAverageShare%2CannualDilutedAverageShares%2CtrailingDilutedAverageShares%2CannualBasicAverageShares%2CtrailingBasicAverageShares%2CannualearningsPerShare%2CtrailingearningsPerShare%2CannualDilutedEPS%2CtrailingDilutedEPS%2CannualBasicEPS%2CtrailingBasicEPS%2CannualNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CannualNetIncome%2CtrailingNetIncome%2CannualNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CannualTaxProvision%2CtrailingTaxProvision%2CannualPretaxIncome%2CtrailingPretaxIncome%2CannualOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CannualInterestExpense%2CtrailingInterestExpense%2CannualOperatingIncome%2CtrailingOperatingIncome%2CannualOperatingExpense%2CtrailingOperatingExpense%2CannualSellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CannualResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CannualGrossProfit%2CtrailingGrossProfit%2CannualCostOfRevenue%2CtrailingCostOfRevenue%2CannualTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580726527&corsDomain=finance.yahoo.com'
# # r = requests.get(url)
# # print(r.cookies.keys())
# # print(r.cookies['BDORZ'])
#
# def getcookies():
#     cj = http.cookiejar.MozillaCookieJar('cookies.txt')
#     cj.load()
#     cookieProcessor = urllib.request.HTTPCookieProcessor(cj.load())
#     opener = urllib.request.build_opener(cookieProcessor)
#     response = opener.open(url).read().decode('utf-8')
#
#     match = re.search(r'(root\.App\.main).*', response)
#     match = match.group(0)
#     match = match.replace('root.App.main =', '')
#     match = match.replace('root.App.main=', '')
#     mlen = len(match)
#     if match[mlen - 1] == ";":
#         match = match[0:mlen - 1]
#     match = json.loads(match)
#
#     print(match['context']['dispatcher']['stores']['QuoteTimeSeriesStore']['timeSeries'])
#     # print(len(cj))
# # url = 'http://www.lizenghai.com'
# # cookies = getcookies()
# # res = requests.get(url, cookies=cookies)
# # html = res.content.decode()
# # print('登出' in html)
#
# cookies = getcookies()
# # session = requests.session()
# # requests.utils.add_dict_to_cookiejar(session.cookies, cookies)
# # res = session.get(url3)
# # html = res.content.decode()
# # print(html)
a = 'dd'
b = ['aa','bb','dd']
print(a in b)