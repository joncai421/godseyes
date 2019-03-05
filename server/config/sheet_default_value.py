import time
def get_sheet_default_value(type):
    if type == 'cashflowStatements':
        return {
            "investments": 0,#
            "changeToLiabilities": 0,#
            "totalCashflowsFromInvestingActivities": 0,#
            "netBorrowings": 0,#借款净额
            "totalCashFromFinancingActivities": 0,#
            "changeToOperatingActivities": 0,#
            "issuanceOfStock": 0,#
            "netIncome": 0,#净收益
            "changeInCash": 0,#
            "endDate": 0,#统计日期
            "repurchaseOfStock": 0,#
            "totalCashFromOperatingActivities": 0,#
            "depreciation": 0,#折旧损耗及摊稍
            "otherCashflowsFromInvestingActivities": 0,#
            "dividendsPaid": 0,#本期已支付股息
            "changeToInventory": 0,#
            "changeToAccountReceivables": 0,#
            "changeToNetincome": 0,#
            "capitalExpenditures": 0,##资本支出(是指企业为取得长期资产而发生的支出)
            "otherCashflowsFromFinancingActivities": 0,
            "Finsert_time":time.strftime('%Y-%m-%d %H:%M:%S'),
            "Fmodify_time":time.strftime('%Y-%m-%d %H:%M:%S'),
            "Flastest_modify_time":time.strftime('%Y-%m-%d %H:%M:%S')
        }
    elif type == "balanceSheetStatements":
        return {
            "totalLiab": 0,#合计总负债
            "totalStockholderEquity": 0,#股东权益合计
            "otherCurrentLiab": 0,#其他流动负债
            "totalAssets": 0,#合计总资产
            "endDate": 0,#统计日期
            "commonStock": 0,#普通股股本
            "otherCurrentAssets": 0,#其他流动资产
            "retainedEarnings": 0,#保留盈余
            "otherLiab": 0,#其他负债
            "treasuryStock": 0,#
            "otherAssets": 0,#其他资产
            "cash": 0,#现金
            "totalCurrentLiabilities": 0,#流动负债
            "shortLongTermDebt": 0,#长期债务
            "otherStockholderEquity": 0,#
            "propertyPlantEquipment": 0,#厂房及设备净资产
            "totalCurrentAssets": 0,#流动资产
            "longTermInvestments": 0,#项目总投资及垫款/长期投资
            "netTangibleAssets": 0,#净有形资产
            "shortTermInvestments": 0,#
            "netReceivables": 0,#短期应收账款
            "longTermDebt": 0,#
            "inventory": 0,#存货
            "accountsPayable": 0,#应付账款
            "goodWill": 0,#商誉
            "intangibleAssets": 0,#无形资产
            "Finsert_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            "Fmodify_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            "Flastest_modify_time": time.strftime('%Y-%m-%d %H:%M:%S')
        }
    elif type == "incomeStatementHistory":
        return {
            "researchDevelopment": 0,#研发费用
            "effectOfAccountingCharges": 0,#
            "incomeBeforeTax": 0,#税前利润
            "minorityInterest": 0,#少数股东权益
            "netIncome": 0,#净利润
            "sellingGeneralAdministrative": 0,#銷售及管理費用
            "grossProfit": 0,#毛利润
            "ebit": 0,#息稅前利潤 = 净利润+所得税+利息支出
            "endDate": 0,#统计日期
            "operatingIncome": 0,#营业利益
            "otherOperatingExpenses": 0,#其他经营开支
            "interestExpense": 0,#利息费用
            "extraordinaryItems": 0,#非经常性损益
            "nonRecurring": 0,#非经常性项目
            "otherItems": 0,#
            "incomeTaxExpense": 0,#所得税开支
            "totalRevenue": 0,#净收入/总收入/营业收入/营业总收入
            "totalOperatingExpenses": 0,#总经营成本
            "costOfRevenue": 0,#销售成本/营业成本
            "totalOtherIncomeExpenseNet": 0,#税前营业收入特殊项目
            "discontinuedOperations": 0,#非持续性经营活动
            "netIncomeFromContinuingOps": 0,#税收收入/净利润
            "netIncomeApplicableToCommonShares": 0,#税收收入/净利润/属于母公司股东的净利润?
            "Finsert_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            "Fmodify_time": time.strftime('%Y-%m-%d %H:%M:%S'),
            "Flastest_modify_time": time.strftime('%Y-%m-%d %H:%M:%S')
        }
