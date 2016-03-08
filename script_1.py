__name__ = "vutsuak"

import requests
import random
import re
def get_recent_links(tags, number=5):
    while number > 0:
        random.shuffle(tags)

        random.shuffle(tags)
        tag = tags[0]

        url = "https://www.instagram.com/explore/tags/" + tag + "/"

        response = requests.get(url)
        url_status = response.status_code
        url_data = response.content
        pattern = re.compile(r'"code":".*?"likes":{"count"')
        matches = pattern.findall(url_data)

        # print matches
        for match in matches:
            match = match.replace(",", "")
            match = match.replace("date", "")
            match = match.replace('"', "")
            match = match.replace("likes:{count", "")
            caption = match.split("}caption:")[1]
            caption = caption.lower()

            split_data = match.split(":")
            url_data = split_data[1]
            if 'click' not in caption and 'push' not in caption and 'c1ick' not in caption:
                try:
                    pic_url = "https://www.instagram.com/p/" + url_data + "/"
                    #run_pic(pic_url)
                    print pic_url
                    number = number - 1
                    break
                except:
                    print "error"
                    pass

if __name__=="vutsuak":
    get_recent_links(["cat"])
