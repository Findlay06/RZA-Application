from fonts import App # Imports all the fonts in from the font file and App class
from pathlib import Path # Imports path, this will allow for windows to be linked
import webbrowser # This import will help the file open other existing files
from tkinter import * # Usually a bad practice to import "*" as it could cause many problems but it does have the benefit of allowing some methods which are needed
from tkinter.ttk import * # Imports tkinter themed widgets
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\assets\frame2") # This path is used in order for the file to recognise any assets that will be used

def open_window(tab):
    webbrowser.open_new_tab(tab) # Is a function for file paths, will be used to refer back to when the relevant button is clicked
    window.iconify() # window.iconify will allow for the current window (this file) to close when clicking a button to go to the next file in order to prevent bloat.


def msgbox_colorblind(): # Message box function
    messagebox.showinfo("Notification", "Colorblind mode on!") # Will display messagebox with "Notification" as the title and "Colorblind mode on!" as the text.

def msgbox_keyboard():
    messagebox.showinfo("Notification", "Keyboard only on!")

def msgbox_vfx():
    messagebox.showinfo("Notification", "Limited VFX on!")

def relative_to_assets(path: str) -> Path: # Will be used to refer back to the path of the assets, in order for elements to work as intended
    return ASSETS_PATH / Path(path) # Returns path


window = Tk() # Sets the variable "window" as the tk module
window.title('Accessibility') # Makes the title of the window/file: "Accessibility"

icon = PhotoImage(file = 'C:\\Users\\EXAM1243\\Documents\\SoftwareDev\\Versions\\Ver_9\\assets\\zoo_image.png') # This will be the icon for the window/file

window.iconphoto(False, icon) # Implements the icon provided in line 33

window.geometry("862x519") # Sets the size of the window/file
window.configure(bg = "#287EFF") # Sets the background of the window/file


canvas = Canvas( # Canvas class, essentially a background
    window,
    bg = "#287EFF", # Sets Background color
    height = 519, # Sets the heigh of the canvas
    width = 862, # Sets the width of the canvas
    bd = 0,
    highlightthickness = 0,
    relief = "ridge" # The simulated effects around the outside of a widget
)

canvas.place(x = 0, y = 0) # Places the canvas
canvas.create_rectangle( # Creates a rectangle for the file as well as for the other elements
    0.0,
    0.0,
    431.0,
    66.0,
    fill="#FCFCFC",
    outline="")

canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FCFCFC",
    outline="")

image_image_1 = PhotoImage( # Sets element as image
    file=relative_to_assets("image_1.png")) # Refers to the assets path for the relevant image
image_1 = canvas.create_image( # Creates image
    706.0,
    37.0,
    image=image_image_1 # Returns
)

canvas.create_text( # Creates text, will repeat in the file multiple times
    36.0,
    88.0,
    anchor="nw", 
    text="Welcome to the Accessibility Window",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    607.0,
    25.0,
    anchor="nw",
    text="Options:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    468.0,
    93.0,
    anchor="nw",
    text="Colorblind Mode:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    477.0,
    308.0,
    anchor="nw",
    text="Keyboard Only:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    681.0,
    308.0,
    anchor="nw",
    text="Limited Visual FX:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    712.0,
    93.0,
    anchor="nw",
    text="Font Editor:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_rectangle(
    36.0,
    125.0,
    96.0,
    130.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    36.0,
    152.0,
    anchor="nw",
    text="The Ridget Zoo app offers...",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    36.0,
    210.0,
    anchor="nw",
    text="Many accessibility features such as:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    263.0,
    anchor="nw",
    text="Colorblind Mode.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    282.0,
    anchor="nw",
    text="Font Editor.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    301.0,
    anchor="nw",
    text="Keyboard Only.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    320.0,
    anchor="nw",
    text="Limited Visual FX.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    47.0,
    23.0,
    anchor="nw",
    text="Rza",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    20.0,
    34.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    407.0,
    101.0,
    image=image_image_3
)

button_image_1 = PhotoImage( # Sets element as button
    file=relative_to_assets("button_1.png")) # Refers to the assets path to get the relevant image
button_1 = Button( # Creates button class
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\AttractionsAndFacilities.py'), # This is a command, on the click of this button it will open up another file
    relief="flat"
)
button_1.place( # Places the relevant button
    x=106.0,
    y=15.0,
    width=109.53570556640625,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\BookReserveAvailability.py'),
    relief="flat"
)
button_2.place(
    x=234.0,
    y=15.0,
    width=109.53570556640625,
    height=35.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    50.0,
    465.0,
    image=image_image_4
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: msgbox_colorblind(),
    relief="flat"
)
button_3.place(
    x=468.0,
    y=130.0,
    width=163.0,
    height=133.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: msgbox_keyboard(),
    relief="flat"
)
button_4.place(
    x=468.0,
    y=344.0,
    width=163.0,
    height=133.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: msgbox_vfx(),
    relief="flat"
)
button_5.place(
    x=685.0,
    y=344.0,
    width=163.0,
    height=133.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\fonts.py'),
    relief="flat"
)
button_6.place(
    x=687.0,
    y=130.0,
    width=163.0,
    height=133.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\Accessibility.py'),
    relief="flat"
)
button_7.place(
    x=355.0,
    y=20.0,
    width=27.0,
    height=25.0
)
window.resizable(False, False) # Decides if the window will be resized
window.mainloop() # Outputs the contents of the file

### NOTE: MANY OF THE FILES RELATED TO THE APP INCLUDE COPIES OF CODE HERE AND THUS SOME OF THE CODE WILL NOT BE COMMENTED ON