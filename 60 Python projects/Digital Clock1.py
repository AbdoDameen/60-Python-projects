"""Display a live digital clock using tkinter."""

from tkinter import *
from tkinter import font
import time

# Create the main application window
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(True, True)

# Styling configuration
text_font = ("Boulder", 70, "bold")
background = "orange"
foreground = "blue"
border_width = 255

# Create the clock label
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=0)


def digital_clock() -> None:
    """Update the label with the current time every 200ms."""
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


if __name__ == '__main__':
    digital_clock()
    app_window.mainloop()
