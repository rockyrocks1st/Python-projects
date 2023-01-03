#importing tkinter
from tkinter import *
import random

#creating window
win=Tk()
win.geometry("400x45")
win.title("Dice Roll Simulator")

#creating a label
lbl=Label(win,text="Click the button to roll the dice")
lbl.pack()

#creating a button
def clicked():
    global lbl
    lbl.config(text="Dice Rolled: "+str(random.randint(1,6)))

btn=Button(win,text="Roll",command=clicked)
btn.pack()

#run mainloop
win.mainloop()
