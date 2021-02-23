import turtle


d_len = 100

turtle.bgcolor('light sky blue')
turtle.showturtle()
turtle.hideturtle()
turtle.fillcolor('white')

turtle.begin_fill()
turtle.left(45)
turtle.forward(d_len)
turtle.right(90)
turtle.forward(d_len)
turtle.right(90)
turtle.forward(d_len)
turtle.right(90)
turtle.forward(2 * d_len)
turtle.left(90)
turtle.forward(d_len)
turtle.left(90)
turtle.forward(d_len)
turtle.left(90)
turtle.forward(d_len)

turtle.end_fill()

turtle.done()
