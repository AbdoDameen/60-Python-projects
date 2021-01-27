from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import Label
import time
import datetime


app_window  = TK()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font=("Boulder", 70, 'bold')
background="orange"
forground="blue"
border_width=255

label=Label(app_window, font=text_font, bg=background, fg=forground, bd=border_width)
label.grid(row=0, column=0)

def digital_clock():
    time_live=time.strftime("%H:%M,%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()
