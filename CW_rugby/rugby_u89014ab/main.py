
from tkinter import *
import asyncio
import time
from tkinter import ttk
# root
root = Tk(className=" Run Lily-liver ")
root.geometry("1920x1080")
root.configure(bg='Grey')
root.grid()

# interactable items
label1 = Label(root, text="Hello World!", bg='Grey').grid(column=0, row=0)  # create label text
butt1 = Button(root, text="Quit",  command=root.destroy, bg='Black', fg='White')
x = 0.5
y = 0.5

butt1.place(relx=x, rely=y)
button = Button(root, text='Submit', bg='Red', fg='Red', command=butt1.destroy).grid(column=2, row=0)
# inputs


def w_pressed(event):
    global y
    y -= 0.005
    butt1.place(relx=x, rely=y)
    print(event.char)


def a_pressed(event):
    global x
    x -= 0.005 * 0.5625
    butt1.place(relx=x, rely=y)
    print(event.char)


def s_pressed(event):
    global y
    y += 0.005
    butt1.place(relx=x, rely=y)
    print(event.char)


def d_pressed(event):
    global x
    x += 0.005 * 0.5625
    butt1.place(relx=x, rely=y)
    print(event.char)


root.mainloop()

