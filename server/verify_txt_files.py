import glob
path = 'asset/premium_report_txt'
report_files = glob.glob("asset/premium_report_txt/report_*.txt")
error_symbols = {}
checked_symbols = []
print('-------------program start----------------')

for f in report_files:
    symbol = f.split('/')[2].replace('.txt','').split('_')[1]
    if symbol not in checked_symbols:
        match_files = glob.glob("asset/premium_report_txt/report_"+symbol+"_*.txt")
        if len(match_files)!=6:
            error_symbols[symbol] = len(match_files)
        checked_symbols.append(symbol)

print(error_symbols)
