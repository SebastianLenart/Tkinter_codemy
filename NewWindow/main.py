from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com Image Viewer")


def open():
    top = Toplevel()
    top.title("top")
    lbl = Label(top, text="     sth      ").pack()
    # jak chcemy wyswietlic obraz to musmy zadeklarowac zmienna jako global!
    bnt2 = Button(top, text="exit", command=top.destroy).pack()

btn = Button(root, text="open window", command=open).pack()

root.mainloop()

