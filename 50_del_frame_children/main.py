from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    return

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill="both", expand=1)
    myLabel = Label(file_new_frame, text="FILE").pack()

def edit_cut():
    hide_all_frames()
    edit_cut_frame.pack(fill="both", expand=1)
    myLabel = Label(edit_cut_frame, text="CUT").pack()

    child_label = Label(edit_cut_frame, text=edit_cut_frame.winfo_children())
    child_label.pack()


# hide all frames
def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()
    for widget in edit_cut_frame.winfo_children():
        widget.destroy()
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()


# create a menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="new..", command=file_new)
file_menu.add_separator()
file_menu.add_command(label="exit..", command=root.quit)

# create an edit item
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="edit", menu=edit_menu)
edit_menu.add_command(label="cut", command=edit_cut)
edit_menu.add_command(label="copy", command=our_command)

# create an options item
option_menu = Menu(my_menu)
my_menu.add_cascade(label="options", menu=option_menu)
option_menu.add_command(label="find", command=our_command)
option_menu.add_command(label="find2", command=our_command)

# create some frames
file_new_frame = Frame(root, width=400, height=400, bg="red")
edit_cut_frame = Frame(root, width=400, height=400, bg="blue")



root.mainloop()