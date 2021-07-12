from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from idlelib.percolator import Percolator
from idlelib.colorizer import ColorDelegator
from submenu import file_menu, format_menu, edit_menu, revision_menu, help_menu, rightmenu
import os
from sys import platform


def main():
    def run_terminal(*args):
        if platform == 'darwin':
            os.system('open -a Terminal -n')
        elif platform == 'win32':
            os.system('start cmd')
        elif platform == 'linux':
            os.system('gnome-terminal')

    root = Tk()

    root.title("Notepy")
    root.geometry("1200x600")
    root.minsize(width=600, height=600)
    root.iconbitmap("icons/notepy.ico")
    status_bar = Label(root, text='Ready   ', anchor=E)
    status_bar.pack(fill="x", side="bottom", ipady=4)


    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    text = Text(root, state='normal', width=400, height=400, wrap='word', pady=2,
            padx=3, undo=True, selectbackground="yellow", selectforeground="black",)
    text.pack(fill=Y, expand=1)
    text.config(yscrollcommand=scrollbar.set)
    text.focus_set()
    scrollbar.config(command=text.yview)

    menubar = Menu(root)

    file_menu.main(root, text, menubar, status_bar)

    edit_menu.main(root, text, menubar, status_bar)

    format_menu.main(root, text, menubar, status_bar)

    revision_menu.main(root, text, menubar, status_bar)

    rightmenu.main(root, text, menubar, status_bar)

    menubar.add_command(label="Run terminal", command=run_terminal)

    help_menu.main(root, text, menubar)

    Percolator(text).insertfilter(ColorDelegator())

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)

    root.bind_all("<Control-t>", run_terminal)

    root.mainloop()
