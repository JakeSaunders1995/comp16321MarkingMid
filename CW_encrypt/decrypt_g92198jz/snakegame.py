import tkinter
import tkinter as tk
import PIL
import PIL.Image
from PIL import *
from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from tkinter import Tk,PhotoImage, Button, messagebox
import random
#About Food
def placeFood():  # to place the food at the start stage
    global food, foodX, foodY
    food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue" )
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)
def moveFood(): #move the food after it is eaten
    global food, foodX, foodY
    canvas.move(food, (foodX * (-1)), (foodY * (-1)))
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)
#About Key Entered
def leftKey(event):
    global direction
    direction = "left"
def rightKey(event):
    global direction
    direction = "right"
def upKey(event):
    global direction
    direction = "up"
def downKey(event):
    global direction
    direction = "down"
def cheatcode(event):
    if len(snake)>1:
        canvas.move(snake[len(snake)-1], (foodX * (-1)), (foodY * (-1)))
        snake.pop()
def bosskey():
    global bosskeywindow
    global workimg
    window.withdraw()
    bosskeywindow = Tk()#
    bosskeywindow.title("on work")
    c = Canvas(bosskeywindow, width=1920, height=1080, bd=0, highlightthickness=0)
    workimg = "pyimage1.jpg"
    photo = PhotoImage(master = c,file = workimg)
    c.create_image(950, 450, image=photo)
    c.pack()
    bosskeywindow.mainloop()
def Saveleftkey(event):
    keybind[0]= leftkeybind.get()
def Saverightkey(event):
    keybind[1]= rightkeybind.get()
def Saveupkey(event):
    keybind[2]= upkeybind.get()
def Savedownkey(event):
    keybind[3]= downkeybind.get()
def checkReturn(event):
    global username
    username = nameentry.get()
    updateleaderboard()
    entername.destroy()
    window.destroy()
    showleaderboard()
#About the window
def setWindowDimensions(w,h):  #set the dimensions for the menu and the game window
    global x
    global y
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window
#About the snake
def growSnake():  #grow the snake when it eats the
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize,fill = "#FDF3F3"))
    if (direction == "left"):
        canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize,lastElementPos[1], lastElementPos[2] + snakeSize, lastElementPos[3])
    elif (direction == "right"):
        canvas.coords(snake[lastElement + 1], lastElementPos[0] - snakeSize, lastElementPos[1], lastElementPos[2] - snakeSize, lastElementPos[3])
    elif (direction == "up"):
        canvas.coords(snake[lastElement + 1], lastElementPos[0],lastElementPos[1] + snakeSize, lastElementPos[2],lastElementPos[3] + snakeSize)
    else:
        canvas.coords(snake[lastElement + 1], lastElementPos[0],lastElementPos[1] - snakeSize, lastElementPos[2],lastElementPos[3] - snakeSize)
    global score
    score += 10
    txt = "score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)
def overlapping(a,b): #if the snake overlap something
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False
def moveSnake():
    canvas.pack()
    positions = []
    positions.append(canvas.coords(snake[0]))
    if positions[0][0] < 0:
        canvas.coords(snake[0], width, positions[0][1], width - snakeSize, positions[0][3])
    elif positions[0][2] > width:
        canvas.coords(snake[0], 0 - snakeSize, positions[0][1], 0, positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(snake[0], positions[0][0], 0 - snakeSize, positions[0][2], 0)
    elif positions[0][1] < 0:
        canvas.coords(snake[0], positions[0][0], height, positions[0][2], height - snakeSize)
    positions.clear()
    positions.append(canvas.coords(snake[0]))
    if direction == "left":
        canvas.move(snake[0], -snakeSize, 0)
    elif direction == "right":
        canvas.move(snake[0], snakeSize, 0)
    elif direction == "up":
        canvas.move(snake[0], 0, -snakeSize)
    elif direction == "down":
        canvas.move(snake[0], 0, snakeSize)
    sHeadPos = canvas.coords(snake[0])
    foodPos = canvas.coords(food)
    if overlapping(sHeadPos, foodPos):
        moveFood()
        growSnake()
    for i in range(1, len(snake)):
        if overlapping(sHeadPos, canvas.coords(snake[i])):
            gameOver = True
            canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold", text="Game Over! Enter your name to the leaderboard")
            Getname()
    for i in range(1, len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake) - 1):
        canvas.coords(snake[i + 1], positions[i][0], positions[i][1], positions[i][2], positions[i][3])
    if pause == False:
        if 'gameOver' not in locals():
            window.after(90, moveSnake)
