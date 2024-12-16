import tkinter as tk
import pygame

# Initialize the pygame mixer for sound
pygame.mixer.init()

# Load sound files (ensure these files are in the 'sounds' folder or adjust the path accordingly)
SOUNDS = {
    # Octave 4
    "C4": "sounds/C4.mp3",
    "Db4": "sounds/Db4.mp3",
    "D4": "sounds/D4.mp3",
    "Eb4": "sounds/Eb4.mp3",
    "E4": "sounds/E4.mp3",
    "F4": "sounds/F4.mp3",
    "Gb4": "sounds/Gb4.mp3",
    "G4": "sounds/G4.mp3",
    "Ab4": "sounds/Ab4.mp3",
    "A4": "sounds/A4.mp3",
    "Bb4": "sounds/Bb4.mp3",
    "B4": "sounds/B4.mp3",
    
    # Octave 5
    "C5": "sounds/C5.mp3",
    "Db5": "sounds/Db5.mp3",
    "D5": "sounds/D5.mp3",
    "Eb5": "sounds/Eb5.mp3",
    "E5": "sounds/E5.mp3",
    "F5": "sounds/F5.mp3",
    "Gb5": "sounds/Gb5.mp3",
    "G5": "sounds/G5.mp3",
    "Ab5": "sounds/Ab5.mp3",
    "A5": "sounds/A5.mp3",
    "Bb5": "sounds/Bb5.mp3",
    "B5": "sounds/B5.mp3"
}

# Function to play sound
def play_sound(note):
    sound_file = SOUNDS.get(note)
    if sound_file:
        pygame.mixer.Sound(sound_file).play()

# Create the main application window
root = tk.Tk()
root.title("Piano App")
root.geometry("1400x300")  # Adjusted for more keys
root.resizable(False, False)

# Create a frame to hold the keys
frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill="both")

# Define white and black keys for octaves 4 and 5
white_keys = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "D5", "E5", "F5", "G5", "A5", "B5"]
black_keys = ["Db4", "Eb4", None, "Gb4", "Ab4", "Bb4", None, "Db5", "Eb5", None, "Gb5", "Ab5", "Bb5"]

# Draw white keys
white_button_width = 100
white_button_height = 260
white_buttons = []

for i, note in enumerate(white_keys):
    btn = tk.Button(frame, text=note, width=10, height=5, bg="white", fg="black",
                    relief="raised", borderwidth=3, command=lambda n=note: play_sound(n))
    btn.place(x=i * white_button_width, y=0, width=white_button_width, height=white_button_height)
    white_buttons.append(btn)

# Draw black keys (overlay on white keys)
black_key_width = 60
black_key_height = 130
black_key_positions = [
    1, 2, None, 4, 5, 6, None, 8, 9, None, 11, 12, 13
]

for i, note in enumerate(black_keys):
    if note:
        x_position = (black_key_positions[i] * white_button_width) - (black_key_width / 2)
        btn = tk.Button(frame, text=note, width=5, height=3, bg="black", fg="white",
                        relief="raised", borderwidth=3, command=lambda n=note: play_sound(n))
        btn.place(x=x_position, y=0, width=black_key_width, height=black_key_height)

# Start the application loop
root.mainloop()
