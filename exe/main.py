from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com Image Viewer")
root.geometry("400x400")

"""
pip3 install pyinstaller
pyinstaller.exe --onefile --icon=sciezka_do_png main.py


"""






# r = IntVar()
# r.set("2")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")
for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="option1", variable=r , value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="option2", variable=r , value=2, command=lambda: clicked(r.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="click", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()