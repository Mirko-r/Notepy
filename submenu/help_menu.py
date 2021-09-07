from tkinter.messagebox import *
from tkinter import messagebox, Menu
from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
import webbrowser
import platform
import sys

class Help():
    def showAbout():
        messagebox.showinfo(
            "About Notepy",
            "Notepy Version: 3.5\n" +
            "Date of Release: xx/xx/xxxx\n"
            "Os: " + platform.system() + "\n" + 
            "Python Version: " + sys.version + "\n"
        )

    def keyb_short():
        messagebox.showinfo(
            "Keyboard Shortcut", "Ctrl+b = Bold\nCtrl+i = Italic\nCtrl+u = Underline\nCtrl+t = Overstrike\n\n" +
            "Ctrl+c = Copy\nCtrl+x = Cut\nCtrl+v = Paste\nCtrl+y = Undo\nCtrl+z = Redo\nCtrl+f = Find\nCtrl+a = Select all\nCtrl+d = Delete all\nCtrl+Shift+u = Uppercase\n\n" +
            "Ctrl+n = New file\nCtrl+o = Open file\nCtrl+s = Save file\n\n" +
            "Ctrl+q = Quit\n\n" +
            "Ctrl+t = Run terminal"
        )

    def release():
        webbrowser.open("https://mirko-r.github.io/notepy/docs/changelog.html")
        """Add code menu, this menu is totally for coders"""
    def license():

        root = Tk()
        root.title("Notepy license")
        root.iconbitmap("icons/license.ico")
          
        t = Text(root, width = 80, height = 25, wrap = NONE)

        f = open('submenu/license/LICENSE.txt','r').read()
        t.insert(END, f)

        t.pack(side=TOP, fill=X)
  
  
        root.mainloop()

    def term_help():

        root = Tk()
        root.title("Help terminal command")
        root.iconbitmap("icons/help.ico")
        v = Scrollbar(root)
  
        v.pack(side = RIGHT, fill = Y)
          
        t = Text(root, width = 120, height = 25, wrap = NONE,
                 yscrollcommand = v.set)

        f = open('submenu/terminal/term_command.txt','r').read()
        t.insert(END, f)

        t.pack(side=TOP, fill=X)
  
        v.config(command=t.yview)
  
        root.mainloop()


def main(root, text, menubar):

    helpmenu = Menu(menubar, tearoff=False)  # Help menu gui
    helpmenu.add_command(label='License', command=Help.license)
    helpmenu.add_command(label='About', command=Help.showAbout)
    helpmenu.add_command(label='Shortcut', command=Help.keyb_short)
    helpmenu.add_command(label='Release notes', command=Help.release)
    helpmenu.add_command(label="Terminal command", command=Help.term_help)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
