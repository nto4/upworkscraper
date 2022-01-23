import requests
import re
from bs4 import BeautifulSoup as bs
def get_senior_center_in_city(SC_URL):
    BASE_URL = "https://seniorcenter.us"
    URL = BASE_URL + SC_URL
    headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    html = requests.get(URL, headers=headersparam).content
    data = bs(html, 'html.parser')


    z = open("sc_in_citys.txt", "w")
    z.close()

    f = open("sc_in_citys.txt", "a")

    import sys
    my_list= []
    check = True
    for divtag in data.find_all('div', {'class': 'img-indent-bot'}):
        for h3tag in divtag.find_all('h3'):
            for atag in h3tag.find_all('a'):
                tmp = str(atag)
                # print(tmp)
                matches = re.findall(r'".+?"',tmp)
                # print(matches)
                tmp = matches[0]
                tmp = tmp[1:-1]
                # f.write(tmp + "\n")
                my_list.append(tmp)

    return my_list
    # import numpy as np

    # print(len(my_list))
    # def unique(list1):
    #     x = np.array(list1)
    #     print(np.unique(x))

    # unique(my_list)

