from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("700x500")


def number():
    try:
        int(my_box.get())
        answer.config(text="that is nr")
    except ValueError:
        answer.config(text="that is NOT nr")



my_label = Label(root, text="Enter nr")
my_label.pack()

my_box = Entry(root)
my_box.pack()

my_button = Button(root, text="enter nr", command=number)
my_button.pack()

answer = Label(root, text="")
answer.pack()

root.mainloop()