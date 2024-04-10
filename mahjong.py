import tkinter
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.messagebox import *
import random

window = Tk()
window.geometry('1000x750')
window.title('Mahjong')
can_m = Canvas(window, width = 1000, height = 800, bg = 'lightblue')
can_m.pack()
head = tkinter.PhotoImage(file ='Resources/head.png')
background= tkinter.PhotoImage(file='Resources/background.png')
image_m = can_m.create_image(500,400, image = head)
game_w = Toplevel(window)
name_w = Toplevel(window)
name_w.geometry('250x200')
name_w.withdraw()
playername='hhh'
name_bg = tkinter.PhotoImage(file ='Resources/name.png')
can_n = Canvas(name_w, width = 500, height = 400, bg = 'green')
can_n.place(x = 0, y = 0)
#game_w.overrideredirect(1)
game_w.geometry('1000x750')
#game_w.lift()
#game_w.attributes('-topmost',True)
#game_w.after_idle(game_w.attributes,'-topmost',True)
game_w.withdraw()
records=['nope' for i in range(10)]
can_g = Canvas(game_w, width = 1000, height = 750)
can_g.place(relx=0,rely=0)
isEnabled=[[[True for i in range(5)]for j in range(6)] for k in range(3)]
pole=[[[0 for i in range(5)]for j in range(6)] for k in range(3)]
sizex=80
sizey=114
x=400
tim=0
y=10
img=Image.open('Resources/1111.png')
img=ImageTk.PhotoImage(img)
img1=Image.open('Resources/2222.png')
img1=ImageTk.PhotoImage(img1)
img2=Image.open('Resources/3333.png')
enabledi=-1
enavledj=-1
enabledk=-1
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
winwin=0
#for the high score table
def record():
    window.withdraw()
    name_w.deiconify()
    image_n = can_n.create_image(125,100, image = name_bg)
    t = Label(name_w, text='Введите свой никнейм!', bg='darkred',fg = 'white')
    t.place(x=65, y = 20)
    buttonGO=Button(name_w,text='Играть',command=game)
    buttonGO.place(x=107,y=100)
    
def draw():
    image_b=can_g.create_image(500,370, image=background)
    for k in range(3):
        x=k*12+42+250
        for i in range(6):
            y=k*12+58+20
            for j in range(5):
                if pole[k][i][j]==1:
                    can_g.create_image(x,y,image=img)
                if pole[k][i][j]==2:
                    can_g.create_image(x,y,image=img1)
                if pole[k][i][j]==3:
                    can_g.create_image(x,y,image=img2)
                if pole[k][i][j]==4:
                    can_g.create_image(x,y,image=img3)
                if pole[k][i][j]==5:
                    can_g.create_image(x,y,image=img4)
                if pole[k][i][j]==6:
                    can_g.create_image(x,y,image=img5)
                if pole[k][i][j]==7:
                    can_g.create_image(x,y,image=img6)
                if pole[k][i][j]==8:
                    can_g.create_image(x,y,image=img7)
                if pole[k][i][j]==9:
                    can_g.create_image(x,y,image=img8)
                y+=sizey
            x+=sizex
        if enabledi>-1 and enabledk==k:
            x1=enabledk*12+42+250+sizex*enabledi
            y1=enabledk*12+58+20+sizey*enabledj
            can_g.create_rectangle(x1-40,y1-57,x1+40,y1+57,width=4,outline='red')
            

def generator():
    global pole
    for k in range(3):
        for i in range(6):
            for j in range(5):
                pole[k][i][j]=0
    for t in range(5):
        for u in range(9):
            for s in range(2):
                i=random.randint(0,5)
                j=random.randint(0,4)
                k=0
                while pole[k][i][j]>0:
                    i=random.randint(0,5)
                    j=random.randint(0,4)
                    k=0
                    while pole[k][i][j]>0:
                        k+=1
                        if k==2:
                            break
                pole[k][i][j]=u+1
    for k in range(2):
        for i in range(6):
            for j in range(5):
                if pole[k+1][i][j]>0:
                    isEnabled[k][i][j]=False
                
                
