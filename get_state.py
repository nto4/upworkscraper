import requests
import re
from bs4 import BeautifulSoup as bs
def get_states():
    # URL = "https://seniorcenter.us/senior-centers-state/california"
    URL = "https://seniorcenter.us/"
    # URL = "https://seniorcenter.us/senior-centers-state/washington"
    headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    html = requests.get(URL, headers=headersparam).content
    # soup = bs(r.content, "lxml", from_encoding='UTF-8')
    data = bs(html, 'html.parser')

    # clean file 
    z = open("states.txt", "w")
    z.close()

    f = open("states.txt", "a")

    my_list= []
    check = True
    for maptag in data.find_all('map', {'name': 'usmap'}):
        # print(ultag)
        for areatag in maptag.find_all('area'):
            tmp = str(areatag)
            tmp= tmp.split()
            # my_list.append(tmp[2])
            t = str(tmp[2])
            t = t[1:-1]
            t = t.replace("ref=\"","")
            f.write(t + ",")
            # tmp = str(atag)
            # matches = re.findall(r'".+?"',tmp)
            # # print(matches)
            # tmp = matches[0]
            # tmp = tmp[1:-1]
            # f.write(tmp + "\n")
            # my_list.append(tmp)


    # f = open("states.txt", "r")
    # x = f.read()
    # x = x.split(",")
    # # for i in x:
    #     print(i)
    # print(my_list)



    """
    Burdan eyaletleri çektiriyorum 
    https://seniorcenter.us/

    her eyalet için bu sayfadan https://seniorcenter.us/senior-centers-state/wyoming




    """