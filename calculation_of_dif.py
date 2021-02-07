import math
import json



Spare_torpedoes = [0, 0, 0]
cistern12 = [0, 0, 0]
oil2_1 = [0, 0, 0]
oil2_2 = [0, 0, 0]
oil1_2 = [0, 0, 0]
water1 = [0, 0, 0]
food = [0, 0, 0]
water4 = [0, 0, 0]
summ = [0, 0]


with open("dif.json") as database:
    data = json.load(database)
'''    for i in data[1]:
        print(i)'''

print(Spare_torpedoes)
'''
with open("dif_out.json", 'r') as new_data:
    for i in data:
        json.dumps(i)


'''
'''print(data[2])
print(data[2]['Изменение нагрузки'])'''

'''for i in range(2,11):
    data[i]["Изменение нагрузки"]'''