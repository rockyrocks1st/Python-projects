import tkinter as tk
import random

# Define the window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class FallingLetter:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, WINDOW_WIDTH)
        self.y = 0
        self.letter = chr(random.randint(65, 90))  # Select a random capital letter
        self.color = "#00FF00"  # Green color

        self.id = self.canvas.create_text(self.x, self.y, text=self.letter, fill=self.color)

    def move(self):
        self.canvas.move(self.id, 0, 5)  # Move the letter 5 pixels down
        self.y += 5

    def is_out_of_bounds(self):
        return self.y >= WINDOW_HEIGHT

class FallingLettersGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()

        self.falling_letters = []
        for i in range(10):
            letter = FallingLetter(self.canvas)
            self.falling_letters.append(letter)

        self.game_loop()

    def game_loop(self):
        for letter in self.falling_letters:
            letter.move()
            if letter.is_out_of_bounds():
                self.falling_letters.remove(letter)
                del letter

        # Add new letters to the game
        while len(self.falling_letters) < 10:
            letter = FallingLetter(self.canvas)
            self.falling_letters.append(letter)

        self.master.after(50, self.game_loop)


if __name__ == "__main__":
    root = tk.Tk()
    game = FallingLettersGame(root)
    root.mainloop()
