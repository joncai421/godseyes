def get_report_definition(rtype):
    if rtype == 'balance':
            return {
                    # current Liabilities/流动债务：
                    'IncomeTaxPayable': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Taxes payable','cn_name': '应付所得税'},
                    'CurrentAccruedExpenses': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Accrued liabilities', 'cn_name': '当前应计费用总计'},# CurrentAccruedExpenses = Accrued liabilities + OtherCurrentLiabilities.  Accrued expenses are those liabilities which have built up over time and are due to be paid.
                    'OtherCurrentLiabilities': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Other Current Liabilities', 'cn_name': '其他流动债务'},
                    'CurrentDebt': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Total Revenue','cn_name': '部分流动债务'},
                    'CurrentDeferredRevenue': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Deferred revenues', 'cn_name': '当前递延收入'},# Deferred revenue is when a company receives payment from a customer before the product or service has been delivered; however, the payment is not yet counted as revenue. Deferred revenue, which is also referred to as unearned revenue, is listed as a liability
                    'AccountsPayable': {'data_type': 'int', 'default_value': 0, 'cn_name': '应付账款'},
                    'CurrentLiabilities': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Total Current Liabilities', 'cn_name': '总流动负债'},# add up for above items
                    # non current Liabilities:
                    'LongTermDebt': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Long Term Debt','cn_name': '长期债务'},
                    'LongTermDebt_ratio': {'data_type': 'float', 'default_value': 0,'cn_name': '长期负债比率'}, # LongTermDebt / TotalAssets
                    'LongDebtToOprtInc_ratio': {'data_type': 'float', 'default_value': 0,'cn_name': '长期债务与营运资金比率'}, # LongTermDebt / OperatingIncome
                    'OtherNonCurrentLiabilities': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Other long-term liabilities', 'cn_name': '其他长期债务'},
                    'NonCurrentDeferredTaxesLiabilities': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Deferred taxes liabilities','cn_name': '递延税项负债'},
                    'NonCurrentDeferredRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name': '非当前递延收入'},
                    'TotalNonCurrentLiabilitiesNetMinorityInterest': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Total non-current liabilities','cn_name': '总非流动债务'},
                    # Total Liabilities
                    'TotalLiabilitiesNetMinorityInterest': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Total Liabilities', 'cn_name': '总债务'},
                    'debtRatio':{'data_type': 'float', 'default_value': 0, 'cn_name':'负债率'},# TotalLiabilitiesNetMinorityInterest / TotalAssets
                    'current_ratio':{'data_type': 'float', 'default_value': 0, 'cn_name':'流动比率'},# CurrentLiabilities / CurrentAssets
                    'total_debt_to_equity_ratio':{'data_type': 'float', 'default_value': 0, 'cn_name':'债务股权比率D/E'},# TotalLiabilitiesNetMinorityInterest / StockholdersEquity
                    'quickRatio':{'data_type': 'float', 'default_value': 0, 'cn_name':'速动比率'},# CurrentAssets - Inventory / CurrentLiabilities
                    'cashRatio':{'data_type': 'float', 'default_value': 0, 'cn_name':'现金比率'},# CashCashEquivalentsAndMarketableSecurities / CurrentAssets

                    # Stockholders' Equity:
                    'CapitalStock': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Common Stock','cn_name': ''},
                    'GainsLossesNotAffectingRetainedEarnings': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Accumulated other comprehensive income', 'cn_name': '累计其他综合收益'},
                    'RetainedEarnings': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Retained Earnings', 'cn_name': '累计留存收益'},#累计叠加
                    'StockholdersEquity': {'data_type': 'int', 'default_value': 0, 'name_on_page': "Total stockholder's equity", 'cn_name': '股东权益总额'},
                    'retainedEarnings_rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '留存收益率'},#RetainedEarnings（当年RetainedEarnings- 上一年RetainedEarnings） / NetIncome
                    'BookValue': {'data_type': 'int', 'default_value': 0, 'cn_name': '账面价值'},# TotalAssets - TotalLiabilitiesNetMinorityInterest - OtherIntangibleAssets
                    #bv=Total Common Shareholders Equity – Preferred Stock （bv ratio = bv/Number of Outstanding Common Shares）(市净率=bv/总股本。账面市值比book to market value(账面市值比是市净率的倒数))

                    # non current Assets:
                    'Goodwill': {'data_type': 'int', 'default_value': 0, 'cn_name': '商誉'},
                    'OtherNonCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name': '其他非流动资产'},
                    'GrossPPE': {'data_type': 'int', 'default_value': 0,'name_on_page':'gross property, plant and equipment','cn_name': 'gross PP&E '},
                    'AccumulatedDepreciation': {'data_type': 'int', 'default_value': 0, 'cn_name': '累计折旧'},
                    'NetPPE': {'data_type': 'int', 'default_value': 0,'name_on_page':'Net property, plant and equipment','cn_name': '净有型资产'},#netTangibleAssets = Gross property, plant and equipment + Accumulated afre(净有形资产=资产值-累计折旧)
                    'OtherIntangibleAssets': {'data_type': 'int', 'default_value': 0, 'name_on_page':'Intangible Assets','cn_name': '无形资产'},
                    'InvestmentsAndAdvances': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Equity and other investments', 'cn_name': '股权及其他投资'},
                    'TotalNonCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name': '总非流动资产'},
                    # current Assets
                    'CashCashEquivalentsAndMarketableSecurities': {'data_type': 'int', 'default_value': 0,'name_on_page':'Total Cash','cn_name': '现金证券和等价物'},#CashAndCashEquivalents + OtherShortTermInvestments
                    'CashAndCashEquivalents': {'data_type': 'int', 'default_value': 0, 'name_on_page':'Cash And Cash Equivalents', 'cn_name': '现金和等价物'},
                    'OtherShortTermInvestments': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Short Term Investments', 'cn_name': '其他短期投资'},
                    'AccountsReceivable': {'data_type': 'int', 'default_value': 0, 'name_on_page':'Net Receivables','cn_name': '应收账款'},
                    'OtherCurrentAssets': {'data_type': 'int', 'default_value': 0, 'name_on_page':'Other Current Assets','cn_name': '其他流动资产'},
                    'Inventory': {'data_type': 'int', 'default_value': 0, 'cn_name': '库存'},
                    'CurrentAssets': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Total Current Assets', 'cn_name': '流动总资产'},
                    # total Assets
                    'TotalAssets': {'data_type': 'int', 'default_value': 0, 'cn_name': '总资产'},
                    'receivables_rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '应收账款周转率'},# Net Credit Sales / Average Accounts Receivable（本期加上期AccountsReceivable/2）

                    "report_timestamp": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表时间戳'},
                    "report_datetime": {'data_type': 'date', 'default_value': '0000-00-00', 'cn_name': '报表日期'},
                    "report_year": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表年'},
                    "report_month": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表月'},
                    "report_date": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表日'},
                    "report_type": {'data_type': 'string', 'default_value': '', 'cn_name': '报表类型'}
            }
    if rtype == 'balance_annual':
        return {'annualCurrentDeferredRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualLongTermDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualInvestmentsAndAdvances': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCurrentDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualStockholdersEquity': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualIncomeTaxPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualGoodwill': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualTotalNonCurrentLiabilitiesNetMinorityInterest': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualAccumulatedDepreciation': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNonCurrentDeferredTaxesLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualTotalAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherShortTermInvestments': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCashCashEquivalentsAndMarketableSecurities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherIntangibleAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualTotalLiabilitiesNetMinorityInterest': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualGainsLossesNotAffectingRetainedEarnings': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetPPE': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCurrentLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCurrentAccruedExpenses': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualTotalNonCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherNonCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherCurrentLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualRetainedEarnings': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCashAndCashEquivalents': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualAccountsPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualGrossPPE': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCapitalStock': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherNonCurrentLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualAccountsReceivable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNonCurrentDeferredRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualInventory': {'data_type': 'int', 'default_value': 0, 'cn_name':''}}
    elif rtype == 'banlance_quaterly':
        return {'quarterlyLongTermDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCapitalStock': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNonCurrentDeferredTaxesLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyStockholdersEquity': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherNonCurrentLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCashCashEquivalentsAndMarketableSecurities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNonCurrentDeferredRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyTotalNonCurrentLiabilitiesNetMinorityInterest': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherNonCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyAccumulatedDepreciation': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCurrentDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyIncomeTaxPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCurrentAccruedExpenses': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyAccountsReceivable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyGrossPPE': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyGoodwill': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCurrentLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyTotalNonCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherIntangibleAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCashAndCashEquivalents': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyTotalAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherShortTermInvestments': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyRetainedEarnings': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNetPPE': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherCurrentAssets': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCurrentDeferredRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyAccountsPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyTotalLiabilitiesNetMinorityInterest': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherCurrentLiabilities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyGainsLossesNotAffectingRetainedEarnings': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyInvestmentsAndAdvances': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyInventory': {'data_type': 'int', 'default_value': 0, 'cn_name':''}}
    elif rtype == 'income':
        return {'TotalRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':'总收入'},
                'CostOfRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name': '销售成本'},
                'GrossProfit': {'data_type': 'int', 'default_value': 0, 'cn_name': '毛利润'},
                'SellingGeneralAndAdministration': {'data_type': 'int', 'default_value': 0, 'cn_name':'銷售及管理費用'},
                'ResearchAndDevelopment': {'data_type': 'int', 'default_value': 0, 'cn_name': '研发费用'},
                'OperatingExpense': {'data_type': 'int', 'default_value': 0, 'cn_name': '经营开支'},
                'OperatingIncome': {'data_type': 'int', 'default_value': 0, 'cn_name': '营业收入'},
                'InterestExpense': {'data_type': 'int', 'default_value': 0, 'cn_name': '利息费用'},
                'OtherIncomeExpense': {'data_type': 'int', 'default_value': 0,'name_on_page': 'Total Other Income/Expenses Net', 'cn_name': '税前营业收入特殊项目'},
                'PretaxIncome': {'data_type': 'int', 'default_value': 0, 'cn_name': '税前利润'},
                'TaxProvision': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Income Tax Expense','cn_name': '所得税开支'},
                'taxRate': {'data_type': 'float', 'default_value': 0, 'cn_name': '税率'}, #TaxProvision / PretaxIncome
                'NetIncomeContinuousOperations': {'data_type': 'int', 'default_value': 0, 'cn_name': '持续经营收入'},
                'NetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name': '净利润'},
                'NetIncomeCommonStockholders': {'data_type': 'int', 'default_value': 0, 'cn_name': '可分配给普通股股东的净收入'},
                'NOPAT': {'data_type': 'int', 'default_value': 0, 'cn_name': '税后净营业利润/net operating profit after tax'},# OperatingIncome x (1 - taxRate)
                'Ebitda': {'data_type': 'int', 'default_value': 0, 'cn_name':'税前息前折旧前摊销前利润'}, #EBITDA= Ebit + DepreciationAndAmortization
                'Ebit': {'data_type': 'int', 'default_value': 0, 'cn_name':'税前息前折旧前摊销前利润'}, # Ebit = net income + tax expense + interest expense = Ebitda - DepreciationAndAmortization
                'InterestCoverageRatio': {'data_type': 'float', 'default_value': 0, 'cn_name':'利息覆盖率'}, # EBIT / InterestExpense (一般认为低于2.5即为警讯，以1.5为最低勉强可接受数字)
                'DaOfEbitda': {'data_type': 'float', 'default_value': 0, 'cn_name':'折旧、摊销额占EBITDA的百分比'}, #  DepreciationAndAmortization / Ebitda
                'BasicEPS': {'data_type': 'float', 'default_value': 0, 'cn_name': '每股净收益'},
                'DilutedEPS': {'data_type': 'float', 'default_value': 0, 'cn_name': '稀释每股净收益'},
                'BasicAverageShares': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Weighted average shares outstanding','cn_name':''},
                'DilutedAverageShares': {'data_type': 'int', 'default_value': 0,  'name_on_page': 'Weighted average shares outstanding','cn_name': '稀释'},
                'salesPerShare': {'data_type': 'int', 'default_value': 0,'cn_name': '每股销售额'}, # ？

                'GrossProfitMargin': {'data_type': 'float', 'default_value': 0, 'cn_name': '毛利率'}, # GrossProfit / TotalRevenue
                'NOPATtoTotRevRatio': {'data_type': 'float', 'default_value': 0, 'cn_name': 'NOPAT盈利率(税后净营业利润率)'}, # NOPAT / TotalRevenue
                'pretaxIncomeAssetsRate': {'data_type': 'float', 'default_value': 0, 'cn_name': '基本盈利能力比率'},#PretaxIncome / TotalAssets
                'research_cost_rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '研发费用比率'}, #ResearchAndDevelopment / TotalRevenue
                'NetInterestRate': {'data_type': 'float', 'default_value': 0, 'cn_name': '净利润率'}, # NetIncome / TotalRevenue
                'ebitdaToRevRatio': {'data_type': 'float', 'default_value': 0, 'cn_name': '净利润率'}, # NetIncome / TotalRevenue
                'SGA_Rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '銷售及管理費用费用比率'}, #SellingGeneralAndAdministration / TotalRevenue
                'costOfRevenue_Rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '营业成本比率'}, # CostOfRevenue / TotalRevenue
                'interest_Rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '利息比率'}, # InterestExpense / OperatingIncome
                'share_capital': {'data_type': 'float', 'default_value': 0, 'cn_name': '总股本'}, # NetIncome / BasicEPS
                'ROE': {'data_type': 'float', 'default_value': 0, 'cn_name': 'ROE return of Equity/股本回报率'}, # net income / StockholdersEquity
                'ROA': {'data_type': 'float', 'default_value': 0, 'cn_name': 'ROA return of Assets/资产回报率'}, # net income / Average total assets

                "report_timestamp": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表时间戳'},
                "report_datetime": {'data_type': 'date', 'default_value': '0000-00-00', 'cn_name': '报表日期'},
                "report_year": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表年'},
                "report_month": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表月'},
                "report_date": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表日'},
                "report_type": {'data_type': 'string', 'default_value': '', 'cn_name': '报表类型'}
                }
    elif rtype == 'income_quaterly':
        return {'quarterlySellingGeneralAndAdministration': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingTotalRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCostOfRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNetIncomeCommonStockholders': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOperatingIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyInterestExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingTaxProvision': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyTotalRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOperatingIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingPretaxIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingSellingGeneralAndAdministration': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOperatingExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCostOfRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyBasicEPS': {'data_type': 'float', 'default_value': 0, 'cn_name':''},
                'quarterlyNetIncomeContinuousOperations': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyEbitda': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingGrossProfit': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOperatingExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyDilutedAverageShares': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyPretaxIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyTaxProvision': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyDilutedEPS': {'data_type': 'float', 'default_value': 0, 'cn_name':''},
                'trailingNetIncomeCommonStockholders': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyGrossProfit': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOtherIncomeExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherIncomeExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyBasicAverageShares': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetIncomeContinuousOperations': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyResearchAndDevelopment': None, 'trailingDilutedAverageShares': None,
                'trailingBasicAverageShares': None, 'trailingBasicEPS': None, 'trailingInterestExpense': None,
                'trailingDilutedEPS': None, 'trailingResearchAndDevelopment': None}
    elif rtype == 'income_annual':
        return {'annualPretaxIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualEbitda': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingTotalRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualDilutedAverageShares': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCostOfRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualInterestExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOperatingIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingTaxProvision': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualBasicAverageShares': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualTaxProvision': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingPretaxIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingSellingGeneralAndAdministration': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherIncomeExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOperatingExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOperatingIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetIncomeCommonStockholders': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingGrossProfit': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOperatingExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualDilutedEPS': {'data_type': 'float', 'default_value': 0, 'cn_name':''},
                'annualSellingGeneralAndAdministration': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualGrossProfit': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCostOfRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualTotalRevenue': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetIncomeCommonStockholders': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetIncomeContinuousOperations': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOtherIncomeExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualBasicEPS': {'data_type': 'float', 'default_value': 0, 'cn_name':''},
                'trailingNetIncomeContinuousOperations': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingDilutedAverageShares': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingDilutedEPS': {'data_type': 'float', 'default_value': 0, 'cn_name':''},
                'trailingBasicEPS': {'data_type': 'float', 'default_value': 0, 'cn_name':''},
                'annualResearchAndDevelopment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingInterestExpense': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingResearchAndDevelopment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingBasicAverageShares': {'data_type': 'int', 'default_value': 0, 'cn_name':''}}
    elif rtype == 'cash':
        return {
                # Cash flows from operating activities
                'NetIncome': {'data_type': 'int', 'default_value': 0, 'name_on_page': '', 'cn_name': ''},
                'DepreciationAndAmortization': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Depreciation & amortization', 'cn_name':''},
                'DeferredIncomeTax': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Deferred income taxes', 'cn_name': ''},
                'StockBasedCompensation': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Stock based compensation', 'cn_name': '员工激励股权'},
                'ChangeInWorkingCapital': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Change in working capital', 'cn_name': '营运资金'},#营运资金亦称“运用资金”。国外称为营运资本。是合营企业流动资产总额减流动负债总额后的净额，即企业在经营中可供运用、周转的流动资金净额。Working capital is a financial metric which represents operating liquidity available to a business, organization, or other entity, including governmental entities.
                'ChangesInAccountReceivables': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Accounts receivable', 'cn_name': ''},
                'ChangeInAccountPayable': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Accounts receivable', 'cn_name': ''},
                'ChangeInInventory': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'chang in Inventory', 'cn_name': ''},
                'OtherNonCashItems': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Other non-cash items', 'cn_name': ''},
                'OperatingCashFlow': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Net cash provided by operating activites', 'cn_name': '运营资金'},#1、Operating Cash Flow（OCF）在估值当中不是很常用，更常用的现金流指标是Free Cash Flow（FCF）。虽然各个行业差距很大，但一般>10% FCF Yield就算比较高了，20%的FCF Yield说明公司五年左右赚的现金加起来就是目前的市值。有这样的估值，说明市场认为公司目前的现金流不能持续，也就是很不看好公司的未来。很多偏价值风格的投资经理会用Bloomberg或者Factset来筛选FCF Yield高的股票（比如>15%），在其中寻找自己比市场更看好的公司来投资。
                'OpertCashToFCF_ratio': {'data_type': 'float', 'default_value': 0, 'name_on_page': '', 'cn_name': '运营资金/自由现金流'},#1、Operating Cash Flow（OCF）在估值当中不是很常用，更常用的现金流指标是Free Cash Flow（FCF）。虽然各个行业差距很大，但一般>10% FCF Yield就算比较高了，20%的FCF Yield说明公司五年左右赚的现金加起来就是目前的市值。有这样的估值，说明市场认为公司目前的现金流不能持续，也就是很不看好公司的未来。很多偏价值风格的投资经理会用Bloomberg或者Factset来筛选FCF Yield高的股票（比如>15%），在其中寻找自己比市场更看好的公司来投资。

                #Cash flows from investing activities
                'PurchaseOfBusiness': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Acquisitions, net', 'cn_name': ''},
                'PurchaseOfInvestment': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Purchases of investments', 'cn_name': ''},
                'SaleOfInvestment': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Sales/Maturities of investments', 'cn_name': ''},
                'NetOtherInvestingChanges': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Other investing activites', 'cn_name': ''},
                'InvestingCashFlow': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Net cash used for investing activites', 'cn_name': ''},

                #Cash flows from financing activities
                'RepaymentOfDebt': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Debt repayment', 'cn_name': ''},
                'CommonStockIssuance': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Common stock issued', 'cn_name': ''},
                'RepurchaseOfCapitalStock': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Common stock repurchased', 'cn_name': ''},
                'CashDividendsPaid': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Dividends Paid', 'cn_name': '已发放现金股息'},
                'NetOtherFinancingCharges': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Other financing activites', 'cn_name':''},
                'CashFlowFromContinuingFinancingActivities': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Net cash used privided by (used for) financing activities', 'cn_name': ''},
                # change in cash
                'ChangeInCashSupplementalAsReported': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Net change in cash','cn_name': '现金变化'},
                'BeginningCashPosition': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Cash at beginning of period', 'cn_name':''},
                'EndCashPosition': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Cash at end of period', 'cn_name':''},
                'CapitalExpenditure': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Capital Expenditure', 'cn_name': '资本支出'},# normally = Investments in property, plant and equipment
                'FreeCashFlow': {'data_type': 'int', 'default_value': 0, 'name_on_page': 'Free Cash Flow', 'cn_name':'自由现金流'},

                # 'depreciation_rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '折旧率'},
                'capitalExpenditures_rate': {'data_type': 'float', 'default_value': 0, 'cn_name': '资本开支率(CapitalExpenditure/netIncome)'},
                'capitalExpenditures_rate2': {'data_type': 'float', 'default_value': 0, 'cn_name': '资本开支率（除去股票回购率）(getRate(CapitalExpenditure-abs(repurchaseOfStock),netIncome))'},
                'buybackRatio': {'data_type': 'float', 'default_value': 0, 'cn_name': '回购占比'}, # RepurchaseOfCapitalStock / netIncome

                "report_timestamp": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表时间戳'},
                "report_datetime": {'data_type': 'date', 'default_value': '0000-00-00', 'cn_name': '报表日期'},
                "report_year": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表年'},
                "report_month": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表月'},
                "report_date": {'data_type': 'int', 'default_value': 0, 'cn_name': '报表日'},
                "report_type": {'data_type': 'string', 'default_value': '', 'cn_name': '报表类型'}
                }
    elif rtype == 'cash_quaterly':
        return {'trailingOtherNonCashItems': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyBeginningCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingPurchaseOfBusiness': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNetOtherFinancingCharges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyChangeInAccountPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCashFlowFromContinuingFinancingActivities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCapitalExpenditure': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyChangeInWorkingCapital': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyDeferredIncomeTax': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingDepreciationAndAmortization': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingSaleOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyDepreciationAndAmortization': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyChangesInAccountReceivables': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetOtherFinancingCharges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCashDividendsPaid': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyEndCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingDeferredIncomeTax': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingRepurchaseOfCapitalStock': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInAccountPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyFreeCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInWorkingCapital': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOperatingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingPurchaseOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyChangeInCashSupplementalAsReported': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangesInAccountReceivables': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingBeginningCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyRepaymentOfDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingEndCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyInvestingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOperatingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCashFlowFromContinuingFinancingActivities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCashDividendsPaid': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyNetOtherInvestingChanges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlySaleOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingFreeCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyStockBasedCompensation': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingStockBasedCompensation': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyPurchaseOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInCashSupplementalAsReported': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyRepurchaseOfCapitalStock': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyPurchaseOfBusiness': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingInvestingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyCommonStockIssuance': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCapitalExpenditure': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyOtherNonCashItems': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetOtherInvestingChanges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCommonStockIssuance': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingRepaymentOfDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInInventory': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'quarterlyChangeInInventory': {'data_type': 'int', 'default_value': 0, 'cn_name':''}}
    elif rtype == 'cash_quaterly':
        return {'trailingOtherNonCashItems': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingPurchaseOfBusiness': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualRepaymentOfDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualChangeInWorkingCapital': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingDepreciationAndAmortization': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualSaleOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingSaleOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualDepreciationAndAmortization': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualInvestingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetOtherFinancingCharges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetOtherFinancingCharges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualStockBasedCompensation': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetOtherInvestingChanges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCommonStockIssuance': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualFreeCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualChangeInCashSupplementalAsReported': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingDeferredIncomeTax': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCapitalExpenditure': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingRepurchaseOfCapitalStock': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInAccountPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualPurchaseOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualPurchaseOfBusiness': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualBeginningCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInWorkingCapital': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingOperatingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingPurchaseOfInvestment': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualChangesInAccountReceivables': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCashDividendsPaid': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualEndCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangesInAccountReceivables': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingBeginningCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingEndCashPosition': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCashFlowFromContinuingFinancingActivities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCashDividendsPaid': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualCashFlowFromContinuingFinancingActivities': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingFreeCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualDeferredIncomeTax': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingStockBasedCompensation': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInCashSupplementalAsReported': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualChangeInAccountPayable': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetIncome': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingInvestingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOperatingCashFlow': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCapitalExpenditure': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualOtherNonCashItems': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualRepurchaseOfCapitalStock': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'annualChangeInInventory': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingNetOtherInvestingChanges': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingCommonStockIssuance': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingRepaymentOfDebt': {'data_type': 'int', 'default_value': 0, 'cn_name':''},
                'trailingChangeInInventory': {'data_type': 'int', 'default_value': 0, 'cn_name':''}}
