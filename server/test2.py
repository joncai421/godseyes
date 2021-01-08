import sqlite3
import cookielib
import Cookie
import urllib2

def build_opener_with_chrome_cookies(domain=None):
    cookie_file_path = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Cookies')
    if not os.path.exists(cookie_file_path):
        raise Exception('Cookies file not exist!')
    conn = sqlite3.connect(cookie_file_path)
    sql = 'select host_key, name, value, path from cookies'
    if domain:
        sql += ' where host_key like "%{}%"'.format(domain)

    cookiejar = cookielib.CookieJar()  # No cookies stored yet

    for row in conn.execute(sql):
        cookie_item = cookielib.Cookie(
            version=0, name=row[1], value=row[2],
            port=None, port_specified=None,
            domain=row[0], domain_specified=None, domain_initial_dot=None,
            path=row[3], path_specified=None,
            secure=None,
            expires=None,
            discard=None,
            comment=None,
            comment_url=None,
            rest=None,
            rfc2109=False,
        )
        cookiejar.set_cookie(cookie_item)  # Apply each cookie_item to cookiejar
    conn.close()
    return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))  # Return opener


if __name__ == '__main__':
    opener = build_opener_with_chrome_cookies(domain='.yahoo.com')
    html_doc = opener.open('https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=annualTotalAssets%2CtrailingTotalAssets%2CannualStockholdersEquity%2CtrailingStockholdersEquity%2CannualGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CannualRetainedEarnings%2CtrailingRetainedEarnings%2CannualCapitalStock%2CtrailingCapitalStock%2CannualTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CannualTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CannualOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CannualNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CannualNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CannualLongTermDebt%2CtrailingLongTermDebt%2CannualCurrentLiabilities%2CtrailingCurrentLiabilities%2CannualOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CannualCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CannualCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CannualIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CannualAccountsPayable%2CtrailingAccountsPayable%2CannualCurrentDebt%2CtrailingCurrentDebt%2CannualTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CannualOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CannualOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CannualGoodwill%2CtrailingGoodwill%2CannualInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CannualNetPPE%2CtrailingNetPPE%2CannualAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CannualGrossPPE%2CtrailingGrossPPE%2CannualCurrentAssets%2CtrailingCurrentAssets%2CannualOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CannualInventory%2CtrailingInventory%2CannualAccountsReceivable%2CtrailingAccountsReceivable%2CannualCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CannualOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CannualCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1580725608&corsDomain=finance.yahoo.com').read()
    import re
    print 'Title:', re.search('<title>(.*?)</title>', html_doc, re.IGNORECASE).g