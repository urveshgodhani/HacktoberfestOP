import os
import tkinter as tk
from tkinter.constants import BOTH, END, NO, RIGHT, Y
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
import ctypes
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

class TextEditor(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry("1044x588")
        self.title("Untitled - TextEditor")
        self.wm_iconbitmap("hp_notepad_pencil.ico")

    def newFile(self):
        global file
        self.title("Untitled - TextEditor")
        file = None

        self.TextArea.delete(1.0, END)

    def openFile(self):
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            self.title(f"{os.path.basename(file)} - TextEditor")
            self.TextArea.delete(1.0, END)
            f = open(file, "r")
            self.TextArea.insert(1.0, f.read())
            f.close()

    def saveFile(self):
        global file
        if file == None:
            file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            
            if file == "":
                file = None

            else:
                f = open(file, "w")
                f.write(self.TextArea.get(1.0, END))
                f.close()

                self.title(f"{os.path.basename(file)} - TextEditor")
        else:
            f = open(file, "w")
            f.write(self.TextArea.get(1.0, END))
            f.close()

    def lightTheme(self):
        pass

    def darkTheme(self):
        pass

    def cut(self):
        self.TextArea.event_generate(("<<Cut>>"))

    def copy(self):
        self.TextArea.event_generate(("<<Copy>>"))

    def paste(self):
        self.TextArea.event_generate(("<<Paste>>"))

    def undo(self):
        self.TextArea.event_generate(("<<Undo>>"))

    def widgets(self):

        # TextArea
        self.TextArea = tk.Text(self, font="Lucida 11", undo=True) 
        self.file = None
        self.TextArea.pack(expand=True, fill=BOTH)

        # MenuBar
        self.MenuBar = tk.Menu(self)

        # FileMenu
        self.FileMenu = tk.Menu(self.MenuBar, tearoff=0)

        self.FileMenu.add_command(label="New", command=self.newFile, accelerator="Ctrl+N")
        self.FileMenu.add_command(label="Open", command=self.openFile, accelerator="Ctrl+O")
        self.FileMenu.add_command(label="Save", command=self.saveFile, accelerator="Ctrl+S")
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", command=self.quit)

        self.MenuBar.add_cascade(label="File", menu=self.FileMenu)

        # EditMenu
        self.EditMenu = tk.Menu(self.MenuBar, tearoff=0)

        self.EditMenu.add_command(label="Undo", command=self.TextArea.edit_undo, accelerator="Ctrl+Z")
        self.FileMenu.add_separator()
        self.EditMenu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        self.EditMenu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        self.EditMenu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")

        self.MenuBar.add_cascade(label="Edit", menu=self.EditMenu)

        # ThemeMenu
        self.ThemeMenu = tk.Menu(self.MenuBar, tearoff=0)

        self.ThemeMenu.add_command(label="Light", command=self.lightTheme)
        self.ThemeMenu.add_command(label="Dark", command=self.darkTheme)

        self.MenuBar.add_cascade(label="Theme", menu=self.ThemeMenu)

        self.config(menu=self.MenuBar)

        self.ScrollBar = tk.Scrollbar(self.TextArea)
        self.ScrollBar.pack(side=RIGHT, fill=Y)
        self.ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=self.ScrollBar.set)

if __name__ == '__main__':
    root = TextEditor()
    # font = Font(family="Lucida Sans", size=11)
    root.widgets()
    root.mainloop()

