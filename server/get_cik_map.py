import requests
url = 'http://rankandfiled.com/data/identifiers?start='
index = '0'
result = requests.get(url+index).json()['list']

for r in result:
    print (r)
