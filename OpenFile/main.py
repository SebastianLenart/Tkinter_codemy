from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Codemy.com Image Viewer")

# root.filename = filedialog.askopenfilename(initialdir="/home/sebastian/GitHub/Tkinter_codemy/Image_9",
#                                            title="select a file",
#                                            filetypes=(("png files", "*.png"), ("all files", ".*")))
#
# my_label = Label(root, text=root.filename).pack()
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image).pack()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/home/sebastian/GitHub/Tkinter_codemy/Image_9",
                                               title="select a file",
                                               filetypes=(("png files", "*.png"), ("all files", ".*")))

    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop()
