from graph import *
from math import *
windowSize(500,600)
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
def GRIB(x,y,nx,ny,ug):
    b=0
    c=120*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),50,0.8*nx,2*ny,ug,1,(200,200,200),"white")
    b=0
    c=0
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),50,3*nx,ny,ug,1,(200,200,200),"red")
    b=-110*nx
    c=-10*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),7,2*nx,ny,ug,1,(200,200,200),"white")
    b=-60*nx
    c=30*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),5,2*nx,ny,ug,1,(200,200,200),"white")
    b=-30*nx
    c=-20*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),5,3*nx,ny,ug,1,(200,200,200),"white")
    b=30*nx
    c=20*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),5,2*nx,1.5*ny,ug,1,(200,200,200),"white")
    b=30*nx
    c=-25*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),5,3*nx,ny,ug,1,(200,200,200),"white")
    b=110*nx
    c=-20*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),10,2*nx,ny,ug,1,(200,200,200),"white")
def IGOLKI(x,y,nx,ny,ug):
    penSize(1)
    penColor(0,0,0)
    brushColor(50,50,50)
    a=[]
    b=20*nx
    c=0
    a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    b=10*nx
    c=-100*ny
    a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    b=0
    c=0
    a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    b=-10*nx
    c=-100*ny
    a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    b=-20*nx
    c=0
    a.append((x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug)))
    polygon(a)
def YOZH(x,y,nx,ny,ug):
    b=-110*nx
    c=40*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),7,2*nx,1*ny,ug,1,(200,200,200),(100,80,80))
    b=110*nx
    c=35*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),10,1*nx,1*ny,ug,1,(200,200,200),(100,80,80))
    b=0
    c=0
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),60,2*nx,1.2*ny,ug,1,(200,200,200),(100,80,80))
    b=120*nx
    c=10*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),20,2*nx,1*ny,ug,1,(200,200,200),(100,80,80))
    b=90*nx
    c=60*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),10,2*nx,1.2*ny,ug,1,(200,200,200),(100,80,80))
    b=-90*nx
    c=60*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),10,2*nx,1.2*ny,ug,1,(200,200,200),(100,80,80))
    b=120*nx
    c=5*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),5,1*nx,1*ny,ug,1,(200,200,200),(0,0,0))
    b=135*nx
    c=0
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),5,1*nx,1*ny,ug,1,(200,200,200),(0,0,0))
    b=160*nx
    c=10*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),3,1*nx,1*ny,ug,1,(200,200,200),(0,0,0))
    for i in range(0,3):
        for k in range(0,3):
            b=(-90+80*i+10*k)*nx
            c=(30-30*k)*ny
            IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug-0.3)
            b=(-100+80*i+10*k*k)*nx
            c=(50-30*k)*ny
            IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug+0.3)
    b=-80*nx
    c=30*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug-1)
    b=-80*nx
    c=30*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug-0.3)
    b=-10*nx
    c=-110*ny
    GRIB(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),0.4*nx,0.35*ny,ug+0.5)
    b=-60*nx
    c=-40*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),25,1*nx,1*ny,ug,1,(200,200,200),(200,150,100))
    b=-80*nx
    c=-35*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),25,1*nx,1*ny,ug,1,(200,200,200),(200,150,100))
    b=60*nx
    c=-50*ny
    OVAL(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),30,1*nx,1*ny,ug,1,(200,200,200),"red")
    b=-70*nx
    c=0
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug-0.7)
    b=-30*nx
    c=-10*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug)
    b=40*nx
    c=-10*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug)
    b=-40*nx
    c=40*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug)
    b=40*nx
    c=40*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug-0.3)
    b=-40*nx
    c=50*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug-0.3)
    b=10*nx
    c=60*ny
    IGOLKI(x+b*cos(ug)-c*sin(ug),y+b*sin(ug)+c*cos(ug),nx,ny,ug)
penColor(200,200,200)
brushColor(150,130,130)
rectangle(0, 0, 500, 600)
brushColor(100,190,100)
rectangle(0, 0, 500, 350)
YOZH(470,350,0.5,0.45,0)
YOZH(180,370,0.4,0.35,0)
YOZH(330,500,0.8,0.7,0)
YOZH(-10,550,0.4,0.35,0)
penColor(200,200,200)
brushColor(250,210,0)
rectangle(0, 0, 40, 380)
rectangle(350, 0, 390, 380)
rectangle(460, 0, 490, 420)
rectangle(60, 0, 180, 580)
GRIB(240,570,0.3,0.25,0)
GRIB(300,585,0.15,0.125,0)
GRIB(340,575,0.25,0.2,0.2)
GRIB(380,595,0.15,0.125,0)
GRIB(425,560,0.3,0.25,-0.2)
GRIB(465,575,0.15,0.125,0)
GRIB(510,540,0.3,0.3,0.2)
run()
