from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("500x500")

my_canvas =Canvas(root, width=300, height=200, bg="white")
my_canvas.pack()

my_canvas.create_rectangle(50, 150, 250, 50, fill="pink") # top left, bottom right
my_canvas.create_line(0, 100, 300, 100, fill="red")
my_canvas.create_line(150, 0, 150, 200, fill="red")
# my_canvas.create_rectangle(50, 150, 250, 50, fill="pink") # top left, bottom right

my_canvas.create_oval(50, 150, 250, 50, fill="cyan")


root.mainloop()