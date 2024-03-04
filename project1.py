from tkinter import *
from PIL import ImageTk,Image

top=Tk()
top.geometry('1200x700')
top.title('welcome to the basic calculator')
top.iconbitmap("C:/Users/Dheeraj/Downloads/Dtafalonso-Android-Lollipop-Calculator.512.png")

def add():
    k=int(E1.get())
    k2=int(E2.get())
    k3=k+k2
    L5.config(text=k3)

def sub():
    j=int(E1.get())
    j2=int(E2.get())
    j3=j-j2
    L5.config(text=j3)

def mul():
    l=int(E1.get())
    l2=int(E2.get())
    l3=l*l2
    L5.config(text=l3)

def div():
    m=int(E1.get())
    m2=int(E2.get())
    m3=m/m2
    L5.config(text=m3)

path="C:/Users/Dheeraj/Downloads/hand-drawn-scientific-formulas-chalkboard_23-2148496321 (1).jpg"
img2=ImageTk.PhotoImage(Image.open(path))

L2=Label(top,image=img2)
L2.pack()

L=Label (top,text='CALCULATOR',bg='gray',fg='white',font=('Elephant 30 bold'))
L.place(x=450,y=50)

L3=Label(top,text='First No',bg='yellow',fg='black',font=('Arial 20 bold'))
L3.place(x=300,y=200)

E1=Entry(top,font=('Magneto 20 bold'))
E1.place(x=550,y=200)

L4=Label(top,text='Second No',bg='yellow',fg='black',font=('Arial 20 bold'))
L4.place(x=300,y=300)

E2=Entry(top,font=('Magneto 20 bold'))
E2.place(x=550,y=300)

B1=Button(top,text='ADD',bg='teal',font=('Arial 20 bold'),command=add)
B1.place(x=250,y=400)

L5=Label(top,text='Result',bg='pink',fg='Black',font=('Jokerman 30 bold'))
L5.place(x=500,y=500)

B2=Button(top,text='SUB',bg='cyan',font=('Arial 20 bold'),command=sub)
B2.place(x=450,y=400)

B3=Button(top,text='MUL',bg='lime',font=('Arial 20 bold'),command=mul)
B3.place(x=650,y=400)

B4=Button(top,text='DIV',bg='light green',font=('Arial 20 bold'),command=div)
B4.place(x=850,y=400)


top.config(bg='grey')
top.mainloop()