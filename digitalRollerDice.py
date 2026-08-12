import tkinter as tk
import random
import time

# --- STEP 1: Create the Game Window ---
window = tk.Tk()
window.title("🎲 Magic Dice Roller 🎲")
window.geometry("400x450")
window.configure(bg="#2C3E50")  # Dark blue background

# --- STEP 2: The Kid's Customizing Zone ---
# Teach variables: Let the child change these colors!
TEXT_COLOR = "#FFFFFF"  # White text
BUTTON_COLOR = "#2ECC71"  # Emerald green button
DICE_COLOR = "#F1C40F"  # Bright yellow dice text


# --- STEP 3: The Rolling Logic ---
def roll_dice():
    # Visual Trick: Flash random numbers to look like a spinning dice!
    for _ in range(8):
        fake_roll = random.randint(1, 6)
        dice_label.config(text=str(fake_roll))
        window.update()
        time.sleep(0.08)  # Pause for a split second

    # The actual final result
    final_roll = random.randint(1, 6)
    dice_label.config(text=str(final_roll))

    # Teach Conditionals: Give a special cheer for a lucky number 6!
    if final_roll == 6:
        status_label.config(text="🎉 LUCKY SIX! Roll again! 🎉")
    else:
        status_label.config(text="Great roll! Try for a 6!")


# --- STEP 4: Designing the Screen Objects (Widgets) ---
# Title Text
title_label = tk.Label(window, text="CLICK TO ROLL!", font=("Arial", 24, "bold"), bg="#2C3E50", fg=TEXT_COLOR)
title_label.pack(pady=20)

# The Giant Dice Number Display
dice_label = tk.Label(window, text="?", font=("Arial", 90, "bold"), bg="#2C3E50", fg=DICE_COLOR)
dice_label.pack(pady=20)

# Secret message tracker
status_label = tk.Label(window, text="Can you roll a 6?", font=("Arial", 14), bg="#2C3E50", fg="#BDC3C7")
status_label.pack(pady=10)

# The Clickable Roll Button
roll_button = tk.Button(window, text="🎲 ROLL DICE 🎲", font=("Arial", 16, "bold"), bg=BUTTON_COLOR, fg="white",
                        command=roll_dice, height=2, width=15)
roll_button.pack(pady=30)

# Start the game loop
window.mainloop()
