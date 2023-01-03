#importing tkinter module 
import tkinter as tk 

#creating main GUI window
window = tk.Tk() 

#giving title to the window
window.title("Whiteboard") 

#creating canvas object
canvas = tk.Canvas(window, width = 400, height = 400) 
canvas.pack() 

#Initializing the color to black
color = 'black'

#function that changes color of pen
def change_color(new_color): 
	global color 
	color = new_color 

#function that draws on canvas
def draw(event): 
	x1, y1 = (event.x - 1), (event.y - 1) 
	x2, y2 = (event.x + 1), (event.y + 1) 
	canvas.create_oval(x1, y1, x2, y2, fill = color, outline = color) 

#binding draw function with left mouse click 
canvas.bind("<B1-Motion>", draw) 

#creating a frame for the buttons
frame = tk.Frame(window) 
frame.pack() 

#list of colors to choose from 
colors = ['red', 'green', 'blue', 'yellow', 'black', 'orange'] 

#creating buttons for all the colors
for i in range(6): 
	tk.Button(frame, bg = colors[i], command = lambda col = colors[i]: change_color(col)).grid(row = 0, column = i) 

#running the application 
window.mainloop()
