import turtle
#  t = turtle.Turtle()
import random
import math

import py

PHI = 360 / 7
R = 50

def gotoxy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def circle(r,col):
    turtle.fillcolor(col)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def drum(x,y):
    gotoxy(x,y)
    turtle.circle(80)
    gotoxy(x,160 + y)
    circle(5,'red')
    for i in range(0,7):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad)* R + x, math.cos(phi_rad)* R + 60 + y) 
        circle(21,'white')
    return(x,y)

def rotate(x,y,start):
    for i in range(start, random.randrange(7,49)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(math.sin(phi_rad)* R + x, math.cos(phi_rad)* R + 60 + y) 
        circle(21,'brown')
        circle(21,'white')
    return i % 7

start = 0
answer = 'y'    
turtle.speed(0)

drum(22,32)

        
while answer != 'n':

    answer = turtle.textinput("Сыграем ?", "y/n")
    if answer == 'y':

        gotoxy(-50,250)
        turtle.write('              ', font=('Helvetica',16,'normal'))

        start = rotate(22,32,start)
        
        if start == 0:
            gotoxy(-50,250)
            turtle.write('Бах! Ты убит!', font=('Helvetica',16,'normal'))
            
            if random.randint(1,2) == 1: 
                py.del_rnd('tst')
                print('Удален случайный файл')
            else:
                py.dupl_all('tst')
                print('Файлы дублированы')

    else:
        pass

