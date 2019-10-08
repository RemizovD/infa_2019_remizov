from graph import*
from math import*
from tkinter import *
import math
width=1000
height=600
windowSize(width,height)
def OVAL(x,y,r,nx,ny,ug,t,c1,c2): 
    a=[]
    penSize(t)
    penColor(c1)
    brushColor(c2)
    for i in range (0,1*r+1):
        b=i*nx
        c=((abs(r*r-i*i))**0.5)*ny
        a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    for i in range (1*r,-1,-1):
        b=i*nx
        c=-1*((abs(r*r-i*i))**0.5)*ny
        a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    for i in range (0,1*r+1):
        b=-1*i*nx
        c=-1*((abs(r*r-i*i))**0.5)*ny
        a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    for i in range (1*r,-1,-1):
        b=-1*i*nx
        c=((abs(r*r-i*i))**0.5)*ny
        a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    polygon(a)
    
def ZONT(size,x_center,y_center, size_width):
    penSize(1*size)
    """Рисует шляпку зонтика"""
    brushColor(244,81,81)
    penColor(244,81,81)
    polygon([(x_center-size_width*40*size,y_center),(x_center,y_center-40*size),(x_center+size_width*40*size,y_center),(x_center-size_width*40*size,y_center)])
    """Рисует линии на шляпке зонтика"""
    brushColor(181,60,60)
    penColor(181,60,60)
    line(x_center,y_center-40*size,x_center+10*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center+20*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center+30*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center-10*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center-20*size_width*size,y_center)
    line(x_center,y_center-40*size,x_center-30*size_width*size,y_center)
    """Рисует ножку зонтика"""
    penSize(0.1*size)
    brushColor(244,81,81)
    penColor(181,60,60)
    rectangle(x_center-2*size_width*size,y_center-40*size,x_center+2*size_width*size,y_center)
    penSize(6*size)
    brushColor(227,130,25)
    penColor(227,130,25)
    line(x_center , y_center , x_center , y_center+120*size)

def SOLNCE(r_max,r_min,x_center,y_center,n):
    a=[]
    for i in range (0,n):
        x=x_center+math.cos(2*math.pi*i/n)*r_max
        y=y_center+math.sin(2*math.pi*i/n)*r_max
        a.append((x , y))
        x=x_center+math.cos(2*math.pi*i/n+math.pi/n)*r_min
        y=y_center+math.sin(2*math.pi*i/n+math.pi/n)*r_min
        a.append((x , y))
    brushColor('yellow')
    penColor('yellow')
    penSize(1)
    polygon(a)

def VOLNA(width,height,n,k,screen_height):
    a=[]
    for i in range (0,width):
        x=i
        y=height+k*math.sin(0.02*math.pi*i*n)
        a.append((x , y))
    a.append((width, screen_height-1))
    a.append((0, screen_height-1))
    brushColor('yellow')
    penColor('yellow')
    penSize(1)
    polygon(a)
def OBLAKO (x,y,nx,ny,ug):
    brushColor('white')
    penColor('black')
    penSize(1)
    OVAL(x,y,50,nx,ny,ug,1,"black","white")
def LODKA(x,y,nx,ny):
    """Рисует четверть окружности лодки"""
    brushColor(186,80,5)
    penColor('black')
    penSize(1)
    a=[]
    for i in range (20,-1,-1):
        b=-1*i*nx
        c=((abs(400-i*i))**0.5)*ny
        a.append((x-75*nx+b,y-10*ny+c))
    a.append((x-75*nx,y-10*ny))
    polygon(a)
    """Рисует прямоугольник лодки"""
    brushColor(186,80,5)
    penSize(1)
    penColor('black')
    rectangle(x-75*nx,y-10*ny,x+105*nx,y+10*ny)
    """Рисует треугольник лодки"""
    penColor('black')
    polygon([(x+105*nx,y-10*ny),(x+155*nx,y-10*ny),(x+105*nx,y+10*ny),(x+105*nx,y-10*ny)])
    """Рисует окружность на лодке"""
    brushColor('white')
    penColor('black')
    penSize(3)
    circle(x+115*nx,y-2*ny,5*ny)
    """Рисует мачту"""
    brushColor('black')
    penColor('black')
    penSize(4)
    line(x-35*nx,y-10*ny,x-35*nx,y-110*ny)
    """Рисует парус"""
    brushColor(222,213,153)
    penColor('black')
    penSize(1)
    polygon([(x-35*nx,y-110*ny),(x+25*nx,y-60*ny),(x-15*nx,y-60*ny),(x-35*nx,y-110*ny)])
    polygon([(x-35*nx,y-10*ny),(x+25*nx,y-60*ny),(x-15*nx,y-60*ny),(x-35*nx,y-10*ny)])

def RISUNOK():
    global dx1
    global dx2
    global q1
    global q2
    global q3
    global l
    canvas().delete(ALL)
    SOLNCE(80,65,width*0.9,height*0.15,50)
    """Рисует темно-синий прямоугольник"""
    brushColor(68,35,223)
    penSize(400)
    penColor(68,35,223)
    line(0,250,1000,250)
    """Рисует светло-синий прямоугольник"""
    brushColor(161,245,255)
    penSize(420)
    penColor(161,245,255)
    line(0,0,1000,0)
    OBLAKO(100,100,l*2,0.5,0)
    OBLAKO(300,150,l*3,0.5,0)
    OBLAKO(600,50,l*0.5,0.25,0)
    OBLAKO(800,120,l*1,0.5,0)
    LODKA(dx2,230,q2,1)
    LODKA(dx1,290,2*q1,2)
    VOLNA(width,height*0.6,0.6,15,height)
    ZONT(2,width*0.2,height*0.5,1.5)
    ZONT(1,width*0.4,height*0.6,1)
    if(q1==1):
        dx1=dx1+10
        if(dx1>=700):
            q1=-1
    else:
        dx1=dx1-10
        if(dx1<=300):
            q1=1
            
    if(q2==1):
        dx2=dx2+20
        if(dx2>=850):
            q2=-1
    else:
        dx2=dx2-20
        if(dx2<=150):
            q2=1
    if(q3==1):
        l=l+0.01
        if(l>=1):
            q3=-1
    else:
        l=l-0.01
        if(l<=0.3):
            q3=1
l=1
q3=1
q1=1        
dx1=600
q2=-1        
dx2=350
onTimer(RISUNOK, 1)
run()
