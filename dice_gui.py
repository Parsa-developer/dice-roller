import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk

class DiceRollerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll Simulator")
        self.root.geometry("300x400")

        self.dice_images = {
            i: ImageTk.PhotoImage(Image.open(f"assets/Dice-{i}.png").resize((150,150)))
            for i in range(1, 7)
        }

        self.create_widgets()
    
    def create_widgets(self):
        self.dice_label = ttk.Label(self.root)
        self.dice_label.pack(pady=20)

        self.result_label = ttk.Label(self.root, font=('Helvetica', 14))
        self.result_label.pack()

        roll_btn = ttk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        roll_btn.pack(pady=20)

        self.roll_dice

    def roll_dice(self):
        result = random.randint(1, 6)
        self.dice_label.config(image=self.dice_images[result])
        self.result_label.config(text=f"You rolled: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRollerApp(root)
    root.mainloop()