import turtle
#colors=['red', 'purple', 'blue', 'green', 'orange', 'yellow']
colors=['white', 'yellow', 'orange', 'red', 'blue', 'black']
t=turtle.Pen()

turtle.bgcolor('purple')
for x in range(2000):
    t.pencolor(colors[x%6])
    t.width(x/100+3)
    t.forward(x)
    t.left(59)
