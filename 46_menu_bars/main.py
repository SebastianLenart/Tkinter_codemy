from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    return


# create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="new..", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="exit..", command=root.quit)

# create an edit item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="edit", menu=edit_menu)
edit_menu.add_command(label="cut", command=our_command)
edit_menu.add_command(label="copy", command=our_command)

# create an options item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="options", menu=option_menu)
option_menu.add_command(label="find", command=our_command)
option_menu.add_command(label="find2", command=our_command)


root.mainloop()