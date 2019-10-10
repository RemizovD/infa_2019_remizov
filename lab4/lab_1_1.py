from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

e = Entry(root, width=20)
canv = Canvas(root,bg='white')
TEXT = Label(root, bg='black', fg='white', width=20, text="OCHKI 0")
canv.pack(fill=BOTH,expand=1)
TEXT.pack()

colors = ['red','orange','yellow','green','blue']

def SHAR1():
    global x1,y1,r1,v1,c1
    if((v1[0]==0) and (v1[1]==0)):
        v1=[rnd(-4,4),rnd(-4,4)]
    if(x1<=r1):
        x1=r1+1
        v1=[rnd(1,4),rnd(-4,4)]
    elif(x1>=800-r1):
        x1=799-r1
        v1=[rnd(-4,-1),rnd(-4,4)]
    elif(y1<=r1):
        y1=r1+1
        v1=[rnd(-4,4),rnd(1,4)]
    elif(y1>=600-r1):
        y1=599-r1
        v1=[rnd(-4,4),rnd(-4,-1)]
    x1 = x1+v1[0]
    y1 = y1+v1[1]
    canv.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill = c1, width=0)

def CLICK(event):
    global o
    if(((event.x-x1)**2+(event.y-y1)**2)<=r1**2):
        o=o+1
        TEXT['text']="OCHKI "+str(o)
    elif(((event.x-x2)**2+(event.y-y2)**2)<=r2**2):
        o=o+1
        TEXT['text']="OCHKI "+str(o)

def SHAR2():
    global x2,y2,r2,v2,c2
    if((v2[0]==0) and (v2[1]==0)):
        v2=[rnd(-4,4),rnd(-4,4)]
    if(x2<=r2):
        x2=r2+1
        v2=[rnd(1,4),rnd(-4,4)]
    elif(x2>=800-r2):
        x2=799-r2
        v2=[rnd(-4,-1),rnd(-4,4)]
    elif(y2<=r2):
        y2=r2+1
        v2=[rnd(-4,4),rnd(1,4)]
    elif(y2>=600-r2):
        y2=599-r2
        v2=[rnd(-4,4),rnd(-4,-1)]
    x2 = x2+v2[0]
    y2 = y2+v2[1]
    canv.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill = c2, width=0)

def RISUNOK():
    global x1,x2,y1,y2,v1,v2,c1,c2
    canv.delete(ALL)
    SHAR1()
    SHAR2()
    root.after(5,RISUNOK)

o=0
v1=[0,0]
x1=300
y1=300
r1=50
c1=choice(colors)
v2=[0,0]
x2=500
y2=500
r2=100
c2=choice(colors)
RISUNOK()
canv.bind('<Button-1>', CLICK)
mainloop()
