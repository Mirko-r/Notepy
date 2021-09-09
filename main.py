from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from tkinter.ttk import *
from submenu import file_menu, format_menu, edit_menu, revision_menu, code_menu, help_menu, rightmenu, run_menu


def main():
    root = Tk()
    root.title("Notepy")

    #center the window
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    left = (screenWidth / 2) - 600
    top = (screenHeight / 2) - 300

    root.geometry('%dx%d+%d+%d' % (1200,  600, left, top))
    
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

    code_menu.main(root, text, menubar, status_bar)

    rightmenu.main(root, text, menubar, status_bar)
    
    help_menu.main(root, text, menubar)

    run_menu.main(root, menubar)

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)

    root.mainloop()
