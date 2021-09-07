from tkinter.messagebox import *
from tkinter import messagebox, Menu
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *

class Code():
    def __init__(self, text, root, status_bar):
        self.text = text
        self.root = root
        self.status_bar = status_bar
        
def main(root, text, menubar, status_bar):

    codemenu = Menu(menubar, tearoff=False)
    objCode = Code(text, root, status_bar)

    menubar.add_cascade(label="Code", menu=codemenu)
    root.config(menu=menubar)

if __name__ == "__main__":
    messagebox.showerror("Error", "Please run main.py")