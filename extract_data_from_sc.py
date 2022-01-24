import requests
import re
from bs4 import BeautifulSoup as bs

def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

def scrape_data(SC_URL):
    try:
        BASE_URL = "https://seniorcenter.us"
        URL = BASE_URL + str(SC_URL)
        headersparam = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
        html = requests.get(URL, headers=headersparam).content
        data = bs(html, 'html.parser')


        # z = open("extract.txt", "w")
        # z.close()

        f = open("extract.txt", "a", encoding="utf-8")

        import sys
        my_list= []
        check = True
        c = 0
        result = []
        for divtag in data.find_all('div', {'class': 'data-table'}):
            
            # for divrowtag in divtag.find_all('div'):
            #     for divdatatag in divrowtag.find_all('div'):
            if c == 5:
                c +=1
                
                tmp = str(divtag)
                # print("LEN: " + str(len(tmp)))
                # print("TMP:" + str(tmp))
                tmp = tmp.replace("<div class=\"data-table\">","")
                tmp = tmp.replace("</div>","")
                tmp = tmp.replace(",","")
                tmp = tmp.replace("\n","")

                if "data-cfemail" in tmp:  
                    tmp = tmp.split()
                    tmp = tmp[2]
                    # print("girdi")
                    # print("LEN: " + str(len(tmp)))
                    # print("TMP:" + str(tmp))
                    tmp = tmp.replace("data-cfemail=","")
                    tmp = tmp.replace("\"","")
                    tmp = cfDecodeEmail(tmp)
    
                if tmp == "":
                    tmp = "NOMAIL"
                # print("*"*80)
                # print(tmp)
                # print("*"*80)            
                result.append(tmp) 
                # print(tmp)         

            elif c != 6:
                if c ==1:
                    c +=1
                    tmp = str(divtag)
                    tmp = tmp.replace("<div class=\"data-table\">","")
                    tmp = tmp.replace("</div>","")
                    tmp = tmp.replace("\n","")
                    ztmp = tmp.replace(","," ")
                    tmp = tmp.replace(",","__")
                    

                
                    tmp2 = tmp.split()
                    tmp3 = tmp.split("__")
                    tmp3 = tmp3[1].replace("__", " ")

                    # print(tmp2[-1])
                    # print(tmp2[-2])
                    # print(tmp3)
                    tmp = str(ztmp) + "," + str(tmp2[-1]) + "," + str(tmp2[-2]) + "," +  str(tmp3)
                    # print(tmp)
                    result.append(tmp)
                else:
                    # print(c)
                    c +=1
                    tmp = str(divtag)
                    tmp = tmp.replace("<div class=\"data-table\">","")
                    tmp = tmp.replace("</div>","")
                    tmp = tmp.replace(",","")
                    tmp = tmp.replace("\n","")

                    result.append(tmp)

                    # print(tmp)
            else:
                # print(c)
                c +=1
                tmp = str(divtag)
                # print(tmp)
                matches = re.findall(r'".+?"',tmp)
                if len(matches)>1:
                    tmp = matches[1]
                    tmp = tmp[1:-1]
                else:
                    tmp= matches[0]
                
                # tmp = tmp.replace("<div class=\"data-table\">","")
                # tmp = tmp.replace("</div>","")
                tmp = tmp.replace(",","")
                tmp = tmp.replace("\n","")
                result.append(tmp)
                # print(tmp)
        # print(str(result[0]) + "," + str(result[1]) + "," + str(result[3]) + "," + str(result[4])+ "," + str(result[5])+ "," + str(result[6])+ "," + str(result[7])+ "," + str(result[8]) + "," + str(result[9])  +"," + str(result[10])  +"," + str(result[11]) + "\n")
        # for i in result:
        #     print(i)
        # f.write("Name,Address,Phone,Contact Name,Email address,Website,Details,Services,Age requirements,Operation Time")
        s = str(result[0]) + "," + str(result[1]) + "," + str(result[3]) + "," + str(result[4])+ "," + str(result[5])+ "," + str(result[6])+ "," + str(result[7])+ "," + str(result[8]) + "," + str(result[9])  +"," + str(result[10])  +"," + str(result[11]) + "\n" 
        return s
    except:
        print("bir hata olustu")
        return str(URL)+ "\n"



    # for h1tag in divtag.find_all('div', {'class': 'data-table'}):
    #     name = str(h1tag)
    #     # matches = re.findall(r'<h1>.+?<\/h1>',name)
    #     name = name.replace("<h1>","")
    #     name = name.replace("</h1>","")
    #     print("name: \n" + str(name))
    #     # for atag in h3tag.find_all('a'):
    #     #     tmp = str(atag)
        #     # print(tmp)
        #     matches = re.findall(r'".+?"',tmp)
        #     # print(matches)
        #     tmp = matches[0]
        #     tmp = tmp[1:-1]
        #     f.write(tmp + "\n")
        #     my_list.append(tmp)


# import numpy as np

# print(len(my_list))
# def unique(list1):
#     x = np.array(list1)
#     print(np.unique(x))

# unique(my_list)

# print(scrape_data("/sc/albertville_senior_citizens_center_albertville_al"))

# print(scrape_data("/sc/martling_senior_center_albertville_al"))