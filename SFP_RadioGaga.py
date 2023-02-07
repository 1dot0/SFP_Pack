
import os
import random
import time
from tkinter import Tk, PhotoImage, Label

WAITTIME = 5
FOLDER_PATH = "RadioGaGaImgs"
window = None

def show_img():
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.gif')]

    # Choose a random image file
    image_file = random.choice(image_files)
    image_path = os.path.join(FOLDER_PATH, image_file)

    # Create a new Tkinter window
    window = Tk()
    window.geometry("300x300")
    window.configure(background='white')
    window.title("Random Image")
    window.attributes("-topmost", True) #this will make the window always on top

    # Create a PhotoImage object with the chosen image
    image = PhotoImage(file=image_path)

    # Create a Label widget to display the image
    label = Label(window, image=image)
    label.pack()

    # Show the window
    window.mainloop()

while True:
    show_img()
    time.sleep(WAITTIME)
    if window.getKey() == 'q':
        break