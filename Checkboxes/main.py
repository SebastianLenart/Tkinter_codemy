from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("sliders")
root.geometry("400x400")

var = StringVar()

c = Checkbutton(root, text="Check", variable=var, onvalue="On", offvalue="off")
c.deselect() # default
c.pack()

def show():
    my_label = Label(root, text=var.get()).pack()


myButton = Button(root, text="show", command=show).pack()


root,mainloop()