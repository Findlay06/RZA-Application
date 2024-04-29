
from pathlib import Path # Imports path, this will allow for windows to be linked
import webbrowser # This import will help the file open other existing files
from tkinter import * # Usually a bad practice to import "*" as it could cause many problems but it does have the benefit of allowing some methods which are needed
from tkinter.ttk import * # Imports tkinter themed widgets
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\assets\frame1") #This path is used in order for the file to recognise any assets that will be used
# Is a function for file paths, will be used to refer back to when the relevant button is clicked
def open_window(url):
    webbrowser.open_new_tab(url)
    window.iconify() # window.iconify will allow for the current window (this file) to close when clicking a button to go to the next file in order to prevent bloat

def relative_to_assets(path: str) -> Path: # Will be used to refer back to the path of the assets, in order for elements to work as intended
    return ASSETS_PATH / Path(path) # Returns path


window = Tk() # Sets the variable "window" as the tk module
window.title('Login') # Makes the title of the window/file: "Login"

icon = PhotoImage(file = 'C:\\Users\\your-username\\Documents\\SoftwareDev\\Versions\\Ver_9\\assets\\zoo_image.png') # Sets the image in the assets folder as an icon

window.iconphoto(False, icon) # Implements the icon provided in line 24

window.geometry("862x519") # Sets the size of the window/file
window.configure(bg = "#FCFCFC") # Sets the background of the window/file


canvas = Canvas( # Canvas class, essentially a background
    window,
    bg = "#FCFCFC", # Sets Background color
    height = 519, # Sets the heigh of the canvas
    width = 862, # Sets the width of the canvas
    bd = 0,
    highlightthickness = 0,
    relief = "ridge" # The simulated effects around the outside of a widget
)

canvas.place(x = 0, y = 0) # Places the canvas
canvas.create_rectangle( # Creates a rectangle for the file as well as for the other elements
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text( # Creates text, will repeat in the file multiple times
    326.0,
    55.0,
    anchor="nw",
    text="Enter your details:",
    fill="#080E2C", # Color of textbox
    font=("ABeeZee Regular", 24 * -1) # Implements the font chosen
)

entry_image_1 = PhotoImage( # Creates entry image
    file=relative_to_assets("entry_1.png")) # Gathers the relevant entry image from the assets function
entry_bg_1 = canvas.create_image( # Implements image
    430.5,
    190.5,
    image=entry_image_1 # Returns
)
entry_1 = Entry( # Creates entry
    bd=0,
    bg="#287EFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place( # Places entry (image)
    x=270.0,
    y=160.0,
    width=321.0,
    height=59.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    430.5,
    290.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#287EFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=270.0,
    y=260.0,
    width=321.0,
    height=59.0
)

canvas.create_text(
    172.0,
    177.0,
    anchor="nw",
    text="User:",
    fill="#080E2C",
    font=("ABeeZee Regular", 24 * -1)
)

canvas.create_text(
    128.0,
    277.0,
    anchor="nw",
    text="Password:",
    fill="#080E2C",
    font=("ABeeZee Regular", 24 * -1)
)

button_image_1 = PhotoImage( # Sets element as button
    file=relative_to_assets("button_1.png")) # Refers to the assets path to get the relevant image
button_1 = Button( # Creates button class
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\LoyaltyAndRewardScheme.py'), # This is a command, on the click of this button it will open up another file
    relief="flat"
)
button_1.place( # Places the relevant button
    x=382.0,
    y=360.0,
    width=98.0,
    height=55.0
)
window.resizable(False, False) # Decides if the window will be resized
window.mainloop() # Outputs the contents of the file

### NOTE: THIS FILE INCLUDES DUPLICATES OF CODE AND THUS SOME OF THE CODE WILL NOT BE COMMENTED ON