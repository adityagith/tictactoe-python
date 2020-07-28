from tkinter import *

a = 0

f = 0 #1 if anyone wins , else 2 or 3 draws player 2 wins

a11=a12=a13=a21=a22=a23=a31=a32=a33=0

#Maintain a matrix 2x2 or list 2x2

#Functions

def value():
    
    global a11,a12,a13,a21,a22,a23,a31,a32,a33

    print("{} {} {}    {} {} {}    {} {} {} ".format(a11,a12,a13,a21,a22,a23,a31,a32,a33))
    print("\n\n")

def check():
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    
    #Vertical Possibilities
    
    if(a11==a21==a31):
        if(a11==1):
            return 1
        if(a11==2):
            return 2
        if(a11==0):
            return 0
        
    if(a12==a22==a32):
        if(a12==1):
            return 1
        if(a12==2):
            return 2
        if(a12==0):
            return 0
        
    if(a13==a23==a33):
        if(a13==1):
            return 1
        if(a13==2):
            return 2
        if(a13==0):
            return 0

    #Horizontal Possibilities

    if(a11==12==a13):
        if(a11==1):
            return 1
        if(a11==2):
            return 2
        if(a11==0):
            return 0
        
    if(a21==a22==a23):
        if(a21==1):
            return 1
        if(a21==2):
            return 2
        if(a21==0):
            return 0
        
    if(a31==a32==a33):
        if(a31==1):
            return 1
        if(a31==2):
            return 2
        if(a31==0):
            return 0

    #Diagonal Possibilities

    if(a11==22==a33):
        if(a11==1):
            return 1
        if(a11==2):
            return 2
        if(a11==0):
            return 0
        
    if(a13==a22==a31):
        if(a13==1):
            return 1
        if(a13==2):
            return 2
        if(a13==0):
            return 0
    else:
        return 0

def change11():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a11=1
        button11.destroy()
        button11c = Button(frame11,text="X",bg="yellow",font="Verdana 31")
        button11c.pack(expand="True",fill="both")
        chance.set("Player 2 chance")
        chanceentry.update()
        a=1
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
    else:
        a11=2
        button11.destroy()
        button11c = Button(frame11,text="O",bg="yellow",font="Verdana 30")
        button11c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()

def change12():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a12=1
        button12.destroy()
        button12c = Button(frame12,text="X",bg="yellow",font="Verdana 31")
        button12c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
    else:
        a12=2
        button12.destroy()
        button12c = Button(frame12,text="O",bg="yellow",font="Verdana 30")
        button12c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
        

def change13():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a13=1
        button13.destroy()
        button13c = Button(frame13,text="X",bg="yellow",font="Verdana 31")
        button13c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
    else:
        a13=2
        button13.destroy()
        button13c = Button(frame13,text="O",bg="yellow",font="Verdana 30")
        button13c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()


def change21():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a21=1
        button21.destroy()
        button21c = Button(frame21,text="X",bg="yellow",font="Verdana 31")
        button21c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
    else:
        a21=2
        button21.destroy()
        button21c = Button(frame21,text="O",bg="yellow",font="Verdana 30")
        button21c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()


def change22():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a22=1
        button22.destroy()
        button22c = Button(frame22,text="X",bg="yellow",font="Verdana 31")
        button22c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
    else:
        a22=2
        button22.destroy()
        button22c = Button(frame22,text="O",bg="yellow",font="Verdana 30")
        button22c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()

def change23():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a23=1
        button23.destroy()
        button23c = Button(frame23,text="X",bg="yellow",font="Verdana 31")
        button23c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()
    else:
        a23=2
        button23.destroy()
        button23c = Button(frame23,text="O",bg="yellow",font="Verdana 30")
        button23c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
            quit()
        value()

def change31():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a31=1
        button31.destroy()
        button31c = Button(frame31,text="X",bg="yellow",font="Verdana 31")
        button31c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
            quit()
        if(b==2):
            print("Player 2 wins")
        value()
    else:
        a31=2
        button31.destroy()
        button31c = Button(frame31,text="O",bg="yellow",font="Verdana 30")
        button31c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
        if(b==2):
            print("Player 2 wins")
        value()

