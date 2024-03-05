import tkinter as tk
import base64
import os

def handle_click(category):
    print(f"Clicked {category}")


# Help Category Handlers
def open_documentation():
    print("Opened Documentation")

def open_about():
    print("Opened About")


# Appearance Category Handlers
def night_mode():
    print("Enabled Dark Mode")

def day_mode():
    print("Enabled Light Mode")


# Edit Category Handlers
def cut_handler():
    print("Successfully Cut")

def paste_handler():
    print("Successfully Pasted")

def undo_handler():
    print("Successfully Undid")

def redo_handler():
    print("Successfully Redid")


# File Category Handlers
def open_handler():
    print("Successfully Opened")

def save_handler():
    print("Successfully Saved")

def save_as_handler():
    print("Successfully Saved As")


# Terminal Category Handlers
def terminal_handler():
    print("Successfully Opened Terminal")


root = tk.Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

scriptDir = os.path.dirname(os.path.abspath(__file__))
assetsDir = os.path.join(scriptDir, "Assets")

iconPath = os.path.join(assetsDir, "icon.png")
with open(iconPath, "rb") as file:
    pngData = file.read()

base64Data = base64.b64encode(pngData).decode()

root.title("GogEngine v1.10")
root.configure(bg="#999999")

windowWidth = 1000
windowHeight = 600
x = (screenWidth - windowWidth) // 2
y = (screenHeight - windowHeight) // 2
root.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

menuBar = tk.Menu(root)
root.config(menu=menuBar)


# File Category
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open", command=open_handler)
fileMenu.add_command(label="Save", command=save_handler)
fileMenu.add_command(label="Save As", command=save_as_handler)


# Edit Category
editMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Cut", command=cut_handler)
editMenu.add_command(label="Paste", command=paste_handler)
editMenu.add_command(label="Undo", command=undo_handler)
editMenu.add_command(label="Redo", command=redo_handler)


# Appearance Category
appearanceMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Appearance", menu=appearanceMenu)

appearanceMenu.add_command(label="Night Mode", command=night_mode)
appearanceMenu.add_command(label="Day Mode", command=day_mode)


# Help Category
helpMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)

helpMenu.add_command(label="About", command=open_about)
helpMenu.add_command(label="Documentation", command=open_documentation)


# Terminal Option
terminalMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_command(label="Terminal", command=terminal_handler)


photo = tk.PhotoImage(data=base64Data)

root.tk.call('wm', 'iconphoto', root._w, photo)

root.mainloop()
