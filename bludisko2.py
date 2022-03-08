import time
import tkinter
c=60
d=70
canvas=tkinter.Canvas(height=c*15,width=d*20, bg="limegreen")
canvas.pack()


diamant = tkinter.PhotoImage(file = './emerald2.png')
stena = tkinter.PhotoImage(file = './stena2.png')
zavrete = tkinter.PhotoImage(file = './dvere2.png')
ohen = tkinter.PhotoImage(file = './ohen2.png')
mario = tkinter.PhotoImage(file = './steve2.png')
otvorene = tkinter.PhotoImage(file = './dvere.png')
win = tkinter.PhotoImage(file = './win2.png')
nie = tkinter.PhotoImage(file = './nic2.png')
stena2 = tkinter.PhotoImage(file = './stena3.png')

mario_x=0
mario_y=0

dvere_x=0
dvere_y=0

mario_img=()


pole=[ [ 6, 0, 3, 0, 1, 3, 1, 3, 0, 1, 3, 0, 0, 0, 0, 0, 4, 0, 1, 4],
       [ 0, 0, 3, 3, 0, 3, 0, 3, 0, 0, 3, 1, 0, 3, 0, 3, 4, 0, 3, 4],
       [ 0, 0, 0, 0, 0, 3, 0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 0, 0, 0, 0],                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
       [ 0, 0, 3, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 4, 4],
       [ 0, 0, 3, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 4, 9, 4],
       [ 0, 0, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [ 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 4, 0, 0],
       [ 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [ 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0],
       [ 0, 3, 0, 0, 4, 8, 4, 4, 0, 0, 0, 0, 4, 4, 4, 0, 0, 0, 3, 0],
       [ 1, 3, 0, 3, 4, 0, 0, 4, 0, 0, 0, 0, 4, 1, 4, 0, 3, 0, 3, 4],
       [ 1, 3, 0, 0, 4, 1, 1, 4, 0, 0, 0, 0, 4, 0, 4, 0, 3, 0, 1, 1],
       [ 2, 3, 3, 0, 4, 1, 1, 4, 0, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3],
       [ 4, 3, 1, 0, 4, 4, 4, 4, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5] ]

pohyb= [ [0]*20 for k in range(15) ]


def plan():
    global d, c, diamant, stena, zavrete, ohen, mario, dvere_x, dvere_y, mario_x, mario_y, mario_img, pohyb, pole
    
    mario_x=mario_y=dvere_x=dvere_y=x=y=0
    
    for n in range(0,15):
        for i in range(0,20):
            pohyb[n][i]=pole[n][i]
            
    for n in range(0,15):
        for i in range(0,20):
            x=0+i*d
            y=0+n*c
            
            if pole[n][i]==1:
                img=canvas.create_image(x,y,anchor="nw", image=diamant, tag="D"+str(n)+str(i))
                canvas.tag_lower(img)
                
            if pole[n][i]==3:
                img=canvas.create_image(x,y,anchor="nw", image=stena)
                canvas.tag_lower(img)
                
            if pole[n][i]==5:
                img=canvas.create_image(x,y,anchor="nw", image=zavrete, tag="zavrete")
                canvas.tag_lower(img)
                dvere_x=x
                dvere_y=y
                
            if pole[n][i]==4:
                img=canvas.create_image(x,y,anchor="nw", image=ohen)
                canvas.tag_lower(img)

            if pole[n][i]==8:
                img=canvas.create_image(x,y,anchor="nw", image=nie)
                canvas.tag_lower(img)

            if pole[n][i]==2:
                img=canvas.create_image(x,y,anchor="nw", image=stena2)
                canvas.tag_lower(img)
                
            if pole[n][i]==6:
                mario_img=canvas.create_image(x,y,anchor="nw", image=mario, tag="mario")
                canvas.tag_raise(mario_img)
                mario_x=n
                mario_y=i


def left(event):
    global d, mario_img, mario_x, mario_y, pohyb
    
    x = -d
    y = 0
    
    if mario_y-1>=0 and pohyb[mario_x][mario_y-1] in (0,1,4,5,6,8,2):
        pohyb[mario_x][mario_y-1]=0
        vymaz("D"+str(mario_x)+str(mario_y))
        mario_y= mario_y-1
        canvas.move(mario_img, x, y)
        vyhodnotenie()

def right(event):
    global d, mario_img, mario_x, mario_y, pohyb
    
    x = d
    y = 0
    
    if mario_y+1<20 and pohyb[mario_x][mario_y+1] in (0,1,4,5,6,8,2):
        pohyb[mario_x][mario_y+1]=0
        vymaz("D"+str(mario_x)+str(mario_y))
        mario_y= mario_y+1
        canvas.move(mario_img, x, y)
        vyhodnotenie()

def up(event):
    global c, mario_img, mario_x, mario_y, pohyb
    
    x = 0
    y = -c
    
    if mario_x-1>=0 and pohyb[mario_x-1][mario_y] in (0,1,4,5,6,8,2):
        pohyb[mario_x-1][mario_y]=0
        vymaz("D"+str(mario_x)+str(mario_y))
        mario_x= mario_x-1
        canvas.move(mario_img, x, y)
        vyhodnotenie()

def down(event):
    global c, mario_img, mario_x, mario_y, pohyb
    
    x = 0
    y = c
    
    if mario_x+1<15 and pohyb[mario_x+1][mario_y] in (0,1,4,5,6,8,2):
        pohyb[mario_x+1][mario_y]=0
        vymaz("D"+str(mario_x)+str(mario_y))
        mario_x= mario_x+1
        canvas.move(mario_img, x, y)
        vyhodnotenie()

def vymaz(nazov):
    if len(canvas.find_withtag(nazov)) != 0:
        canvas.delete("D"+str(mario_x)+str(mario_y))
 
def vyhodnotenie():
    global win, dvere_x, dvere_y, mario_x, mario_y, pole

    if pole[mario_x][mario_y] in (4,):
            reset()
    if pole[mario_x][mario_y] in (8,):
            canvas.create_text(400,700,text="Skús znova:D", fill="green", font=('Helvetica 30 bold'))
            canvas.after(1000,reset)
            

    if ( not any( 1 in sublist for sublist in pohyb) ):
        if canvas.find_withtag("zavrete"):
            canvas.delete("zavrete")
            
        if not canvas.find_withtag("otvorene"):
            img=canvas.create_image(dvere_x, dvere_y ,anchor="nw", image=otvorene, tag="otvorene")
            canvas.tag_lower(img)
            
        if canvas.coords("mario") == canvas.coords("otvorene"):
            canvas.delete("all")
            canvas.create_image(400, 300 ,anchor="nw", image=win)

def reset():
    canvas.delete("all")
    plan()


time = 10
def tick():
    canvas.delete("cas")
    global time
    time -= 1
    cas=canvas.create_text(400, 400, text=time, font="arial 30",fill='red',tag='cas')
    if time == 0:
        canvas.delete("cas")
        canvas.create_text(400, 400, text="skap", font="arial 60",fill='red',tag='cas')
    else:
        canvas.after(1000, tick)

canvas.after(1, tick)
canvas.bind_all("<Left>", left)
canvas.bind_all("<Right>", right)
canvas.bind_all("<Up>", up)
canvas.bind_all("<Down>", down)
plan()
canvas.mainloop()
