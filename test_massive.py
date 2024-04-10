import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import random
window = Tk()
window.geometry('1000x750+300+200')
window.title('Mahjong')
can_m = Canvas(window, width = 1000, height = 800, bg = 'lightblue')
can_m.pack()
pole=[[[0 for i in range(5)]for j in range(5)] for k in range(3)]
print(pole)
sizex=80
sizey=114
x=0
y=0
img=Image.open('Resources/1111.png')
img=ImageTk.PhotoImage(img)
img1=Image.open('Resources/2222.png')
img1=ImageTk.PhotoImage(img1)
img2=Image.open('Resources/3333.png')
img2=ImageTk.PhotoImage(img2)
img3=Image.open('Resources/4444.png')
img3=ImageTk.PhotoImage(img3)
img4=Image.open('Resources/5555.png')
img4=ImageTk.PhotoImage(img4)
img5=Image.open('Resources/6666.png')
img5=ImageTk.PhotoImage(img5)
img6=Image.open('Resources/7777.png')
img6=ImageTk.PhotoImage(img6)
img7=Image.open('Resources/8888.png')
img7=ImageTk.PhotoImage(img7)
img8=Image.open('Resources/9999.png')
img8=ImageTk.PhotoImage(img8)
def draw():
    for k in range(3):
        x=k*12
        for i in range(5):
            x+=sizex
            y=k*12
            for j in range(5):
                y+=sizey
                if pole[k][i][j]==1:
                    pole[k][i][j]=num1=can_m.create_image(x,y,image=img)
                if pole[k][i][j]==2:
                    pole[k][i][j]=num2=can_m.create_image(x,y,image=img1)
                if pole[k][i][j]==3:
                    pole[k][i][j]=num3=can_m.create_image(x,y,image=img2)
                if pole[k][i][j]==4:
                    pole[k][i][j]=num4=can_m.create_image(x,y,image=img3)
                if pole[k][i][j]==5:
                    pole[k][i][j]=num5=can_m.create_image(x,y,image=img4)
                if pole[k][i][j]==6:
                    pole[k][i][j]=num6=can_m.create_image(x,y,image=img5)
                if pole[k][i][j]==7:
                    pole[k][i][j]=num7=can_m.create_image(x,y,image=img6)
                if pole[k][i][j]==8:
                    pole[k][i][j]=num8=can_m.create_image(x,y,image=img7)
                if pole[k][i][j]==9:
                    pole[k][i][j]=num9=can_m.create_image(x,y,image=img8)
##                pole[2][4][j]=0
##                pole[2][i][4]=0
##                pole[2][0][j]=0
##                pole[2][i][0]=0
                
def generator():
    for k in range(3):
        for i in range(5):
            for j in range(5):
                pole[k][i][j]=random.randint(1,9)

#===============================
generator()
draw()
