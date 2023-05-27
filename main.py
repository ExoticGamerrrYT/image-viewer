"""
¡DISCLAIMER!
SOME FUNCTIONS ARE THERE BUT THEY DONT WORK.
DISCORD: 3xotic#2903
"""

from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
import os
# GLOBALS
directory = ""
files = []
item = 0


def print_hello(event):
    print("Hello!")


def open_file_explorer():
    """
    Open an explorer window that can only see folders and the formats
    .jpg and .png then print directory of file. Also opens the file in a var
    """
    """
    # file = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.png")])
    # print("Selected file:", file)
    """
    global directory
    directory = filedialog.askdirectory()
    print("Selected directory: ", directory)

    global files
    files = os.listdir(directory)
    print("Files: ", files)

    """ <- Commented for a time...
    global image
    image = Image.open(file)

    # Resize if necessary
    max_width = 300
    # max_height = 700
    if image.width > max_width:
        proportion = max_width / float(image.width)
        height = int(image.height * proportion)
        image = image.resize((max_width, height), Image.LANCZOS)
    """

    """ Resize but now the height (max_height is commented above) <- Commented for a time...
    if image.height > max_height:
        proportion = max_height / float(image.height)
        width = int(image.width * proportion)
        image = image.resize((width, max_height), Image.LANCZOS)
    
    image_tk = ImageTk.PhotoImage(image)
    image_label.configure(image=image_tk)
    image_label.image = image_tk
    """
    listbox = Listbox(wn, height=28, width=15, bg=GRAY, borderwidth=0, selectmode=SINGLE)

    increase = 0
    for i in files:
        listbox.insert(END, files[increase])
        increase += 1

    listbox.place(x=10, y=80)
    """
        for item in :
        print("You have selected " + str(item + 1))
    
    global index
    index = listbox.curselection()
    index = int(index)
    """

    def show_index():
        global item
        for item in listbox.curselection():
            print("You have selected " + str(item + 0))

    def show_image(event):
        show_index()
        image_path = os.path.join(directory + "/" + files[item])
        image = Image.open(image_path)

        max_width = 300
        if image.width > max_width:
            proportion = max_width / float(image.width)
            height = int(image.height * proportion)
            image = image.resize((max_width, height), Image.LANCZOS)

        image_tk = ImageTk.PhotoImage(image)
        image_label.configure(image=image_tk)
        image_label.image = image_tk

        image_tk = ImageTk.PhotoImage(image)
        image_label.configure(image=image_tk)
        image_label.image = image_tk

    listbox.bind("<<ListboxSelect>>", show_image)


def rote_left(events):
    pass


def show_image_1(events):
    pass


def show_image_2(events):
    pass


# Constants for colors
BLACK = "#131313"
WHITE = "#FFFFFF"
GRAY = "#E5E5E5"

DARK_GREY = "#9BA4B5"
DARK_BLUE = "#212A3E"
LIGHT_BLUE = "#394867"
SHARK_WHITE = "#F1F6F9"

# Window Config
wn = Tk()
wn.title("Image Editor")
wn.geometry("600x600")
wn.resizable(False, False)
wn.iconbitmap("images/icons/icons8_image_1.ico")
wn.config(bg=DARK_GREY)

# Style
style = ttk.Style()
style.configure("TButton", background=DARK_GREY)

# Frame
"""
# list_frame = Frame(wn, height=450, width=95, bg=GRAY)  <- This was the frame of the left
# list_frame.place(x=10, y=80)
"""

image_frame = Frame(wn, height=452, width=475, bg=SHARK_WHITE)  # <- Frame of the image viewer
image_frame.place(x=115, y=80)

# Labels
title_lbl = ttk.Label(text="Image Editor", background=DARK_GREY, foreground=DARK_BLUE, font=("Montserrat Black", 34))  # <- Title
title_lbl.place(x=185, y=0)

# Buttons
btn_rote_left = ttk.Button(wn, text="R. Left")  # <- Rotate left button
btn_rote_left.place(x=100, y=570)

btn_rote_right = ttk.Button(wn, text="R. Right")  # <- Rotate right button
btn_rote_right.place(x=180, y=570)

btn_mirror = ttk.Button(wn, text="Mirror")  # <- Mirror image button
btn_mirror.place(x=260, y=570)

btn_sharpness = ttk.Button(wn, text="Sharpness")  # <- Sharpness button
btn_sharpness.place(x=340, y=570)

btn_bnw = ttk.Button(wn, text="BnW")  # <- Convert image to BnW
btn_bnw.place(x=420, y=570)

btn_folder = ttk.Button(wn, text="Folder", command=open_file_explorer)  # <- Open image
btn_folder.place(x=20, y=50)

# Image
image_label = Label(image_frame)  # <- Show image
image_label.place(anchor=CENTER, relx=0.5, rely=0.5)

"""
# Lists // I wanted to place here the recent files, too difficult for me xD
# listbox = Listbox(wn, height=28, width=15, bg=GRAY, borderwidth=0, selectmode=SINGLE) <- maybe in the def?

index_num = 0
for i in names_:
    listbox.insert(END, i)
    index_num += 1


# listbox.insert(END, "files[2]")
print("dir: ", directory)

listbox.insert(0, "Image 1")
listbox.insert(1, "Image 2")

# listbox.place(x=10, y=80)
"""

wn.mainloop()  # <- Keep the window on

"""

  .oooo.                             .    o8o                   .o   .o     .oooo.    .ooooo.     .oooo.     .oooo.   
.dP""Y88b                          .o8    `"'                  .8'  .8'   .dP""Y88b  888' `Y88.  d8P'`Y8b  .dP""Y88b  
      ]8P' oooo    ooo  .ooooo.  .o888oo oooo   .ooooo.    .888888888888'       ]8P' 888    888 888    888       ]8P' 
    <88b.   `88b..8P'  d88' `88b   888   `888  d88' `"Y8     .8'  .8'         .d8P'   `Vbood888 888    888     <88b.  
     `88b.    Y888'    888   888   888    888  888       .888888888888'     .dP'           888' 888    888      `88b. 
o.   .88P   .o8"'88b   888   888   888 .  888  888   .o8   .8'  .8'       .oP     .o     .88P'  `88b  d88' o.   .88P  
`8bd88P'   o88'   888o `Y8bod8P'   "888" o888o `Y8bod8P'  .8'  .8'        8888888888   .oP'      `Y8bd8P'  `8bd88P'   
                                                                                                                      
"""
