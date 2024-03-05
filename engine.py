import tkinter as tk
import base64
import os
import tkinter.filedialog
import tkinter.scrolledtext


def handle_click(category):
    print(f"Clicked {category}")


# Help Category Handlers
def open_documentation():
    print("Opened Documentation")

def open_about():
    print("Opened About")


# Appearance Category Handlers
def night_mode():
    root.configure(bg="#333333")

def day_mode():
    root.configure(bg="#999999")


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
    global currentFilePath
    global textEditor
    
    filePath = tkinter.filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        if textEditor:
            textEditor.pack_forget()
            textEditor.destroy()
            
        textEditor = tkinter.scrolledtext.ScrolledText(root, wrap=tk.WORD)
        textEditor.pack(expand=True, fill=tk.BOTH)
        
        with open(filePath, 'r') as file:
            fileContent = file.read()

            textEditor.delete(1.0, tk.END)
            textEditor.insert(tk.END, fileContent)
            currentFilePath = filePath


def save_handler(event=None):
    global currentFilePath
    if currentFilePath: 
        fileContent = textEditor.get(1.0, tk.END)
        with open(currentFilePath, 'w') as file:
            file.write(fileContent)


def save_as_handler():
    global currentFilePath
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        file_content = textEditor.get(1.0, tk.END)
        with open(file_path, 'w') as file:
            file.write(file_content)
        currentFilePath = file_path


def new_file_handler():
    global textEditor
    
    filePath = tkinter.filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        if textEditor:
            textEditor.pack_forget()
            textEditor.destroy()
        
        textEditor = tkinter.scrolledtext.ScrolledText(root, wrap=tk.WORD)
        textEditor.pack(expand=True, fill=tk.BOTH)
        
        textEditor.delete(1.0, tk.END)
        with open(filePath, 'w') as file:
            file.write("# Welcome to my new Python file!\n")
            print("New file created:", filePath)
    else:
        print("No file created.")

# Terminal Category Handlers
def terminal_handler():
    os.system("start cmd")


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

textEditor = None


# File Category
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New File", command=new_file_handler)
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


# Terminal Category
terminalMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Terminal", menu=terminalMenu)
terminalMenu.add_command(label="Open Terminal", command=terminal_handler)


photo = tk.PhotoImage(data=base64Data)

root.tk.call('wm', 'iconphoto', root._w, photo)

root.mainloop()
import tkinter as tk
import base64
import os
import tkinter.filedialog
import tkinter.scrolledtext


def handle_click(category):
    print(f"Clicked {category}")


# Help Category Handlers
def open_documentation():
    print("Opened Documentation")

def open_about():
    print("Opened About")


# Appearance Category Handlers
def night_mode():
    root.configure(bg="#333333")

def day_mode():
    root.configure(bg="#999999")


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
    global currentFilePath
    global textEditor
    
    filePath = tkinter.filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        if textEditor:
            textEditor.pack_forget()
            textEditor.destroy()
            
        textEditor = tkinter.scrolledtext.ScrolledText(root, wrap=tk.WORD)
        textEditor.pack(expand=True, fill=tk.BOTH)
        
        with open(filePath, 'r') as file:
            fileContent = file.read()

            textEditor.delete(1.0, tk.END)
            textEditor.insert(tk.END, fileContent)
            currentFilePath = filePath


def save_handler(event=None):
    global currentFilePath
    if currentFilePath: 
        fileContent = textEditor.get(1.0, tk.END)
        with open(currentFilePath, 'w') as file:
            file.write(fileContent)


def save_as_handler():
    global currentFilePath
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        file_content = textEditor.get(1.0, tk.END)
        with open(file_path, 'w') as file:
            file.write(file_content)
        currentFilePath = file_path


def new_file_handler():
    global textEditor
    
    filePath = tkinter.filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if filePath:
        if textEditor:
            textEditor.pack_forget()
            textEditor.destroy()
        
        textEditor = tkinter.scrolledtext.ScrolledText(root, wrap=tk.WORD)
        textEditor.pack(expand=True, fill=tk.BOTH)
        
        textEditor.delete(1.0, tk.END)
        with open(filePath, 'w') as file:
            file.write("# Welcome to my new Python file!\n")
            print("New file created:", filePath)
    else:
        print("No file created.")

# Terminal Category Handlers
def terminal_handler():
    os.system("start cmd")


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

textEditor = None


# File Category
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New File", command=new_file_handler)
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


# Terminal Category
terminalMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Terminal", menu=terminalMenu)
terminalMenu.add_command(label="Open Terminal", command=terminal_handler)


photo = tk.PhotoImage(data=base64Data)

root.tk.call('wm', 'iconphoto', root._w, photo)

root.mainloop()
