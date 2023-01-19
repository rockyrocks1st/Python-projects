from tkinter import *
import pyshorteners

root = Tk()
root.title("Link Shortener")
root.geometry("400x400")

def short():
    link = entry.get()
    shortener = pyshorteners.Shortener()
    short_link = shortener.tinyurl.short(link)
    label2 = Label(root, text=short_link, font=("Helvetica", 12))
    label2.grid(row=2, column=0, columnspan=2)

label = Label(root, text="Enter Link:", font=("Helvetica", 12))
label.grid(row=0, column=0, sticky=W)

entry = Entry(root, width=50, borderwidth=5)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

button = Button(root, text="Shorten", command=short)
button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

root.mainloop()
