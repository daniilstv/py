import turtle


turtle.circle(20)

answer = ''
#while answer != 'N':
#    answer = turtle.textinput("Нарисовать ?", "Y/N")

r = 200
x = 0
y = 0 - r / 2

        gotoxy(x, y)
        turtle.fillcolor('red')

        turtle.circle(r)
        turtle.end_fill()

        turtle.color('white')

        phi = math.pi * 2 / 5
        for i in range(1,6):
            xi = math.sin(math.pi + phi*i*2)*r-x
            yi = math.cos(math.pi + phi*i*2)*r-y

            turtle.goto(xi, yi)