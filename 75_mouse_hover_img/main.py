from tkinter import *


root = Tk()
root.title("resize")
root.geometry("600x400")

def change(e):
    my_pic = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/75_mouse_hover_img/img2.png")
    my_label.config(image=my_pic)
    my_label.image = my_pic

def change_back(e):
    my_pic = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/75_mouse_hover_img/img.png")
    my_label.config(image=my_pic)
    my_label.image = my_pic

my_pic = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/75_mouse_hover_img/img.png")
my_label = Label(root, image=my_pic)
# my_label = Button(root, image=my_pic) # moze byc button
my_label.pack()

my_label.bind("<Enter>", change) # po najechaniu myszka
my_label.bind("<Leave>", change_back) # po usunieciu kursora z obszaru obrazka

root.mainloop()