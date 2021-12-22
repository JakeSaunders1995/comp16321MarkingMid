from tkinter import *

window = Tk()
window.title("FootPong Game")
window.geometry("360x240")

backround = PhotoImage(file="images/footballpitch.png")

myCanvas = Canvas(window, width = 360, height = 240)
myCanvas.pack()

def AddBackround():
	myCanvas.create_image(0,0, image = backround, anchor = "nw")

AddBackround()

playerscore = 0

player = myCanvas.create_rectangle(325,110,340,170, fill='white')

#ball=myCanvas.create_oval(165,115,185,135, fill='white')

scoreboard = myCanvas.create_text(90, 10 ,fill = 'red',font="Helvetica", text =(f"Your score total is: {playerscore}"))

def up(event):
	x=0
	y=-10
	myCanvas.move(player,x,y)

def down(event):
	x=0
	y=10
	myCanvas.move(player,x,y)


window.bind("<Up>", up)
window.bind("<w>", up)
window.bind("<s>", down)
window.bind("<Down>", down)

from ballMov import *
import time


ball = ballMov(myCanvas,0,0,20,1,1, "white")
while True:
	ball.move()
	window.update()
	time.sleep(0.01)

	



ballMovement(1,1)

window.mainloop()