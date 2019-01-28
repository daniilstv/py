import turtle
#  t = turtle.Turtle()
import random
import math


def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def circle(r,col):
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

answer = 'y'    
while answer != 'n':

    answer = turtle.textinput("Сыграем ?", "y/n")
    if answer == 'y':
        
        turtle.speed(40)

        gotoxy(0,0)
        turtle.circle(80)

        gotoxy(0,160)
        circle(5,'red')

        phi = 360 / 7
        r = 50



        for i in range(0,7):
            phi_rad = phi * i * math.pi / 180.0
            gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60) 
            circle(21,'brown')
            circle(21,'white')


        gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r + 60) 

        circle(21,'brown')
        

    else:
        pass

