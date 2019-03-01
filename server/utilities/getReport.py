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
import urllib.request

def getPage(symbol):
    url = 'https://finance.yahoo.com/quote/AAPL/financials?p='+symbol
    response = urllib.request.urlopen(url)
    result = response.read().decode('utf-8')
    print(result)

def getReport():
    getPage('AAPL')