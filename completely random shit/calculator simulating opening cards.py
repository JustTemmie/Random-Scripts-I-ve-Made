import random

def calc_average(price):
    x = 53
    spent = price
    while x > 0:
        spent += price
        if random.random() <= x/53:
            x -= 1
        
    return spent

list = []
total_spent = 0
succesful = 0
for y in range(0,100):
    list.append(calc_average(400))

for thing in list:
    if thing < 2400:
        succesful += 1
    total_spent += thing

print(total_spent/100)
print(succesful/100*100)