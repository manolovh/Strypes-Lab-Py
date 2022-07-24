from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import pygame
import time
from mutagen.mp3 import MP3
import lyricsgenius

root = Tk()
root.title('MP3 PLAYER')
root.geometry('580x570')

pygame.mixer.init()

car_playlist = []
home_playlist = []
temporary_playlist = []

# Load playlist data in memory
with open('car_playlist.txt', 'r') as car_pl:
    for song in car_pl.readlines():
        song = song.rstrip('\n')
        car_playlist.append(song)

with open('home_playlist.txt', 'r') as home_pl:
    for song in home_pl.readlines():
        song = song.rstrip('\n')
        home_playlist.append(song)

with open('temporary_playlist.txt', 'r') as temp_pl:
    for song in temp_pl.readlines():
        song = song.rstrip('\n')
        temporary_playlist.append(song)

# Main functions
def add_songs():
    songs = filedialog.askopenfilenames(initialdir='C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles',
                                       title='Choose a song: ')
    for song in songs:
        # strip extra path and extension info
        song = song.replace('C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles/', '')
        song = song.replace('.mp3', '')
        playlist_box.insert(END, song)

def delete_song():
    playlist_box.delete(ANCHOR)

def clear_current_playlist():
    playlist_box.delete(0, END)

def play_song():
    status_label.config(text='')
    song_slider.config(value=0)
    global stopped
    stopped = False

    song_ = playlist_box.get(ACTIVE)
    # get the entire path of the song to play it
    song = f"C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles/{song_}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    get_time()

    # Display song lyrics
    song_info = song_.split(' - ')
    artist = str(song_info[0])
    title = str(song_info[1])

    acces_token = "TSTneJtAfZ5xkdvVurePl2SMokIcixtCfiEAlCwoefrR-m20GOmEBSBglbQCDGZv"

    genius = lyricsgenius.Genius(acces_token)
    song_lyrics = genius.search_song(artist, title)
    lyric = song_lyrics.lyrics

    lyrics_tab.delete('1.0', 'end')
    lyrics_tab.insert(END, lyric)

stopped = False
def stop_song():
    pygame.mixer.music.stop()
    playlist_box.select_clear(ACTIVE)

    status_label.config(text='')
    song_slider.config(value=0)

    global stopped
    stopped = True
    global paused
    paused = False

    lyrics_tab.delete('1.0', 'end')

paused = False
def pause_song(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def go_forward():
    status_label.config(text='')
    song_slider.config(value=0)

    next_song = playlist_box.curselection()
    # get the first item from the returned tuple and add 1 to it to receive the next song index
    next_song = next_song[0] + 1
    # get the song name from the index
    song = playlist_box.get(next_song)
    # add the whole path to it
    song = f"C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # change the selected song field
    playlist_box.select_clear(0, END)
    playlist_box.activate(next_song)
    playlist_box.selection_set(next_song)


def go_backward():
    status_label.config(text='')
    song_slider.config(value=0)

    previous_song = playlist_box.curselection()
    # get the first item from the returned tuple and add 1 to it to receive the previous song index
    previous_song = previous_song[0] - 1
    # get the song name from the index
    song = playlist_box.get(previous_song)
    # add the whole path to it
    song = f"C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles/{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # change the selected song field
    playlist_box.select_clear(0, END)
    playlist_box.activate(previous_song)
    playlist_box.selection_set(previous_song)

def double_click_play(event):
    play_song()

# PLAYLIST FUNCTIONS
def add_to_car():
    song = playlist_box.get(ACTIVE)
    car_playlist.append(song)

def add_to_home():
    song = playlist_box.get(ACTIVE)
    home_playlist.append(song)

def save_temporary_playlist():
    global temporary_playlist
    all_songs = playlist_box.get(0, END)
    temporary_playlist = [song for song in all_songs]

def load_car_playlist():
    clear_current_playlist()
    for song in car_playlist:
        playlist_box.insert(END, song)

def load_home_playlist():
    clear_current_playlist()
    for song in home_playlist:
        playlist_box.insert(END, song)

def load_temporary_playlist():
    clear_current_playlist()
    for song in temporary_playlist:
        playlist_box.insert(END, song)

# Get current time position of the song
def get_time():
    if stopped:
        return

    # current_time = pygame.mixer.music.get_pos() // 1000

    song = playlist_box.get(ACTIVE)
    song = f"C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles/{song}.mp3"

    song_mutagen = MP3(song)
    global song_length
    song_length = song_mutagen.info.length
    # convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

    global paused
    if int(song_slider.get()) == int(song_length):
        stop_song()
    elif not paused:
        next_time = int(song_slider.get()) + 1
        song_slider.config(to=int(song_length), value=next_time)

        # get the time position from the slider
        current_time = int(song_slider.get())
        converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

        if current_time >= 0:
            status_label.config(text=f"Elapsed time: {converted_current_time}/{converted_song_length}")
    status_label.after(1000, get_time)


# Slider functions
def set_volume(event):
    current_volume = volume_slider.get()
    pygame.mixer.music.set_volume(current_volume)

def slide_song(event):
    song = playlist_box.get(ACTIVE)
    song = f"C:/Users/hmano/PycharmProjects/StrypesLab/venv/MP3PROJECT/MusicFiles/{song}.mp3"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(song_slider.get()))

