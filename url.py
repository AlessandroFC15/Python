import urllib2

response = urllib2.urlopen('http://www.wdylike.appspot.com/')

# Get all data
html = response.read()
print "Get all data: ", html
