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

def add_img():
    global my_image
    my_image = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/101_img_textbox/img.png")
    position = my_text.index(INSERT)
    my_text.image_create(position, image=my_image)
    my_label.config(text=position)

my_frame = Frame(root)
my_frame.pack()

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=60, height=20, selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)

open_button = Button(root, text="open text file", command=open_txt)
open_button.pack()

save_button = Button(root, text="save", command=save)
save_button.pack()

image_button = Button(root, text="add image", command=add_img)
image_button.pack()

my_label = Label(root, text="")
my_label.pack()


root.mainloop()
