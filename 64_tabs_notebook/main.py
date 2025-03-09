from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame2, text="red tab")

def select():
    my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="blue")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="red")
my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="blue tab")
my_notebook.add(my_frame2, text="red tab")

my_button = Button(my_frame1, text="hide tab 2", command=hide).pack()
my_button2 = Button(my_frame1, text="show tab 2", command=show).pack()
my_button3 = Button(my_frame1, text="navigate to tab 2", command=select).pack()



root.mainloop()