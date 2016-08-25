import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "https://moose.ncbs.res.in/"
depth = 0

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
                depth+=1
        except : 
                urls.pop(0)
                print '""""""""ERROR : BROKEN PAGE **********' 
print visited
