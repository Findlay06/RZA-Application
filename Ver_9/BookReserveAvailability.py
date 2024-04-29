
from pathlib import Path # Imports path, this will allow for windows to be linked
import webbrowser # This import will help the file open other existing files
from tkinter import * # Usually a bad practice to import "*" as it could cause many problems but it does have the benefit of allowing some methods which are needed
from tkinter.ttk import * # Imports tkinter themed widgets
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\your-username\EXAM1243\Documents\SoftwareDev\Versions\Ver_9\assets\frame9")
# Is a function for file paths, will be used to refer back to when the relevant button is clicked
def open_window(tab):
    webbrowser.open_new_tab(tab)
    window.iconify() # window.iconify will allow for the current window (this file) to close when clicking a button to go to the next file in order to prevent bloat

def relative_to_assets(path: str) -> Path: # Will be used to refer back to the path of the assets, in order for elements to work as intended
    return ASSETS_PATH / Path(path) # Returns path


window = Tk() # Sets the variable "window" as the tk module
window.title('Booking/Reserving/Availability') # Makes the title of the window/file: "Booking/Reserving/Availability"

icon = PhotoImage(file = 'C:\\Users\\your-username\\Documents\\SoftwareDev\\Versions\\Ver_9\\assets\\zoo_image.png') # Sets the image in the assets folder as an icon

window.iconphoto(False, icon) # Implements the icon provided in line 24

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
    834.0,
    31.0,
    image=image_image_1 # Returns
)

canvas.create_text( # Creates text, will repeat in the file multiple times
    36.0,
    86.0,
    anchor="nw",
    text="Welcome to the Bookings Window",
    fill="#FFFFFF", # Color of textbox
    font=("ABeeZee Regular", 20 * -1) # Implements the font chosen
)

canvas.create_text(
    484.0,
    23.0,
    anchor="nw",
    text="Book, Reserve & Check Availability",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    487.0,
    93.0,
    anchor="nw",
    text="Book Tickets:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    474.0,
    308.0,
    anchor="nw",
    text="Reserve Tickets:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    670.0,
    308.0,
    anchor="nw",
    text="Check Availability:",
    fill="#080E2C",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    702.0,
    93.0,
    anchor="nw",
    text="Hotel booking:",
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
    140.0,
    anchor="nw",
    text="The Ridget Zoo app offers other features:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
)

canvas.create_text(
    36.0,
    186.0,
    anchor="nw",
    text="Options for booking and gaining resources.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    246.0,
    anchor="nw",
    text="Book tickets or a stay at the hotel.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    36.0,
    296.0,
    anchor="nw",
    text="A loyalty and reward scheme",
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
    374.0,
    98.0,
    image=image_image_3
)

button_image_1 = PhotoImage( # Sets element as button
    file=relative_to_assets("button_1.png")) # Refers to the assets path to get the relevant image
button_1 = Button( # Creates button class
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\your-username\EXAM1243\Documents\SoftwareDev\Versions\Ver_9\AttractionsAndFacilities.py'), # This is a command, on the click of this button it will open up another file
    relief="flat"
)
button_1.place( # Places the relevant button
    x=106.0,
    y=15.0,
    width=109.53570556640625,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\Login.py'),
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
    48.0,
    466.0,
    image=image_image_4
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\BookingTickets.py'),
    relief="flat"
)
button_3.place(
    x=467.0,
    y=148.0,
    width=163.0,
    height=133.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\HotelBooking.py'),
    relief="flat"
)
button_4.place(
    x=686.0,
    y=145.0,
    width=163.0,
    height=133.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\HotelAvailability.py'),
    relief="flat"
)
button_5.place(
    x=686.0,
    y=361.0,
    width=163.0,
    height=133.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_window (r'C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\ReserveTickets.py'),
    relief="flat"
)
button_6.place(
    x=467.0,
    y=361.0,
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

### NOTE: THIS FILE INCLUDES DUPLICATES OF CODE AND THUS SOME OF THE CODE WILL NOT BE COMMENTED ON