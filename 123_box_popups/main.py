from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("resize")
root.geometry("300x300")

# messagebox.showinfo("showinfo", "Information")

def choose(optopn):
    pop.destroy()
    if optopn == "yes":
        my_label.config(text="YES")
    else:
        my_label.config(text="NO")

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("popup")
    pop.geometry("250x250")
    pop.config(bg="green")

    global me
    me = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/123_box_popups/pause.png")
    pop_label = Label(pop, text="something", bg="green", fg="white")
    pop_label.pack()

    my_frame = Frame(pop, bg="green")
    my_frame.pack()

    me_pic = Label(my_frame, image=me, borderwidth=0)
    me_pic.grid(row=0, column=0)

    yes = Button(my_frame, text="YES", command=lambda: choose("yes"), bg="orange")
    yes.grid(row=0, column=1)

    no = Button(my_frame, text="NO", command=lambda: choose("no"), bg="yellow")
    no.grid(row=0, column=2)


my_button = Button(root, text="Click me", command=clicker)
my_button.pack()

my_label = Label(root, text="")
my_label.pack()

root.mainloop()
