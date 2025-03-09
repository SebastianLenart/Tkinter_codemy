import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("600x400")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock) # SPRYTNEEEE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def update():
    my_label.config(text="New Text")

my_label = Label(root, text="")
my_label.pack()

clock()

# my_label.after(5000, update)

root.mainloop()