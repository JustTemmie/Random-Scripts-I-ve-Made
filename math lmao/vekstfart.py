from pylab import *

def f(x):
    return 4*x**2+1

delx = 5.0
grensa = 0.0001

inputx = float(input("x value = "))
    
while delx > grensa:
    vekstfart = (f(inputx+delx)-f(inputx)) / (delx)
    print(f"delta er {delx} og stigningstallet er {vekstfart}")
    delx /= 2
        
    
