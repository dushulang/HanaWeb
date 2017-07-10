import urllib.request as ur

with ur.urlopen('http://www.python.org/') as f:
    print(f.read())

