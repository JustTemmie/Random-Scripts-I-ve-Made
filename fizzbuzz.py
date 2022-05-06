#make fizzbuzz 
from re import X


fizz = 3
buzz = 5
for x in range(0,1000):
    output = ""
    if x % fizz == 0:
        output += "fizz"
    if x % buzz == 0:
        output += "buzz"
    
    if x % fizz != 0 and x % buzz != 0:
        output = x
    
    print(output)