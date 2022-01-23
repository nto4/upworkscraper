import get_state
import get_citys
import get_sc_in_city
import extract_data_from_sc
from time import sleep

# get state urls
get_state.get_states()
f = open("states.txt", "r")
states = f.read()

states = states.split(",")

# for state in states:
#     print(state)

# get citys for each state
count = 0
for state in states:
    citys = get_citys.get_cityss(state)
    for city in citys:
        senior_centers = get_sc_in_city.get_senior_center_in_city(city)
        for sc in senior_centers:
            count +=1
            print(count)
            print(sc)
            extract_data_from_sc.scrape_data(sc)
            #sleep(0.5)

print("BU KADAR MERKEZ VAR SAGLAMA ICN: " + str(count))
# for i in range(len(citys)):
#     print(str(i) + citys[i])

# senior_centers = get_sc_in_city.get_senior_center_in_city(citys[0])

# for sc in senior_centers:
#     extract_data_from_sc.scrape_data(sc)

# get senior center for eacn city