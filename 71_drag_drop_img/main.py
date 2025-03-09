from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("800x600")

w = 600
h = 400
x = w//2
y = h//2

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack()

img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/71_drag_drop_img/img.png")
my_img = my_canvas.create_image(260, 125, anchor=NW, image=img)

def move(e):
    global img
    img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/71_drag_drop_img/img.png")
    my_img = my_canvas.create_image(e.x, e.y, image=img) # usunieto nchor=NW bo lapalo w lewym gornym rogu, a tera nie
    my_label.config(text="coordinates: x=" + str(e.x) + " , y=" + str(e.y))


my_label = Label(root, text="")
my_label.pack()

my_canvas.bind("<B1-Motion>", move) # wcisniety przycisk, to specjalna komenda B1-motion...

root.mainloop()