from tkinter.messagebox import *
from tkinter import messagebox, Menu

class Help():
    def showAbout():
        messagebox.showinfo(
                        "About Notepy v2.x", 
                        "Notepy v2.x\nThe code is written totally in python\n"+
                        "The source code is open,\n"+
                        "you can see it on GitHub: Mirko-r/Notepy\n\n"+
                        "By Mirko Rovere"
                        )

    def keyb_short():
        messagebox.showinfo(
                        "Keyboard Shortcut", "Ctrl+b = Bold\nCtrl+i = Italic\nCtrl+u = Underline\nCtrl+t = Overstrike\n\n"+
                        "Ctrl+c = Copy\nCtrl+x = Cut\nCtrl+v = Paste\nCtrl+y = Undo\nCtrl+z = Redo\nCtrl+f = Find\nCtrl+a = Select all\nCtrl+d = Delete all\n\n"+
                        "Ctrl+n = New file\nCtrl+o = Open file\nCtrl+s = Save file\n\n"+
                        "Ctrl+q = Quit\n\n"+
                        "Ctrl+t = Run terminal"
                        )

    def release():
        messagebox.showinfo(
            "Version 2.x", 
            "What's new:\n\n"+
            "- Added support for open and saveAs a lot of filetypes\n"
            "- Better SaveAs and Open functions\n"
            "- Improved status bar\n"
            "- Now the program icon changes according to the extension of the file\n"
            "- Added text align submenu on format menu\n"
            "- Better format menu separation\n"
            "- Added Splash Screen\n"
            "- Added readability function on Revision menu\n"
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
