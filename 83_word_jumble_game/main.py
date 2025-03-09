import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice, shuffle


root = Tk()
root.title("resize")
root.geometry("600x400")

my_label = Label(root, text="")
my_label.pack()

def shuffler():
    entry_answer.delete(0, END)
    answer_label.config(text="")
    states = ["Washington", "Oregon", "California", "Ohio"]
    global word
    word = choice(states)
    break_apart_word = list(word)
    shuffle(break_apart_word)
    global shuffled_word
    shuffled_word = ""
    for letter in break_apart_word:
        shuffled_word += letter
    my_label.config(text=shuffled_word)

def answer():
    if word == entry_answer.get():
        answer_label.config(text="correct")
    else:
        answer_label.config(text="incorrect")

entry_answer = Entry(root)
entry_answer.pack()

button_frame = Frame(root)
button_frame.pack()

my_button = Button(button_frame, text="pick another word", command=shuffler)
my_button.grid(row=0, column=0)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=1)


answer_label = Label(root, text="")
answer_label.pack()


shuffler()

root.mainloop()