def change32():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a32=1
        button32.destroy()
        button32c = Button(frame32,text="X",bg="yellow",font="Verdana 31")
        button32c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
        if(b==2):
            print("Player 2 wins")
        value()
    else:
        a32=2
        button32.destroy()
        button32c = Button(frame32,text="O",bg="yellow",font="Verdana 30")
        button32c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
        if(b==2):
            print("Player 2 wins")
        value()

def change33():
    global a
    global a11,a12,a13,a21,a22,a23,a31,a32,a33
    if(a==0):
        a33=1
        button33.destroy()
        button33c = Button(frame33,text="X",bg="yellow",font="Verdana 31")
        button33c.pack(expand="True",fill="both")
        a=1
        chance.set("Player 2 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
        if(b==2):
            print("Player 2 wins")
        value()
    else:
        a33=2
        button33.destroy()
        button33c = Button(frame33,text="O",bg="yellow",font="Verdana 30")
        button33c.pack(expand="True",fill="both")
        a=0
        chance.set("Player 1 chance")
        chanceentry.update()
        value()
        b = check()
        if(b==1):
            print("Player 1 wins")
        if(b==2):
            print("Player 2 wins")
        value()

        
root = Tk()


root.title("Tic-Tac-Toe")


root.geometry("300x300")


frame1 = Frame(root,bg="yellow")
frame11 = Frame(frame1,bg="yellow")
frame12 = Frame(frame1,bg="yellow")
frame13 = Frame(frame1,bg="yellow")


button11 = Button(frame11,text=" ",bg="yellow",font="Verdana 40",command=change11)
button11.pack(expand="True",fill="both")
button12 = Button(frame12,text=" ",bg="yellow",font="Verdana 40",command=change12)
button12.pack(expand="True",fill="both")
button13 = Button(frame13,text=" ",bg="yellow",font="Verdana 40",command=change13)#border=0
button13.pack(expand="True",fill="both")


frame11.pack(expand="True",fill="both",side=LEFT)
frame12.pack(expand="True",fill="both",side=LEFT)
frame13.pack(expand="True",fill="both",side=LEFT)



frame2 = Frame(root)
frame21 = Frame(frame2)
frame22 = Frame(frame2)
frame23 = Frame(frame2)
frame21.pack(expand="True",fill="both",side=LEFT)
frame22.pack(expand="True",fill="both",side=LEFT)
frame23.pack(expand="True",fill="both",side=LEFT)


button21 = Button(frame21,text=" ",bg="yellow",font="Verdana 40",command=change21)
button21.pack(expand="True",fill="both")
button22 = Button(frame22,text=" ",bg="yellow",font="Verdana 40",command=change22)
button22.pack(expand="True",fill="both")
button23 = Button(frame23,text=" ",bg="yellow",font="Verdana 40",command=change23)
button23.pack(expand="True",fill="both")


frame3 = Frame(root)
frame31 = Frame(frame3)
frame32 = Frame(frame3)
frame33 = Frame(frame3)
frame31.pack(expand="True",fill="both",side=LEFT)
frame32.pack(expand="True",fill="both",side=LEFT)
frame33.pack(expand="True",fill="both",side=LEFT)


button31 = Button(frame31,text=" ",bg="yellow",font="Verdana 40",command=change31)
button31.pack(expand="True",fill="both")
button32 = Button(frame32,text=" ",bg="yellow",font="Verdana 40",command=change32)
button32.pack(expand="True",fill="both")
button33 = Button(frame33,text=" ",bg="yellow",font="Verdana 40",command=change33)
button33.pack(expand="True",fill="both")

frame4 = Frame(root)
frame5 = Frame(root)

chance = StringVar()

chanceentry = Entry(frame4,textvariable=chance,width=20,bg="Gray")

chanceentry.pack()

#Label needed to be created in frame 4 and frame5

frame1.pack(expand="True",fill="both",side=TOP)
frame2.pack(expand="True",fill="both",side=TOP)
frame3.pack(expand="True",fill="both",side=TOP)
frame4.pack(expand="True",fill="both",side=TOP)
frame5.pack(expand="True",fill="both",side=TOP)


root.mainloop() 
