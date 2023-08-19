import tkinter as tk
from PIL import ImageTk, Image
import subprocess

def start_program():
    global process
    process = subprocess.Popen(['python', 'drowsiness_yawn.py'])

def stop_program():
    process.terminate()

# Create the main Tkinter window
window = tk.Tk()
window.title("Driver Drowsiness Detection")
window.geometry("600x400")

# Load the background image
background_image = Image.open("background.jpg")
background_image = background_image.resize((600, 400), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame for the heading
heading_frame = tk.Frame(window, bg="white", bd=5)
heading_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor="n")

# Create the heading label
heading_label = tk.Label(heading_frame, text="Driver Drowsiness Detection", font=("Arial", 24, "bold"), bg="white")
heading_label.pack(fill="both", expand=True)

# Create a frame for the buttons
button_frame = tk.Frame(window, bg="white", bd=5)
button_frame.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.1, anchor="n")

# Create the "Start" button
start_button = tk.Button(button_frame, text="Start", font=("Arial", 16, "bold"), fg="white", bg="green", padx=15, pady=8, command=start_program)
start_button.pack(side="left", padx=10)

# Create the "Stop" button
stop_button = tk.Button(button_frame, text="Stop", font=("Arial", 16, "bold"), fg="white", bg="red", padx=15, pady=8, command=stop_program)
stop_button.pack(side="right", padx=10)

# Set the background image as the window background
window.configure(background='white')

# Start the Tkinter event loop
window.mainloop()
