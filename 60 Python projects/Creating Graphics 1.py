import turtle

# Color palette for the spiral pattern
colors = ['white', 'yellow', 'orange', 'red', 'blue', 'black']

# Create the turtle pen
pen = turtle.Pen()
turtle.bgcolor('purple')

# Draw a colorful spiral pattern
for x in range(2000):
    pen.pencolor(colors[x % 6])
    pen.width(int(x / 100 + 3))
    pen.forward(x)
    pen.left(59)

if __name__ == '__main__':
    # Keep the window open until clicked
    turtle.done()
