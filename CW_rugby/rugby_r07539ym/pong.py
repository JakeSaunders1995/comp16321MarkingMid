from tkinter import Tk, Canvas
import random,time
resolution = (1280, 720)
centre = (resolution[0] / 2, resolution[1] / 2)



class Bat:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = 1250
        self.y = centre[1]-10
        self.batSprite = self.canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 100,fill="white") #creating the bat

    def move(self, event): # Allows movement of the bat, and sets restrictions
        if event.char == "w" and (self.canvas.coords(self.batSprite)[1]>10):
            self.canvas.move(self.batSprite, 0, -20)

        elif event.char == "s" and (self.canvas.coords(self.batSprite)[3]<resolution[1]-10):
            self.canvas.move(self.batSprite, 0, 20)

class Ball:
    radius = 20

    def __init__(self, canvas):
        self.canvas = canvas
        self.ballSprite = self.canvas.create_oval(0, 0, self.radius * 2, self.radius * 2, fill="white")
        self.speed = 3
        self.x_vel = self.speed * random.choice([1,-1])
        self.y_vel = -self.speed* random.choice([1,-1])
        self.reset_position()
    def move(self):
        if self.get_coords()[1] <= 0 or (self.get_coords()[3]  >= self.canvas.winfo_height()):
            self.y_vel *= -1
        elif self.get_coords()[0]<=0 or self.get_coords()[2]>=self.canvas.winfo_width():
            self.reset_position()
        self.canvas.move(self.ballSprite,self.x_vel,self.y_vel)
    def get_coords(self):
        return self.canvas.coords(self.ballSprite)
    def reset_position(self):
        self.canvas.moveto(self.ballSprite,centre[0] - self.radius, centre[1] - self.radius)
        self.direction = random.choice([1,-1])
        self.x_vel*=self.direction
        self.y_vel*=self.direction


def getWindow(width, height, title):
    """
    :param width:
    :param height:
    :param title:
    :return: A window with a given width, height and title
    """
    window = Tk()
    window.title(title)
    window.geometry("{}x{}".format(width, height))
    return window



def level():
    """
    The level screen
    """
    window = getWindow(resolution[0], resolution[1], "Pong Game")
    canvas = Canvas(window, bg="#FF5733", width=resolution[0], height=resolution[1])
    canvas.create_line(centre[0], 0, centre[0], resolution[1], fill="white")
    bat = Bat(canvas)
    ball = Ball(canvas)
    while True:
        ball.move()
        window.bind("<Key>", bat.move)
        canvas.pack()
        window.update()
        time.sleep(0.01)
    window.mainloop()


if __name__ == '__main__':
    level()
