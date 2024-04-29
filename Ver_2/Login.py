
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\EXAM1243\Documents\SoftwareDev\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#FCFCFC")


canvas = Canvas(
    window,
    bg = "#FCFCFC",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FCFCFC",
    outline="")

canvas.create_text(
    326.0,
    55.0,
    anchor="nw",
    text="Enter your details:",
    fill="#080E2C",
    font=("ABeeZee Regular", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    430.5,
    190.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#287EFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
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
    text="Email:",
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
    x=382.0,
    y=360.0,
    width=98.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()
