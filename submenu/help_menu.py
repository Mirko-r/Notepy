from tkinter import messagebox
from tkinter import *
from datetime import datetime
import webbrowser
import platform
import sys
import os
import requests
import base64

class Help():
    def showAbout():
        try:
            response = requests.get("https://api.github.com/repos/Mirko-r/Notepy/releases/tags/4.0")
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
        except requests.exceptions.Timeout as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.TooManyRedirects as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.RequestException as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.HTTPError as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.InvalidURL as err:
            messagebox.showerror("Error", err)

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
        except webbrowser.Error as err:
            messagebox.showerror("Error", err)

        """

        """
    def license():
        try:
            req = requests.get("https://api.github.com/repos/Mirko-r/Notepy/contents/LICENSE").json()["content"]
            messagebox.showinfo("License", base64.b64decode(req.encode('ascii')).decode('ascii'))
        except requests.exceptions.Timeout as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.TooManyRedirects as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.RequestException as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.HTTPError as err:
            messagebox.showerror("Error", err)
        except requests.exceptions.InvalidURL as err:
            messagebox.showerror("Error", err)

    def term_help():

        if "nt" == os.name:
            root = Tk()
            root.title("Help terminal command")
        
            if "nt" == os.name:
                root.wm_iconbitmap(bitmap = "./icons/help.ico")
            else:
                root.wm_iconbitmap(bitmap = "@./icons/help.xbm")
            v = Scrollbar(root)
            v.pack(side = RIGHT, fill = Y)
          
            t = Text(root, width = 120, height = 25, wrap = NONE,
                    yscrollcommand = v.set)

            f = open('submenu/terminal/term_command.txt','r').read()
            t.insert(END, f)

            t.pack(side=TOP, fill=X)
  
            v.config(command=t.yview)
  
            root.mainloop()
        else:
            messagebox.showinfo("Help terminal command", "Terminal command list is not available")


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
    messagebox.showerror("Eror", "Please run 'main.py'")
