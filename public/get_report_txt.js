/**
    this code should be run in the browser console, in order to pass the cookie check from the server
    1. log in to Finance Yahoo first: finance.yahoo.com (with premium active account)
    2. open https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/V?lang=en-US&region=US&symbol=V&padTimeSeries=true&type=annualTotalAssets%2CtrailingTotalAssets%2CannualStockholdersEquity%2CtrailingStockholdersEquity%2CannualGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CannualRetainedEarnings%2CtrailingRetainedEarnings%2CannualCapitalStock%2CtrailingCapitalStock%2CannualTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CannualTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CannualOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CannualNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CannualNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CannualLongTermDebt%2CtrailingLongTermDebt%2CannualCurrentLiabilities%2CtrailingCurrentLiabilities%2CannualOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CannualCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CannualCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CannualIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CannualAccountsPayable%2CtrailingAccountsPayable%2CannualCurrentDebt%2CtrailingCurrentDebt%2CannualTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CannualOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CannualOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CannualGoodwill%2CtrailingGoodwill%2CannualInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CannualNetPPE%2CtrailingNetPPE%2CannualAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CannualGrossPPE%2CtrailingGrossPPE%2CannualCurrentAssets%2CtrailingCurrentAssets%2CannualOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CannualInventory%2CtrailingInventory%2CannualAccountsReceivable%2CtrailingAccountsReceivable%2CannualCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CannualOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CannualCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1580725608&corsDomain=finance.yahoo.com
    3. run the code below in the web console
    ps: request speed must be limited, if requests were sent too quickly, the respond would be 404
**/


