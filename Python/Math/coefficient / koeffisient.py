# programmet løser et linært likningssystem med to ukjente når ae - bd ikke er 0

a = float(input("koeffisient a: "))
b = float(input("koeffisient b: "))
c = float(input("tallet c: "))
d = float(input("koeffisient d: "))
e = float(input("koeffisient e: "))
f = float(input("tallet f "))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print(f"x = {x} og y = {y}")