# Python program to demonstrate
# tangent circle drawing


from turtle import *
	
t = Turtle()
t.speed(10000)

while True:
    #t.clear()
    # radius for smallest circle
    r = 5

    # loop for printing tangent circles
    for i in range(1, 200 + 1, 1):
        t.left(90)
        t.circle(r + r*i)
        t.right(90)
        #t.clear()
        t.penup()
        t.forward(3)
        t.pendown()

        