function get_request_url(symbol, type, isPremuim, isHK) {
    if(isHK){
        symbol = symbol +'.HK'
    }
    let url  = '';
    if (type=='balance_annual'){
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'?lang=en-US&region=US&symbol='+symbol+'&padTimeSeries=true&type=annualTotalAssets%2CtrailingTotalAssets%2CannualStockholdersEquity%2CtrailingStockholdersEquity%2CannualGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CannualRetainedEarnings%2CtrailingRetainedEarnings%2CannualCapitalStock%2CtrailingCapitalStock%2CannualTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CannualTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CannualOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CannualNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CannualNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CannualLongTermDebt%2CtrailingLongTermDebt%2CannualCurrentLiabilities%2CtrailingCurrentLiabilities%2CannualOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CannualCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CannualCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CannualIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CannualAccountsPayable%2CtrailingAccountsPayable%2CannualCurrentDebt%2CtrailingCurrentDebt%2CannualTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CannualOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CannualOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CannualGoodwill%2CtrailingGoodwill%2CannualInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CannualNetPPE%2CtrailingNetPPE%2CannualAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CannualGrossPPE%2CtrailingGrossPPE%2CannualCurrentAssets%2CtrailingCurrentAssets%2CannualOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CannualInventory%2CtrailingInventory%2CannualAccountsReceivable%2CtrailingAccountsReceivable%2CannualCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CannualOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CannualCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1580725608&corsDomain=finance.yahoo.com'
    } else if (type == 'banlance_quarterly'){
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'?lang=en-US&region=US&symbol='+symbol+'&padTimeSeries=true&type=quarterlyTotalAssets%2CtrailingTotalAssets%2CquarterlyStockholdersEquity%2CtrailingStockholdersEquity%2CquarterlyGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CquarterlyRetainedEarnings%2CtrailingRetainedEarnings%2CquarterlyCapitalStock%2CtrailingCapitalStock%2CquarterlyTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CquarterlyTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CquarterlyOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CquarterlyNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CquarterlyNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CquarterlyLongTermDebt%2CtrailingLongTermDebt%2CquarterlyCurrentLiabilities%2CtrailingCurrentLiabilities%2CquarterlyOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CquarterlyCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CquarterlyCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CquarterlyIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CquarterlyAccountsPayable%2CtrailingAccountsPayable%2CquarterlyCurrentDebt%2CtrailingCurrentDebt%2CquarterlyTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CquarterlyOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CquarterlyOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CquarterlyGoodwill%2CtrailingGoodwill%2CquarterlyInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CquarterlyNetPPE%2CtrailingNetPPE%2CquarterlyAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CquarterlyGrossPPE%2CtrailingGrossPPE%2CquarterlyCurrentAssets%2CtrailingCurrentAssets%2CquarterlyOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CquarterlyInventory%2CtrailingInventory%2CquarterlyAccountsReceivable%2CtrailingAccountsReceivable%2CquarterlyCashCashEquivalentsAndMarketableSecurities%2CtrailingCashCashEquivalentsAndMarketableSecurities%2CquarterlyOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CquarterlyCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1580726454&corsDomain=finance.yahoo.com'
    } else if (type == 'income_quarterly'){
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'?lang=en-US&region=US&symbol='+symbol+'&padTimeSeries=true&type=quarterlyEbitda%2CtrailingEbitda%2CquarterlyWeighteAverageShare%2CtrailingWeighteAverageShare%2CquarterlyDilutedAverageShares%2CtrailingDilutedAverageShares%2CquarterlyBasicAverageShares%2CtrailingBasicAverageShares%2CquarterlyearningsPerShare%2CtrailingearningsPerShare%2CquarterlyDilutedEPS%2CtrailingDilutedEPS%2CquarterlyBasicEPS%2CtrailingBasicEPS%2CquarterlyNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CquarterlyNetIncome%2CtrailingNetIncome%2CquarterlyNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CquarterlyTaxProvision%2CtrailingTaxProvision%2CquarterlyPretaxIncome%2CtrailingPretaxIncome%2CquarterlyOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CquarterlyInterestExpense%2CtrailingInterestExpense%2CquarterlyOperatingIncome%2CtrailingOperatingIncome%2CquarterlyOperatingExpense%2CtrailingOperatingExpense%2CquarterlySellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CquarterlyResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CquarterlyGrossProfit%2CtrailingGrossProfit%2CquarterlyCostOfRevenue%2CtrailingCostOfRevenue%2CquarterlyTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580726564&corsDomain=finance.yahoo.com'
    } else if (type == 'income_annual'){
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'?lang=en-US&region=US&symbol='+symbol+'&padTimeSeries=true&type=annualEbitda%2CtrailingEbitda%2CannualWeighteAverageShare%2CtrailingWeighteAverageShare%2CannualDilutedAverageShares%2CtrailingDilutedAverageShares%2CannualBasicAverageShares%2CtrailingBasicAverageShares%2CannualearningsPerShare%2CtrailingearningsPerShare%2CannualDilutedEPS%2CtrailingDilutedEPS%2CannualBasicEPS%2CtrailingBasicEPS%2CannualNetIncomeCommonStockholders%2CtrailingNetIncomeCommonStockholders%2CannualNetIncome%2CtrailingNetIncome%2CannualNetIncomeContinuousOperations%2CtrailingNetIncomeContinuousOperations%2CannualTaxProvision%2CtrailingTaxProvision%2CannualPretaxIncome%2CtrailingPretaxIncome%2CannualOtherIncomeExpense%2CtrailingOtherIncomeExpense%2CannualInterestExpense%2CtrailingInterestExpense%2CannualOperatingIncome%2CtrailingOperatingIncome%2CannualOperatingExpense%2CtrailingOperatingExpense%2CannualSellingGeneralAndAdministration%2CtrailingSellingGeneralAndAdministration%2CannualResearchAndDevelopment%2CtrailingResearchAndDevelopment%2CannualGrossProfit%2CtrailingGrossProfit%2CannualCostOfRevenue%2CtrailingCostOfRevenue%2CannualTotalRevenue%2CtrailingTotalRevenue&merge=false&period1=493590046&period2=1580726527&corsDomain=finance.yahoo.com'
    } else if (type == 'cash_quarterly'){
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'?lang=en-US&region=US&symbol='+symbol+'&padTimeSeries=true&type=quarterlyFreeCashFlow%2CtrailingFreeCashFlow%2CquarterlyCapitalExpenditure%2CtrailingCapitalExpenditure%2CquarterlyOperatingCashFlow%2CtrailingOperatingCashFlow%2CquarterlyEndCashPosition%2CtrailingEndCashPosition%2CquarterlyBeginningCashPosition%2CtrailingBeginningCashPosition%2CquarterlyChangeInCashSupplementalAsReported%2CtrailingChangeInCashSupplementalAsReported%2CquarterlyCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CquarterlyNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CquarterlyCashDividendsPaid%2CtrailingCashDividendsPaid%2CquarterlyRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CquarterlyCommonStockIssuance%2CtrailingCommonStockIssuance%2CquarterlyRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CquarterlyInvestingCashFlow%2CtrailingInvestingCashFlow%2CquarterlyNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CquarterlySaleOfInvestment%2CtrailingSaleOfInvestment%2CquarterlyPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CquarterlyPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CquarterlyOtherNonCashItems%2CtrailingOtherNonCashItems%2CquarterlyChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CquarterlyChangeInInventory%2CtrailingChangeInInventory%2CquarterlyChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CquarterlyChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CquarterlyStockBasedCompensation%2CtrailingStockBasedCompensation%2CquarterlyDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CquarterlyDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CquarterlyNetIncome%2CtrailingNetIncome&merge=false&period1=493590046&period2=1580726233&corsDomain=finance.yahoo.com'
    } else if (type == 'cash_annual'){
        url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/premium/timeseries/'+symbol+'?lang=en-US&region=US&symbol='+symbol+'&padTimeSeries=true&type=annualFreeCashFlow%2CtrailingFreeCashFlow%2CannualCapitalExpenditure%2CtrailingCapitalExpenditure%2CannualOperatingCashFlow%2CtrailingOperatingCashFlow%2CannualEndCashPosition%2CtrailingEndCashPosition%2CannualBeginningCashPosition%2CtrailingBeginningCashPosition%2CannualChangeInCashSupplementalAsReported%2CtrailingChangeInCashSupplementalAsReported%2CannualCashFlowFromContinuingFinancingActivities%2CtrailingCashFlowFromContinuingFinancingActivities%2CannualNetOtherFinancingCharges%2CtrailingNetOtherFinancingCharges%2CannualCashDividendsPaid%2CtrailingCashDividendsPaid%2CannualRepurchaseOfCapitalStock%2CtrailingRepurchaseOfCapitalStock%2CannualCommonStockIssuance%2CtrailingCommonStockIssuance%2CannualRepaymentOfDebt%2CtrailingRepaymentOfDebt%2CannualInvestingCashFlow%2CtrailingInvestingCashFlow%2CannualNetOtherInvestingChanges%2CtrailingNetOtherInvestingChanges%2CannualSaleOfInvestment%2CtrailingSaleOfInvestment%2CannualPurchaseOfInvestment%2CtrailingPurchaseOfInvestment%2CannualPurchaseOfBusiness%2CtrailingPurchaseOfBusiness%2CannualOtherNonCashItems%2CtrailingOtherNonCashItems%2CannualChangeInAccountPayable%2CtrailingChangeInAccountPayable%2CannualChangeInInventory%2CtrailingChangeInInventory%2CannualChangesInAccountReceivables%2CtrailingChangesInAccountReceivables%2CannualChangeInWorkingCapital%2CtrailingChangeInWorkingCapital%2CannualStockBasedCompensation%2CtrailingStockBasedCompensation%2CannualDeferredIncomeTax%2CtrailingDeferredIncomeTax%2CannualDepreciationAndAmortization%2CtrailingDepreciationAndAmortization%2CannualNetIncome%2CtrailingNetIncome&merge=false&period1=493590046&period2=1580726340&corsDomain=finance.yahoo.com'
    }

    if (isPremuim){
        return url
    }else {
        return url.replace('premium', '')
    }
}
function download(filename, text) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}
function XHR2v2(url, data, params) {
    var self = this;
    var xhr = new XMLHttpRequest();
    data = data || {};
    params = params || {};
    try {
        function _delStr(str) {
            return str.replace(/[^\S\t ]/g, ' ').replace(/[\u0001-\u0008\u000c\u000e-\u001f\u007f]+/g, '');
        }
        // 处理类型
        var type = params['type'] || 'POST';
        // 处理数据参数
        var form;

        if (/GET/i.test(type)) {
            form = '';
            for (var p in data) {
                form = (form == '') ? (p + '=') : (form + '&' + p + '=');
                var valueType = typeof data[p];
                if (valueType == 'string') {
                    form += params.preDeal ? params.preDeal(value) : _delStr(data[p]);
                } else if (valueType == 'number') {
                    form += data[p];
                } else {
                    form += JSON.stringify(data[p]);
                }
            }
        } else {
            form = new FormData();
            for (var p in data) {
                var value = data[p],
                    valueType = typeof value;
                if (value == null) {
                    form.append(p, '');
                } else if (valueType == 'number' || value.toString() == '[object File]') {
                    form.append(p, value);
                } else {
                    if (valueType != 'string') {
                        value = JSON.stringify(value);
                    }
                    value = params.preDeal ? params.preDeal(value) : _delStr(value);
                    form.append(p, params.encodeURIComponent ? encodeURIComponent(value) : value);
                }
            }
        }
        // 超时
        params.timeout > 0 && (xhr.timeout = params.timeout);
        // 添加回调函数
        xhr.ontimeout = function (){
            params.onLoad('timeout!');
        };
        xhr.onload = function(e,r) {
            // console.log('----onload---');
            if (this.status != 200 || !this.responseText) {
                if(this.status ==404){
                    bad_request++;
                }
                params.onLoad(this);
            }else {
                params.onLoad(null, this.responseText);
            }
        };

        xhr.onabort = params['onabort'];
        xhr.onerror = function(e) {
            console.log(e.stack);
            params.onLoad(e);
        };

        xhr.open(type, url, true);
        // xhr 发送头参数设置
        if (!window.XDomainRequest && (type.toUpperCase() == 'GET')) {
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;");
        }
        xhr.send(form);
    } catch (e) {
        console.log(e.stack);
        console.log("请求失败： " + e.message);
    }
    return xhr;
}


