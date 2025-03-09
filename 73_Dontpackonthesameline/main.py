from tkinter import *
from tkinter import ttk

from PIL.ImageOps import expand
from tkcalendar import *

from Image_9.main import my_label

root = Tk()
root.title("resize")
root.geometry("600x400")
def grab():
    my_label.config(text=my_box.get())
my_box = Entry(root)
my_box.pack()

my_button = Button(root, text="grab", command=grab)
my_button.pack()

my_label = Label(root, text="")
my_label.pack()


"""

zawsze .pack() dawac w kolejnej linijce !!!

"""
root.mainloop()