from tkinter import *
from tkinter import ttk
from random import randint
from PIL import ImageTk, Image
import random

root = Tk()
root.title("resize")
root.geometry("400x400")

def math_random():
    global num_1
    global num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    global add_image_1
    global add_image_2
    card1 = "sciezka/" + str(num_1) + ".png"
    card2 = "sciezka/" + str(num_2) + ".png"
    add_image_1 = ImageTk.PhotoImage(Image.open("sciezka"))
    add_image_2 = ImageTk.PhotoImage(Image.open("sciezka"))

    add_1.config(image=card1)
    add_2.config(image=card2)

def answer_add():
    answer = num_1 + num_2
    if int(add_answer.get()) == answer:
        response = "correct"
    else:
        response = "wrong"
    answer_message.config(text=response)
    add_answer.delete(0, "end")
    math_random()

def add():
    hide_all_frames()
    add_frame.pack(fill="both", expand=1)
    add_label = Label(add_frame, text="addition").pack()
    pic_frame = Frame(add_frame, width=400, height=300)
    pic_frame.pack()

    global num_1
    global num_2
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    global add_1
    global add_2
    add_1 = Label(pic_frame)
    add_2 = Label(pic_frame)
    math_sigh = Label(pic_frame, text="+")
    add_1.grid(row=0, column=0)
    math_sigh.grid(row=0, column=1)
    add_2.grid(row=0, column=2)

    global add_image_1
    global add_image_2
    card1 = "sciezka/" + str(num_1) + ".png"
    card2 = "sciezka/" + str(num_2) + ".png"
    add_image_1 = ImageTk.PhotoImage(Image.open("sciezka"))
    add_image_2 = ImageTk.PhotoImage(Image.open("sciezka"))

    add_1.config(image=card1)
    add_2.config(image=card2)

    global add_answer
    add_answer = Entry(add_frame)
    add_answer.pack()

    add_answer_button = Button(add_frame, text="answer", command=answer_add)
    add_answer_button.pack()

    global answer_message
    answer_message = Label(add_frame, text="")
    answer_message.pack()


def random_state():
    global our_states
    global rando
    our_states = ["california", "florida", "texas"]
    rando = randint(0, len(our_states) - 1)
    state = "states/" + our_states[rando] + ".png"
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_img, bg="white")

def state_capital_answer():
    if capital_radio.get() == our_states_capitals[answer]:
        response = "Correct" + our_states_capitals[answer].title() + " ... " + answer.title()
    else:
        response = "Incorrect" + our_states_capitals[answer].title() + " ... " + answer.title()
    answer_label_capitals.config(text=response)




def state_answer():
    answer = answer_input.get()
    answer = answer.replace(" ", "")
    if answer.lower() == our_states[rando]:
        reponse = "correct" + our_states[rando].title()
    else:
        response = "incorrect" + our_states[rando].title()
    answer_label.config(text=response)
    answer_input.delete(0, "end")
    random_state()

def states():
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    # my_label = Label(state_frame, text="states").pack()

    global show_state
    show_state = Label(state_frame)
    show_state.pack()

    global answer_input
    answer_input = Entry(state_frame)
    answer_input.pack()

    rando_button = Button(state_frame, text="pass", command=states)
    rando_button.pack()

    answer_button = Button(state_frame, text="answer", command=state_answer)
    answer_button.pack()

    global answer_label
    answer_label = Label(state_frame, text="", bg="white" )
    answer_label.pack()

def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)
    # my_label = Label(state_capitals_frame, text="capitals").pack()
    global show_state
    show_state = Label(state_capitals_frame)
    show_state.pack()

    global our_states
    our_states = ["california", "florida", "texas"]

    global our_states_capitals
    our_states_capitals = {
        "california": "cap_c",
        "florida": "cap_f",
        "texas": "cap_t"
    }

    # global rando
    # rando = randint(0, len(our_states) - 1)
    # answer = our_states[rando]
    answer_list = []
    count = 1
    global answer


    while count < 4:
        rando = randint(0, len(our_states) - 1)
        if count == 1:
            answer = our_states[rando]
            global state_img
            state = "states/" + our_states[rando] + ".png"
            state_img =ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_img)
        answer_list.append(our_states[rando])
        our_states.remove(our_states[rando])
        random.shuffle(our_states)
        count += 1
    random.shuffle(answer_list)

    global capital_radio
    capital_radio = StringVar()
    capital_radio.set(our_states_capitals[answer_list[0]])
    capital_radio_button1 = Radiobutton(state_capitals_frame, text=our_states_capitals[answer_list[0]].title(), variable=capital_radio, value=our_states_capitals[answer_list[0]]).pack()
    capital_radio_button2 = Radiobutton(state_capitals_frame, text=our_states_capitals[answer_list[1]].title(), variable=capital_radio, value=our_states_capitals[answer_list[1]]).pack()
    capital_radio_button3 = Radiobutton(state_capitals_frame, text=our_states_capitals[answer_list[2]].title(), variable=capital_radio, value=our_states_capitals[answer_list[2]]).pack()

    pass_button = Button(state_capitals_frame, text="Pass", command=state_capitals)
    pass_button.pack()

    capital_answer_button = Button(state_capitals_frame, text="Answer", command=state_capital_answer)
    capital_answer_button.pack()

    global answer_label_capitals
    answer_label_capitals = Label(state_capitals_frame, text="")
    answer_label_capitals.pack()


def hide_all_frames():
    for widget in state_frame.winfo_children():
        widget.destroy()
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    for widget in add_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()
    add_frame.pack_forget()


my_menu = Menu(root)
root.config(menu=my_menu)

states_menu = Menu(my_menu)
my_menu.add_cascade(label="geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="state capitals", command=state_capitals)
states_menu.add_command(label="Exit", command=root.quit)

math_menu = Menu(my_menu)
my_menu.add_cascade(label="math", menu=math_menu)
math_menu.add_command(label="addition", command=add)


state_frame = Frame(root, width=500, height=500, bg="white")
state_capitals_frame = Frame(root, width=500, height=500)
add_frame = Frame(root, width=500, height=500)

root.mainloop()