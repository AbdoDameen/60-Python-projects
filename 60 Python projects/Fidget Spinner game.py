"""A simple fidget spinner game using turtle graphics.
Press the spacebar to spin the fidget spinner."""

from turtle import *

# Track the spinner's rotation state
state = {"turn": 0}


def spinner() -> None:
    """Draw the fidget spinner at the current angle."""
    clear()
    angle = state["turn"] / 10
    right(angle)
    forward(100)
    dot(120, "red")
    back(100)
    right(120)
    forward(100)
    dot(120, "green")
    back(100)
    right(120)
    forward(100)
    dot(120, "blue")
    back(100)
    right(120)
    update()


def animate() -> None:
    """Decelerate the spinner and redraw it every 20ms."""
    if state["turn"] > 0:
        state["turn"] -= 1

    spinner()
    ontimer(animate, 20)


def flick() -> None:
    """Increase the spinner speed (called on spacebar press)."""
    state["turn"] += 10


if __name__ == "__main__":
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    width(20)
    onkey(flick, "space")
    listen()
    animate()
    done()
