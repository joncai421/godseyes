def get_dict(type):
    if type == 'cash_flow_sheet':
        return {
            "netIncome": ['Net Income', '净收益'],
            "investments":['investments', '投资'],
            "changeToLiabilities":['Accounts Payable', '应付账款'],
            "totalCashflowsFromInvestingActivities":['Net cash used for investing activites', '用于投资活动的现金净额'],#Investments in property, plant and equipment + Acquisitions, net + Purchases of investments + Sales/Maturities of investments + Other investing activites (所有项目如为正数则为投资收入，负数则为投资支出)
            "netBorrowings":['netBorrowings', '借款净额'],
            "totalCashFromFinancingActivities":['Net cash used privided by (used for) financing activities', '筹资活动（用于）所占用的现金净额'],
            "changeToOperatingActivities":['changeToOperatingActivities', '经营活动变化'],
            "issuanceOfStock":['issuanceOfStock', '股票发行'],

            "changeInCash":['change To Netincome', '现金净变动'],#Cash at end of period - Cash at beginning of period
            "effectOfExchangeRate":['effect Of Exchange Rate', '汇率的影响'],
            "repurchaseOfStock":['repurchaseOfStock', '回购股票'],

            "depreciation":['depreciation', '折旧损耗及摊稍'],
            "otherCashflowsFromInvestingActivities":['otherCashflowsFromInvestingActivities', '其他用于投资活动的现金净额'],
            "dividendsPaid":['Dividends Paid', '本期已支付股息'],
            "changeToInventory":['changeToInventory', '存货变化'],
            "changeToAccountReceivables":['Accounts receivable', '应收账款变化'],
            "changeToNetincome":['', '资本支出(是指企业为取得长期资产而发生的支出)'],
            "otherCashflowsFromFinancingActivities": ['other cash used privided by (used for) financing activities', '其他筹资活动（用于）所占用的现金净额'],#otherCashflowsFromFinancingActivities=Debt repayment+Common stock issued+Common stock repurchased+Dividends Paid+Other financing activites(所有项目如为正数则为投资收入，负数则为投资支出)

            "totalCashFromOperatingActivities": ['Operating Cash Flow', '经营性现金流'],
            "capitalExpenditures": ['Capital Expenditure', '资本支出'],# normally = Investments in property, plant and equipment
            "FreeCashFlow": ['Free Cash Flow','自由现金流'], # NEW, FreeCashFlow = totalCashFromOperatingActivities + capitalExpenditures

            "depreciation_rate":['depreciation_rate', '折旧率'],  #折旧率(depreciation/totalAssets)
            "capitalExpenditures_rate":['capitalExpenditures_rate', '资本开支率(capitalExpenditures/netIncome)'],  #资本开支率(capitalExpenditures/netIncome)
            "capitalExpenditures_rate2":['capitalExpenditures_rate2', '资本开支率（除去股票回购率）(getRate(capitalExpenditures-abs(repurchaseOfStock),netIncome))'],  #资本开支率(capitalExpenditures-abs(repurchaseOfStock/netIncome))
            "repurchaseOfStock_rate":['repurchaseOfStock_rate', '资本开支率'],  #资本开支率repurchaseOfStock/netIncome
            "report_year":['report_year', '报表年份'],
            "report_month":['report_month', '报表月份'],
            "report_date":['report_date', '报表日'],
            "report_type":['report_type', '报表类型'],
            "endDate": ['endDate', '统计日期'],
        }
    elif type == "balance_sheet":
        return {
            #Liabilities
            "totalLiab":['Total Liabilities', '合计总负债'],
            "totalCurrentLiabilities": ['total Current Liabilities', '总流动负债'],
            "otherCurrentLiab": ['other Current Liabilities', '其他流动负债'],
            "longTermDebt": ['Long Term Debt', '长期债务'],
            "deferredLongTermLiab": ['deferred LongTerm Liabilities', '递延长期负债'],
            "shortLongTermDebt": ['short Long-Term Debt', '本年需偿还的长期债务'],#The short/current long-term debt is a separate line item on a balance sheet account. It outlines the total amount of debt that must be paid within the current year—within the next 12 months. ... In some cases, the short-term liability may be due to be paid within the current fiscal year.
            "otherLiab": ['other non-current Liabilities', '其他非流动负债'],#Deferred taxes liabilities+Deferred revenues+Other long-term liabilities
            "totalNonCurrentLiabilities":['total Non-Current Liabilities', '总非流动债务'],#totalLiab-totalCurrentLiabilities / totalCurrentLiabilities + otherLiab
            "accountsPayable": ['accounts Payable', '应付账款'],

            #Assets
            "totalAssets":['Total Assets', '合计总资产'],
            "treasuryStock": ['Treasury stock', '库存股票'],  # 库存股票(如果资产负债表上出现了库存股票，表明公司曾经回. 购股票，那么这家公司很可能具有一种与之有利的持续性竞争优势。)Treasury stock, also known as treasury shares or reacquired stock refers to previously outstanding stock that is bought back from stockholders by the issuing company. The result is that the total number of outstanding shares on the open market decreases. These shares are issued but no longer outstanding and are not included in the distribution of dividends or the calculation of earnings per share (EPS).
            "otherAssets": ['Other long-term assets', '其他非流动资产'],
            "cash": ['Cash And Cash Equivalents', '现金或等价物'],
            "total_cash":['total_cash','现金总值'], #total_cash = cash + shortTermInvestments
            "deferredLongTermAssetCharges": ['deferredLongTermAssetCharges', '递延长期资产费用'],#A deferred charge is a long-term prepaid expense that is carried as an asset on a balance sheet until used/consumed. ... Deferred charges often stem from a business making payments for goods and services it has not yet received, such as prepaid insurance premiums or rent.
            "propertyPlantEquipment": ['propertyPlantEquipment', '厂房及设备净资产'],
            "totalCurrentAssets": ['totalCurrentAssets', '流动资产'],
            "otherCurrentAssets": ['otherCurrentAssets', '其他流动资产'],
            "longTermInvestments": ['Equity and other investments', '长期投资'],  # 项目总投资及垫款/长期投资
            "netTangibleAssets": ['net Tangible Assets', '净有形资产'],#netTangibleAssets = Gross property, plant and equipment + Accumulated afre(净有形资产=资产值-累计折旧)
            "shortTermInvestments": ['shortTermInvestments', '短期投资'],
            "netReceivables": ['netReceivables', '短期应收账款'],
            "inventory": ['inventory', '存货'],
            "intangibleAssets": ['Intangible Assets', '无形资产'],
            "goodWill": ['Goodwill', '商誉'],

            # Stockholder Equity
            "totalStockholderEquity": ['totalStockholderEquity', '股东权益合计'],
            "otherStockholderEquity": ['totalStockholderEquity', '其他股东权益'],
            "commonStock": ['commonStock', '普通股股本'],
            "minorityInterest": ['minority Interest', '少数权益'],
            "capitalSurplus": ['capital Surplus', '资本盈余'],# Like retained earnings, capital surplus is a component of shareholders’ equity and is used to account for the amount an organization raises in excess of the par value of the shares. The par value is the stated value or face value of the shares. Shares issued and paid plus capital surplus are defined as the total amount actually paid by investors for the issued shares. Shares that have no par value generally do not have any capital surplus, and therefore all funds from shares issued are credited to common stock issued. 指公司股票的原始销售超过名义价值的数额部分。
            "retainedEarnings": ['retained Earnings', '保留盈余'],
            # 保留盈余/留存收益 (Retained earnings are defined as ALL the profits an organization has earned since it came into existence, minus dividends paid to shareholders.)
            # ---capital Surplus VS retained Earnings---
            # Both retained earnings and capital surplus represent an increase in the shareholders’ equity of an organization,
            # but both affect it in different ways. Contributed surplus is the amount of money or assets invested in the company by shareholders,
            # while retained earnings are the profits made by the organization but that have not yet been paid out to shareholders. Surplus can be thought of as checks shareholders are writing to the organization,
            # while retained earnings can be thought of as the shareholders choosing to leave some of the profits with the organization rather than taking them.


            "debtRatio":['debtRatio', '负债率'],  # 负债率(totalLiab/totalAssets)
            "receivables_rate":['receivables_rate', '应收账款率'],  # 应收账款率(netReceivables/totalAssets)
            "current_ratio":['current_ratio', '流动比率'],  # 流动比率(totalCurrentAssets/totalCurrentLiabilities)
            "cash_ratio":['cash_ratio', '流动比率'],
            "total_debt_to_equity_ratio":['total_debt_to_equity_ratio', '债务股权比率'],  # 债务股权比率(totalLiab/totalStockholderEquity)
            "retainedEarnings_rate":['retainedEarnings_rate', '留存收益率'],  # 留存收益率(retainedEarnings/netIncome)
            "report_year":['report_year', '报表年份'],
            "report_month":['report_month','报表月份'],
            "report_date":['report_date','报表日'],
            "report_type":['report_type','报表类型'],
            "endDate": ['endDate', '统计日期'],
        }
    elif type == "income_statement_sheet":
        return {
            "totalRevenue": ['totalRevenue', '总收入'],  # 净收入/总收入/营业收入/营业总收入
            "costOfRevenue": ['costOfRevenue', '销售成本'],  # 销售成本 or 营业成本
            "grossProfit": ['grossProfit', '毛利润'],#grossProfit = totalRevenue - costOfRevenue
            "researchDevelopment": ['researchDevelopment', '研发费用'],
            "sellingGeneralAdministrative": ['SGA', '銷售及管理費用'],
            "otherOperatingExpenses": ['otherOperatingExpenses', '其他经营开支'],  # ??
            "totalOperatingExpenses": ['totalOperatingExpenses', '总经营成本'],#totalOperatingExpenses = sellingGeneralAdministrative + researchDevelopment + otherOperatingExpenses
            "operatingIncome": ['operatingIncome', '营业收入'], #operatingIncome = grossProfit - totalOperatingExpenses
            "totalOtherIncomeExpenseNet": ['totalOtherIncomeExpenseNet', '税前营业收入特殊项目'],
            "interestExpense": ['interestExpense', '利息费用'],
            "incomeBeforeTax": ['incomeBeforeTax', '税前利润'],#incomeBeforeTax = grossProfit - interestExpense -
            "incomeTaxExpense": ['incomeTaxExpense', '所得税开支'],
            "netIncome": ['netIncome', '净利润'], # netIncome = incomeBeforeTax - incomeTaxExpense
            "netIncomeFromContinuingOps": ['netIncomeFromContinuingOps', '持续经营收入'],  # 持续经营收入/净利润
            "netIncomeApplicableToCommonShares": ['Net Income available to common shareholders', '可分配给普通股股东的净收入'],
            # 税收收入/净利润/可分配给普通股股东的净收入/属于母公司股东的净利润
            "minorityInterest":['minorityInterest', '少数股东权益'],
            "ebit":['EDIT', '息稅前利潤（净利润+所得税+利息支出）'],#息稅前利潤 = 净利润+所得税+利息支出
            "effectOfAccountingCharges": ['effectOfAccountingCharges', '会计费用'],
            "extraordinaryItems":['extraordinaryItems', '非经常性损益'],
            "nonRecurring":['nonRecurring', '非经常性项目'],
            "otherItems":['otherItems', '其他项目'],
            "discontinuedOperations":['discontinuedOperations', '非持续性经营活动'],
            "GrossProfitMargin":['GrossProfitMargin', '毛利率'],  # 毛利率(grossProfit/totalRevenue)
            "research_cost_rate":['research_cost_rate', '研发费用比率'],  # 研发费用比率(researchDevelopment/totalRevenue)
            "NetInterestRate":['NetInterestRate', '净利润率'],  # 净利润率(netIncome/totalRevenue)
            "SGA_Rate":['SGA_Rate', '銷售及管理費用费用比率'],  # 銷售及管理費用费用比率(sellingGeneralAdministrative/totalRevenue)
            "costOfRevenue_Rate":['costOfRevenue_Rate', '营业成本比率'],  # 销售成本/营业成本比率(costOfRevenue/totalRevenue)
            "interest_Rate":['interest_Rate', '利息比率'],  # 利息比率(interestExpense/totalRevenue)
            "Earnings_per_share":['Earnings_per_share', '每股净收益'],  # 每股净收益(netIncome/市场股数(总股本)share_capital/sharesOutstanding)
            "share_capital":['share_capital','总股本'],#share_capital = netIncome/EPS
            "WASO":['Weighted average shares outstanding','加权平均流通股'],#Average Shares
            "report_year":['report_year', '报表年份'],
            "report_month":['report_month', '报表月份'],
            "report_date":['report_date', '报表日'],
            "report_type":['report_type', '报表类型'],
            "endDate": ['endDate', '统计日期'],
        }