from tkinter import *

root = Tk()
root.title("resize")
root.geometry("600x400")

def grab():
    my_label.config(text=my_spin.get())


names = ("Seba", "Ola", "Ada", "Olo")
# my_spin = Spinbox(root, from_=0, to=10, increment=2)
my_spin = Spinbox(root, values=names, increment=2)
my_spin.pack()

my_button = Button(root, text="Sumbit", command=grab)
my_button.pack()

my_label = Label(root, text="")
my_label.pack()

root.mainloop()
