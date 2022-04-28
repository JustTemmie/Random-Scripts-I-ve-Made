t = float(input("topp "))
n = float(input("nevner "))

if n == 0:
    print(f"{n} er ikke ett gylding tall for en nevner")
    exit()
    
if n < 0:
    n = n * -1
    t = t * -1
    
print(f"{t}/{n} = {t/n}")
print(f"{t}/{n}")
