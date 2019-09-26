import turtle
import math
def Nugolnik(n,l):
    for i in range(0,n):
        turtle.forward(l)
        turtle.left(360/n)
turtle.left(90)
for k in range(3,13):
    turtle.left(180/k)
    Nugolnik(k,2*30*(k-2)*math.sin(math.pi/k))
    turtle.penup()
    turtle.right(180/k)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()

        
