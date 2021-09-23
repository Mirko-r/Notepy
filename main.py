from tkinter import *
from modules import status_bar_line_and_column, submenu_caller

def modules_connect(root, text,menubar, status_bar):

        # Display current cursor position on status bat
        status_bar_line_and_column.main(text, status_bar)

        # call all submenu
        submenu_caller.main(root, text, menubar, status_bar)

def center_window(root):
    #center the window
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    left = (screenWidth / 2) - 600
    top = (screenHeight / 2) - 300

    root.geometry('%dx%d+%d+%d' % (1200,  600, left, top))

def main():
    root = Tk()
    root.title("Notepy")

    center_window(root)
    root.minsize(width=600, height=600)
    root.iconbitmap('icons/notepy.ico')
    status_bar = Label(root, text='Ready   ', anchor=E)
    status_bar.pack(fill="x", side="bottom", ipady=4)

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    text = Text(root, state='normal', width=400, height=400, wrap='word', pady=2,
            padx=3, undo=True, selectbackground="yellow", selectforeground="black", font="monospace")

    text.pack(fill=Y, expand=1)
    text.config(yscrollcommand=scrollbar.set)
    text.focus_set()

    scrollbar.config(command=text.yview)

    menubar = Menu(root)

    root.grid_columnconfigure(0, weight=1)
    root.resizable(True, True)
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)

    modules_connect(root, text, menubar, status_bar)
    
    root.mainloop()
