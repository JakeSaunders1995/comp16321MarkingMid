from tkinter import *



window = Tk()
window.title("Coursework Game")
window.geometry("960x540")


backround = PhotoImage(file="images/spcebackround.png")
newbg = PhotoImage(file="images/pacbg.png")

myCanvas = Canvas(window, width=900, height=600)
myCanvas.pack(fill="both", expand = True)


def addBackround():
	myCanvas.create_image(0,0, image=backround, anchor="nw")

addBackround()
def newBackround():
	myCanvas.create_image(0,0, image=newbg, anchor="nw")
	

def startText():
	myCanvas.create_text(475, 250, text="press <start> to start", font=("Helvetica",50), fill="red")
	startbutton = Button(window, text="start",fg="white", bg="red", font=("Helvetica", 50), padx=35, pady=25, command = startRound)
	startbutton.place(x=455, y=300)

def removebutton():
	startbutton.place_forget()

def startRound():
	newBackround()
	myCanvas.create_text(475, 50, text="please enter your initials", font=("Helvetica",50), fill="red")
	initials = Entry(window)
	initials.place(x=400, y=95)
	removebutton()

startText()













window.mainloop()