
import urllib.request

def x():
    response = urllib.request.urlopen('http://python.org/')
    result = response.read().decode('utf-8')
    print(result)

x()