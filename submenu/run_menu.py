import os
from sys import platform
from tkinter import *
from tkinter import Menu

class run():
    def run_terminal(*args):
        if platform == 'darwin':
            os.system('open -a Terminal -n')
        elif platform == 'win32':
            os.system('start cmd')
        elif platform == 'linux':
            os.system('gnome-terminal')

def main(root, menubar):
   
    runmenu = Menu(menubar, tearoff=False)

    runmenu.add_command(label="Run terminal", command=run.run_terminal)
    menubar.add_cascade(label="▷", menu=runmenu)

    root.config(menu=menubar)
    
    root.bind_all("<Control-t>", run.run_terminal)