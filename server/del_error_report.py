import glob
isHongKong = True
suffix = '_HK' if isHongKong == True else ''
path = 'asset/premium_report_txt'+suffix
error_files = glob.glob("asset/premium_report_txt"+suffix+"/error*.txt")
error_symbol = []
related_report_to_del = []
import os

print('-------------program start----------------')
def rm(path):
    command = 'rm -rf '+path
    os.system(command)
    print(command)

print('-------------error_files_to_del:-------------')
for f in error_files:
    symbol = f.split('/')[2].replace('.txt','').split('_')[1]
    if symbol not in error_symbol:
        error_symbol.append(symbol)
    rm(f)

for e in error_symbol:
    p = "asset/premium_report_txt"+suffix+"/report_"+e+"_*.txt"
    reports_to_del = glob.glob(p)
    related_report_to_del = reports_to_del + related_report_to_del

print('-------------related_report_files_to_del:-------------')
for r in related_report_to_del:
    rm(r)

f= open(path+"/aaa_error_symbols_to_retry.txt","w+")
f.write('"'+'","'.join(error_symbol)+'" \r\n \r\n')
f.write(','.join(error_symbol))
f.close()
print('-------------error symbols:-------------')
print(error_symbol)
