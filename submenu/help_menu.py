from tkinter.messagebox import *
from tkinter import messagebox, Menu

class Help():
    def showAbout():
        messagebox.showinfo(
                        "About Notepy v2.0", 
                        "Notepy v2.0\nThe code is written totally in python\n"+
                        "The source code is open,\n"+
                        "you can see it on GitHub: Mirko-r/Notepy\n\n"+
                        "By Mirko Rovere"
                        )

    def keyb_short():
        messagebox.showinfo(
                        "Keyboard Shortcut", "Ctrl+b = Bold\nCtrl+i = Italic\nCtrl+u = Underline\nCtrl+t = Overstrike\n\n"+
                        "Ctrl+c = Copy\nCtrl+x = Cut\nCtrl+v = Paste\nCtrl+z = Undo\nCtrl+y = Redo\nCtrl+f = Find\nCtrl+a = Select all\nCtrl+d = Delete all\n\n"+
                        "Ctrl+n = New file\nCtrl+o = Open file\nCtrl+s = Save file\n\n"+
                        "Ctrl+q = Quit"
                        )

    def release():
        messagebox.showinfo(
            "Release Notes for version 2.0", 
            "- All subprogram moved to submenu folder\n- Added release notes in help menu"
        )
def main(root, text, menubar):
    
    helpmenu = Menu(menubar, tearoff=False) # Help menu gui
    helpmenu.add_command(label = 'About', command = Help.showAbout)
    helpmenu.add_command(label = 'Shortcut', command = Help.keyb_short)
    helpmenu.add_command(label = 'Release notes', command = Help.release)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
