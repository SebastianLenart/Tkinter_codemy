from email.contentmanager import get_text_content
from tkinter import *

root = Tk()
root.title("resize")
root.geometry("600x400")

def clear():
    my_text.delete(1.0, END) # roznica !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def get_text():
    my_label.config(text=my_text.get(1.0, END))

my_text = Text(root, width=60, height=20)
my_text.pack()

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text="clear", command=clear)
clear_button.grid(row=0, column=0)

get_text_button = Button(button_frame, text="get text", command=get_text)
get_text_button.grid(row=0, column=1)

my_label = Label(root, text="")
my_label.pack()

root.mainloop()
