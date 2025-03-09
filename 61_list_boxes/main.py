from tkinter import *
from tkinter import ttk

root = Tk()
root.title("resize")
root.geometry("400x400")

my_frame = Frame(root)
my_scroll = Scrollbar(my_frame, orient=VERTICAL)

# selectmode = SINGLE, BROWSE (przesuwac), MULTIPLE, EXTENDED (trzymac shift)
my_listbox = Listbox(my_frame, width=50, yscrollcommand=my_scroll.set, selectmode=MULTIPLE) # mozna pare na raz wybrac
my_scroll.config(command=my_listbox.yview)
my_scroll.pack(side=RIGHT, fill=Y)
my_frame.pack()

my_listbox.pack()

my_listbox.insert(END, "this is item")
my_listbox.insert(0, "this is item2")

my_list = ["one", "two", "three"]

for item in my_list:
    my_listbox.insert(END, item)

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text="")

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0, END)

def select_all():
    result = ""
    for item in my_listbox.curselection():
        result  = result + str(my_listbox.get(item)) + "\n"
    # print(my_listbox.curselection())
    # my_label.config(text=my_listbox.get(result))
    my_label.config(text=result)

def delete_mutlitple():
    for item in reversed(my_listbox.curselection()): # bo po kazdym delete lista sie zmienia, dlatego trzeba reversed
        my_listbox.delete(item)

my_button = Button(root, text="delete", command=delete)
my_button.pack()

my_button2 = Button(root, text="select", command=select)
my_button2.pack()

global my_label
my_label = Label(root, text="")
my_label.pack()

my_button3 = Button(root, text="delete all", command=delete_all)
my_button3.pack()

my_button4 = Button(root, text="select all", command=select_all)
my_button4.pack()

my_button5 = Button(root, text="delete mutlitple", command=delete_mutlitple)
my_button5.pack()



root.mainloop()