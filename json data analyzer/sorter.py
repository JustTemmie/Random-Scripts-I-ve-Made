from calendar import week
import json
from re import M
import time
import pandas as pd
import operator
#import matplotlib.pyplot as plt

input = json.load(open('hendex.json', 'r'))

unixtime = []
timetoday = {}
weekday = []
messagelen = []
channel = []

reference = {}

s = 0

for h in range(0, 24):
    for m in range(0, 60, 1):
        for s in range(0, 60, 10):
            q = str(s)
            w = str(m)
            f = str(h)
            if s < 10:
                q = '0' + str(s)
            if m < 10:
                w = '0' + str(m)
            if h < 10:
                f = '0' + str(h)
            reference[((str(f"{f}{w}{q}")))] = [int(f"{f}{w}{q}"), str(f"{f}:{w}:{q}")]


col1 = "unixtime"
col2 = "timetoday"
col3 = "weekday"
col4 = "len"
col5 = "channel"


for y, x in input.items():
    
    i = x.split(", ")
    #print(i[0])

    
    #unixtime.append(x[0])
    #timetoday[time.time()] = x[0]
    a = [int(time.strftime("%H%M%S", time.localtime(float(y)))), str(time.strftime("%H:%M.%S", time.localtime(float(y)))), i[0]]
    reference[str(time.strftime("%H:%M.%s", time.localtime(float(y))))] = a
    #timelist = sorted(markdict.items(), key=lambda x:x[1])
    #sortdict = dict(marklist)
    #print(str(time.strftime("%H:%M:%S", time.localtime(float(x[0])))))
    #weekday.append(time.strftime("%D", time.localtime(float(x[0]))))
    
    #timetoday = sorted(timetoday)
    
    #messagelen.append(i[0])
    #channel.append(i[1])
   
   
marklist= sorted(reference.items(), key=operator.itemgetter(1)) 
sortdict=dict(marklist)

ars = []
qwf = []
for x in sortdict.items():
    #print(x)
    try:
        ars.append(x[1][2])
        qwf.append(x[1][1])
    except:
        ars.append(0)
        qwf.append(x[1][1])

print(len(ars), len(qwf))

#plt.plot(qwf, ars)
#plt.show()

#data = pd.DataFrame({col1:unixtime,col2:timetoday,col3:weekday,col4:messagelen,col5:channel})
data = pd.DataFrame({col2:qwf,col4:ars})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)