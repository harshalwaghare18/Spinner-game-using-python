from turtle import *
from tkinter import *
state = {'turn':0}
def spinner():
    clear()
    angle =state['turn']/10
    right(angle)
    forward(100)
    dot(120,'red')
    back(100)
    right(120)
    forward(100)
    dot(120,'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()


def animate():
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick():
    state['turn']+= 40

setup(420,420,370,0)
hideturtle()
tracer(False)
bgcolor('black')
width(20)
color('orange')
onkey(flick,'space')
listen()
animate()
done()