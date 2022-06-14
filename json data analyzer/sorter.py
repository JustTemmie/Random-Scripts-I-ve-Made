from calendar import week
import json
from re import M
import time
import pandas as pd
import operator
#import matplotlib.pyplot as plt

#input = json.load(open('hendex.json', 'r'))
#input = json.load(open('temdex.json', 'r'))
input = json.load(open('everyone.json', 'r'))

unixtime = []
timetoday = {}
weekday = []
messagelen = []
channel = []

reference = {}

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0
thirteen = 0
fourteen = 0
fifteen = 0
sixteen = 0
seventeen = 0
eighteen = 0
nineteen = 0
twenty = 0
twentyone = 0
twentytwo = 0
twentythree = 0

time_stamps_values = ["kl: 00", "kl: 01", "kl: 02", "kl: 03", "kl: 04", "kl: 05", "kl: 06", "kl: 07", "kl: 08", "kl: 09", "kl: 10", "kl: 11", "kl: 12", "kl: 13", "kl: 14", "kl: 15", "kl: 16", "kl: 17", "kl: 18", "kl: 19", "kl: 20", "kl: 21", "kl: 22", "kl: 23",]

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

amount_message = "messages"
lenght_message = "total length"
time_stamps = "time stamps"
ratio_msglen = "ratio"

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

chat_temp = []
time_temp = []
author = []
for x in sortdict.items():
    #print(x)
    try:
        chat_temp.append(x[1][2])
        time_temp.append(x[1][1])
        #print(x)
        #author.append(x[1][3])
    except:
        chat_temp.append(0)
        time_temp.append(x[1][1])
        #author.append(0)

print(len(chat_temp), len(time_temp))


amnt_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
len_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
to0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

for i in range(0, 24):
    amnt_list[i] = 0
    len_list[i] = 0
    to0[i] = 0.0

end_time = []
end_chat = []
for x, y in zip(chat_temp, time_temp):
    #if y.startswith('00'):
    #if not int(x) > 200:
    #if not z in [368423564229083137, 689565874612469784]:
        #print(y)
        
        #if int(x) > 150:
        #   x = 150
        
        tim = (y[:-6])
        
        for i in range(0, 24):
            if int(tim) == i and int(x) > 0:
                amnt_list[i] += 1
                len_list[i] += int(x)#/19.59856#/10.4188615#/19.48600311
                
       
            
        end_time.append(y)#[3:])
        end_chat.append(x)


#plt.plot(time_temp, chat_temp)
#plt.show()
print(len(end_time), len(end_chat))

total = [0, 0]
for x, z in zip(amnt_list, len_list):
    if z != 0:
        total[1] += int(x)
        total[0] += int(z)
print(f"average message length is {total[0]/total[1]}")

for x, (y, z) in enumerate(zip(amnt_list, len_list)):
    if y != 0:
        to0[x] = z/y
        

#data = pd.DataFrame({col1:unixtime,col2:timetoday,col3:weekday,col4:messagelen,col5:channel})
data = pd.DataFrame({col2:end_time,col4:end_chat})
data.to_excel('0-30.xlsx', sheet_name='sheet1', index=False)

data = pd.DataFrame({time_stamps:time_stamps_values,amount_message:amnt_list,lenght_message:len_list,ratio_msglen:to0})
data.to_excel('fuck_it.xlsx', sheet_name='sheet1', index=False)