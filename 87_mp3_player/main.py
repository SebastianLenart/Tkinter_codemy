import time
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from random import choice, shuffle
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("resize")
root.geometry("600x400")

pygame.mixer.init()

def play_time():
    if stopped:
        return
    current_time = pygame.mixer.music.get_pos() / 1000
    # slider_label.config(text=f"Slider: {int(my_slider.get())} and Song Pos: {int(current_time)}")
    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))


    # current_one = song_box.curselection()
    song = song_box.get(ACTIVE)
    song = f"/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/{song}.mp3"
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length
    converted_song_length = time.strftime('%H:%M:%S', time.gmtime(song_length))
    current_time += 1
    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f"time Elapsed: {converted_song_length}")
    elif paused:
        pass
    elif int(my_slider.get()) == int(current_time):
        # slider hasnt been moved
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(current_time))
    else:
        # slider has been moved
        slider_position = int(song_length)
        my_slider.config(to=slider_position, value=int(my_slider.get()))
        converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(my_slider.get())))
        status_bar.config(text=f"time Elapsed: {converted_current_time} of {converted_song_length}")
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)

    # status_bar.config(text=f"time Elapsed: {converted_current_time} of {converted_song_length}")
    #     my_slider.config(value=int(current_time))
    #     slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=int(current_time))
    status_bar.after(1000, play_time) # update every 1 s


def add_song():
    song = filedialog.askopenfilename(initialdir="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player", title="choose a song",
                                      filetypes=(("mp3 Files", "*.mp3"),))
    # strip out the directory info and .mp3 extension grom the song
    song = song.replace("/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/", "")
    song = song.replace(".mp3", "")
    song_box.insert(END, song)

def play():
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f"/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()
    # slider_position = int(song_length)
    # my_slider.config(to=slider_position, value=0)

    # current_volume = pygame.mixer.music.get_volume()
    # slider_label.config(text=current_volume * 100)

    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100  # bo mamy zakres 0-1 czyli float
    # slider_label.config(text=current_volume * 100)
    # picture:
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    # etc ..

global stopped
stopped = False
def stop():
    status_bar.config(text="")
    my_slider.config(value=0)

    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    status_bar.config(text="")

    global stopped
    stopped = True

def next_song():
    status_bar.config(text="")
    my_slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0] + 1 # [0] bo tuple
    song = song_box.get(next_one)
    song = f"/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.select_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last=None)

def previous_song():
    status_bar.config(text="")
    my_slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0] - 1 # [0] bo tuple
    song = song_box.get(next_one)
    song = f"/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.select_clear(0, END)
    song_box.activate(next_one)
    song_box.select_set(next_one, last=None)

def delete_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()

global paused
paused = False

def pause(is_pause):
    global paused
    paused = is_pause

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player",
                                     title="choose a song",
                                     filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace("/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/", "")
        song = song.replace(".mp3", "")
        song_box.insert(END, song)

def slide(x):
    # song_length = 0 # dla testow bo nie mam utworow !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # slider_label.config(text=f"{int(my_slider.get())} of {int(song_length)}")
    song = song_box.get(ACTIVE)
    song = f"/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    current_volume = pygame.mixer.music.get_volume()
    current_volume = current_volume * 100 # bo mamy zakres 0-1 czyli float
    # slider_label.config(text=current_volume * 100)
    # picture:
    if int(current_volume) < 1:
        volume_meter.config(image=vol0)
    elif int(current_volume) > 0 and int(current_volume) <= 25:
        volume_meter.config(image=vol1)
    # etc ..


master_frame = Frame(root)
master_frame.pack()

song_box = Listbox(master_frame, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="black")
song_box.grid(row=0, column=0)

back_btn_img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/back.png")
forward_btn_img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/forward.png")
play_btn_img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/play.png")
pause_btn_img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/pause.png")
stop_btn_img = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/stop.png")


controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)

volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=20)

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0,command=stop)
back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=add_song_menu)
add_song_menu.add_command(label="add one song to playlist", command=add_song)
add_song_menu.add_command(label="add many songs to playlist", command=add_many_songs)
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove songs", menu=remove_song_menu)
remove_song_menu.add_command(label="delete a song from playlist", command=delete_song)
remove_song_menu.add_command(label="delete songs from playlist", command=delete_all_songs)

# define volume images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/stop.png") # powinny byc inne png ale nie bede robic
vol1 = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/stop.png")# powinny byc inne png ale nie bede robic
vol2 = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/stop.png")# powinny byc inne png ale nie bede robic
vol3 = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/stop.png")# powinny byc inne png ale nie bede robic
vol4 = PhotoImage(file="/home/sebastian/GitHub/Tkinter_codemy/87_mp3_player/stop.png")# powinny byc inne png ale nie bede robic

status_bar = Label(root, text="", bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0)

volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
volume_slider.pack(pady=10)

volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1)

# slider_label = Label(root, text="0")
# slider_label.pack()

root.mainloop()
