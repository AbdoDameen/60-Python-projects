import turtle as tu


def main():
    """Draw a colorful fractal tree pattern using turtle graphics."""
    roo = tu.Turtle()
    wn = tu.Screen()
    wn.bgcolor("purple")
    wn.title("Fractal Tree Pattern")
    roo.left(90)
    roo.speed(20)

    # Define the branches to draw: (color, pensize, scale_factor, initial_length, angle_before)
    branches = [
        ("yellow", 2, 3 / 4, 20, 0),
        ("magenta", 2, 3 / 4, 20, 90),
        ("red", 2, 3 / 4, 20, 180),
        ("#FFF8DC", 2, 3 / 4, 20, 270),
        ("lightgreen", 3, 4 / 5, 40, 0),
        ("red", 3, 4 / 5, 40, 90),
        ("yellow", 3, 4 / 5, 40, 180),
        ("#FFF8DC", 3, 4 / 5, 40, 270),
        ("cyan", 2, 6 / 7, 60, 0),
        ("yellow", 2, 6 / 7, 60, 90),
        ("magenta", 2, 6 / 7, 60, 180),
        ("#FFF8DC", 2, 6 / 7, 60, 270),
    ]

    def draw_branch(length: float, pensize: int, color: str, scale_factor: float):
        """Recursively draw a fractal tree branch."""
        if length < 10:
            return
        roo.pensize(pensize)
        roo.pencolor(color)
        roo.forward(length)
        roo.left(30)
        draw_branch(scale_factor * length, pensize, color, scale_factor)
        roo.right(60)
        draw_branch(scale_factor * length, pensize, color, scale_factor)
        roo.left(30)
        roo.backward(length)

    for color, pensize, scale, length, angle in branches:
        roo.speed(2000)
        roo.setheading(90)  # Reset to pointing up
        roo.left(angle)     # Rotate to the desired angle
        draw_branch(length, pensize, color, scale)

    wn.exitonclick()


if __name__ == '__main__':
    main()
