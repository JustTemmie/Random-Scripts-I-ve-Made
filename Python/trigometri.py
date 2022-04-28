from pylab import *

a = float(input("kortside a cm "))
b = float(input("kortside b cm "))
c = float(input("langside c cm "))

if a <= 0 or b <= 0 or c <= 0 or a+b < c:
    print("not valid trekant no >:(")
    exit()

difference = abs(a**2+b**2-c**2)
print((a**2+b**2)/35, difference)

if (a**2+b**2)/35 > difference:
    print("trekanten er rettvinklet")
else:
    print("it ain't lmao")

