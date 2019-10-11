from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
e = Entry(root, width=20)
canv = Canvas(root,bg='white',height=550)
B=Button(root,text="SAVE" )
BF=Button(root,text="SAVE IN FILE" )
E=Entry(root,width = 30)
TEXT = Label(root, bg='black', fg='white', width=20, text="OCHKI 0")
canv.pack(fill=BOTH,expand=0)
colors = ['red','orange','yellow','green','blue']
def SOHRANENIE(event):
    global o,file
    n=E.get()+" "+str(o)+"\n"
    file = open("names.txt","a",newline="\n")
    file.write(n)
    o=0
    TEXT['text']="OCHKI "+str(o)

def FILE(event):
    global file
    file.close()
def SHAR1():
    global x,y,r,v,c1
    if((v[0][0]==0) and (v[0][1]==0)):
        v[0]=[rnd(-4,4),rnd(-4,4)]
    if(x[0]<=r[0]):
        x[0]=r[0]+1
        v[0]=[rnd(1,4),rnd(-4,4)]
    elif(x[0]>=800-r[0]):
        x[0]=799-r[0]
        v[0]=[rnd(-4,-1),rnd(-4,4)]
    elif(y[0]<=r[0]):
        y[0]=r[0]+1
        v[0]=[rnd(-4,4),rnd(1,4)]
    elif(y[0]>=550-r[0]):
        y[0]=549-r[0]
        v[0]=[rnd(-4,4),rnd(-4,-1)]
    x[0] = x[0]+v[0][0]
    y[0] = y[0]+v[0][1]
    canv.create_oval(x[0]-r[0],y[0]-r[0],x[0]+r[0],y[0]+r[0],fill = c1, width=0)

def CLICK(event):
    global o,c1,c2,c3,c4,r,x,y
    if(((event.x-x[0])**2+(event.y-y[0])**2)<=r[0]**2):
        o=o+1
        TEXT['text']="OCHKI "+str(o)
        c1=choice(colors)
        r[0]=rnd(10,100)
        x[0]=rnd(10,700)
        y[0]=rnd(10,500)
    elif(((event.x-x[1])**2+(event.y-y[1])**2)<=r[1]**2):
        o=o+1
        TEXT['text']="OCHKI "+str(o)
        c2=choice(colors)
        r[1]=rnd(10,100)
        x[1]=rnd(10,700)
        y[1]=rnd(10,500)
    elif(((event.x-x[2])**2+(event.y-y[2])**2)<=r[2]**2):
        o=o+10
        TEXT['text']="OCHKI "+str(o)
        c3=choice(colors)
        x[2]=rnd(10,700)
        y[2]=rnd(10,500)
    elif(((event.x-x[3])**2+(event.y-y[3])**2)<=r[3]**2):
        o=o+10
        TEXT['text']="OCHKI "+str(o)
        c4=choice(colors)
        x[3]=rnd(10,700)
        y[3]=rnd(10,500)

def SHAR2():
    global x,y,r,v,c2
    if((v[1][0]==0) and (v[1][1]==0)):
        v[1]=[rnd(-4,4),rnd(-4,4)]
    if(x[1]<=r[1]):
        x[1]=r[1]+1
        v[1]=[rnd(1,4),rnd(-4,4)]
    elif(x[1]>=800-r[1]):
        x[1]=799-r[1]
        v[1]=[rnd(-4,-1),rnd(-4,4)]
    elif(y[1]<=r[1]):
        y[1]=r[1]+1
        v[1]=[rnd(-4,4),rnd(1,4)]
    elif(y[1]>=550-r[1]):
        y[1]=549-r[1]
        v[1]=[rnd(-4,4),rnd(-4,-1)]
    x[1] = x[1]+v[1][0]
    y[1] = y[1]+v[1][1]
    canv.create_oval(x[1]-r[1],y[1]-r[1],x[1]+r[1],y[1]+r[1],fill = c2, width=0)
def KVADRAT1():
    global x,y,r,v,c3
    if((v[2][0]==0) and (v[2][1]==0)):
        v[2]=[rnd(-8,8),rnd(-8,8)]
    if(x[2]<=r[2]):
        x[2]=r[2]+1
        v[2]=[rnd(1,8),rnd(-8,8)]
    elif(x[2]>=800-r[2]):
        x[2]=799-r[2]
        v[2]=[rnd(-8,-1),rnd(-8,8)]
    elif(y[2]<=r[2]):
        y[2]=r[2]+1
        v[2]=[rnd(-8,8),rnd(1,8)]
    elif(y[2]>=550-r[2]):
        y[2]=549-r[2]
        v[2]=[rnd(-8,8),rnd(-8,-1)]
      
    x[2] = x[2]+v[2][0]
    y[2] = y[2]+v[2][1]
    canv.create_polygon(x[2]-r[2],y[2]-r[2],x[2]-r[2],y[2]+r[2],x[2]+r[2],y[2]+r[2],x[2]+r[2],y[2]-r[2],fill = c3,outline ='black')
    
def KVADRAT2():
    global x,y,r,v,c4
    if((v[3][0]==0) and (v[3][1]==0)):
        v[3]=[rnd(-8,8),rnd(-8,8)]
    if(x[3]<=r[3]):
        x[3]=r[3]+1
        v[3]=[rnd(1,8),rnd(-8,8)]
    elif(x[3]>=800-r[3]):
        x[3]=799-r[3]
        v[3]=[rnd(-8,-1),rnd(-8,8)]
    elif(y[3]<=r[3]):
        y[3]=r[3]+1
        v[3]=[rnd(-8,8),rnd(1,8)]
    elif(y[3]>=550-r[3]):
        y[3]=549-r[3]
        v[3]=[rnd(-8,8),rnd(-8,-1)]
      
    x[3] = x[3]+v[3][0]
    y[3] = y[3]+v[3][1]
    canv.create_polygon(x[3]-r[3],y[3]-r[3],x[3]-r[3],y[3]+r[3],x[3]+r[3],y[3]+r[3],x[3]+r[3],y[3]-r[3],fill = c4,outline ='black')
 
def RISUNOK():
    global x,y,r,v,c1,c2,c3,c4
    canv.delete(ALL)
    SHAR1()
    SHAR2()
    KVADRAT1()
    KVADRAT2()
    root.after(5,RISUNOK)


o=0
v=[[0,0],[0,0],[0,0],[0,0]]
x=[300,500,200,0]
y=[300,500,500,0]
r=[50,100,10,10]
c1=choice(colors)
c2=choice(colors)
c3=choice(colors)
c4=choice(colors)
RISUNOK()
canv.bind('<Button-1>', CLICK)
B.bind('<Button-1>', SOHRANENIE)
BF.bind('<Button-1>', FILE)
B.place(x=10,y=570)
BF.place(x=600,y=570)
E.place(x=100,y=570)
TEXT.place(x=400,y=570)
mainloop()
