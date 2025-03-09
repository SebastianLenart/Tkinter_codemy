import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("600x400")

def resize():
    w = width_entry.get()
    h = 300
    root.geometry(f"{w}x{h}")
    # root.geometry("{width}x{height}".format(width=w, height=h))
    # root.geometry("%ix%i" % (w, h))


width_label = Label(root, text="width:")
width_label.pack()
width_entry = Entry(root)
width_entry.pack()

my_button = Button(root, text="resize", command=resize)
my_button.pack()


root.mainloop()