# Load images in memory
play_button_image = PhotoImage(file='Images/play.png')
stop_button_image = PhotoImage(file='Images/stop.png')
pause_button_image = PhotoImage(file='Images/pause.png')
next_button_image = PhotoImage(file='Images/forward.png')
previous_button_image = PhotoImage(file='Images/back.png')

# Main widgets
playlist_box = Listbox(root, bg='black', fg='white', selectbackground='white', selectforeground='red', width=60)
playlist_box.grid(row=0, column=0, sticky='nsew', columnspan=5, rowspan=5, pady=30)

playlist_scrollbar = Scrollbar(root, orient=VERTICAL, width=20, command=playlist_box.yview)
playlist_scrollbar.grid(row=0,rowspan=5, column=6, sticky='nsw', pady=30)
playlist_box['yscrollcommand'] = playlist_scrollbar.set

button_frame = Frame(root)
button_frame.grid(row=6, columnspan=5, rowspan=2, padx=40, pady=10)

play_button = Button(button_frame, image=play_button_image, borderwidth=0, command=play_song)
stop_button = Button(button_frame, image=stop_button_image, borderwidth=0, command=stop_song)
pause_button = Button(button_frame, image=pause_button_image, borderwidth=0, command=lambda:pause_song(paused))
next_button = Button(button_frame, image=next_button_image, borderwidth=0, command=go_forward)
previous_button = Button(button_frame, image=previous_button_image, borderwidth=0, command=go_backward)

previous_button.grid(column=0, row=0, padx=10)
play_button.grid(column=1, row=0, padx=10)
pause_button.grid(column=2, row=0, padx=10)
stop_button.grid(column=3, row=0, padx=10)
next_button.grid(column=4, row=0, padx=10)

choice_menu = Menu(root)
root.config(menu=choice_menu)

add_song_menu = Menu(choice_menu, tearoff=0)
choice_menu.add_cascade(label='Songs', menu=add_song_menu)
add_song_menu.add_command(label='Add song(s) to the playlist', command=add_songs)

delete_song_menu = Menu(choice_menu, tearoff=0)
choice_menu.add_cascade(label='Delete Songs', menu=delete_song_menu)
delete_song_menu.add_command(label='Delete selected song', command=delete_song)
delete_song_menu.add_command(label='Clear the playlist', command=clear_current_playlist)

add_to_playlist_menu = Menu(choice_menu, tearoff=0)
choice_menu.add_cascade(label='Add Song to Collection', menu=add_to_playlist_menu)
add_to_playlist_menu.add_command(label='Add to Car Playlist', command=add_to_car)
add_to_playlist_menu.add_command(label='Add to Home Playlist', command=add_to_home)
add_to_playlist_menu.add_command(label='Add All Songs to the Temporary Playlist', command=save_temporary_playlist)

load_playlist_menu = Menu(choice_menu, tearoff=0)
choice_menu.add_cascade(label='Load A Playlist', menu=load_playlist_menu)
load_playlist_menu.add_command(label='Load Car Playlist', command=load_car_playlist)
load_playlist_menu.add_command(label='Load Home Playlist', command=load_home_playlist)
load_playlist_menu.add_command(label='Load `Here Today - Gone Tommorow` Playlist', command=load_temporary_playlist)

volume_frame = ttk.LabelFrame(root, text='VOLUME')
volume_frame.grid(row=1, column=7, pady=15, padx=20, sticky=E)

volume_slider = ttk.Scale(volume_frame, from_=1, to=0, orient=VERTICAL, length=140, value=0.75, command=set_volume)
volume_slider.grid(row=0, column=1, padx=20)

song_slider = ttk.Scale(root, from_=0, to=60, orient=HORIZONTAL, length=300, value=0, command=slide_song)
song_slider.grid(row=8, column=2, pady=20)

status_label = Label(root, text='', font=('TkTextFont 15 italic'))
status_label.grid(row=9,column=2, columnspan=4, sticky=E, pady=10)

lyrics_tab = Text(root, height=10, width=58, wrap=WORD, borderwidth="1", relief="groove")
lyrics_tab.grid(row=10, columnspan=5)

lyrics_scrollbar = Scrollbar(root, orient=VERTICAL, width=20, command=lyrics_tab.yview)
lyrics_scrollbar.grid(row=10, column=6, sticky='nsw')
lyrics_tab['yscrollcommand'] = lyrics_scrollbar.set

playlist_box.bind('<Double-Button>', double_click_play)

root.mainloop()

# Write changed data to playlist files
with open('car_playlist.txt', 'w') as car_pls:
    for song in car_playlist:
        car_pls.write(f"{song}\n")

with open('home_playlist.txt', 'w') as home_pls:
    for song in home_playlist:
        home_pls.write(f"{song}\n")

with open('temporary_playlist.txt', 'w') as temporary_pls:
    for song in temporary_playlist:
        temporary_pls.write(f"{song}\n")