function send_request(symbol, type, cb){
    let url = get_request_url(symbol,type, true );
    XHR2v2(url, null, {type: 'GET', onLoad:function (error,resp_text){
        if(error){
            download('error_'+symbol+'_'+type+'.txt', 'url:'+url+',     error'+JSON.stringify(error))
        }else{
            download('report_'+symbol+'_'+type+'.txt', resp_text)
        }
        cb(error)
    }});
}

// const symbols = ['DFTBCL', 'BCSDCL', 'GPTA', 'GPEA', 'BCVA', 'IVRA', 'HTB'];
const symbols = ['FUTU','BRK-A','BRK-B'];
// const symbols = ['AAB', 'ABRA', 'ABRB', 'ABRC', 'ABVC', 'ACWD', 'ACTA', 'ADKA', 'AESC', 'AESCCL', 'AFACL', 'AFMCL', 'AFQCL', 'AFSIA', 'AFSIB', 'AFSIC', 'AFSID', 'AFSIE', 'AFSIF', 'AFWCL', 'AGMA', 'AGMC', 'AGNA', 'AGOB', 'AGOE', 'AGOF', 'AHLA', 'AHLB', 'AHLBCL', 'AHLC', 'AHLD', 'AHPB', 'AHTA', 'AHTACL', 'AHTD', 'AHTDCL', 'AHTE', 'AHTECL', 'AHTF', 'AHTG', 'AHTH', 'AHTI', 'AIBCL', 'AIGWS', 'AIVA', 'AIVZ', 'AIVZCL', 'AKOA', 'AKOB', 'ALLA', 'ALLD', 'ALLF', 'ALLG', 'ALLYA', 'ALLYB', 'ALLYBCL', 'ALPO', 'ALPQ', 'ALRB', 'AMHA', 'AMHB', 'AMHC', 'AMHD', 'AMHE', 'AMHF', 'AMHG', 'AMHH', 'AMTGA', 'ANHA', 'ANHB', 'ANHC', 'APOA', 'APOB', 'ARED', 'AREE', 'ARESA', 'ARHC', 'ARIACL', 'ARIC', 'ARLOV', 'ARNCB', 'ARPD', 'ARPE', 'ARRA', 'ARRB', 'ARUCL', 'ARYCL', 'ASBBCL', 'ASBD', 'ASBE', 'ASBWS', 'ASTWS', 'AXSC', 'AXSD', 'AXSE', 'BACA', 'BACB', 'BACC', 'BACD', 'BACE', 'BACI', 'BACK', 'BACW', 'BACWSA', 'BACWSB', 'BACY', 'BACZ', 'BACZCL', 'BANCC', 'BANCD', 'BANCE', 'BBTD', 'BBTE', 'BBTF', 'BBTG', 'BBTH', 'BCB', 'BCSCL', 'BCSA', 'BCSC', 'BCSCCL', 'BCSD', 'BCSDCL', 'BCVA', 'BDCB', 'BDNE', 'BDNECL', 'BFA', 'BFSC', 'BFSD', 'BGEB', 'BGEBCL', 'BHRB', 'BHRD', 'BIOB', 'BIOAWS', 'BIRA', 'BIRACL', 'BMLG', 'BMLH', 'BMLI', 'BMLJ', 'BMLL', 'BOCACL', 'BRGA', 'BRGC', 'BRGD', 'BTXWS', 'BWLA', 'BXPB', 'CK', 'CLCL', 'CS', 'CWSA', 'CWSB', 'CAIA', 'CAIB', 'CBBB', 'CBLD', 'CBLE', 'CCCU', 'CCCWS', 'CCGA', 'CCHU', 'CCHWS', 'CCIA', 'CDEWS', 'CDRC', 'CFCA', 'CFCACL', 'CFRA', 'CHACWS', 'CHKD', 'CHMIA', 'CHSPA', 'CHSPACL', 'CICU', 'CICWS', 'CIGC', 'CIMB', 'CIMC', 'CIMD', 'CIOA', 'CISNWS', 'CLACL', 'CLNSA', 'CLNSACL', 'CLNSB', 'CLNSC', 'CLNSD', 'CLNSE', 'CLNSF', 'CLNSFCL', 'CLNSG', 'CLNSH', 'CLNSI', 'CLNYA', 'CLNYB', 'CLNYC', 'CLNYD', 'CLNYE', 'CLNYG', 'CLNYH', 'CLNYI', 'CLNYJ', 'CMAWS', 'CMOE', 'CMREB', 'CMREC', 'CMRED', 'CMREE', 'CNPB', 'CODIA', 'CODIB', 'COFC', 'COFD', 'COFF', 'COFG', 'COFH', 'COFP', 'COFWS', 'CORA', 'CORRA', 'CPEA', 'CRDB', 'CRMDWS', 'CTQCL', 'CUBEA', 'CUBIC', 'CUBID', 'CUBIE', 'CUBIF', 'CVMWS', 'CWENA', 'CYNC', 'CYND', 'CYSB', 'DCPB', 'DCPC', 'DDA', 'DDB', 'DDRA', 'DDRJ', 'DDRK', 'DFSB', 'DFTA', 'DFTB', 'DFTBCL', 'DFTC', 'DHCPWSA', 'DHCPWSB', 'DHRWD', 'DLNGA', 'DLNGB', 'DLRE', 'DLRECL', 'DLRF', 'DLRFCL', 'DLRG', 'DLRH', 'DLRJ', 'DOWWD', 'DSB', 'DSC', 'DSD', 'DSXB', 'DXA', 'DYNA', 'DYNWS', 'DYNWSA', 'EAACL', 'EBRB', 'ECFA', 'EFMCL', 'ELACL', 'ELBCL', 'ELSC', 'ELSCCL', 'EMZCL', 'ENHA', 'ENHACL', 'ENHB', 'ENHBCL', 'ENHC', 'ENRA', 'EPMA', 'EPMACL', 'EPRG', 'EQCD', 'EQCE', 'EQCECL', 'EQTV', 'ESSH', 'ESSHCL', 'ETPC', 'ETPD', 'EVERA', 'EXLB', 'FBSA', 'FBSACL', 'FCEB', 'FCHA', 'FCHCCL', 'FGWS', 'FHNA', 'FMERA', 'FNBE', 'FNFGB', 'FPACU', 'FPACWS', 'FPIB', 'FPOA', 'FPOACL', 'FPPWS', 'FRCA', 'FRCB', 'FRCBCL', 'FRCC', 'FRCD', 'FRCE', 'FRCECL', 'FRCF', 'FRCG', 'FRCH', 'FRCI', 'FRTC', 'GABD', 'GABG', 'GABH', 'GABJ', 'GAMB', 'GCVB', 'GDLB', 'GDLC', 'GDPC', 'GDPD', 'GDVA', 'GDVG', 'GEFB', 'GGNB', 'GGOA', 'GGOC', 'GGPA', 'GGTB', 'GGTE', 'GGZA', 'GIGU', 'GIGWS', 'GLFWS', 'GLOGA', 'GLOPA', 'GLOPB', 'GLOPC', 'GLPA', 'GLUA', 'GLUB', 'GMWSA', 'GMWSB', 'GMWSC', 'GMREA', 'GNEA', 'GNLA', 'GPEA', 'GPTA', 'GPTB', 'GRAFU', 'GRAFWS', 'GRHC', 'GRPU', 'GRXA', 'GRXB', 'GSA', 'GSN', 'GSAHU', 'GSAHWS', 'GSFCL', 'GSLB', 'GSTA', 'GSTB', 'GTNA', 'GUACL', 'GUTA', 'GUTC', 'GXPA', 'GXPACL', 'GXPB', 'GXPBCL', 'GXPD', 'GXPDCL', 'GXPE', 'GXPECL', 'HBMWS', 'HCACWS', 'HCFTA', 'HCFTACL', 'HCNI', 'HCNJ', 'HEU', 'HEIA', 'HESA', 'HIGG', 'HIGWS', 'HKWS', 'HLB', 'HLM', 'HLSWS', 'HMLPA', 'HPEV', 'HPPB', 'HPPBCL', 'HPTD', 'HSFCB', 'HSFCBCL', 'HTB', 'HTBCL', 'HTE', 'HTGXCL', 'HTSA', 'HUSIDCL', 'HUSIF', 'HUSIG', 'HUSIH', 'HUSIZCL', 'HVTA', 'HZ', 'IA', 'List', 'IDGCL', 'IGCWS', 'IIPRA', 'IMUCWS', 'INDCL', 'INNA', 'INNACL', 'INNB', 'INNC', 'INND', 'INNE', 'INSWA', 'IPLD', 'IPOAU', 'IPOAWS', 'IRCA', 'IRCB', 'IRETB', 'IRETC', 'ISHA', 'ISHB', 'IVRA', 'IVRB', 'JCAPB', 'JEA', 'JPMA', 'JPMD', 'JPMG', 'JPMH', 'JPMWS', 'JWB', 'KAPCL', 'KEYG', 'KEYH', 'KEYI', 'KEYJ', 'KFICL', 'KIMH', 'KIMHCL', 'KIMI', 'KIMJ', 'KIMK', 'KIML', 'KIMM', 'KKRA', 'KKRB', 'KMIA', 'KMIWS', 'KODKWS', 'KODKWSA', 'KRCG', 'KRCH', 'KRCHCL', 'KRGA', 'KRGACL', 'KYNE', 'KYNECL', 'KYNF', 'KYNG', 'KYNGCL', 'LENB', 'LGCU', 'LGCWS', 'LGFA', 'LGFB', 'LGLWS', 'LHCU', 'LHCWS', 'LHOH', 'LHOHCL', 'LHOI', 'LHOJ', 'LNCWS', 'LOUU', 'LOUWS', 'LTNU', 'LTNWS', 'LTSA', 'LXPC', 'LYGA', 'LYGACL', 'MAAI', 'MDGNWS', 'MERD', 'MERDCL', 'MERE', 'MERECL', 'MERF', 'MERFCL', 'MERK', 'MERM', 'MERMCL', 'MERP', 'META', 'METBCL', 'METE', 'MFAB', 'MFACU', 'MFACWS', 'MGRCL', 'MGYWS', 'MHA', 'MHC', 'MHNBCL', 'MHOA', 'MHRC', 'MHRD', 'MHRE', 'MILLC', 'MILLD', 'MITTA', 'MITTB', 'MKCV', 'MNRA', 'MNRACL', 'MNRB', 'MNRBCL', 'MNRC', 'MOGB', 'MOSCU', 'MOSCWS', 'MPD', 'MRHA', 'MRHACL', 'MSE', 'MSJCL', 'MSKCL', 'MSZCL', 'MTBWS', 'MWGCL', 'MWOCL', 'MWRCL', 'NAVD', 'NBGA', 'NBRA', 'NCTB', 'NCTC', 'NCTD', 'NCVA', 'NCZA', 'NEEC', 'NEEG', 'NEEH', 'NEEI', 'NEEJ', 'NEEK', 'NEEO', 'NEEP', 'NEEQ', 'NEER', 'NGLB', 'NGLSA', 'NHCA', 'NHCACL', 'NLYA', 'NLYACL', 'NLYC', 'NLYD', 'NLYE', 'NLYF', 'NLYG', 'NLYH', 'NMH', 'NMKB', 'NMKC', 'NNND', 'NNNE', 'NNNF', 'NRCGWS', 'NRFA', 'NRFB', 'NRFC', 'NRFD', 'NRFE', 'NSB', 'NSAA', 'NSLPA', 'NSPRWS', 'NSPRWSB', 'NWC', 'NWCCL', 'NYCBA', 'NYCBU', 'NYLDA', 'OF', 'OAKA', 'OAKB', 'OAKSA', 'OCRA', 'OCRB', 'OFCL', 'OFCLCL', 'OFGA', 'OFGB', 'OFGD', 'OIBRC', 'OMADU', 'OMADWS', 'PBIA', 'PBIACL', 'PBRA', 'PCGA', 'PCGB', 'PCGC', 'PCGD', 'PCGE', 'PCGG', 'PCGH', 'PCGI', 'PEBA', 'PEBACL', 'PEBB', 'PEBBCL', 'PEBC', 'PEBD', 'PEBE', 'PEBF', 'PEIA', 'PEIB', 'PEIC', 'PEID', 'PFGBCL', 'PJSCL', 'PLC', 'PLCCL', 'PLECL', 'PLYMA', 'PMTA', 'PMTB', 'PNCP', 'PNCQ', 'PNCWS', 'PNTACL', 'PPSA', 'PRED', 'PREDCL', 'PREE', 'PREECL', 'PREG', 'PREH', 'PREI', 'PRIFA', 'PRIFB', 'PRYCL', 'PSAA', 'PSAB', 'PSAC', 'PSAD', 'PSAE', 'PSAF', 'PSAG', 'PSAP', 'PSAPCL', 'PSAQ', 'PSAQCL', 'PSAR', 'PSARCL', 'PSAS', 'PSASCL', 'PSAT', 'PSATCL', 'PSAW', 'PSAX', 'PSAY', 'PSAZ', 'PSBR', 'PSBRCL', 'PSBS', 'PSBT', 'PSBU', 'PSBV', 'PSBW', 'PSBX', 'PSBY', 'PUKA', 'PVCTWS', 'PVTU', 'PVTWS', 'PWA', 'QTSA', 'QTSB', 'RASA', 'RASB', 'RASC', 'RBSE', 'RBSECL', 'RBSF', 'RBSFCL', 'RBSG', 'RBSGCL', 'RBSH', 'RBSHCL', 'RBSI', 'RBSICL', 'RBSL', 'RBSLCL', 'RBSM', 'RBSMCL', 'RBSN', 'RBSNCL', 'RBSP', 'RBSPCL', 'RBSQ', 'RBSQCL', 'RBSR', 'RBSRCL', 'RBSS', 'RBSSCL', 'RBST', 'RBSTCL', 'RDSA', 'RDSB', 'REGF', 'REGG', 'REGGCL', 'REXRA', 'REXRB', 'RFB', 'RHEA', 'RLGTA', 'RLGTACL', 'RLGTACLAMEX', 'RLHA', 'RLHACL', 'RLJA', 'RMPL', 'RNRC', 'RNRE', 'RNRF', 'RPAIA', 'RPTD', 'RSOA', 'RSOB', 'RSOC', 'RWGEU', 'RWGEWS', 'RXNA', 'RYS', 'RYSCL', 'RYAMA', 'SANA', 'SANB', 'SANC', 'SANI', 'SBC', 'SBD', 'SCEB', 'SCEC', 'SCED', 'SCEE', 'SCEF', 'SCEFCL', 'SCEG', 'SCEH', 'SCEJ', 'SCEK', 'SCEL', 'SCHWB', 'SCHWC', 'SCHWD', 'SCQCL', 'SDOPACL', 'SDOPBCL', 'SDOPCCL', 'SDOPHCL', 'SFNCL', 'SGRPW', 'SGYWS', 'SHOD', 'SHODCL', 'SHOF', 'SITCA', 'SITCJ', 'SITCK', 'SNVC', 'SNVD', 'SOVC', 'SPAQU', 'SPAQWS', 'SPEB', 'SPGJ', 'SPLPA', 'SRCA', 'SREB', 'SRGA', 'SSWCCL', 'SSWD', 'SSWE', 'SSWG', 'SSWH', 'SSWI', 'STAGA', 'STAGACL', 'STAGB', 'STAGC', 'STARD', 'STARE', 'STARF', 'STARG', 'STARI', 'STIA', 'STIWSA', 'STIWSB', 'STLA', 'STTD', 'STTE', 'STTG', 'STZB', 'SUIA', 'SUZV', 'TAKV', 'TALOWS', 'TAPA', 'TCBB', 'TCBC', 'TCBWS', 'TCCCL', 'TCFB', 'TCFD', 'TCFWS', 'TCOJ', 'TCOK', 'TCRXCL', 'TDWWS', 'TDWWSA', 'TDWWSB', 'TEUC', 'TGPA', 'TGPB', 'TIA', 'TMKB', 'TMKC', 'TMUSA', 'TNPB', 'TNPC', 'TNPD', 'TNPE', 'TNPF', 'TOOA', 'TOOB', 'TOOE', 'TPGEU', 'TPGEWS', 'TPGHU', 'TPGHWS', 'TPVZCL', 'TRCWS', 'TRNOA', 'TRNOACL', 'TWOA', 'TWOB', 'TWOD', 'TWOE', 'TYGB', 'TYGBCL', 'TYGC', 'TYGCCL', 'TZFCL', 'UBPF', 'UBPG', 'UBPH', 'UBSD', 'UBSDCL', 'UMHA', 'UMHACL', 'UMHB', 'UMHC', 'UMHD', 'USBA', 'USBH', 'USBM', 'USBN', 'USBNCL', 'USBO', 'USBP', 'UTXA', 'UUUUWS', 'VALEP', 'VERF', 'VLYA', 'VLYB', 'VLYWS', 'VNOG', 'VNOI', 'VNOJ', 'VNOJCL', 'VNOK', 'VNOL', 'VRACL', 'VRB', 'VRBCL', 'VSTWSA', 'WBSE', 'WBSWS', 'WELLI', 'WFV', 'WFCJ', 'WFCL', 'WFCN', 'WFCO', 'WFCP', 'WFCQ', 'WFCR', 'WFCT', 'WFCV', 'WFCW', 'WFCWS', 'WFCX', 'WFCY', 'WFEA', 'WIZEIV'];
let types = ['balance_annual','balance_quarterly','income_quarterly','income_annual','cash_quarterly','cash_annual'];
let l = symbols.length;


