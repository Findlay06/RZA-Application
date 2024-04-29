from pathlib import Path # Imports path, this will allow for windows to be linked
import webbrowser # This import will help the file open other existing files
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\assets\frame0") #This path is used in order for the file to recognise any assets that will be used
# Is a function for file paths, will be used to refer back to when the relevant button is clicked
def open_window(url):
    webbrowser.open_new_tab(url)
    window.iconify() # window.iconify will allow for the current window (this file) to close when clicking a button to go to the next file in order to prevent bloat

def relative_to_assets(path: str) -> Path: # Will be used to refer back to the path of the assets, in order for elements to work as intended
    return ASSETS_PATH / Path(path) # Returns path


window = Tk() # Sets the variable "window" as the tk module
window.title('Home') # Makes the title of the window/file: "Home"

icon = PhotoImage(file = 'C:\\Users\\your-username\\Documents\\SoftwareDev\\Versions\\Ver_9\\assets\\zoo_image.png') # This will be the icon for the window/file

window.iconphoto(False, icon) # Implements the icon provided in line 22

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
    1.1368683772161603e-13,
    7.105427357601002e-15,
    431.0000000000001,
    58.00000000000001,
    fill="#FCFCFC",
    outline="")

canvas.create_rectangle(
    430.9999999999999,
    7.105427357601002e-15,
    861.9999999999999,
    519.0,
    fill="#FCFCFC",
    outline="")

image_image_1 = PhotoImage( # Sets element as image
    file=relative_to_assets("image_1.png")) # Refers to the assets path for the relevant image
image_1 = canvas.create_image( # Creates image
    767.9999999999999,
    36.00000000000001,
    image=image_image_1 # Returns
)

button_image_1 = PhotoImage( # Sets element as button
    file=relative_to_assets("button_1.png")) # Refers to the assets path to get the relevant image
button_1 = Button( # Creates button class
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\register.py'), # This is a command, on the click of this button it will open up another file
    relief="flat"
)
button_1.place( # Places the relevant button
    x=597.9999999999999,
    y=451.0,
    width=98.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\AttractionsAndFacilities.py'),
    relief="flat"
)
button_2.place(
    x=105.99999999999989,
    y=15.000000000000007,
    width=109.53570556640625,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\\BookReserveAvailability.py'),
    relief="flat"
)
button_3.place(
    x=233.9999999999999,
    y=15.000000000000007,
    width=109.53570556640625,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\Accessibility.py'),
    relief="flat"
)
button_4.place(
    x=354.9999999999999,
    y=20.000000000000007,
    width=27.0,
    height=25.0
)

canvas.create_text( # Creates text, will repeat in the file multiple times
    35.999999999999886,
    91.0,
    anchor="nw",
    text="Welcome to the Ridget Zoo App!",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    546.9999999999999,
    22.000000000000007,
    anchor="nw",
    text="Our Zoo Animals:",
    fill="#080E2C",
    font=("ABeeZee Regular", 24 * -1)
)

canvas.create_rectangle(
    35.999999999999886,
    134.0,
    95.99999999999989,
    139.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    35.999999999999886,
    150.0,
    anchor="nw",
    text="The Ridget Zoo app offers",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    35.999999999999886,
    180.0,
    anchor="nw",
    text="Information on:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    35.999999999999886,
    220.0,
    anchor="nw",
    text="Facilities",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    35.999999999999886,
    259.0,
    anchor="nw",
    text="Attractions",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    35.999999999999886,
    296.0,
    anchor="nw",
    text="Bookings",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    35.999999999999886,
    333.0,
    anchor="nw",
    text="Much more!",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    46.999999999999886,
    21.000000000000007,
    anchor="nw",
    text="Rza",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    19.999999999999886,
    32.00000000000001,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    360.9999999999999,
    104.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    53.000000000000114,
    459.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    541.9999999999999,
    160.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    752.9999999999999,
    357.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    538.9999999999999,
    357.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    752.9999999999999,
    160.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    538.9999999999999,
    156.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    753.9999999999999,
    159.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    538.9999999999999,
    351.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    752.9999999999999,
    356.0,
    image=image_image_12
)
window.resizable(False, False) # Decides if the window will be resized
window.mainloop() # Outputs the contents of the file

### NOTE: MANY OF THE FILES RELATED TO THE APP INCLUDE COPIES OF CODE HERE AND THUS SOME OF THE CODE WILL NOT BE COMMENTED ON