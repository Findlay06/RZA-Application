
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\EXAM1243\Documents\SoftwareDev\build\assets\frame2")


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
    706.0,
    37.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    408.0,
    32.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    549.0,
    410.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    768.0,
    410.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    549.0,
    410.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    549.0,
    196.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    768.0,
    196.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    769.0,
    196.0,
    image=image_image_8
)

canvas.create_text(
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
    217.0,
    anchor="nw",
    text="Many accessibility features such as:",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    30.0,
    263.0,
    anchor="nw",
    text="Colorblind Mode.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    30.0,
    284.0,
    anchor="nw",
    text="Font Editor.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    30.0,
    305.0,
    anchor="nw",
    text="Keyboard Only.",
    fill="#FFFFFF",
    font=("ABeeZee Regular", 16 * -1)
)

canvas.create_text(
    30.0,
    326.0,
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

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    20.0,
    34.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    550.0,
    196.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    766.0,
    410.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    203.0,
    337.0,
    image=image_image_12
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

canvas.create_rectangle(
    7.0,
    411.0,
    114.0,
    519.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
