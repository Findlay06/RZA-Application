import tkinter as tk # Imports tk module
from tkinter import * # Usually a bad practice to import "*" as it could cause many problems but it does have the benefit of allowing some methods which are needed
from tkinter import PhotoImage, font # Imports the PhotoImage and font classes
from tkinter import Tk, messagebox, Canvas, Entry, Text, Button, PhotoImage, messagebox
from tkinter.ttk import * # Imports tkinter themed widgets
from pathlib import Path # Imports path, this will allow for windows to be linked

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\your-username\Documents\SoftwareDev\Versions\Ver_9\assets\frame1") #This path is used in order for the file to recognise any assets that will be used

def relative_to_assets(path: str) -> Path: # Will be used to refer back to the path of the assets, in order for elements to work as intended
    return ASSETS_PATH / Path(path) # Returns path


class App(tk.Tk): # App class
    def __init__(self):
        tk.Tk.__init__(self)

        #font reference
        textfont = font.Font(family='arial', size='14')
        
        #uses the persistent font reference
        tk.Text(self, font=textfont).grid(row=0, column=0, sticky='nswe')
        
        #have the textfield fill all available space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #font chooser
        fc = tk.Listbox(self)
        fc.grid(row=0, column=1, sticky='nswe')

        #insert all of the fonts
        for f in font.families():
            fc.insert('end', f)

        #switch textfont family with release
        fc.bind('<ButtonRelease-1>', lambda e: textfont.config(family=fc.get(fc.curselection())))
        
        #scrollbar - use the mousewheel
        vsb = tk.Scrollbar(self)
        vsb.grid(row=0, column=2, sticky='ns')
        
        #connecting the scrollbar and font chooser
        fc.configure(yscrollcommand=vsb.set)
        vsb.configure(command=fc.yview)

#Output
if __name__ == "__main__":
    app = App()
    app.title('Font Picker')
    app.geometry(f'800x600+200+200')
    icon = PhotoImage(file = 'C:\\Users\\your-username\\Documents\\SoftwareDev\\Versions\\Ver_9\\assets\\zoo_image.png')
    app.iconphoto(False, icon)
    app.mainloop()
    