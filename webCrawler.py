import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "https://moose.ncbs.res.in/"
depth = 0
#url = "http://www.thehindu.com/sport"
#url = "http://www.google.com"
#base = "http://www.google.com"
#
#htmlFile = urllib.urlopen( url )
#
#soup = BeautifulSoup(htmlFile, "lxml")
#
#for tag in soup.findAll('a', href=True) : 
#        print urlparse.urlparse(tag['href']).path
#        #print urlparse.urlparse(tag['href']).hostname
#        #print tag['href']
#        #print base + "/" + tag['href']

# Rahul - This part is to browse through the ref links in a given url
#br = mechanize.Browser()
#br.set_handle_robots(False) #Am not a robot
#
#br.open(url)
#
#
#for link in br.links() : 
#        newurl = urlparse.urljoin(link.base_url, link.url)
#        baseurl = link.base_url
#        b2 = urlparse.urlparse(newurl).path
#        b1 = urlparse.urlparse(newurl).hostname
#        print "http://"+b1+b2

# Rahul - This part is to crawl the web using these references 
br = mechanize.Browser()
br.set_handle_robots(False) #Am not a robot

urls = [url]
visited = [url]

while len(urls)>0 and depth < 10: 
        try : 
                br.open(urls[0])
                urls.pop(0)
                for link in br.links() : 
                        newurl = urlparse.urljoin(link.base_url, link.url)
                        baseurl = link.base_url
                        b2 = urlparse.urlparse(newurl).path
                        b1 = urlparse.urlparse(newurl).hostname
                        print "http://"+b1+b2
                        
                        if newurl not in visited and urlparse.urlparse(url).hostname in newurl: 
                                visited.append(newurl)
                                urls.append(newurl)
                                #print newurl
                depth+=1
        except : 
                urls.pop(0)
                print '""""""""ERROR : BROKEN PAGE **********' 
print visited
