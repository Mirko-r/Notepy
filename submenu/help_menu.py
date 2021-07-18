from tkinter.messagebox import *
from tkinter import messagebox, Menu


class Help():
    def showAbout():
        messagebox.showinfo(
            "About Notepy v3.0",
            "Notepy v3.0\nThe code is written totally in python\n" +
            "The source code is open,\n" +
            "you can see it on GitHub: Mirko-r/Notepy\n\n" +
            "By Mirko Rovere"
        )

    def keyb_short():
        messagebox.showinfo(
            "Keyboard Shortcut", "Ctrl+b = Bold\nCtrl+i = Italic\nCtrl+u = Underline\nCtrl+t = Overstrike\n\n" +
            "Ctrl+c = Copy\nCtrl+x = Cut\nCtrl+v = Paste\nCtrl+y = Undo\nCtrl+z = Redo\nCtrl+f = Find\nCtrl+a = Select all\nCtrl+d = Delete all\n\n" +
            "Ctrl+n = New file\nCtrl+o = Open file\nCtrl+s = Save file\n\n" +
            "Ctrl+q = Quit\n\n" +
            "Ctrl+t = Run terminal"
        )

    def release():
        messagebox.showinfo(
            "Version 3.0",
            "What's new:\n\n" +
            "- Better splash screen\n"+
            "- Now the program is under MIT license, you can read it on license command under Help menu\n"+
            "- Added basic syntax highlight function on Edit menu"
        )

    def license():
        messagebox.showinfo(
            "Notepy License",
            "MIT License\n\n"+

            "Copyright(c) 2021 Mirko Rovere\n\n"+
            
            "Permission is hereby granted, free of charge, to any person obtaining a copy "+
            "of this software and associated documentation files(the 'Software'), to deal "+
            "in the Software without restriction, including without limitation the rights "+
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell "+
            "copies of the Software, and to permit persons to whom the Software is "+
            "furnished to do so, subject to the following conditions:\n\n"+

            "The above copyright notice and this permission notice shall be included in all "+
            "copies or substantial portions of the Software.\n\n"+

            "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR "+
            "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, "+
            "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE "+
            "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER"+
            "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,"+
            "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE "+
            "SOFTWARE."
        )


def main(root, text, menubar):

    helpmenu = Menu(menubar, tearoff=False)  # Help menu gui
    helpmenu.add_command(label='License', command=Help.license)
    helpmenu.add_command(label='About', command=Help.showAbout)
    helpmenu.add_command(label='Shortcut', command=Help.keyb_short)
    helpmenu.add_command(label='Release notes', command=Help.release)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Eror", "Please run 'main.py'")
