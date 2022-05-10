#make fizzbuzz 
from re import X

fizz = 3
buzz = 5
fozz = 7
bozz = 11

def check(x, nr, string):
    if x % nr == 0:
        return string
    return ""

for x in range(0,1000):
    output = ""
    output += check(x, fizz, "fizz")
    output += check(x, buzz, "buzz")
    output += check(x, fozz, "fozz")
    output += check(x, bozz, "bozz")
    
    
    if output == "":
        output = x
    
    print(output)