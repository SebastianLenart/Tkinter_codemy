from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

def selected(event):
    myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == "Monday":
        # jakis label czy cos innego
        pass

def comboclick(event):
    myLabel = Label(root, text=myCombo.get()).pack()


options = [
    "Monday",
    "Truesday",
    "Wednesday",
    "Thursday"
]
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack()

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()


# mybutton = Button(root, text="select from list", command=selected)
# mybutton.pack()


root.mainloop()