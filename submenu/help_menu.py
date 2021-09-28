from tkinter import messagebox
from tkinter import *
from datetime import datetime
import webbrowser
import platform
import sys
import os
import requests

class Help():
    def showAbout():
        try:
            response = requests.get("https://api.github.com/repos/Mirko-r/Notepy/releases/tags/3.5")
            date = response.json()["published_at"]
            datetimeobject = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            version = response.json()["tag_name"]
            messagebox.showinfo(
                "About Notepy",
                "Notepy Version: " + version + "\n" +
                "Date of Release: " + str(datetimeobject) + "\n"+
                "Os: " + platform.system() + "\n" + 
                "Python Version: " + sys.version + "\n"
            )
        except:
            messagebox.showerror("Error", "Sometings went wrong\nTry later ")

    def keyb_short():
        messagebox.showinfo(
            "Keyboard Shortcut", "Ctrl+b = Bold\nCtrl+i = Italic\nCtrl+u = Underline\nCtrl+t = Overstrike\n\n" +
            "Ctrl+c = Copy\nCtrl+x = Cut\nCtrl+v = Paste\nCtrl+y = Undo\nCtrl+z = Redo\nCtrl+f = Find\nCtrl+a = Select all\nCtrl+d = Delete all\nCtrl+Shift+u = Uppercase\nCtrl+Shift+l = Lowercase\n\n" +
            "Ctrl+n = New file\nCtrl+o = Open file\nCtrl+s = Save file\n\n" +
            "Ctrl+q = Quit\n\n" +
            "Ctrl+t = Run terminal"
        )

    def release():
        try:
            webbrowser.open("https://mirko-r.github.io/notepy/docs/changelog.html")
        except webbrowser.Error:
            messagebox.showerror("Error", "Something went wrong when opening webbrowser")

    def license():

        root = Tk()
        root.title("Notepy license")

        if "nt" == os.name:
            root.wm_iconbitmap(bitmap = "./icons/license.ico")
        else:
            root.wm_iconbitmap(bitmap = "@./icons/license.xbm")
          
        t = Text(root, width = 80, height = 25, wrap = NONE)

        f = open('submenu/license/LICENSE.txt','r').read()
        t.insert(END, f)

        t.pack(side=TOP, fill=X)
  
  
        root.mainloop()

    def term_help():

        root = Tk()
        root.title("Help terminal command")
        
        if "nt" == os.name:
            root.wm_iconbitmap(bitmap = "./icons/help.ico")
        else:
            root.wm_iconbitmap(bitmap = "@./icons/help.xbm")
        v = Scrollbar(root)

        if "nt" == os.name:
            v.pack(side = RIGHT, fill = Y)
          
            t = Text(root, width = 120, height = 25, wrap = NONE,
                    yscrollcommand = v.set)

            f = open('submenu/terminal/term_command.txt','r').read()
            t.insert(END, f)

            t.pack(side=TOP, fill=X)
  
            v.config(command=t.yview)
  
            root.mainloop()
        else:
            messagebox.showinfo("Help terminal command", "The help for your system is not already available")


def main(root, menubar):

    helpmenu = Menu(menubar, tearoff=False)  # Help menu gui
    helpmenu.add_command(label='License', command=Help.license)
    helpmenu.add_command(label='About', command=Help.showAbout)
    helpmenu.add_command(label='Shortcut', command=Help.keyb_short)
    helpmenu.add_command(label='Release notes', command=Help.release)
    helpmenu.add_command(label="Terminal command", command=Help.term_help)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    messagebox.showerror("Error", "Please run 'main.py'")