#About menus
def start_menu(): #initialization of the start menu
    global menu
    global newgame
    menu = setWindowDimensions(width, height)
    menu.configure(bg = "black")
    frm = ttk.Frame(menu, padding=0,height=height,width=width)
    frm.place(x=x - width/2 + 90,y=y + height/2)
    ttk.Label(frm, text="                                                                                             Snake Game!",width=100,font="Times 40 italic bold").grid(column=1, row=0)
    ttk.Button(frm, text="Start a new Game", command=lambda :opennewgame(),width=100).grid(column=1, row=1)
    ttk.Button(frm, text="Load a Game", command=lambda :loadgame(),width=100).grid(column=1, row=2)
    ttk.Button(frm, text="Keybindings", command=lambda :keybinding(), width=100).grid(column=1, row=3)
    ttk.Button(frm, text="Leaderboard", command=lambda: showleaderboard(), width=100).grid(column=1, row=4)
    ttk.Button(frm, text="Quit", command=menu.destroy,width=100).grid(column=1, row=5)
    newgame=False
    menu.mainloop()
def Getname(): #Get name from the user
    global entername
    global nameentry
    entername = Tk()
    entername.title("Get name")
    name = Label(entername, text="Enter your name for leaderboard and hit enter to continue:")
    name.pack(side = LEFT)
    nameentry = Entry(entername)
    nameentry.pack(side = RIGHT)
    nameentry.focus_set()
    nameentry.bind("<Return>", checkReturn)
    entername.mainloop()
def showleaderboard():
    leaderboarddata = []
    leaderboardfile = open("leaderboard.txt", "r")
    for v in leaderboardfile:
        print(type(v))
        leaderboarddata.append(v)
    Sortedleaderboard = sorted(leaderboarddata, key=get_score,reverse=True)
    print(Sortedleaderboard)
    leaderboard = setWindowDimensions(width,height)
    Label(leaderboard, text="This Board will show the Top Five", width=55, font="Times 40 italic bold").grid(column=2, row=0)
    Label(leaderboard,text = "1. " + Sortedleaderboard[0],width=55,font="Times 40 italic bold").grid(column=2,row=1)
    Label(leaderboard, text="2. " + Sortedleaderboard[1],width=55,font="Times 40 italic bold").grid(column=2, row=2)
    Label(leaderboard, text="3. " + Sortedleaderboard[2],width=55,font="Times 40 italic bold").grid(column=2, row=3)
    Label(leaderboard, text="4. " + Sortedleaderboard[3],width=55,font="Times 40 italic bold").grid(column=2, row=4)
    Label(leaderboard, text="5. " + Sortedleaderboard[4], width=55, font="Times 40 italic bold").grid(column=2, row=5)
    leaderboard.mainloop()
def pausemenu1(): #initialization of the pausemenu
    global pausemenu
    pausemenu = Tk()
    pausemenu.title("Pause menu")
    Button(pausemenu, text="continue ", command= lambda:pausegame("<Escape>") ).grid()
    Button(pausemenu, text="save current game ", command=lambda:savegame() ).grid()
    Button(pausemenu, text="Quit Game", command=lambda:closegame()).grid()

    pausemenu.mainloop()
#Update dan get method
def updateleaderboard():
    leaderboardfile = open("leaderboard.txt","a")
    leaderboardfile.write(username+","+str(score)+"\n")
def get_score(t): #get out the score from the data
    for x in range(len(t)):
        if t[x:x+1] ==",":
            return t[x+1:len(t)]
            continue
def getpos(bodyposs): #get the position stored in the savedgame file
    global bodyposx1
    global bodyposy1
    global bodyposx2
    global bodyposy2
    xend = 0
    bodyposx1 = ""
    bodyposy1 = ""
    bodyposx2 = ""
    bodyposy2 = ""
    for x in range(1,len(bodyposs)):
        if bodyposs[x:x+1] !=".":
            bodyposx1 = bodyposx1 + bodyposs[x:x+1]
            xend = x+1
        else:
            break
    yend = xend+4
    for i in range(yend,len(bodyposs)):
        if bodyposs[i:i+1] !=".":
            bodyposy1 = bodyposy1 + bodyposs[i:i+1]
            yend = yend +1
        else:
            break
    xend = yend +4
    for x in range(xend,len(bodyposs)):
        if bodyposs[x:x+1] !=".":
            bodyposx2 = bodyposx2 + bodyposs[x:x+1]
            xend = x+1
        else:
            break
    for i in range(xend+4,len(bodyposs)):
        if bodyposs[i:i+1] !=".":
            bodyposy2 = bodyposy2 + bodyposs[i:i+1]
        else:
            break
#Effects on Game
def pausegame(event):
    global pause
    if pause == False:
        pause = True
        pausemenu1()
    else:
        pause = False
        pausemenu.destroy()
        savegame()
        window.destroy()
        loadgame()
def closegame():
    window.destroy()
    pausemenu.destroy()
def savegame():
    savedgame = open("savedgame.txt","w")
    savedgame.write(str(score)+"\n")
    savedgame.write(str(len(snake))+"\n")
    savedgame.write(str(foodX)+"\n")
    savedgame.write(str(foodY)+"\n")
    savedgame.write(str(direction)+"\n")
    for x in range(0,len(snake)):
        bodypos = canvas.coords(snake[x])
        savedgame.write(str(bodypos)+"\n")
