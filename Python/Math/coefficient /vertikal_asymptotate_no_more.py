import math

from numpy import inner

#tx = input("1 ")
#bx = input("2 ")
tx = 8
t = 4

bx = 2
b = 6
# -4     -6

for a in range(1000000000000000, 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999,10000000000):
    print(f"{float(((tx*a)-t)/((bx*a)-b))}   {a}    {tx}-{t}/{bx}-{b}")