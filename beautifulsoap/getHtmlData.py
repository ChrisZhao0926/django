from __future__ import absolute_import
import urllib2
from bs4 import BeautifulSoup

# Proxy set up
proxy = urllib2.ProxyHandler({'http': '10.154.250.100:8080'})
# password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
# proxy_auth =urllib2.HTTPBasicAuthHandler(password_mgr)
# proxy_auth.add_password(None,'http://www.gsmarena.com/sony_xperia_xa-7950.php','xxx','xxx')
# Create an URL opener utilizing proxy
# opener = urllib2.build_opener(proxy, proxy_auth)
opener = urllib2.build_opener(proxy,)
urllib2.install_opener(opener)

url = "http://www.gsmarena.com/sony_xperia_xa-7950.php"
url1 = 'http://www.cnblogs.com/bbcar/p/3424790.html'

# add header
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
# Aquire data from URL
try:
    request = urllib2.Request(url, headers=headers)
except urllib2.URLError, e:
    print e.reason

try:
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason

# Extract data as HTML data
html = response.read()

# Parse HTML data
soup = BeautifulSoup(html)
spec = soup.find(id='specs-list')
print(spec.get_text())
# print(soup.find_all('td', class_='nfo'))
#print (soup.title)
# print(soup.get_text())


#
# question_word = "2016"
# url = "http://www.gsmarena.com/sony_xperia_xa-7950.php"
# htmlpage = urllib2.urlopen(url).read()
# soup = BeautifulSoup(htmlpage)
# print len(soup.findAll("table", {"class": "result"}))
# for result_table in soup.findAll("table", {"class": "result"}):
#     a_click = result_table.find("a")
#     print "---------\n" + a_click.renderContents()
#     print "--------\n" + str(a_click.get("href"))
#     print "--------\n" + result_table.find("div", {"class": "c-abstract"}).renderContents()
#     print
# url = '!a.php'
#
# soup = BeautifulSoup(open(url))
# for link in soup.find_all('a'):
#     print(link.get('href'))