function loop(sindex, tindex){
    if(symbols[sindex]){
        let t = types.length;
        let cc = function (error){
            tindex++;
            if(tindex==t){
                console.log(symbols[sindex]+',   '+sindex +'   of   ' +l);
                sindex++;
                if(bad_request>3){
                    console.log('404, WAITING...');
                    setTimeout(function (){
                        bad_request = 0
                        loop(sindex, 0);
                    }, 360000);
                }else{
                    setTimeout(function (){
                        loop(sindex, 0);
                    }, 500);
                }
            }else{
                if(bad_request>3){
                    console.log('404, WAITING...');
                    setTimeout(function (){
                        bad_request = 0
                        send_request(symbols[sindex], types[tindex], cc);
                    }, 360000);
                }else{
                    setTimeout(function (){
                        send_request(symbols[sindex], types[tindex], cc);
                    }, 400);
                }
            }
        };
        send_request(symbols[sindex], types[tindex], cc);

    }else{
        console.log('done');
    }
}
var bad_request = 0;
loop(0, 0);

// for (let i =0;i<a.length;i++){
//     let text = a[i].innerText, sp = text.split(' ');
//     if(sp.length>=2 && sp[0] == parseInt(sp[0]) && sp[0] >3399){
//         b.push({'stock_symbol':sp[0],'stock_name':text.replace(sp[0]+' ','')})
//     }
// }