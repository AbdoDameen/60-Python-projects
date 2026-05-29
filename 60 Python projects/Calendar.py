"""
Calendar application.
Displays a calendar for a given year using Tkinter.
"""

from tkinter import Tk, Toplevel, Label, Entry, Button
import calendar


def show_calendar():
    """Create a new window to display the calendar for the entered year."""
    year = int(year_field.get())
    new_window = Toplevel()
    new_window.config(background='grey')
    new_window.title("Calendar for the year")
    new_window.geometry('600x750')

    calendar_content = calendar.calendar(year)
    cal_label = Label(new_window, text=calendar_content, font='Consolas 10 bold')
    cal_label.grid(row=0, column=0, padx=20)


def main():
    """Create the main window with input fields and calendar button."""
    global year_field
    main_window = Tk()
    main_window.config(background='grey')
    main_window.title('Calendar')
    main_window.geometry('260x150')

    title_label = Label(main_window, text='Calendar', bg='grey', font=('times', 28, 'bold'))
    year_label = Label(main_window, text='Enter Year', bg='red')
    year_field = Entry(main_window)
    show_button = Button(
        main_window, text="Show Calendar", fg='Black', bg='Blue', command=show_calendar
    )

    title_label.grid(row=0, column=0)
    year_label.grid(row=1, column=0)
    year_field.grid(row=2, column=0)
    show_button.grid(row=3, column=0)

    main_window.mainloop()


if __name__ == '__main__':
    main()
