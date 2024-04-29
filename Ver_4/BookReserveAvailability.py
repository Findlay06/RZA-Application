
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\EXAM1243\Documents\SoftwareDev\build\assets\frame3")


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

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    834.0,
    31.0,
    image=image_image_1
)

canvas.create_text(
    36.0,
    86.0,
    anchor="nw",
    text="Welcome to the Bookings Window",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 20 * -1)
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
    408.0,
    33.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    374.0,
    98.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=358.0,
    y=21.0,
    width=27.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=106.0,
    y=15.0,
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
    x=234.0,
    y=15.0,
    width=109.53570556640625,
    height=35.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    48.0,
    466.0,
    image=image_image_5
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
    x=467.0,
    y=148.0,
    width=163.0,
    height=133.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=686.0,
    y=145.0,
    width=163.0,
    height=133.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=686.0,
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
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=467.0,
    y=361.0,
    width=163.0,
    height=133.0
)
window.resizable(False, False)
window.mainloop()
