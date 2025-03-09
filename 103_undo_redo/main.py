from email.contentmanager import get_text_content
from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("resize")
root.geometry("600x700")

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
    name = text_file
    name = name.replace("/home/sebastian/GitHub/Tkinter_codemy/100_RW_textfile/", "")
    name = name.replace(".txt", "")
    text_file = open(text_file, "r")
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    root.title(f"{name} - Textpad")

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

def select():
    selected = my_text.selection_get()
    my_label.config(text=selected)


# trudene do, pomieszane strasznie !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def bolder():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")
    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")



my_frame = Frame(root)
my_frame.pack()

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=60, height=20, selectbackground="yellow", selectforeground="black", yscrollcommand=text_scroll.set, undo=True)
my_text.pack()

text_scroll.config(command=my_text.yview)

open_button = Button(root, text="open text file", command=open_txt)
open_button.pack()

save_button = Button(root, text="save", command=save)
save_button.pack()

image_button = Button(root, text="add image", command=add_img)
image_button.pack()

select_button = Button(root, text="Select text", command=select)
select_button.pack()

bold_button = Button(root, text="bold", command=bolder)
bold_button.pack()

italics_button = Button(root, text="italics", command=italics)
italics_button.pack()

redo_button = Button(root, text="redo", command=my_text.edit_redo)
redo_button.pack()

undo_button = Button(root, text="undo", command=my_text.edit_undo)
undo_button.pack()


my_label = Label(root, text="")
my_label.pack()


root.mainloop()