def loadgame():
    global savegamedata
    global foodX
    global foodY
    global score
    global directioncontinue
    global snakelength
    global newgame
    global bodypos
    global snakepositions
    savedgamedata = open("savedgame.txt")
    score = int(savedgamedata.readline())
    snakelength = int(savedgamedata.readline())
    foodX = int(savedgamedata.readline())
    foodY = int(savedgamedata.readline())
    directioncontinue = str(savedgamedata.readline())
    newgame = False
    snakepositions = []
    for x in range(0, snakelength):
        snakepositions.append(savedgamedata.readline())

    gameenviroment()
def Onwork(event): #Check if boss key Triggered
    global onwork
    if onwork == False:
        onwork = True
        bosskey()
    else:
        onwork = False
        bosskeywindow.destroy()
#About the setting
def savekeyconfig(): #save the user configuration of the key to the file
    Update = False
    for x in keybind:
        if x[0:1] != "<":
            Update = True
    if Update == True:
        keyconfig = open("keybind.txt", "w")
        for i in keybind:
            print(i)
            if i[0:1] != "<":
                print(i)
                keyconfig.write("<"+i+">"+"\n")
def loadkeyconfig(): #load the user configuration of the key from the file
    global keybind
    keybind = ["","","",""]  # LEFT.RIGHT.UP,DOWN
    keyconfig = open("keybind.txt")
    counter = 0
    for x in keyconfig:
        keybind[counter] = x
        counter = counter+1
def keybinding(): #Use window to get the key and change the key binding
    global leftkeybind
    global rightkeybind
    global upkeybind
    global downkeybind
    loadkeyconfig()
    keybindmenu = setWindowDimensions(width,height)
    Left = Label(keybindmenu, text="Go left(press return so the program can update it and press save when you are done):")
    Left.pack()
    leftkeybind = tk.Entry(keybindmenu)
    leftkeybind.insert(0,keybind[0])
    leftkeybind.pack()
    leftkeybind.focus_set()
    leftkeybind.bind("<Return>", Saveleftkey)
    right = Label(keybindmenu, text="Go right(press return so the program can update it and press save when you are done):")
    right.pack()
    rightkeybind = tk.Entry(keybindmenu)
    rightkeybind.insert(0,keybind[1])
    rightkeybind.pack()
    rightkeybind.focus_set()
    rightkeybind.bind("<Return>", Saverightkey)
    up = Label(keybindmenu, text="Go Up(press return so the program can update it and press save when you are done):")
    up.pack()
    upkeybind = tk.Entry(keybindmenu)
    upkeybind.insert(0,keybind[2])
    upkeybind.pack()
    upkeybind.focus_set()
    upkeybind.bind("<Return>", Saveupkey)
    down = Label(keybindmenu, text="Go down(press return so the program can update it and press save when you are done):")
    down.pack()
    downkeybind = tk.Entry(keybindmenu)
    downkeybind.insert(0,keybind[3])
    downkeybind.pack()
    downkeybind.focus_set()
    downkeybind.bind("<Return>", Savedownkey)
    savebutton = Button(keybindmenu,text="save",width="160", height="160", command=lambda: savekeyconfig())
    savebutton.pack()
    keybindmenu.mainloop()
#Main manu
def opennewgame():
    global newgame
    newgame = True
    gameenviroment()
def gameenviroment():
    global scoreText
    global direction
    global canvas
    global snake
    global snakeSize
    global window
    global score
    global txt
    global pause
    global newgame
    global food
    global snakepositions
    global onwork
    loadkeyconfig()
    window = setWindowDimensions(width, height)
    canvas = Canvas(window, bg="black", width=width, height=height)
    snake = []
    snakeSize = 15
    snake.append(canvas.create_rectangle(snakeSize, snakeSize, snakeSize * 2, snakeSize * 2, fill="white"))
    onwork = False
    pause = False
    canvas.bind(keybind[0], leftKey)
    canvas.bind(keybind[1], rightKey)
    canvas.bind(keybind[2], upKey)
    canvas.bind(keybind[3], downKey)
    canvas.bind("<Escape>", pausegame)
    canvas.bind("<7>", cheatcode)
    canvas.bind("<b>", Onwork)
    canvas.focus_set()
    direction = "right"
    if newgame == True:
        score = 0
        placeFood()
        moveSnake()
    else:
        score = score
        if directioncontinue == "up\n":
            direction = "up"
        elif directioncontinue == "left\n":
            direction = "left"
        elif directioncontinue == "right\n":
            direction = "right"
        elif directioncontinue == "down\n":
            direction = "down"
        food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steel blue")
        canvas.move(food, foodX, foodY)
        getpos(snakepositions[0])
        canvas.coords(snake[0],int(bodyposx1),int(bodyposy1),int(bodyposx2),int(bodyposy2))
        moveSnake()
        for x in range(1,snakelength):
            snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3"))
            getpos(snakepositions[x])
            canvas.coords(snake[x],int(bodyposx1),int(bodyposy1),int(bodyposx2),int(bodyposy2))

    txt = "Score:" + str(score)
    scoreText = canvas.create_text(width / 2, 10, fill="white", font="Times 20 italic bold", text=txt)
    window.mainloop()

width = 1600
height = 900
start_menu()