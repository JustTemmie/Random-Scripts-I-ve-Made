# sqrt(200) = sqrt(10² * 2) = 10*sqrt(2)

x = input("x: ")

def check_valid():
    if x > 0:
        print("x cannot be smaller than 0")
        return False
    elif x == 0:
        print("x cannot be equal to 0")
        return False
    

if check_valid():
    a = 