__name__ = "vutsuak"

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
        codes_url[ct - 1] = (codes_url[ct - 1] + (codes[ct - 1]).split(":")[1:11][0][1:-1])
        ct += 1
        if ct > 15:
            break
    x= image_filter(codes_url)  # contains 2 lists having filtered urls having no click kik and push and owner's name
    print x[0]
    print x[1]


def image_filter(image_list):
    final_urls=[]
    urls = []
    usernames=[]
    for i in image_list:
        try:
            resp = requests.get(i)
            soup = bs4.BeautifulSoup(resp.content)
            x = soup.findAll("meta")[6]["content"]
            if "click" in x or "kik" in x or "push" in x:
                continue
            else:
                #print i
                #print x
                urls.append(i)
                script = soup.find("script", text=re.compile('window\._sharedData'))
                pattern=re.compile(r'"owner":{"username":".+""')
                usernames.append(pattern.findall(script)[0].split(":")[2].split(",")[0])
                #print usernames[-1]

        except:
            continue
    final_urls.append(urls)
    final_urls.append(usernames)
    return final_urls


if __name__ == "vutsuak":
    get_recent_links(["cat"])
