
from pathlib import Path # Imports path, this will allow for windows to be linked
import webbrowser # This import will help the file open other existing files
from tkinter import * # Usually a bad practice to import "*" as it could cause many problems but it does have the benefit of allowing some methods which are needed
from tkinter.ttk import * # Imports tkinter themed widgets
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\assets\frame5") # This path is used in order for the file to recognise any assets that will be used
# Is a function for file paths, will be used to refer back to when the relevant button is clicked
def open_window(url):
    webbrowser.open_new_tab(url)
    window.iconify() # window.iconify will allow for the current window (this file) to close when clicking a button to go to the next file in order to prevent bloat

def msgbox_checkout(): # Messagebox function
    messagebox.showinfo("Notification", "API implementation not done!") # Shows a message box including 2 strings

def relative_to_assets(path: str) -> Path: # Will be used to refer back to the path of the assets, in order for elements to work as intended
    return ASSETS_PATH / Path(path) # Returns path


window = Tk() # Sets the variable "window" as the tk module
window.title('Reserve Tickets') # Makes the title of the window/file: "Reserve Tickets"

icon = PhotoImage(file = 'C:\\Users\\your-username\\Documents\\SoftwareDev\\Versions\\Ver_9\\assets\\zoo_image.png') # Sets the image in the assets folder as an icon

window.iconphoto(False, icon) # Implements the icon provided in line 27

window.geometry("387x519") # Sets the size of the window/file
window.configure(bg = "#287EFF") # Sets the background of the window/file


canvas = Canvas( # Canvas class, essentially a background
    window,
    bg = "#287EFF", # Sets Background color
    height = 519, # Sets the heigh of the canvas
    width = 387, # Sets the width of the canvas
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

canvas.create_text( # Creates text, will repeat in the file multiple times
    36.0,
    86.0,
    anchor="nw",
    text="Reserve",
    fill="#FFFFFF", # Color of textbox
    font=("ABeeZee Regular", 20 * -1) # Implements the font chosen
)

canvas.create_rectangle(
    36.0,
    125.0,
    96.0,
    130.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    47.0,
    23.0,
    anchor="nw",
    text="Rza",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

image_image_1 = PhotoImage( # Sets element as image
    file=relative_to_assets("image_1.png")) # Refers to the assets path for the relevant image
image_1 = canvas.create_image( # Creates image
    20.0,
    34.0,
    image=image_image_1 # Returns
)

button_image_1 = PhotoImage( # Sets element as button
    file=relative_to_assets("button_1.png")) # Refers to the assets path to get the relevant image
button_1 = Button( # Creates button class
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\Home.py'), # This is a command, on the click of this button it will open up another file
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
    command=lambda: msgbox_checkout(),
    relief="flat"
)
button_2.place(
    x=41.0,
    y=475.0,
    width=109.53570556640625,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\Login.py'),
    relief="flat"
)
button_3.place(
    x=234.0,
    y=15.0,
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
    x=355.0,
    y=20.0,
    width=27.0,
    height=25.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    131.0,
    99.0,
    image=image_image_2
)

canvas.create_text(
    36.0,
    145.0,
    anchor="nw",
    text="Reserving will allow for you to pay for a\n",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    196.0,
    anchor="nw",
    text="Enter you details:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    228.0,
    anchor="nw",
    text="CC Number:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    220.0,
    228.0,
    anchor="nw",
    text="Arrival Date:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    311.0,
    anchor="nw",
    text="Name:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    394.0,
    anchor="nw",
    text="Security Number:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    164.0,
    anchor="nw",
    text="ticket in advance.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    331.99996269866824,
    467.9999848343432,
    image=image_image_3
)

entry_image_1 = PhotoImage( # Creates entry image
    file=relative_to_assets("entry_1.png")) # Gathers the relevant entry image from the assets function
entry_bg_1 = canvas.create_image( # Implements image
    286.5,
    280.0,
    image=entry_image_1 # Returns
)
entry_1 = Entry( # Creates entry
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place( # Places entry (image)
    x=228.0,
    y=260.0,
    width=117.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    99.5,
    280.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=41.0,
    y=260.0,
    width=117.0,
    height=38.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    99.5,
    360.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=41.0,
    y=340.0,
    width=117.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    99.5,
    440.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=41.0,
    y=420.0,
    width=117.0,
    height=38.0
)
window.resizable(False, False) # Decides if the window will be resized
window.mainloop() # Outputs the contents of the file

### NOTE: THIS FILE INCLUDES DUPLICATES OF CODE AND THUS SOME OF THE CODE WILL NOT BE COMMENTED ON