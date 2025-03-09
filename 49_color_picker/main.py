from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

root = Tk()
root.title("resize")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()[1] # bo to jest lista (2 pozycje w liscie)
    my_color2 = colorchooser.askcolor()[0][2] # bo to jest lista (2 pozycje w liscie)
    my_label = Label(root, text=my_color).pack()
    my_label2 = Label(root, text = "you pick", font=("Helvetica", 32), bg=my_color).pack()

my_button = Button(root, text="Pick a color", command=color).pack()

root.mainloop()