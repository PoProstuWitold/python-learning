from tkinter import *
import time
import random

class Ball:


    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)

        if(coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0):
            self.xVelocity = -self.xVelocity
        if(coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)


def gen_speed(): return random.randint(0,10)
def gen_size(): return random.randint(10,50)
def gen_coords(): return random.randint(300,699)
def gen_color(): return ('#%06X' % random.randint(0, 0xFFFFFF))

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

number = 5
balls = []
for i in range(int(number)):
    i = Ball(canvas, gen_coords(), gen_coords(), gen_size(), gen_speed(), gen_speed(), gen_color())    # Everything is generated automatically
    balls.append(i)


while True:
    for i in balls:
        i.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
