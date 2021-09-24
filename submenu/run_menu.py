from tkinter import Menu
from tkinter import *
from tkterminal import Terminal
import os


class run():
    def run_terminal(*args):
        main = Tk()
        main.title("Terminal")
        if "nt" == os.name:
            main.wm_iconbitmap(bitmap = "./icons/terminal.ico")
        else:
            main.wm_iconbitmap(bitmap = "@./icons/terminal.xbm")
        terminal = Terminal(main, padx=5, pady=5,
                            background='black', foreground='white')
        terminal.shell = True
        terminal.basename = "Notepy$ > "
        terminal.pack(expand=True, fill=BOTH)
        main.mainloop()


def main(root, menubar):

    runmenu = Menu(menubar, tearoff=False)

    runmenu.add_command(label="Run terminal", command=run.run_terminal)
    menubar.add_cascade(label="▷", menu=runmenu)

    root.config(menu=menubar)

    root.bind_all("<Control-t>", run.run_terminal)
