from email.contentmanager import get_text_content
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("resize")
root.geometry("600x400")

"""
read only r
read and write r+ (beginning of file)
write anly w (over-written)
write and read w+ (over written)
append anly a (end of file)
append and read a+ (and of file)

"""


def open_txt():
    text_file = filedialog.askopenfilename(initialdir="/home/sebastian/GitHub/Tkinter_codemy/100_RW_textfile",
                                           title="open text file",
                                           filetypes=(("Text Files", "*.txt"),))


    text_file = open(text_file, "r")
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def save():
    text_file = filedialog.askopenfilename(initialdir="/home/sebastian/GitHub/Tkinter_codemy/100_RW_textfile",
                                           title="open text file",
                                           filetypes=(("Text Files", "*.txt"),))
    text_file = open(text_file, "w")
    text_file.write(my_text.get(1.0, END))

my_text = Text(root, width=60, height=20)
my_text.pack()

button_frame = Frame(root)
button_frame.pack()

open_button = Button(button_frame, text="open text file", command=open_txt)
open_button.grid(row=0, column=0)

save_button = Button(button_frame, text="save", command=save)
save_button.grid(row=0, column=1)



root.mainloop()
