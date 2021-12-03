from tkinter import *
from tkinter import messagebox
import random
import hashlib
import csv

class Game():
    
    def __init__(self, root):

        ### Initialising master window and 'main' frames ###

        self.root = root
        self.root.geometry('1366x768')
        self.root.title("KIM    JONG    JOYRIDE")
        self.mainFrame1 = Frame(self.root, height=200, width=1366, highlightbackground="black", highlightthickness=1)
        self.mainFrame1.pack()
        self.mainFrame1.pack_propagate(0)
        self.mainFrame2 = Frame(self.root, height=568, width=1366, highlightbackground="black", highlightthickness=1)
        self.mainFrame2.pack()
        self.mainFrame2.pack_propagate(0)

        ### Initialising images used ###

        self.startScreenKimPicOne = PhotoImage(file="images/KimStartScreen.png")
        self.startScreenKimPicTwo = PhotoImage(file="images/KimCursorEdited.png")
        self.DestroyTheWorld = PhotoImage(file="images/DestroyTheWorld.png")
        self.southKoreaFlag = PhotoImage(file="images/SouthKorea.png")
        self.japanFlag = PhotoImage(file="images/Japan.png")
        self.englandFlag = PhotoImage(file="images/England.png")
        self.USAFlag = PhotoImage(file="images/USA.png")
        self.russiaFlag = PhotoImage(file="images/Russia.png")
        self.lastLevelFlag = PhotoImage(file="images/LastLevel.png")
        self.SouthKoreaBackground = PhotoImage(file="images/SouthKoreaBackground.png")
        self.Missile = PhotoImage(file="images/Missile.png")
        self.Cannon = PhotoImage(file="images/Cannon.png")
        self.Steel = PhotoImage(file="images/Steel.png")
        self.Cheese = PhotoImage(file="images/Cheese.png")
        self.Potion = PhotoImage(file="images/potion.png")

        ### Initialising cheat codes ###
        
        self.slowWeapons = False
        self.infHealth = False
        self.satan = False

        ### Initialising game data ###
        
        self.paused = False        
        self.level = 1
        self.score = 0
        self.health = 100
        self.username = ""
        self.password = ""
        self.passwordHash = ""
        self.currentLevelTitleText = "Level 1 - South Korea"
        self.currentFlag = self.southKoreaFlag
        self.objectsInCanvas = []
        self.cannonsInCanvas = []
        self.bulletsInCanvas = []
        self.steelInCanvas = []
        self.cheeseInCanvas = []
        self.potionsInCanvas = []
        self.bulletCooldown = 0
        self.cannonCooldown = 0
        self.steelCooldown = 0
        self.levelTime = 0


    ### Clears any widgets from main frames ###

    def clearWidgets(self):
        
        for widget in self.mainFrame1.winfo_children():
            widget.destroy()
        for widget in self.mainFrame2.winfo_children():
            widget.destroy()


    ### When cursor enters widget dimensions of picture on start screen, swap to second picture ###

    def onEnterKimPic(self, event):
        self.startScreenLabel3.config(image=self.startScreenKimPicTwo)


    ###  When cursor leaves widget dimensions of picture on start screen, revert to first picture ###    

    def onLeaveKimPic(self, event):
        self.startScreenLabel3.config(image=self.startScreenKimPicOne)

    
    ### Apply cheat codes from options ###

    def applyCheatCodes(self):

        code = self.optionsScreenEntry.get().upper()
        if (code == "SLOWWEAPONS"):
            self.slowWeapons = True            
            self.optionsScreenLabel4.config(text="SLOWWEAPONS cheat activated. Enemy bullets and bombs are now slower.", fg="#FF0000")
        elif (code == "INFHEALTH"):
            self.infHealth = True
            self.optionsScreenLabel4.config(text="INFHEALTH cheat activated. Collision detection turned off.", fg="#FF0000")
        elif (code == "SATAN"):
            self.satan = True
            self.optionsScreenLabel4.config(text="SATAN cheat activated. Skips to last level. You monster...", fg="#FF0000")
        else:
            self.optionsScreenLabel4.config(text="Cheat code does not exist...", fg="#000000")


    ### Display controls from pause screen ###

    def controls(self):
        
        for widget in self.gameScreenFrame2.winfo_children():
            widget.destroy()
        
        ctrlText = "Controls:\n\nMove missile up: ↑\n\nMove missile down: ↓\n\nBoss key: Esc"
        
        self.controlsLabel = Label(self.gameScreenFrame2, text=ctrlText, font=("Courier", 32), pady=20)
        self.controlsLabel.pack()    


    ### Log In ###

    def login(self):

        loggedIn = False        
        self.username = str(self.loadUsernameEntry.get())
        self.password = str(self.loadPasswordEntry.get())
        self.passwordHash = hashlib.sha256(self.password.encode()).hexdigest()
        
        with open('data/userdata.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
                
        for i in range(0, len(data)-1):
            if (data[i] != []):
                if (data[i][0] == self.username and data[i][1] == self.passwordHash):
                    self.level = data[i][2]
                    self.score = data[i][3]
                    loggedIn = True

        if (loggedIn):
            self.loadDiv.config(text="Logged in!")
            self.gameScreenLevelLabel.config(text="Level: " + str(self.level))
            self.gameScreenScoreLabel.config(text="Score: " + str(self.score))
            if (str(self.level) == "1"):
                self.currentFlag = self.southKoreaFlag
                self.currentLevelTitleText = "Level 1 - South Korea"
            elif (str(self.level) == "2"):
                self.currentFlag = self.japanFlag
                self.currentLevelTitleText = "Level 2 - Japan"
            elif (str(self.level) == "3"):
                self.currentFlag = self.englandFlag
                self.currentLevelTitleText = "Level 3 - Manchester, England"
            elif (str(self.level) == "4"):
                self.currentFlag = self.USAFlag
                self.currentLevelTitleText = "Level 4 - USA"
            elif (str(self.level) == "5"):
                self.currentFlag = self.russiaFlag
                self.currentLevelTitleText = "Level 5 - Russia"
            elif (str(self.level) == "?"):
                self.currentFlag = self.lastLevelFlag
                self.currentLevelTitleText = "Level ? - NUCLEAR ARMAGGEDON"
            else:
                self.currentFlag = self.southKoreaFlag           
        else:
            self.loadDiv.config(text="Log in failed.")
            self.username = ""
            self.password = ""
            self.passwordHash = ""        


    ### Load Progress ###

    def load(self):
        
        for widget in self.gameScreenFrame2.winfo_children():
            widget.destroy()
        
        self.loadUsernameLabel = Label(self.gameScreenFrame2, text = "Username:", font=("Courier", 24), pady=20, padx=20)
        self.loadUsernameLabel.pack()
        self.loadUsernameInfo = Label(self.gameScreenFrame2, text = "Username must be  1 to 5 characters long.", font=("Courier", 12), fg="#FF0000")
        self.loadUsernameInfo.pack()
        self.loadUsernameEntry = Entry(self.gameScreenFrame2, font=("Courier", 24))
        self.loadUsernameEntry.pack()

        self.loadPasswordLabel = Label(self.gameScreenFrame2, text = "Password:", font=("Courier", 24), pady=20, padx=20)
        self.loadPasswordLabel.pack()
        self.loadPasswordInfo = Label(self.gameScreenFrame2, text = "Password must be  8 to 12 characters long.", font=("Courier", 12), fg="#FF0000")
        self.loadPasswordInfo.pack()
        self.loadPasswordEntry = Entry(self.gameScreenFrame2, font=("Courier", 24))
        self.loadPasswordEntry.pack()

        self.loadDiv = Label(self.gameScreenFrame2, text=" ", font=("Courier", 12), fg="#FF0000", pady=20)
        self.loadDiv.pack()

        self.loginButton = Button(self.gameScreenFrame2, text = "LOG IN", font=("Courier", 72), width=100, pady=40, command=self.login)
        self.loginButton.pack()
        

    ### Save Progress ###

    def save(self):
        
        if (self.username != ""):      
            lineEdited = False
            newEntry = [self.username, self.passwordHash, self.level, self.score]
            lines = []
            with open('data/userdata.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    lines.append(row)
            i=0
            for row in lines:
                if (row[0] == self.username):
                    lines[i] = newEntry
                    lineEdited = True
                i+=1 
            if not lineEdited:
                lines.append(newEntry)
            with open('data/userdata.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(lines)


    ### Resume state ###

    def resume(self):

        self.paused = False

        self.gameScreenPauseButton.config(text="PAUSE", command=self.onPause)

        for widget in self.gameScreenFrame2.winfo_children():
            widget.destroy()     

        self.gameScreenLevelTitleLabel = Label(self.gameScreenFrame2, text=self.currentLevelTitleText, font=("Courier", 24), pady=15)
        self.gameScreenLevelTitleLabel.pack()
        self.gameScreenFlag = Label(self.gameScreenFrame2, image=self.currentFlag)
        self.gameScreenFlag.pack()


    ### Pause state ###

    def onPause(self):

        self.paused = True
        
        self.gameScreenPauseButton.config(text="RESUME", command=self.resume)

        for widget in self.gameScreenFrame2.winfo_children():
            widget.destroy()        

        self.gameScreenSaveButton = Button(self.gameScreenFrame2, text="SAVE", font=("Courier", 100), width=100, pady=15, command=self.save)
        self.gameScreenSaveButton.pack()
        self.gameScreenLoadButton = Button(self.gameScreenFrame2, text="LOAD", font=("Courier", 100), width=100, pady=15, command=self.load)
        self.gameScreenLoadButton.pack()
        self.gameScreenControlsButton = Button(self.gameScreenFrame2, text="CONTROLS", font=("Courier", 100), width=100, pady=15, command=self.controls)
        self.gameScreenControlsButton.pack()


    ### Leaderboard screen ###

    def leaderboardScreen(self):
        
        self.clearWidgets()

        self.leaderboardScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.leaderboardScreenFrame1.pack(side=LEFT)
        self.leaderboardScreenFrame1.pack_propagate(0)
        self.leaderboardScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.leaderboardScreenFrame2.pack()
        self.leaderboardScreenFrame2.pack_propagate(0)

        self.leaderboardScreenLabel1 = Label(self.mainFrame1, text = "LEADERBOARD", font=("Courier", 100), pady=100)
        self.leaderboardScreenLabel1.pack()

        leaders = ""
        with open('data/leaderboards.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        for i in range(1, 6):
            leaders += str(i) + ". " + str(data[i][0]) + " - " + str(data[i][1])
            if (i!=5):
                leaders += "\n\n"
        
        self.leaderboardScreenLabel = Label(self.leaderboardScreenFrame1, text=leaders, font=("Courier, 32"), pady=50)
        self.leaderboardScreenLabel.pack()

        self.leaderboardScreenBackButton = Button(self.leaderboardScreenFrame2, text = "BACK", font=("Courier", 72), width=500, height=500, command=self.startScreen)
        self.leaderboardScreenBackButton.pack()

    
    ### Check credentials ###

    def checkCredentials(self):

        usernameTaken = False        
        self.username = str(self.createAccountScreenUsernameEntry.get())
        self.password = str(self.createAccountScreenPasswordEntry.get())
        self.passwordHash = hashlib.sha256(self.password.encode()).hexdigest()

        with open('data/userdata.csv', newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
        
        for i in range(0, len(data)-1):
            if (data[i][0] == self.username):
                usernameTaken = True
                
        if (usernameTaken):
            self.createAccountScreenLabel2.config(text="Username taken.", fg="#FF0000")
        elif (len(self.username) == 0 or len(self.username) > 5):
            self.createAccountScreenLabel2.config(text="Username out of range.", fg="#FF0000")
        elif (len(self.password) < 8 or len(self.password) > 12):
            self.createAccountScreenLabel2.config(text="Password out of range.", fg="#FF0000")
        else:
            self.gameScreen()


    ### Create account screen ###

    def createAccountScreen(self):
        
        self.clearWidgets()
        
        self.createAccountScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.createAccountScreenFrame1.pack(side=LEFT)
        self.createAccountScreenFrame1.pack_propagate(0)
        self.createAccountScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.createAccountScreenFrame2.pack()    
        self.createAccountScreenFrame2.pack_propagate()

        self.createAccountScreenLabel = Label(self.mainFrame1, text="CREATE ACCOUNT", font=("Courier", 100), pady=100)
        self.createAccountScreenLabel.pack()

        self.createAccountScreenUsernameLabel = Label(self.createAccountScreenFrame1, text = "Username:", font=("Courier", 24), pady=20, padx=20)
        self.createAccountScreenUsernameLabel.pack()
        self.createAccountScreenUsernameInfo = Label(self.createAccountScreenFrame1, text = "Username must be  1 to 5 characters long.", font=("Courier", 12), fg="#FF0000")
        self.createAccountScreenUsernameInfo.pack()
        self.createAccountScreenUsernameEntry = Entry(self.createAccountScreenFrame1, font=("Courier", 24))
        self.createAccountScreenUsernameEntry.pack()

        self.createAccountScreenPasswordLabel = Label(self.createAccountScreenFrame1, text = "Password:", font=("Courier", 24), pady=20, padx=20)
        self.createAccountScreenPasswordLabel.pack()
        self.createAccountScreenPasswordInfo = Label(self.createAccountScreenFrame1, text = "Password must be  8 to 12 characters long.", font=("Courier", 12), fg="#FF0000")
        self.createAccountScreenPasswordInfo.pack()
        self.createAccountScreenPasswordEntry = Entry(self.createAccountScreenFrame1, font=("Courier", 24))
        self.createAccountScreenPasswordEntry.pack()

        self.createAccountScreenLabel2 = Label(self.createAccountScreenFrame1, text="Kim Jong Un does not like \nunoriginal usernames and\nweak passwords.", font=("Courier", 24), pady=100)
        self.createAccountScreenLabel2.pack()

        self.createAccountScreenButton = Button(self.createAccountScreenFrame2, text="APPLY", font=("Courier", 72), width=100, height=100, command=self.checkCredentials)
        self.createAccountScreenButton.pack()
    

    ### Login Prompt Screen ###

    def loginPromptScreen(self):
        
        self.clearWidgets()

        self.loginPromptScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.loginPromptScreenFrame1.pack(side=LEFT)
        self.loginPromptScreenFrame1.pack_propagate(0)
        self.loginPromptScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.loginPromptScreenFrame2.pack()    
        self.loginPromptScreenFrame2.pack_propagate(0)

        self.loginPromptScreenLabel = Label(self.mainFrame1, text="CREATE ACCOUNT?", font=("Courier", 100), pady=100)
        self.loginPromptScreenLabel.pack()
        
        self.loginPromptScreenYesButton = Button(self.loginPromptScreenFrame1, text= "YES", height=3, width=1000, font=("Courier", 72), command=self.createAccountScreen)
        self.loginPromptScreenYesButton.pack()
        self.loginPromptScreenNoButton = Button(self.loginPromptScreenFrame2, text="NO", height=3, width=1000, font=("Courier", 72), command=self.gameScreen)
        self.loginPromptScreenNoButton.pack()

        self.loginPromptScreenLabel2 = Label(self.loginPromptScreenFrame1, text = "By choosing YES, you can\nsave progress and score.", font=("Courier", 32), pady=200)
        self.loginPromptScreenLabel2.pack()

        self.loginPromptScreenLabel3 = Label(self.loginPromptScreenFrame2, text = "By choosing NO, you can\nproceed to game and login.", font=("Courier", 32), pady=200)
        self.loginPromptScreenLabel3.pack()

    
    ### Death Screen and Leaderboard Update ###
    
    def deathScreen(self):

        self.clearWidgets()

        if self.username != "":
            deathScreenText = "Oh no! You died!\nYour score was " + str(self.score) + "\nplaying as " + str(self.username) + ".\nYour score has been added to the leaderboards.\nBetter luck next time!"
        else:
            deathScreenText = "Oh no! You died!\nYour score was " + str(self.score) + ".\nBetter luck next time!"

        self.deathScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.deathScreenFrame1.pack(side=LEFT)
        self.deathScreenFrame1.pack_propagate(0)
        self.deathScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.deathScreenFrame2.pack()    
        self.deathScreenFrame2.pack_propagate(0)

        self.deathScreenGameOverLabel = Label(self.mainFrame1, text="Game Over!", font=("Courier", 100), pady=100)
        self.deathScreenGameOverLabel.pack()

        self.deathScreenDeathText = Label(self.deathScreenFrame1, text=deathScreenText, font=("Courier", 24), pady=50)
        self.deathScreenDeathText.pack()

        self.startScreenLabel3 = Label(self.deathScreenFrame1, image=self.startScreenKimPicOne)
        self.startScreenLabel3.bind('<Enter>', self.onEnterKimPic)
        self.startScreenLabel3.bind('<Leave>', self.onLeaveKimPic)
        self.startScreenLabel3.pack()

        self.deathScreenExitButton = Button(self.deathScreenFrame2, text="EXIT", font=("Courier", 72), height=200, width=200, command=exit)
        self.deathScreenExitButton.pack()

        if self.username != "":
            newLeaderboard = [["NAME","SCORE"]]
            with open('data/leaderboards.csv', newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            dataPlaced = False
            for i in range(1, len(data)):
                if ((int(self.score) > int(data[i][1])) and (dataPlaced == False)):
                    newLeaderboard.append([self.username, self.score])
                    dataPlaced = True
                newLeaderboard.append(data[i])
            if dataPlaced == False:
                newLeaderboard.append([self.username, self.score])
            with open('data/leaderboards.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(newLeaderboard)


    ### Collision Detection ###

    def collisionDetection(self):
        
        missileX0 = self.gameScreenCanvas.coords(self.missileObject)[0]
        missileY0 = self.gameScreenCanvas.coords(self.missileObject)[1]
        missileX1 = missileX0 + 64
        missileY1 = missileY0 + 32
        missilemidX = missileX0 + 32
        missilemidY = missileY0 + 16
        
        bulletCounter = 0
        for bullet in self.bulletsInCanvas:
            bulletX0 = self.gameScreenCanvas.coords(bullet)[0]
            bulletY0 = self.gameScreenCanvas.coords(bullet)[1]
            bulletmidX = bulletX0 + 5
            bulletmidY = bulletY0 + 5
            if (bulletmidX > missileX0 and bulletmidX < missileX1 and bulletmidY > missileY0 and bulletmidY < missileY1): 
                self.gameScreenCanvas.delete(bullet)
                self.bulletsInCanvas.pop(bulletCounter)
                self.objectsInCanvas.remove(bullet)
                self.health -= 10
                self.gameScreenHealthLabel.config(text="Health: " + str(self.health))
            bulletCounter += 1

        cheeseCounter = 0
        for cheese in self.cheeseInCanvas:
            cheeseX0 = self.gameScreenCanvas.coords(cheese)[0]
            cheeseY0 = self.gameScreenCanvas.coords(cheese)[1]
            cheeseX1 = cheeseX0 + 32
            cheeseY1 = cheeseY0 + 32
            if (cheeseX0 <= missileX1 and cheeseX1 >= missileX0 and cheeseY0 <= missileY0 and cheeseY1 >= missileY1): 
                self.gameScreenCanvas.delete(cheese)
                self.cheeseInCanvas.pop(cheeseCounter)
                self.objectsInCanvas.remove(cheese)
                self.score += 100
                self.gameScreenScoreLabel.config(text="Score: " + str(self.score))
            cheeseCounter += 1

        potionCounter = 0
        for potion in self.potionsInCanvas:
            potionX0 = self.gameScreenCanvas.coords(potion)[0]
            potionY0 = self.gameScreenCanvas.coords(potion)[1]
            potionX1 = potionX0 + 32
            potionY1 = potionY0 + 32
            if (potionX0 <= missileX1 and potionX1 >= missileX0 and potionY0 <= missileY0 and potionY1 >= missileY1): 
                self.gameScreenCanvas.delete(potion)
                self.potionsInCanvas.pop(potionCounter)
                self.objectsInCanvas.remove(potion)
                if self.health <= 60:
                    self.health += 40
                else:
                    self.health = 100
                self.gameScreenHealthLabel.config(text="Health: " + str(self.health))
            potionCounter += 1

        steelCounter = 0
        for steel in self.steelInCanvas:
            steelX0 = self.gameScreenCanvas.coords(steel)[0]
            steelY0 = self.gameScreenCanvas.coords(steel)[1]
            steelX1 = steelX0 + 25
            steelY1 = steelY0 + 200
            if (steelX0 < missileX1 and steelX1 > missileX0 and steelY0 < missileY0 and steelY1 > missileY1): 
                self.gameScreenCanvas.delete(steel)
                self.steelInCanvas.pop(steelCounter)
                self.objectsInCanvas.remove(steel)
                self.health -= 20
                self.gameScreenHealthLabel.config(text="Health: " + str(self.health))
            steelCounter += 1
                

    ### Move missile on key press ###

    def onKey(self, event):
        if not self.paused:
            if event.keysym == "Up":
                if (int(self.gameScreenCanvas.coords(self.missileObject)[1]) != 40):
                    self.gameScreenCanvas.move(self.missileObject, 0, -50)
            if event.keysym == "Down":
                if (int(self.gameScreenCanvas.coords(self.missileObject)[1]) != 440):
                    self.gameScreenCanvas.move(self.missileObject, 0, 50)


    ### Level Two Gameplay ###        

    def levelTwo(self):

        if not self.paused:

            self.level = 2
            self.currentFlag = self.japanFlag
            self.currentLevelTitleText = "Level 2 - Japan"

            self.gameScreenLevelTitleLabel.config(text=self.currentLevelTitleText)
            self.gameScreenFlag.config(image = self.currentFlag)
            self.gameScreenLevelLabel.config(text="Level: " + str(self.level))

            self.levelTime += 1
            self.cannonCooldown += 1
            self.steelCooldown += 1
            self.bulletCooldown += 1
            self.randomObj = random.randint(0,225)
            objectGenerator = random.randint(0,1)

            for obj in self.objectsInCanvas:
                self.gameScreenCanvas.move(obj, -2, 0)

            if self.randomObj == 1 and objectGenerator == 0 and self.steelCooldown > 300:
                self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,0,image=self.Steel, anchor=NW))
                self.steelInCanvas.append(self.objectsInCanvas[-1])

            if self.randomObj == 1 and objectGenerator == 1 and self.cannonCooldown > 300:
                self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,500,image=self.Cannon, anchor=SW))
                self.cannonsInCanvas.append(self.objectsInCanvas[-1])

            if (self.levelTime % 500 == 0):
                cheeseY = (random.randint(0,8) * 50) + 40
                self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,cheeseY,image=self.Cheese, anchor=NW))  
                self.cheeseInCanvas.append(self.objectsInCanvas[-1])

            if (self.levelTime % 11000 == 0):
                potionY = (random.randint(0,8) * 50) + 40
                self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,potionY,image=self.Potion, anchor=NW))
                self.potionsInCanvas.append(self.objectsInCanvas[-1])

            if self.bulletCooldown > 150:
                for cannon in self.cannonsInCanvas:
                    x0 = self.gameScreenCanvas.coords(cannon)[0]
                    x1 = x0 + 10
                    y0 = self.gameScreenCanvas.coords(cannon)[1]
                    y1 = y0 + 10
                    self.objectsInCanvas.append(self.gameScreenCanvas.create_oval(x0,y0,x1,y1, fill="#000000"))
                    self.bulletsInCanvas.append(self.objectsInCanvas[-1])
                self.bulletCooldown = 0
            for bullet in self.bulletsInCanvas:
                self.gameScreenCanvas.move(bullet, -2, -2)

            for obj in self.objectsInCanvas:
                if self.gameScreenCanvas.coords(obj)[0] <= 0:
                    self.objectsInCanvas.remove(obj)
                    self.gameScreenCanvas.delete(obj)
                    if obj in self.cheeseInCanvas:
                        self.cheeseInCanvas.remove(obj)
                    if obj in self.cannonsInCanvas:
                        self.cannonsInCanvas.remove(obj)
                    if obj in self.steelInCanvas:
                        self.steelInCanvas.remove(obj)
                    if obj in self.bulletsInCanvas:
                        self.bulletsInCanvas.remove(obj)
                    if obj in self.potionsInCanvas:
                        self.potionsInCanvas.remove(obj)

        self.collisionDetection()

        if self.health <= 0:
            self.deathScreen()
           
        if self.levelTime < 12000:             
            self.root.after(5, self.levelTwo)
        else:
            self.levelTime = 0
            for obj in self.objectsInCanvas:
                self.gameScreenCanvas.delete(obj)
            self.objectsInCanvas = []
            for obj in self.steelInCanvas:
                self.gameScreenCanvas.delete(obj)
            self.steelInCanvas = []
            for obj in self.cannonsInCanvas:
                self.gameScreenCanvas.delete(obj)
            self.cannonsInCanvas = []
            for obj in self.cheeseInCanvas:
                self.gameScreenCanvas.delete(obj)
            self.cheeseInCanvas = []
            for obj in self.bulletsInCanvas:
                self.gameScreenCanvas.delete(obj)
            self.bulletsInCanvas = []
            for obj in self.potionsInCanvas:
                self.gameScreenCanvas.delete(obj)
            self.potionsInCanvas = []
            self.clearWidgets()


    ### Level One Gameplay ###    

    def levelOne(self):

        if self.health <= 0:
            self.paused = True
            self.deathScreen()

        else:

            if not self.paused:

                self.level = 1
                self.currentFlag = self.southKoreaFlag
                self.currentLevelTitleText = "Level 1 - South Korea"

                self.gameScreenLevelTitleLabel.config(text=self.currentLevelTitleText)
                self.gameScreenFlag.config(image = self.currentFlag)
                self.gameScreenLevelLabel.config(text="Level: " + str(self.level))


                self.levelTime += 1
                self.cannonCooldown += 1
                self.steelCooldown += 1
                self.bulletCooldown += 1
                self.randomObj = random.randint(0,250)
                objectGenerator = random.randint(0,1)

                for obj in self.objectsInCanvas:
                    self.gameScreenCanvas.move(obj, -1, 0)

                if self.randomObj == 1 and objectGenerator == 0 and self.steelCooldown > 300:
                    self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,0,image=self.Steel, anchor=NW))
                    self.steelInCanvas.append(self.objectsInCanvas[-1])

                if self.randomObj == 1 and objectGenerator == 1 and self.cannonCooldown > 300:
                    self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,500,image=self.Cannon, anchor=SW))
                    self.cannonsInCanvas.append(self.objectsInCanvas[-1])

                if (self.levelTime % 500 == 0):
                    cheeseY = (random.randint(0,8) * 50) + 40
                    self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,cheeseY,image=self.Cheese, anchor=NW))  
                    self.cheeseInCanvas.append(self.objectsInCanvas[-1])

                if (self.levelTime % 11000 == 0):
                    potionY = (random.randint(0,8) * 50) + 40
                    self.objectsInCanvas.append(self.gameScreenCanvas.create_image(683,potionY,image=self.Potion, anchor=NW))
                    self.potionsInCanvas.append(self.objectsInCanvas[-1])

                if self.bulletCooldown > 200:
                    for cannon in self.cannonsInCanvas:
                        x0 = self.gameScreenCanvas.coords(cannon)[0]
                        x1 = x0 + 10
                        y0 = self.gameScreenCanvas.coords(cannon)[1]
                        y1 = y0 + 10
                        self.objectsInCanvas.append(self.gameScreenCanvas.create_oval(x0,y0,x1,y1, fill="#000000"))
                        self.bulletsInCanvas.append(self.objectsInCanvas[-1])
                    self.bulletCooldown = 0
                for bullet in self.bulletsInCanvas:
                    self.gameScreenCanvas.move(bullet, -1, -1)

                for obj in self.objectsInCanvas:
                    if self.gameScreenCanvas.coords(obj)[0] <= 0:
                        self.objectsInCanvas.remove(obj)
                        self.gameScreenCanvas.delete(obj)
                        if obj in self.cheeseInCanvas:
                            self.cheeseInCanvas.remove(obj)
                        if obj in self.cannonsInCanvas:
                            self.cannonsInCanvas.remove(obj)
                        if obj in self.steelInCanvas:
                            self.steelInCanvas.remove(obj)
                        if obj in self.bulletsInCanvas:
                            self.bulletsInCanvas.remove(obj)
                        if obj in self.potionsInCanvas:
                            self.potionsInCanvas.remove(obj)

            self.collisionDetection()
               
            if self.levelTime < 12000:             
                self.root.after(5, self.levelOne)
            else:
                self.levelTime = 0
                for obj in self.objectsInCanvas:
                    self.gameScreenCanvas.delete(obj)
                self.objectsInCanvas = []
                for obj in self.steelInCanvas:
                    self.gameScreenCanvas.delete(obj)
                self.steelInCanvas = []
                for obj in self.cannonsInCanvas:
                    self.gameScreenCanvas.delete(obj)
                self.cannonsInCanvas = []
                for obj in self.cheeseInCanvas:
                    self.gameScreenCanvas.delete(obj)
                self.cheeseInCanvas = []
                for obj in self.bulletsInCanvas:
                    self.gameScreenCanvas.delete(obj)
                self.bulletsInCanvas = []
                for obj in self.potionsInCanvas:
                    self.gameScreenCanvas.delete(obj)
                self.potionsInCanvas = []
                self.levelTwo()


    ### Game screen ###

    def gameScreen(self):

        self.clearWidgets()

        if (self.satan == True):
            self.level = "?"
            self.currentLevelTitleText = "Level ? - NUCLEAR ARMAGGEDON"
            self.currentFlag = self.lastLevelFlag
        
        self.gameScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.gameScreenFrame1.pack(side=LEFT)
        self.gameScreenFrame1.pack_propagate(0)
        self.gameScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.gameScreenFrame2.pack()
        self.gameScreenFrame2.pack_propagate(0)

        self.gameScreenFrame3 = Frame(self.mainFrame1, height=200, width=683, highlightbackground="black", highlightthickness=1)
        self.gameScreenFrame3.pack(side=LEFT)
        self.gameScreenFrame3.pack_propagate(0)
        self.gameScreenFrame4 = Frame(self.mainFrame1, height=200, width=683, highlightbackground="black", highlightthickness=1)
        self.gameScreenFrame4.pack()
        self.gameScreenFrame4.pack_propagate(0)

        self.gameScreenLevelLabel = Label(self.gameScreenFrame3, text="Level: " + str(self.level), font=("Courier", 24), pady=15)  
        self.gameScreenLevelLabel.pack()
        self.gameScreenScoreLabel = Label(self.gameScreenFrame3, text="Score: " + str(self.score), font=("Courier", 24), pady=15)
        self.gameScreenScoreLabel.pack() 
        self.gameScreenHealthLabel = Label(self.gameScreenFrame3, text="Health: " + str(self.health), font=("Courier", 24), pady=15)
        self.gameScreenHealthLabel.pack()

        self.gameScreenPauseButton = Button(self.gameScreenFrame4, text="PAUSE", font=("Courier", 100), width=100, height=100, pady=20, command=self.onPause)
        self.gameScreenPauseButton.pack()

        self.gameScreenLevelTitleLabel = Label(self.gameScreenFrame2, text=self.currentLevelTitleText, font=("Courier", 24), pady=15)
        self.gameScreenLevelTitleLabel.pack()
        self.gameScreenFlag = Label(self.gameScreenFrame2, image=self.currentFlag)
        self.gameScreenFlag.pack()

        self.gameScreenCanvas = Canvas(self.gameScreenFrame1, bg="#87CEEB", height = 500, width = 683)
        self.gameScreenCanvas.pack()
        self.backgroundObject = self.gameScreenCanvas.create_image(0,0, image=self.SouthKoreaBackground, anchor = NW)
        self.missileObject = self.gameScreenCanvas.create_image(40,40,image=self.Missile, anchor=NW)
        self.root.bind('<Key>', self.onKey)
        self.levelOne()
        

    ### Options screen ###

    def optionsScreen(self):

        self.clearWidgets()

        self.optionsScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.optionsScreenFrame1.pack(side=LEFT)
        self.optionsScreenFrame1.pack_propagate(0)
        self.optionsScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.optionsScreenFrame2.pack()
        self.optionsScreenFrame2.pack_propagate(0)
        self.optionsScreenFrame3 = Frame(self.optionsScreenFrame1, height=284, width=683, highlightbackground="black", highlightthickness=1)
        self.optionsScreenFrame3.pack(side=TOP)
        self.optionsScreenFrame3.pack_propagate(0)
        self.optionsScreenFrame4 = Frame(self.optionsScreenFrame1, height=284, width=683, highlightbackground="black", highlightthickness=1)
        self.optionsScreenFrame4.pack()
        self.optionsScreenFrame4.pack_propagate(0)

        self.optionsScreenLabel1 = Label(self.mainFrame1, text = "OPTIONS", font=("Courier", 100), pady=100)
        self.optionsScreenLabel1.pack()

        self.optionsScreenLabel2 = Label(self.optionsScreenFrame3, text = "CHEAT CODES", font=("Courier", 24), pady=20, padx=20)
        self.optionsScreenLabel2.pack()

        self.optionsScreenEntry = Entry(self.optionsScreenFrame3, font=("Courier", 24))
        self.optionsScreenEntry.pack()

        self.optionsScreenLabel3 = Label(self.optionsScreenFrame3, text = "Cheat codes can be found in\ncheatcodes.txt\nwithin the data folder.", font=("Courier", 24), pady=20, padx=20)
        self.optionsScreenLabel3.pack()

        self.optionsScreenLabel4 = Label(self.optionsScreenFrame3, text = "No cheat codes applied.", font=("Courier", 12))
        self.optionsScreenLabel4.pack()
        
        self.optionsScreenApplyButton = Button(self.optionsScreenFrame4, text = "APPLY", font=("Courier", 24), width=200, height=200, command=self.applyCheatCodes)
        self.optionsScreenApplyButton.pack()

        self.optionsScreenBackButton = Button(self.optionsScreenFrame2, text = "BACK", font=("Courier", 72), width=500, height=500, command=self.startScreen)
        self.optionsScreenBackButton.pack()


    ### Start screen ###

    def startScreen(self):

        self.clearWidgets()

        explanation = "Kim is off his rocker! Rocket-man\nis trying to destroy the world\nagain, and it is your job to ensure\nhe succeeds. Dodge the bombs and\nbullets, eat the Swiss cheese."

        self.startScreenFrame1 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.startScreenFrame1.pack(side=LEFT)
        self.startScreenFrame1.pack_propagate(0)
        self.startScreenFrame2 = Frame(self.mainFrame2, height=568, width=683, highlightbackground="black", highlightthickness=1)
        self.startScreenFrame2.pack()
        self.startScreenFrame2.pack_propagate(0)

        self.startScreenLabel1 = Label(self.mainFrame1, text="KIM JONG JOYRIDE", font=("Courier", 100), pady=100)
        self.startScreenLabel1.pack()
        
        self.startScreenLabel2 = Label(self.startScreenFrame1, text=explanation, width=683, font=("Courier", 24), pady=20, padx=20)
        self.startScreenLabel2.pack(side=TOP)
    
        self.startScreenLabel3 = Label(self.startScreenFrame1, image=self.startScreenKimPicOne)
        self.startScreenLabel3.bind('<Enter>', self.onEnterKimPic)
        self.startScreenLabel3.bind('<Leave>', self.onLeaveKimPic)
        self.startScreenLabel3.pack()

        self.startScreenLeaderboardButton = Button(self.startScreenFrame2, text="LEADERBOARDS", font=("Courier", 30), width=30, height=3, command=self.leaderboardScreen)
        self.startScreenLeaderboardButton.pack()

        self.startScreenOptionsButton = Button(self.startScreenFrame2, text="OPTIONS", font=("Courier", 30), width=30, height=3, command=self.optionsScreen)
        self.startScreenOptionsButton.pack()

        self.startScreenStartButton = Button(self.startScreenFrame2, image=self.DestroyTheWorld, height=500, width=800, command=self.loginPromptScreen)
        self.startScreenStartButton.pack()
        


root = Tk()
newGame = Game(root)
newGame.startScreen()
root.mainloop()

# Unsure on whether I will carry on using an object-oriented approach, as I've only used OOP paradigm with Java.


