from tkinter import *
from tkinter import ttk

from PIL.ImageOps import expand
from tkcalendar import *


root = Tk()
root.title("resize")
root.geometry("600x400")

############# install tkcalendar

cal = Calendar(root, selectmode="day", year=2020, month=5, day=22)
cal.pack(fill="both", expand=True)

def grab_date():
    my_label.config(text=cal.get_date())


my_button = Button(root, text="get date", command=grab_date)
my_button.pack()

my_label = Label(root, text="")
my_label.pack()

root.mainloop()