import urllib.request

fp = urllib.request.urlopen("http://www.rajanews.com")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)
