__name__ = "vutsuak"

import urllib2
import json
import re
import BeautifulSoup as bs4
import requests


def get_recent_links(tag, number=5):
    url = "https://www.instagram.com/explore/tags/"
    site1 = url + tag[0] + "/"
    resp = requests.get(site1)
    soup = bs4.BeautifulSoup(resp.content)
    script = soup.find("script", text=re.compile('window\._sharedData'))
    pattern = re.compile(r'"code":".*?"likes":{"count"')
    raw = pattern.findall(script)
    codes = []
    ct = 1
    codes_url = ["https://www.instagram.com/p/" for i in range(15)]
    for i in raw:
        codes.append(i.split(",")[0])
        codes_url[ct - 1] = (codes_url[ct - 1] +( codes[ct - 1]).split(":")[1:11][0][1:-1])
        print codes_url[ct-1]
        ct += 1
        if ct > 15:
            break


if __name__ == "vutsuak":
    get_recent_links(["cat"])
