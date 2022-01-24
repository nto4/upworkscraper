
import get_state
import get_citys
import get_sc_in_city
import extract_data_from_sc
from time import sleep
import os

import multiprocessing
import time



def run_state(state):  
    final =[] 
    citys = get_citys.get_cityss(state)
    if citys is None:
        pass
    else:
        for city in citys:
            senior_centers = get_sc_in_city.get_senior_center_in_city(city)
            for sc in senior_centers:
                # count +=1
                # print(count)
                # print(sc)
                f = open("extract.txt", "a", encoding="utf-8")

                f.write(extract_data_from_sc.scrape_data(sc))
                f.close()
                final.append(extract_data_from_sc.scrape_data(sc))

    return final
            #sleep(0.5)
if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=6)
    # get state urls
    get_state.get_states()
    f = open("states.txt", "r")
    states = f.read()

    states = states.split(",")
    # print("len states ")
    # print(len(states))

    del states[-1]
    # print(len(states))
    # for state in states:
    #     print(state)
    # get citys for each state
    count = 0
    finals = pool.map(run_state,states)
    # for state in states:
        # run_state(state)
    print("BU KADAR MERKEZ VAR SAGLAMA ICN: " + str(count))
    # for i in range(len(citys)):
    #     print(str(i) + citys[i])
    ff = open("extractson.txt", "a", encoding="utf-8")

    for elem in finals:
        ff.write(elem)
    ff.close()
    # senior_centers = get_sc_in_city.get_senior_center_in_city(citys[0])

    # for sc in senior_centers:
    #     extract_data_from_sc.scrape_data(sc)

    # get senior center for eacn city