import requests
import re
from bs4 import BeautifulSoup as bs
# URL = "https://seniorcenter.us/senior-centers-state/california"
URL = "https://seniorcenter.us/senior-centers-state/california"
# URL = "https://seniorcenter.us/senior-centers-state/washington"
headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
html = requests.get(URL, headers=headersparam).content
# soup = bs(r.content, "lxml", from_encoding='UTF-8')
data = bs(html, 'html.parser')
f = open("citys.txt", "a")

my_list= []
check = True
for ultag in data.find_all('div', {'class': 'us_cities'}):
    # print(ultag)
    for litag in ultag.find_all('li'):
        for atag in ultag.find_all('a'): 
            tmp = str(atag)
            matches = re.findall(r'".+?"',tmp)
            # print(matches)
            tmp = matches[0]
            tmp = tmp[1:-1]
            f.write(tmp + "\n")
            my_list.append(tmp)


import numpy as np

print(len(my_list))
def unique(list1):
    x = np.array(list1)
    print(np.unique(x))

unique(my_list)


"""
Burdan eyaletleri çektiriyorum 
https://seniorcenter.us/

her eyalet için bu sayfadan https://seniorcenter.us/senior-centers-state/wyoming




"""