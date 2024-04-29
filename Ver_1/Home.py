
from pathlib import Path
import webbrowser
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\EXAM1243\Documents\SoftwareDev\Ver_0.5\assets\frame0")

def callback_page_attractions(url):
    webbrowser.open_new(r'C:\\Users\\EXAM1243\\Documents\\SoftwareDev\\Ver_0.5\\AttractionsAndFacilities.py')
    window.iconify()

def callback_page_register(url):
    webbrowser.open_new(r'C:\\Users\\EXAM1243\\Documents\\SoftwareDev\\Register\\register.py')
    window.iconify()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#287EFF")


canvas = Canvas(
    window,
    bg = "#287EFF",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
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

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    767.9999999999999,
    36.00000000000001,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: callback_page_register (r'C:\\Users\\EXAM1243\\Documents\\SoftwareDev\\Register\\register.py'),
    relief="flat"
)
button_1.place(
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
    command=lambda: callback_page_attractions (r'C:\Users\EXAM1243\Documents\SoftwareDev\build\AttractionsAndFacilities.py'),
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
    command=lambda: print("button_3 clicked"),
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
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=354.9999999999999,
    y=20.000000000000007,
    width=27.0,
    height=25.0
)

canvas.create_text(
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
window.resizable(False, False)
window.mainloop()
