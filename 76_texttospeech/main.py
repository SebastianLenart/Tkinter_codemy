from tkinter import *
import pyttsx3

root = Tk()
root.title("resize")
root.geometry("600x400")

####### instal pyttsx3

def talk():
    engine = pyttsx3.init()
    # engine.setProperty("rate", 125)
    engine.say(my_entry.get())
    engine.runAndWait()
    my_entry.delete(0, END)

my_entry = Entry(root)
my_entry.pack()

my_button = Button(root, text="speak", command=talk)
my_button.pack()

root.mainloop()