def left(event):
    global enabledi,enabledj,enabledk,pole, winwin
    x=event.x
    y=event.y
    for k in range(3):
        for i in range(6):
            for j in range(5):
                if isEnabled[k][i][j] and pole[k][i][j]>0:
                    go=False
                    if i==0 or i==5:
                        go=True
                    else:
                        if pole[k][i-1][j]==0 or pole[k][i+1][j]==0:
                            go=True;
                    if go:
                        if i*sizex+k*12+250<x<i*sizex+k*12+250+sizex and j*sizey+k*12+20<y<j*sizey+sizey+k*12+20:
                            print(k,'|',i,'|', j)
                            if enabledi==-1:
                                enabledj=j
                                enabledi=i
                                enabledk=k
                                print('enable!',pole[enabledk][enabledi][enabledj])
                            else:
                                if pole[k][i][j]==pole[enabledk][enabledi][enabledj] and (i!=enabledi or j!=enabledj):
                                   pole[k][i][j]=0
                                   pole[enabledk][enabledi][enabledj]=0
                                   winwin+=1
                                   print(winwin)
                                   if enabledk>0:
                                       isEnabled[enabledk-1][enabledi][enabledj]=True
                                   if k>0:
                                       isEnabled[k-1][i][j]=True
                                   print('delete!')
                                enabledi=-1
                    
    draw()
    win()
can_g.bind('<Button-1>', left)

def win():
    global winwin, tim
    if winwin==45:
        print("win")
        saveFile()
        answer=askyesno(title="Победа!", message="Победа! Хотите выйти?")
        if answer==True:
            game_exit()  
        if answer==False:
            back_to()
#---game-window-
def game():
    global playername, tim
    tim=0
    getFile()
    name_w.withdraw()
    window.withdraw()
    playername=table_name.get()
    game_w.deiconify()
    Back = Button(game_w, text='back to menu', font=('TimesNewRoman',10), command=back_to)
    Back.place(x=0,y=0)
    generator()
    draw()
    

#---back-to-manu
def back_to():
    window.deiconify()
    game_w.withdraw()

    
#----exit-------
def game_exit():
    window.destroy()
    
#-----help------
def help_m():
    wind_h=Toplevel(window)
    wind_h.title=('Help')
    wind_h.geometry('450x200+300+200')
    text=Text(wind_h, width=50, height=15, font=('TimesNewRoman', 12),wrap=WORD)
    text.place(x=0, y=10)
    help1=open('Resources/help.txt')
    s=help1.read()
    text.insert(END,s)
    help1.close()

def table():
    wind_t = Toplevel(window)
    wind_t.title('Table')
    wind_t.geometry('190x200')
    tex=Text(wind_t, width=50, height=15, font=('TimesNewRoman', 12),wrap=WORD)
    tex.place(x=0, y=0)
    tab=open('Resources/record.txt')
    tt=tab.read()
    tex.insert(END,tt)
    tab.close()


def getFile():
    global records
    f=open('Resources/record.txt', 'r')
    records=f.readlines()
    f.close()
    for i in range(10):
        records[i]=records[i][0:-1]
        print(records[i])

def saveFile():
    global records,tim, playername
    getFile()
    timtim=tim
    for i in range(10):
        if i%2>0:
            if int(records[i])>tim:
                t=str(tim)
                tim=int(records[i])
                records[i]=t+'\n'
                na=records[i-1]
                records[i-1]=playername+'\n'
                playername=na
            else:
                records[i-1]=records[i-1]+'\n'
                records[i]=records[i]+'\n'
    f=open('Resources/record.txt', 'w')
    tim=timtim
    f.writelines(records)
    f.close()
                
    
#---menu--------
m_menu=Menu(window)
window.config(menu=m_menu)
f_menu=Menu(m_menu, tearoff=0)
f_menu.add_command(label="Help", command=help_m)
f_menu.add_command(label = 'Exit', command=game_exit)
m_menu.add_cascade(label="Mahjong", menu=f_menu)

def update_clock():
    global tim
    Clock= Button(game_w, text=tim, width=2, height = 1, font = ("TimesNewRoman", 10))
    Clock.place(x=978, y=0)
    tim=tim+1
    game_w.after(1000,update_clock)

#----button------
name = Button(window, text='Mahjong', width = 20, height = 2, font = ("TimesNewRoman", 20), command=record)
name.place(x=322, y=100)
Help = Button(window, text='Help', width = 15, height = 1, font = ("TimesNewRoman", 20),command=help_m)
Help.place(x=365, y=210)
Exit = Button(window, text='Exit', width = 15, height = 1, font = ("TimesNewRoman", 20), command = game_exit)
Exit.place(x=365, y=370)
table_b= Button(window,text = 'Records', width = 15, height = 1, font = ("TimesNewRoman", 20), command = table) 
table_b.place(x=365, y=290)
table_name = Entry(name_w, bg='darkred', fg='white', width=21)
table_name.place( x = 65, y = 50 )

#--вызов-функций-

game_w.after(1000,update_clock)
window.mainloop()
