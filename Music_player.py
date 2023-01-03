# import the Tkinter library
from tkinter import *
import os
import pygame

# create the main window
mainWindow = Tk()
mainWindow.title("Music Player")

# add the menu bar
menuBar = Menu(mainWindow)
mainWindow.config(menu=menuBar)

# create the submenu
subMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=mainWindow.destroy)

# create the playlist
playlist = Listbox(mainWindow, bg="black", fg="green", width=60, selectbackground="green", selectforeground="black")
playlist.pack(pady=20)

# create the buttons
playButton = Button(mainWindow, text="PLAY", width=12, command=play_music)
stopButton = Button(mainWindow, text="STOP", width=12, command=stop_music)
pauseButton = Button(mainWindow, text="PAUSE", width=12, command=pause_music)

# position the buttons
playButton.pack(side=LEFT, padx=10)
stopButton.pack(side=LEFT, padx=10)
pauseButton.pack(side=LEFT, padx=10)

# define the functions
def browse_file():
    global filename
    filename = filedialog.askopenfilename()

def play_music():
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

# set the main window to loop
mainWindow.mainloop()
