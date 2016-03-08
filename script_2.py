__name__ = "vutsuak"

import urllib2
import BeautifulSoup as bs4

def get_recent_links(tag,number=5):
    url="https://www.instagram.com/explore/tags/"
    site1 =url+ tag[0] + "/"
    html= urllib2.urlopen(site1)
    soup = bs4.BeautifulSoup(html)
    for i in soup.findAll("a"):
        print i

if __name__=="vutsuak":
    get_recent_links(["cat"])