from tkinter import *

#creating root object
root = Tk()

#creating label
label_0 = Label(root, text="login Page",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

#creating username label
label_1 = Label(root, text="Username",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

#creating entry for username
entry_1 = Entry(root)
entry_1.place(x=240,y=130)

#creating password label
label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

#creating entry for password
entry_2 = Entry(root)
entry_2.place(x=240,y=180)

#creating login button
Button(root, text='Login',width=20,bg='brown',fg='white').place(x=180,y=230)

#creating quit button
Button(root, text='Quit',width=20,bg='brown',fg='white', command = root.quit).place(x=180,y=280)

#mainloop
root.mainloop()